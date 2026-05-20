#!/usr/bin/env python3
"""Small self-contained server for the XhLab project catalog.

It serves the existing static site, exposes a JSON project API, and provides a
password-protected admin page for adding/editing projects and uploading images.
The implementation uses only Python's standard library so it is easy to deploy
on a small ECS instance.
"""

from __future__ import annotations

import base64
import cgi
import hashlib
import hmac
import html
import json
import mimetypes
import os
import posixpath
import re
import secrets
import sys
import time
import urllib.parse
from http import cookies
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from pathlib import Path
from typing import Optional
from getpass import getpass


ROOT = Path(__file__).resolve().parent
STORAGE_DIR = ROOT / "storage"
UPLOAD_DIR = STORAGE_DIR / "uploads"
PROJECTS_JSON = STORAGE_DIR / "projects.json"
APP_SECRET_FILE = STORAGE_DIR / "app.secret"
ADMIN_PASSWORD_FILE = STORAGE_DIR / "admin.secret"
LEGACY_PROJECTS_JS = ROOT / "data" / "projects.js"
MAX_BODY_SIZE = 12 * 1024 * 1024
SESSION_SECONDS = 7 * 24 * 60 * 60
PASSWORD_HASH_PREFIX = "pbkdf2_sha256"
PASSWORD_HASH_ITERATIONS = 260000


def ensure_storage() -> None:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    if not PROJECTS_JSON.exists():
        PROJECTS_JSON.write_text(json.dumps(load_legacy_projects(), ensure_ascii=False, indent=2), encoding="utf-8")
    if not APP_SECRET_FILE.exists():
        APP_SECRET_FILE.write_text(secrets.token_urlsafe(48), encoding="utf-8")
    if "ADMIN_PASSWORD" not in os.environ and not ADMIN_PASSWORD_FILE.exists():
        ADMIN_PASSWORD_FILE.write_text(make_password_hash(secrets.token_urlsafe(32)), encoding="utf-8")


def load_legacy_projects() -> list[dict]:
    if not LEGACY_PROJECTS_JS.exists():
        return []

    text = LEGACY_PROJECTS_JS.read_text(encoding="utf-8")
    match = re.search(r"window\.PROJECTS\s*=\s*(\[.*\])\s*;?\s*$", text, re.S)
    if not match:
        return []

    projects = json.loads(match.group(1))
    return [normalize_project(project, index + 1) for index, project in enumerate(projects)]


def read_projects() -> list[dict]:
    ensure_storage()
    with PROJECTS_JSON.open("r", encoding="utf-8") as file:
        projects = json.load(file)
    return [normalize_project(project, index + 1) for index, project in enumerate(projects)]


def write_projects(projects: list[dict]) -> None:
    projects = sorted((normalize_project(project, index + 1) for index, project in enumerate(projects)), key=lambda item: item["id"])
    temp = PROJECTS_JSON.with_suffix(".tmp")
    temp.write_text(json.dumps(projects, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(PROJECTS_JSON)


def normalize_project(project: dict, fallback_id: int) -> dict:
    def text_value(key: str) -> str:
        value = project.get(key, "")
        return str(value).strip() if value is not None else ""

    materials = project.get("materials", [])
    if isinstance(materials, str):
        materials = [item.strip() for item in re.split(r"[\n,，、]+", materials) if item.strip()]
    if not isinstance(materials, list):
        materials = []

    try:
        project_id = int(project.get("id", fallback_id))
    except (TypeError, ValueError):
        project_id = fallback_id

    return {
        "id": project_id,
        "name": text_value("name"),
        "description": text_value("description"),
        "tech": text_value("tech"),
        "access": text_value("access") or "付费获取",
        "materials": [str(item).strip() for item in materials if str(item).strip()],
        "sourceUrl": text_value("sourceUrl"),
        "demoVideoUrl": text_value("demoVideoUrl"),
        "configDocUrl": text_value("configDocUrl"),
        "image": text_value("image"),
        "updatedAt": text_value("updatedAt"),
    }


def public_projects() -> list[dict]:
    projects = read_projects()
    for project in projects:
        if project["image"]:
            project["imageUrl"] = project["image"]
    return projects


def read_app_secret() -> str:
    ensure_storage()
    return os.environ.get("APP_SECRET") or APP_SECRET_FILE.read_text(encoding="utf-8").strip()


def make_password_hash(password: str) -> str:
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        PASSWORD_HASH_ITERATIONS,
    )
    encoded = base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")
    return f"{PASSWORD_HASH_PREFIX}${PASSWORD_HASH_ITERATIONS}${salt}${encoded}"


def verify_password(password: str, stored: str) -> bool:
    if stored.startswith(f"{PASSWORD_HASH_PREFIX}$"):
        try:
            _, iterations, salt, encoded = stored.split("$", 3)
            digest = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                salt.encode("utf-8"),
                int(iterations),
            )
            candidate = base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")
            return hmac.compare_digest(candidate, encoded)
        except Exception:
            return False

    # Backward compatibility for existing plaintext admin.secret files.
    return hmac.compare_digest(password, stored)


