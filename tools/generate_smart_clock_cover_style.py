from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "projects" / "stm32_wifi_smart_clock_cover_style.png"
LOGO_PATH = ROOT / "assets" / "images" / "brand" / "logo.png"

SCALE = 3
W, H = 1200, 900
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"

BLUE = "#064da8"
MID_BLUE = "#1f65c8"
TITLE_BLUE = "#3159c5"
DARK = "#1f2630"
CYAN = "#22bdd6"
LIGHT_BG = "#f7fbff"

BRAND_CN = "\u590f\u4faf\u7535\u5b50\u5de5\u574a"
BRAND_SHORT = "\u590f\u4faf\u5de5\u574a"
BRAND_EN = "XHLab"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size * SCALE)


def sc(v):
    return int(round(v * SCALE))


def xy(box):
    return tuple(sc(v) for v in box)


def text(draw, pos, content, size, fill, bold=False, anchor=None):
    draw.text((sc(pos[0]), sc(pos[1])), content, font=font(size, bold), fill=fill, anchor=anchor)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy(box), radius=sc(radius), fill=fill, outline=outline, width=sc(width))


def shadowed_round(canvas, box, radius, fill, outline=None, width=1, shadow=(0, 8), shadow_color="#bed4ee"):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    dx, dy = shadow
    ld.rounded_rectangle(xy((box[0] + dx, box[1] + dy, box[2] + dx, box[3] + dy)),
                         radius=sc(radius), fill=shadow_color)
    layer = layer.filter(ImageFilter.GaussianBlur(sc(2)))
    canvas.alpha_composite(layer)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(xy(box), radius=sc(radius), fill=fill, outline=outline, width=sc(width))


def pill(canvas, box, left="#1f65c8", right="#0b43a6", text_content="", size=31):
    draw = ImageDraw.Draw(canvas)
    x1, y1, x2, y2 = xy(box)
    w, h = x2 - x1, y2 - y1
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, w, h), radius=h // 2, fill=255)
    grad = Image.new("RGB", (w, h), left)
    gd = ImageDraw.Draw(grad)
    c1 = tuple(int(left[i:i + 2], 16) for i in (1, 3, 5))
    c2 = tuple(int(right[i:i + 2], 16) for i in (1, 3, 5))
    for yy in range(h):
        t = yy / max(1, h - 1)
        col = tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3))
        gd.line((0, yy, w, yy), fill=col)
    canvas.alpha_composite(Image.merge("RGBA", (*grad.split(), mask)), (x1, y1))
    draw.rounded_rectangle((x1, y1, x2, y2), radius=h // 2, outline="#78a8e8", width=sc(2))
    if text_content:
        text(draw, ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2 - 1), text_content, size, "#ffffff", True, "mm")


def crop_nonwhite(img):
    rgb = img.convert("RGB")
    inv = ImageOps.invert(rgb)
    # Keep pixels that are meaningfully non-white.
    mask = inv.convert("L").point(lambda p: 255 if p > 22 else 0)
    bbox = mask.getbbox()
    if not bbox:
        return img
    pad = 8
    bbox = (
        max(0, bbox[0] - pad),
        max(0, bbox[1] - pad),
        min(img.width, bbox[2] + pad),
        min(img.height, bbox[3] + pad),
    )
    return img.crop(bbox)


def paste_logo(canvas):
    draw = ImageDraw.Draw(canvas)
    card = (28, 26, 270, 164)
    shadowed_round(canvas, card, 16, "#ffffff", "#d4e5fb", 2, shadow=(0, 5), shadow_color="#cfe0f5")

    if LOGO_PATH.exists():
        logo = crop_nonwhite(Image.open(LOGO_PATH)).convert("RGBA")
        target_w, target_h = sc(218), sc(122)
        logo.thumbnail((target_w, target_h), Image.Resampling.LANCZOS)
        px = sc(card[0] + (card[2] - card[0]) / 2) - logo.width // 2
        py = sc(card[1] + (card[3] - card[1]) / 2) - logo.height // 2
        canvas.alpha_composite(logo, (px, py))
    else:
        text(draw, (183, 74), BRAND_CN, 30, BLUE, True, "mm")
        text(draw, (183, 105), BRAND_EN, 18, "#64748b", True, "mm")


