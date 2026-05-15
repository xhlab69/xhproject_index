from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "brand"
PNG_OUT = OUT_DIR / "xiahou-workshop-logo.png"
SVG_OUT = OUT_DIR / "xiahou-workshop-logo.svg"

W, H = 1600, 1100
SCALE = 3
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"

BLUE = "#064da8"
DARK = "#242a33"
LIGHT_BLUE = "#1d73d4"
MUTED = "#29313b"


def s(v):
    return int(v * SCALE)


def box(values):
    return tuple(s(v) for v in values)


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, s(size))


def text(draw, xy, value, size, fill, bold=False, anchor=None):
    draw.text((s(xy[0]), s(xy[1])), value, font=font(size, bold), fill=fill, anchor=anchor)


def line(draw, xy, fill, width=8):
    draw.line(box(xy), fill=fill, width=s(width), joint="curve")


def round_line(draw, points, fill, width):
    scaled = [(s(x), s(y)) for x, y in points]
    draw.line(scaled, fill=fill, width=s(width), joint="curve")
    radius = s(width) // 2
    for x, y in scaled:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill)


def circle(draw, cx, cy, r, fill, outline=None, width=1):
    draw.ellipse(box((cx - r, cy - r, cx + r, cy + r)), fill=fill, outline=outline, width=s(width))


def rounded(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box(xy), radius=s(radius), fill=fill, outline=outline, width=s(width))


def centered_segments(draw, center_x, y, segments, size, bold=False, anchor_y="mm"):
    fnt = font(size, bold)
    widths = [draw.textlength(value, font=fnt) for value, _ in segments]
    x = s(center_x) - sum(widths) / 2
    for (value, fill), width in zip(segments, widths):
        draw.text((x, s(y)), value, font=fnt, fill=fill, anchor="lm" if anchor_y == "mm" else None)
        x += width


def draw_chip(draw, cx, cy, size):
    half = size / 2
    rounded(draw, (cx - half, cy - half, cx + half, cy + half), 12, "#ffffff", BLUE, 10)
    rounded(draw, (cx - half + 18, cy - half + 18, cx + half - 18, cy + half - 18), 5, "#0f4f9f")
    pin_w = size * 0.08
    for i in range(5):
        x = cx - size * 0.38 + i * size * 0.19
        rounded(draw, (x, cy - half - 28, x + pin_w, cy - half - 8), 3, BLUE)
        rounded(draw, (x, cy + half + 8, x + pin_w, cy + half + 28), 3, BLUE)
    for i in range(5):
        y = cy - size * 0.38 + i * size * 0.19
        rounded(draw, (cx - half - 28, y, cx - half - 8, y + pin_w), 3, BLUE)
        rounded(draw, (cx + half + 8, y, cx + half + 28, y + pin_w), 3, BLUE)


def draw_circuit_side(draw, left=True):
    color = BLUE if left else DARK
    start_x = 170 if left else 1430
    dirn = 1 if left else -1
    base_y = 470
    lengths = [275, 385, 325]
    offsets = [-80, 0, 80]
    for length, off in zip(lengths, offsets):
        y = base_y + off
        circle(draw, start_x, y, 22, "#ffffff", color, 9)
        line(draw, (start_x + dirn * 22, y, start_x + dirn * length, y), color, 9)
        elbow_x = start_x + dirn * length
        line(draw, (elbow_x, y, elbow_x + dirn * 66, y - dirn * 0), color, 9)
        circle(draw, elbow_x + dirn * 74, y, 15, "#ffffff", color, 8)


def draw_logo_png():
    img = Image.new("RGB", (s(W), s(H)), "#ffffff")
    draw = ImageDraw.Draw(img)

    # Circular tech mark.
    draw.arc(box((435, 92, 1165, 782)), 214, 292, fill=BLUE, width=s(36))
    draw.arc(box((435, 92, 1165, 782)), 56, 134, fill=DARK, width=s(36))
    draw.arc(box((485, 142, 1115, 732)), 132, 222, fill=BLUE, width=s(28))
    draw.arc(box((485, 142, 1115, 732)), 312, 42, fill=DARK, width=s(28))

    # Pixel accents.
    for x, y, size, fill in [(1022, 118, 34, BLUE), (1078, 160, 28, BLUE), (1010, 178, 23, DARK)]:
        rounded(draw, (x, y, x + size, y + size), 5, fill)

    draw_circuit_side(draw, True)
    draw_circuit_side(draw, False)

    # Speed bars above the first character.
    rounded(draw, (474, 275, 788, 300), 4, BLUE)
    rounded(draw, (438, 325, 758, 350), 4, BLUE)

    # Main Chinese mark.
    text(draw, (622, 405), "夏", 245, BLUE, True, "mm")
    text(draw, (900, 405), "侯", 245, DARK, True, "mm")

    # A small diagonal bridge makes the mark feel less like plain font text.
    round_line(draw, [(690, 570), (798, 686), (910, 548)], BLUE, 22)

    draw_chip(draw, 800, 675, 124)

    # Brand text.
    centered_segments(draw, 800, 910, [("夏侯", BLUE), ("电子工坊", DARK)], 118, True)

    # Subtitle with decorative lines.
    line(draw, (310, 1010, 505, 1010), BLUE, 4)
    line(draw, (1095, 1010, 1290, 1010), BLUE, 4)
    text(draw, (800, 1010), "嵌入式单片机开发", 52, MUTED, False, "mm")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img.resize((W, H), Image.Resampling.LANCZOS).save(PNG_OUT, quality=96)