def read_admin_secret() -> str:
    ensure_storage()
    return os.environ.get("ADMIN_PASSWORD") or ADMIN_PASSWORD_FILE.read_text(encoding="utf-8").strip()


def verify_admin_password(password: str) -> bool:
    return verify_password(password, read_admin_secret())


def set_admin_password_interactive() -> None:
    ensure_storage()
    password = getpass("New admin password: ").strip()
    confirm = getpass("Retype new admin password: ").strip()
    if not password:
        raise SystemExit("Password cannot be empty.")
    if password != confirm:
        raise SystemExit("Passwords do not match.")
    ADMIN_PASSWORD_FILE.write_text(make_password_hash(password), encoding="utf-8")
    print(f"Updated {ADMIN_PASSWORD_FILE}")


def make_session() -> str:
    expires = int(time.time()) + SESSION_SECONDS
    payload = f"admin:{expires}"
    signature = hmac.new(read_app_secret().encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()
    token = f"{payload}:{signature}".encode("utf-8")
    return base64.urlsafe_b64encode(token).decode("ascii")


def verify_session(token: Optional[str]) -> bool:
    if not token:
        return False
    try:
        raw = base64.urlsafe_b64decode(token.encode("ascii")).decode("utf-8")
        user, expires, signature = raw.split(":", 2)
        payload = f"{user}:{expires}"
        expected = hmac.new(read_app_secret().encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()
        return user == "admin" and int(expires) >= int(time.time()) and hmac.compare_digest(signature, expected)
    except Exception:
        return False


def parse_form(body: bytes, content_type: str) -> dict[str, str]:
    if content_type.startswith("application/x-www-form-urlencoded"):
        parsed = urllib.parse.parse_qs(body.decode("utf-8"), keep_blank_values=True)
        return {key: values[-1] if values else "" for key, values in parsed.items()}
    return {}


def parse_multipart(body: bytes, headers: dict[str, str]) -> tuple[dict[str, str], dict[str, tuple[str, bytes, str]]]:
    environ = {
        "REQUEST_METHOD": "POST",
        "CONTENT_TYPE": headers.get("content-type", ""),
        "CONTENT_LENGTH": headers.get("content-length", "0"),
    }
    form = cgi.FieldStorage(fp=BytesIO(body), environ=environ, keep_blank_values=True)
    fields: dict[str, str] = {}
    files: dict[str, tuple[str, bytes, str]] = {}

    for key in form.keys():
        item = form[key]
        if isinstance(item, list):
            item = item[-1]
        if item.filename:
            files[key] = (item.filename, item.file.read(), item.type or "application/octet-stream")
        else:
            fields[key] = item.value
    return fields, files


def save_upload(file_data: Optional[tuple[str, bytes, str]]) -> str:
    if not file_data:
        return ""
    filename, data, content_type = file_data
    if not filename or not data:
        return ""

    allowed = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
        "image/gif": ".gif",
    }
    suffix = allowed.get(content_type)
    if suffix is None:
        guessed = Path(filename).suffix.lower()
        suffix = guessed if guessed in allowed.values() else ".bin"

    safe_name = f"{int(time.time())}-{secrets.token_hex(8)}{suffix}"
    target = UPLOAD_DIR / safe_name
    target.write_bytes(data)
    return f"/uploads/{safe_name}"


def project_from_fields(fields: dict[str, str], image_path: str, existing: Optional[dict] = None) -> dict:
    existing = existing or {}
    materials = [item.strip() for item in re.split(r"[\n,，、]+", fields.get("materials", "")) if item.strip()]
    project = {
        "id": int(fields.get("id") or existing.get("id") or 0),
        "name": fields.get("name", "").strip(),
        "description": fields.get("description", "").strip(),
        "tech": fields.get("tech", "").strip(),
        "access": fields.get("access", "").strip() or "付费获取",
        "materials": materials,
        "sourceUrl": fields.get("sourceUrl", "").strip(),
        "demoVideoUrl": fields.get("demoVideoUrl", "").strip(),
        "configDocUrl": fields.get("configDocUrl", "").strip(),
        "image": image_path or fields.get("existingImage", "").strip() or existing.get("image", ""),
        "updatedAt": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    return normalize_project(project, project["id"] or 1)


def next_project_id(projects: list[dict]) -> int:
    return max((int(project.get("id", 0)) for project in projects), default=0) + 1


def redirect_html(target: str) -> bytes:
    return f'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={html.escape(target)}">'.encode("utf-8")


def admin_layout(title: str, body: str) -> bytes:
    page = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | XhLab 后台</title>
  <style>
    :root {{ color-scheme: light; --bg:#f6f7f9; --panel:#fff; --text:#1c2430; --muted:#637083; --line:#dde3ea; --brand:#157a6e; --danger:#b42318; }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif; background:var(--bg); color:var(--text); }}
    a {{ color:var(--brand); text-decoration:none; }}
    header {{ position:sticky; top:0; z-index:5; display:flex; align-items:center; justify-content:space-between; gap:16px; padding:14px 24px; background:rgba(255,255,255,.96); border-bottom:1px solid var(--line); }}
    header strong {{ font-size:18px; }}
    nav {{ display:flex; gap:12px; flex-wrap:wrap; }}
    main {{ max-width:1120px; margin:0 auto; padding:24px; }}
    .panel {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:20px; }}
    .toolbar {{ display:flex; align-items:center; justify-content:space-between; gap:16px; margin-bottom:16px; }}
    .button, button {{ display:inline-flex; align-items:center; justify-content:center; min-height:38px; padding:8px 14px; border:1px solid var(--brand); border-radius:6px; background:var(--brand); color:white; font:inherit; cursor:pointer; }}
    .button.secondary, button.secondary {{ background:#fff; color:var(--brand); }}
    button.danger {{ border-color:var(--danger); background:var(--danger); }}
    table {{ width:100%; border-collapse:collapse; background:white; }}
    th, td {{ padding:12px 10px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }}
    th {{ color:var(--muted); font-weight:600; font-size:13px; }}
    .muted {{ color:var(--muted); }}
    .actions {{ display:flex; gap:8px; flex-wrap:wrap; }}
    form.grid {{ display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:16px; }}
    label {{ display:grid; gap:6px; font-weight:600; }}
    input, textarea {{ width:100%; border:1px solid var(--line); border-radius:6px; padding:10px 12px; font:inherit; background:#fff; }}
    textarea {{ min-height:110px; resize:vertical; }}
    .full {{ grid-column:1 / -1; }}
    .preview {{ max-width:180px; max-height:120px; border-radius:6px; border:1px solid var(--line); object-fit:cover; }}
    .login {{ max-width:420px; margin:80px auto; }}
    .error {{ color:var(--danger); margin-bottom:12px; }}
    @media (max-width: 760px) {{ header, .toolbar {{ align-items:flex-start; flex-direction:column; }} form.grid {{ grid-template-columns:1fr; }} table {{ display:block; overflow-x:auto; }} }}
  </style>
</head>
<body>
  <header>
    <strong>XhLab 项目后台</strong>
    <nav>
      <a href="/admin">项目管理</a>
      <a href="/" target="_blank">打开前台</a>
      <form method="post" action="/admin/logout"><button class="secondary" type="submit">退出</button></form>
    </nav>
  </header>
  <main>{body}</main>
</body>
</html>"""
    return page.encode("utf-8")


def login_page(error: str = "") -> bytes:
    page = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>XhLab 后台登录</title>
  <style>
    body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif; background:#f6f7f9; color:#1c2430; }}
    .login {{ max-width:420px; margin:80px auto; background:white; border:1px solid #dde3ea; border-radius:8px; padding:24px; }}
    label {{ display:grid; gap:8px; font-weight:600; margin:16px 0; }}
    input {{ width:100%; border:1px solid #dde3ea; border-radius:6px; padding:10px 12px; font:inherit; }}
    button {{ width:100%; min-height:40px; border:0; border-radius:6px; background:#157a6e; color:white; font:inherit; cursor:pointer; }}
    .error {{ color:#b42318; }}
    .muted {{ color:#637083; line-height:1.7; }}
  </style>
</head>
<body>
  <form class="login" method="post" action="/admin/login">
    <h1>后台登录</h1>
    {f"<p class='error'>{html.escape(error)}</p>" if error else ""}
    <label>管理员密码 <input type="password" name="password" autocomplete="current-password" required autofocus></label>
    <button type="submit">登录</button>
  </form>
</body>
</html>"""
    return page.encode("utf-8")


def project_form(project: Optional[dict] = None) -> bytes:
    project = normalize_project(project or {}, next_project_id(read_projects()))
    is_edit = bool(project.get("id") and any(item["id"] == project["id"] for item in read_projects()))
    title = "编辑项目" if is_edit else "新增项目"
    materials = "\n".join(project.get("materials", []))
    image = project.get("image", "")
    image_preview = f'<p><img class="preview" src="{html.escape(image)}" alt="项目图片"></p>' if image else ""
    body = f"""
      <div class="toolbar">
        <div>
          <h1>{title}</h1>
          <p class="muted">图片、项目名称、简介、物料、源码链接、演示视频和配置文档都可以在这里维护。</p>
        </div>
        <a class="button secondary" href="/admin">返回列表</a>
      </div>
      <form class="panel grid" method="post" action="/admin/project/save" enctype="multipart/form-data">
        <input type="hidden" name="existingImage" value="{html.escape(image)}">
        <label>项目编号 <input name="id" type="number" value="{project["id"]}" required></label>
        <label>获取方式 <input name="access" value="{html.escape(project.get("access", ""))}" placeholder="付费获取"></label>
        <label class="full">项目名称 <input name="name" value="{html.escape(project.get("name", ""))}" required></label>
        <label class="full">项目简介 <textarea name="description" required>{html.escape(project.get("description", ""))}</textarea></label>
        <label class="full">核心器件 / 技术 <textarea name="tech" placeholder="STM32、OLED、WiFi...">{html.escape(project.get("tech", ""))}</textarea></label>
        <label class="full">所需物料 <textarea name="materials" placeholder="每行一个，也可以用逗号分隔">{html.escape(materials)}</textarea></label>
        <label class="full">项目图片 <input name="imageFile" type="file" accept="image/png,image/jpeg,image/webp,image/gif"></label>
        <div class="full">{image_preview}</div>
        <label class="full">源码链接 <input name="sourceUrl" value="{html.escape(project.get("sourceUrl", ""))}" placeholder="https://..."></label>
        <label class="full">演示视频 <input name="demoVideoUrl" value="{html.escape(project.get("demoVideoUrl", ""))}" placeholder="https://..."></label>
        <label class="full">配置文档 <input name="configDocUrl" value="{html.escape(project.get("configDocUrl", ""))}" placeholder="https://..."></label>
        <div class="full actions">
          <button type="submit">保存项目</button>
          <a class="button secondary" href="/admin">取消</a>
        </div>
      </form>
    """
    return admin_layout(title, body)


def admin_list() -> bytes:
    projects = read_projects()
    rows = []
    for project in projects:
        rows.append(f"""
          <tr>
            <td>P{project["id"]:03d}</td>
            <td><strong>{html.escape(project["name"])}</strong><br><span class="muted">{html.escape(project["description"][:90])}</span></td>
            <td>{html.escape(project.get("access", ""))}</td>
            <td class="muted">{html.escape(project.get("updatedAt", ""))}</td>
            <td>
              <div class="actions">
                <a class="button secondary" href="/admin/project?id={project["id"]}">编辑</a>
                <form method="post" action="/admin/project/delete" onsubmit="return confirm('确认删除这个项目？')">
                  <input type="hidden" name="id" value="{project["id"]}">
                  <button class="danger" type="submit">删除</button>
                </form>
              </div>
            </td>
          </tr>
        """)

    body = f"""
      <div class="toolbar">
        <div>
          <h1>项目管理</h1>
          <p class="muted">当前共 {len(projects)} 个项目。修改后前台会通过接口自动读取最新数据。</p>
        </div>
        <a class="button" href="/admin/project">新增项目</a>
      </div>
      <div class="panel">
        <table>
          <thead><tr><th>编号</th><th>项目</th><th>获取方式</th><th>更新时间</th><th>操作</th></tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
      </div>
    """
    return admin_layout("项目管理", body)


class Handler(BaseHTTPRequestHandler):
    server_version = "XhLabServer/1.0"

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - - [%s] %s\n" % (self.client_address[0], self.log_date_time_string(), fmt % args))

    def send_bytes(self, body: bytes, status: int = 200, content_type: str = "text/html; charset=utf-8", headers: Optional[dict[str, str]] = None) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def send_head_only(self, status: int = 200, content_type: str = "text/html; charset=utf-8", content_length: int = 0) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(content_length))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

    def send_json(self, payload: object, status: int = 200) -> None:
        self.send_bytes(json.dumps(payload, ensure_ascii=False).encode("utf-8"), status, "application/json; charset=utf-8")

    def redirect(self, target: str, status: int = 303, headers: Optional[dict[str, str]] = None) -> None:
        body = redirect_html(target)
        self.send_response(status)
        self.send_header("Location", target)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def read_body(self) -> bytes:
        length = int(self.headers.get("content-length", "0"))
        if length > MAX_BODY_SIZE:
            raise ValueError("Request body too large")
        return self.rfile.read(length)

    def is_admin(self) -> bool:
        raw = self.headers.get("Cookie", "")
        jar = cookies.SimpleCookie(raw)
        morsel = jar.get("xh_admin")
        return verify_session(morsel.value if morsel else None)

    def require_admin(self) -> bool:
        if self.is_admin():
            return True
        self.redirect("/admin/login")
        return False

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/projects":
            self.send_json({"projects": public_projects()})
            return
        if path == "/admin/login":
            self.send_bytes(login_page())
            return
        if path == "/admin":
            if self.require_admin():
                self.send_bytes(admin_list())
            return
        if path == "/admin/project":
            if not self.require_admin():
                return
            params = urllib.parse.parse_qs(parsed.query)
            project_id = int(params.get("id", ["0"])[0] or 0)
            project = next((item for item in read_projects() if item["id"] == project_id), None)
            self.send_bytes(project_form(project))
            return
        if path.startswith("/uploads/"):
            self.serve_file(UPLOAD_DIR, path.removeprefix("/uploads/"))
            return

        self.serve_static(path)

    def do_HEAD(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/projects":
            body = json.dumps({"projects": public_projects()}, ensure_ascii=False).encode("utf-8")
            self.send_head_only(200, "application/json; charset=utf-8", len(body))
            return

        if path.startswith("/admin"):
            self.send_head_only(200)
            return

        if path in {"", "/"}:
            target = ROOT / "index.html"
        elif path.startswith("/uploads/"):
            target = (UPLOAD_DIR / posixpath.normpath(urllib.parse.unquote(path.removeprefix("/uploads/"))).lstrip("/")).resolve()
        else:
            clean = posixpath.normpath(urllib.parse.unquote(path.lstrip("/"))).lstrip("/")
            first = clean.split("/", 1)[0]
            allowed_files = {"index.html", "en.html", "favicon.ico"}
            allowed_dirs = {"assets", "data", "pages"}
            if clean not in allowed_files and first not in allowed_dirs:
                self.send_head_only(404, "text/plain; charset=utf-8")
                return
            target = (ROOT / clean).resolve()

        if not target.is_file():
            self.send_head_only(404, "text/plain; charset=utf-8")
            return

        content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
        self.send_head_only(200, content_type, target.stat().st_size)

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        try:
            body = self.read_body()
        except ValueError:
            self.send_bytes(b"Request body too large", 413, "text/plain; charset=utf-8")
            return

        if path == "/admin/login":
            fields = parse_form(body, self.headers.get("content-type", ""))
            if verify_admin_password(fields.get("password", "")):
                session = make_session()
                self.redirect("/admin", headers={"Set-Cookie": f"xh_admin={session}; HttpOnly; SameSite=Lax; Path=/; Max-Age={SESSION_SECONDS}"})
            else:
                self.send_bytes(login_page("密码不正确，请重新输入。"), 403)
            return

        if path == "/admin/logout":
            self.redirect("/admin/login", headers={"Set-Cookie": "xh_admin=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0"})
            return

        if not self.require_admin():
            return

        if path == "/admin/project/save":
            fields, files = parse_multipart(body, {key.lower(): value for key, value in self.headers.items()})
            projects = read_projects()
            image_path = save_upload(files.get("imageFile"))
            project_id = int(fields.get("id", "0") or 0)
            existing = next((item for item in projects if item["id"] == project_id), None)
            project = project_from_fields(fields, image_path, existing)
            projects = [item for item in projects if item["id"] != project["id"]]
            projects.append(project)
            write_projects(projects)
            self.redirect("/admin")
            return

        if path == "/admin/project/delete":
            fields = parse_form(body, self.headers.get("content-type", ""))
            project_id = int(fields.get("id", "0") or 0)
            projects = [item for item in read_projects() if item["id"] != project_id]
            write_projects(projects)
            self.redirect("/admin")
            return

        self.send_bytes(b"Not found", 404, "text/plain; charset=utf-8")

    def serve_static(self, path: str) -> None:
        if path in {"", "/"}:
            path = "/index.html"
        clean = posixpath.normpath(urllib.parse.unquote(path.lstrip("/"))).lstrip("/")
        first = clean.split("/", 1)[0]
        allowed_files = {"index.html", "en.html", "favicon.ico"}
        allowed_dirs = {"assets", "data", "pages"}
        if clean not in allowed_files and first not in allowed_dirs:
            self.send_bytes(b"Not found", 404, "text/plain; charset=utf-8")
            return
        self.serve_file(ROOT, clean)

    def serve_file(self, base: Path, relative: str) -> None:
        clean = posixpath.normpath(urllib.parse.unquote(relative)).lstrip("/")
        if clean.startswith("../"):
            self.send_bytes(b"Forbidden", 403, "text/plain; charset=utf-8")
            return
        target = (base / clean).resolve()
        try:
            target.relative_to(base.resolve())
        except ValueError:
            self.send_bytes(b"Forbidden", 403, "text/plain; charset=utf-8")
            return
        if not target.is_file():
            self.send_bytes(b"Not found", 404, "text/plain; charset=utf-8")
            return
        content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
        with target.open("rb") as file:
            self.send_bytes(file.read(), 200, content_type)


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--set-admin-password":
        set_admin_password_interactive()
        return

    ensure_storage()
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    httpd = ThreadingHTTPServer((host, port), Handler)
    print(f"XhLab server running at http://{host}:{port}")
    print("Admin password verifier ready.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