def draw_top_rule(draw):
    draw.rectangle(xy((0, 0, W, 14)), fill=BLUE)
    draw.line(xy((372, 12, 1185, 12)), fill=BLUE, width=sc(4))


def draw_screw(draw, cx, cy):
    draw.ellipse(xy((cx - 8, cy - 8, cx + 8, cy + 8)), fill="#d7ede3", outline="#064e3b", width=sc(2))
    draw.ellipse(xy((cx - 3, cy - 3, cx + 3, cy + 3)), fill="#86b7a1")


def draw_ic(draw, x, y, w, h, label):
    rounded(draw, (x, y, x + w, y + h), 6, "#172033", "#050914", 2)
    for i in range(8):
        px = x - 6
        py = y + 8 + i * (h - 16) / 7
        draw.rectangle(xy((px, py, px + 7, py + 5)), fill="#b9c2cc")
        draw.rectangle(xy((x + w - 1, py, x + w + 6, py + 5)), fill="#b9c2cc")
    text(draw, (x + w / 2, y + h / 2), label, 10, "#f8fafc", True, "mm")


def draw_module(draw, x, y, w, h, fill, outline, label=None):
    rounded(draw, (x + 4, y + 5, x + w + 4, y + h + 5), 8, "#0b3e2c")
    rounded(draw, (x, y, x + w, y + h), 8, fill, outline, 3)
    if label:
        text(draw, (x + w / 2, y + h / 2), label, 13, "#ffffff", True, "mm")


