# 部署说明

这个项目现在包含两部分：

- 前台：原来的 `index.html`、`assets/`、`data/`。
- 后台：`server.py`，提供 `/admin` 管理页面和 `/api/projects` 项目接口。

## 本地运行

```bash
python server.py
```

访问：

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/admin
```

如果没有设置 `ADMIN_PASSWORD`，首次运行会在 `storage/admin.secret` 生成一个临时后台密码。

## 服务器部署流程

假设部署目录为：

```text
/opt/xhlab/project_index
```

1. 上传整个项目目录到服务器。
2. 安装 Python 3 和 Nginx。
3. 编辑 `deploy/xhlab.service`，把 `ADMIN_PASSWORD=change-this-password` 改成你自己的强密码。
4. 复制 systemd 服务：

```bash
cp deploy/xhlab.service /etc/systemd/system/xhlab.service
systemctl daemon-reload
systemctl enable --now xhlab
```

5. 复制 Nginx 配置：

```bash
cp deploy/nginx-xhlab.conf /etc/nginx/conf.d/xhlab.conf
nginx -t
systemctl reload nginx
```

6. 在域名 DNS 后台添加解析：

```text
xhlab.fanjie.vip -> 服务器公网 IP
```

7. 配置 HTTPS：

```bash
certbot --nginx -d xhlab.fanjie.vip
```

后台地址：

```text
https://xhlab.fanjie.vip/admin
```

## 运行数据

后台新增/编辑的项目会保存到：

```text
storage/projects.json
```

上传图片会保存到：

```text
storage/uploads/
```

部署或迁移服务器时，记得备份整个 `storage/` 目录。