def write_svg():
    svg = f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="{W}" height="{H}" fill="white"/>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M475 642A346 346 0 0 1 1006 117" stroke="{BLUE}" stroke-width="36"/>
    <path d="M1125 281A346 346 0 0 1 594 806" stroke="{DARK}" stroke-width="36"/>
    <path d="M537 631A296 296 0 0 1 651 184" stroke="{BLUE}" stroke-width="28"/>
    <path d="M1063 253A296 296 0 0 1 949 700" stroke="{DARK}" stroke-width="28"/>
  </g>
  <g>
    <rect x="1022" y="118" width="34" height="34" rx="5" fill="{BLUE}"/>
    <rect x="1078" y="160" width="28" height="28" rx="5" fill="{BLUE}"/>
    <rect x="1010" y="178" width="23" height="23" rx="5" fill="{DARK}"/>
  </g>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M192 390H445" stroke="{BLUE}" stroke-width="9"/><circle cx="170" cy="390" r="17.5" fill="white" stroke="{BLUE}" stroke-width="9"/><circle cx="519" cy="390" r="11" fill="white" stroke="{BLUE}" stroke-width="8"/>
    <path d="M192 470H555" stroke="{BLUE}" stroke-width="9"/><circle cx="170" cy="470" r="17.5" fill="white" stroke="{BLUE}" stroke-width="9"/><circle cx="629" cy="470" r="11" fill="white" stroke="{BLUE}" stroke-width="8"/>
    <path d="M192 550H495" stroke="{BLUE}" stroke-width="9"/><circle cx="170" cy="550" r="17.5" fill="white" stroke="{BLUE}" stroke-width="9"/><circle cx="569" cy="550" r="11" fill="white" stroke="{BLUE}" stroke-width="8"/>
    <path d="M1408 390H1155" stroke="{DARK}" stroke-width="9"/><circle cx="1430" cy="390" r="17.5" fill="white" stroke="{DARK}" stroke-width="9"/><circle cx="1081" cy="390" r="11" fill="white" stroke="{DARK}" stroke-width="8"/>
    <path d="M1408 470H1045" stroke="{DARK}" stroke-width="9"/><circle cx="1430" cy="470" r="17.5" fill="white" stroke="{DARK}" stroke-width="9"/><circle cx="971" cy="470" r="11" fill="white" stroke="{DARK}" stroke-width="8"/>
    <path d="M1408 550H1105" stroke="{DARK}" stroke-width="9"/><circle cx="1430" cy="550" r="17.5" fill="white" stroke="{DARK}" stroke-width="9"/><circle cx="1031" cy="550" r="11" fill="white" stroke="{DARK}" stroke-width="8"/>
  </g>
  <rect x="474" y="275" width="314" height="25" rx="4" fill="{BLUE}"/>
  <rect x="438" y="325" width="320" height="25" rx="4" fill="{BLUE}"/>
  <text x="622" y="432" text-anchor="middle" dominant-baseline="middle" font-family="Microsoft YaHei, SimHei, sans-serif" font-size="245" font-weight="800" fill="{BLUE}">夏</text>
  <text x="900" y="432" text-anchor="middle" dominant-baseline="middle" font-family="Microsoft YaHei, SimHei, sans-serif" font-size="245" font-weight="800" fill="{DARK}">侯</text>
  <path d="M690 570L798 686L910 548" stroke="{BLUE}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
  <g>
    <rect x="738" y="613" width="124" height="124" rx="12" fill="white" stroke="{BLUE}" stroke-width="10"/>
    <rect x="756" y="631" width="88" height="88" rx="5" fill="#0F4F9F"/>
    <g fill="{BLUE}">
      <rect x="753" y="585" width="10" height="20" rx="3"/><rect x="777" y="585" width="10" height="20" rx="3"/><rect x="800" y="585" width="10" height="20" rx="3"/><rect x="824" y="585" width="10" height="20" rx="3"/><rect x="847" y="585" width="10" height="20" rx="3"/>
      <rect x="753" y="745" width="10" height="20" rx="3"/><rect x="777" y="745" width="10" height="20" rx="3"/><rect x="800" y="745" width="10" height="20" rx="3"/><rect x="824" y="745" width="10" height="20" rx="3"/><rect x="847" y="745" width="10" height="20" rx="3"/>
      <rect x="710" y="628" width="20" height="10" rx="3"/><rect x="710" y="652" width="20" height="10" rx="3"/><rect x="710" y="675" width="20" height="10" rx="3"/><rect x="710" y="699" width="20" height="10" rx="3"/><rect x="710" y="722" width="20" height="10" rx="3"/>
      <rect x="870" y="628" width="20" height="10" rx="3"/><rect x="870" y="652" width="20" height="10" rx="3"/><rect x="870" y="675" width="20" height="10" rx="3"/><rect x="870" y="699" width="20" height="10" rx="3"/><rect x="870" y="722" width="20" height="10" rx="3"/>
    </g>
  </g>
  <text x="800" y="925" text-anchor="middle" dominant-baseline="middle" font-family="Microsoft YaHei, SimHei, sans-serif" font-size="118" font-weight="800"><tspan fill="{BLUE}">夏侯</tspan><tspan fill="{DARK}">电子工坊</tspan></text>
  <path d="M310 1010H505M1095 1010H1290" stroke="{BLUE}" stroke-width="4"/>
  <text x="800" y="1016" text-anchor="middle" dominant-baseline="middle" font-family="Microsoft YaHei, SimHei, sans-serif" font-size="52" fill="{MUTED}">嵌入式单片机开发</text>
</svg>
"""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SVG_OUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    draw_logo_png()
    write_svg()
    print(PNG_OUT)
    print(SVG_OUT)