def draw_realistic_pcb(canvas, ox, oy):
    draw = ImageDraw.Draw(canvas)

    # Drop shadow and board body.
    shadowed_round(canvas, (ox + 8, oy + 9, ox + 554, oy + 372), 14, "#0e8a48", "#075c32", 4,
                   shadow=(10, 14), shadow_color="#9eb8d8")
    draw = ImageDraw.Draw(canvas)
    rounded(draw, (ox + 22, oy + 22, ox + 532, oy + 350), 10, "#13934d", "#0b6237", 3)
    rounded(draw, (ox + 33, oy + 33, ox + 521, oy + 339), 6, "#168f4d", "#2bb76b", 1)

    # Mounting holes.
    for cx, cy in [(ox + 50, oy + 48), (ox + 504, oy + 48), (ox + 50, oy + 318), (ox + 504, oy + 318)]:
        draw_screw(draw, cx, cy)

    # Fine traces and pads.
    trace = "#8de2b2"
    trace2 = "#66c893"
    trace_paths = [
        (78, 86, 486, 86), (80, 131, 455, 131), (84, 181, 492, 181),
        (82, 231, 468, 231), (118, 285, 410, 285), (164, 62, 164, 298),
        (236, 76, 236, 276), (326, 68, 326, 310), (416, 72, 416, 291),
    ]
    for x1, y1, x2, y2 in trace_paths:
        draw.line(xy((ox + x1, oy + y1, ox + x2, oy + y2)), fill=trace, width=sc(2))
    for i in range(30):
        x = ox + 92 + (i % 10) * 37
        y = oy + 96 + (i // 10) * 75
        draw.ellipse(xy((x - 3, y - 3, x + 3, y + 3)), fill=trace2)

    # Blue-pill STM32 module, central and raised.
    draw_module(draw, ox + 155, oy + 122, 240, 88, "#1e56bd", "#0e3188")
    rounded(draw, (ox + 185, oy + 148, ox + 365, oy + 178), 3, "#102f6f")
    text(draw, (ox + 275, oy + 164), "STM32F103", 17, "#ffffff", True, "mm")
    for i in range(16):
        px = ox + 166 + i * 14
        draw.rectangle(xy((px, oy + 108, px + 6, oy + 122)), fill="#dfe9f6")
        draw.rectangle(xy((px, oy + 210, px + 6, oy + 224)), fill="#dfe9f6")
    draw.ellipse(xy((ox + 205, oy + 186, ox + 219, oy + 200)), fill="#f6c445", outline="#9a6a00", width=sc(1))
    rounded(draw, (ox + 326, oy + 187, ox + 358, oy + 202), 3, "#cbd5e1")

    # WiFi module.
    draw_module(draw, ox + 88, oy + 52, 130, 62, "#1f4fb8", "#173889")
    for i in range(4):
        draw.rectangle(xy((ox + 109 + i * 24, oy + 66, ox + 121 + i * 24, oy + 98)), fill="#dbeafe")
    text(draw, (ox + 153, oy + 41), "ESP8266", 14, "#dbeafe", True, "mm")

    # RTC board with coin cell.
    draw_module(draw, ox + 382, oy + 54, 96, 64, "#2563eb", "#102f80")
    draw.ellipse(xy((ox + 430, oy + 66, ox + 462, oy + 98)), fill="#cfd7df", outline="#64748b", width=sc(2))
    rounded(draw, (ox + 394, oy + 70, ox + 420, oy + 96), 4, "#14213d")
    text(draw, (ox + 407, oy + 83), "RTC", 10, "#ffffff", True, "mm")

    # OLED display.
    rounded(draw, (ox + 205, oy + 238, ox + 345, oy + 326), 9, "#0d1b2a", "#0ea5e9", 3)
    rounded(draw, (ox + 216, oy + 249, ox + 334, oy + 315), 4, "#111827")
    text(draw, (ox + 275, oy + 273), "12:30", 24, "#76f4ff", True, "mm")
    text(draw, (ox + 275, oy + 300), "WiFi OK", 13, "#93c5fd", False, "mm")

    # Buttons and ICs.
    for i in range(4):
        bx, by = ox + 62, oy + 140 + i * 45
        rounded(draw, (bx, by, bx + 34, by + 28), 4, "#d1d5db", "#475569", 2)
        draw.ellipse(xy((bx + 10, by + 7, bx + 24, by + 21)), fill="#374151")
    draw_ic(draw, ox + 116, oy + 252, 56, 34, "DHT")
    draw_ic(draw, ox + 416, oy + 220, 62, 38, "BUZ")

    # Indicators.
    draw.ellipse(xy((ox + 412, oy + 272, ox + 450, oy + 310)), fill="#f04444", outline="#7f1d1d", width=sc(2))
    draw.ellipse(xy((ox + 374, oy + 284, ox + 397, oy + 307)), fill="#facc15", outline="#92400e", width=sc(2))
    draw.ellipse(xy((ox + 448, oy + 315, ox + 482, oy + 349)), fill="#1f2937", outline="#111827", width=sc(2))

    # USB connector and cable.
    rounded(draw, (ox + 530, oy + 170, ox + 605, oy + 222), 8, "#e5e7eb", "#cbd5e1", 2)
    draw.rectangle(xy((ox + 604, oy + 187, ox + 742, oy + 205)), fill="#e5e7eb")
    rounded(draw, (ox + 730, oy + 169, ox + 872, oy + 223), 25, "#f3f4f6", "#d1d5db", 2)


def draw():
    global canvas
    canvas = Image.new("RGBA", (sc(W), sc(H)), "#ffffff")
    draw = ImageDraw.Draw(canvas)

    draw_top_rule(draw)
    paste_logo(canvas)
    draw = ImageDraw.Draw(canvas)

    labels = [
        "\u8054\u7f51\u6821\u65f6",
        "OLED\u663e\u793a",
        "\u95f9\u949f\u63d0\u9192",
        "\u6309\u952e\u8bbe\u7f6e",
        "WiFi\u63a7\u5236",
        "\u6e29\u6e7f\u5ea6\u663e\u793a",
        "\u8fdc\u7a0b\u540c\u6b65",
        "\u8bfe\u7a0b\u8bbe\u8ba1",
    ]
    y = 190
    for item in labels:
        pill(canvas, (68, y, 330, y + 68), text_content=item, size=31)
        y += 85
    draw = ImageDraw.Draw(canvas)

    text(draw, (420, 128), "STM32\u9879\u76ee", 76, TITLE_BLUE, True)
    text(draw, (420, 215), "\u7269\u8054\u7f51\u667a\u80fd\u65f6\u949f", 76, TITLE_BLUE, True)

    draw_realistic_pcb(canvas, 535, 342)
    draw = ImageDraw.Draw(canvas)

    rounded(draw, (596, 750, 965, 806), 28, "#eaf2ff", "#a8c8f5", 2)
    text(draw, (780, 778), "STM32 + ESP8266 + OLED", 24, "#174ea6", True, "mm")

    draw.line(xy((40, 872, 1160, 872)), fill="#d6e6fb", width=sc(3))

    out = canvas.convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.save(OUT, quality=96)
    print(OUT)


if __name__ == "__main__":
    draw()
