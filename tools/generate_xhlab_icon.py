from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "brand"
PNG_OUT = OUT_DIR / "xhlab-icon.png"
SVG_OUT = OUT_DIR / "xhlab-icon.svg"

SIZE = 1024
SCALE = 3
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"


def s(v):
    return int(v * SCALE)


def box(values):
    return tuple(s(v) for v in values)


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, s(size))


def rounded(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box(xy), radius=s(radius), fill=fill, outline=outline, width=s(width))


def text(draw, xy, value, size, fill, bold=False, anchor=None):
    draw.text((s(xy[0]), s(xy[1])), value, font=font(size, bold), fill=fill, anchor=anchor)


def round_line(draw, points, fill, width):
    scaled = [(s(x), s(y)) for x, y in points]
    draw.line(scaled, fill=fill, width=s(width), joint="curve")
    r = s(width) // 2
    for x, y in scaled:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=fill)


def draw_png():
    img = Image.new("RGB", (s(SIZE), s(SIZE)), "#eaf4ff")
    draw = ImageDraw.Draw(img)

    # Clean rounded badge.
    rounded(draw, (64, 64, 960, 960), 132, "#073f9a")
    rounded(draw, (108, 108, 916, 916), 96, "#0b58c8", "#61a8ff", 6)

    # Minimal chip.
    rounded(draw, (248, 248, 776, 776), 72, "#ffffff", "#b8d7ff", 9)
    rounded(draw, (292, 292, 732, 732), 48, "#e9f5ff")

    pin_fill = "#d9ecff"
    for i in range(5):
        x = 344 + i * 68
        rounded(draw, (x, 202, x + 32, 254), 9, pin_fill)
        rounded(draw, (x, 770, x + 32, 822), 9, pin_fill)
    for i in range(5):
        y = 344 + i * 68
        rounded(draw, (202, y, 254, y + 32), 9, pin_fill)
        rounded(draw, (770, y, 822, y + 32), 9, pin_fill)

    # Simple XH mark.
    round_line(draw, [(355, 360), (505, 512), (355, 664)], "#20c1d8", 58)
    round_line(draw, [(505, 360), (355, 512), (505, 664)], "#20c1d8", 58)
    rounded(draw, (584, 352, 646, 672), 24, "#0b4fb3")
    rounded(draw, (712, 352, 774, 672), 24, "#0b4fb3")
    rounded(draw, (620, 482, 738, 542), 24, "#20c1d8")

    final = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    final.save(PNG_OUT, quality=96)


def write_svg():
    svg = """<svg width="1024" height="1024" viewBox="0 0 1024 1024" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="64" y="64" width="896" height="896" rx="132" fill="#073F9A"/>
  <rect x="108" y="108" width="808" height="808" rx="96" fill="#0B58C8" stroke="#61A8FF" stroke-width="6"/>
  <g fill="#D9ECFF">
    <rect x="344" y="202" width="32" height="52" rx="9"/><rect x="412" y="202" width="32" height="52" rx="9"/><rect x="480" y="202" width="32" height="52" rx="9"/><rect x="548" y="202" width="32" height="52" rx="9"/><rect x="616" y="202" width="32" height="52" rx="9"/>
    <rect x="344" y="770" width="32" height="52" rx="9"/><rect x="412" y="770" width="32" height="52" rx="9"/><rect x="480" y="770" width="32" height="52" rx="9"/><rect x="548" y="770" width="32" height="52" rx="9"/><rect x="616" y="770" width="32" height="52" rx="9"/>
    <rect x="202" y="344" width="52" height="32" rx="9"/><rect x="202" y="412" width="52" height="32" rx="9"/><rect x="202" y="480" width="52" height="32" rx="9"/><rect x="202" y="548" width="52" height="32" rx="9"/><rect x="202" y="616" width="52" height="32" rx="9"/>
    <rect x="770" y="344" width="52" height="32" rx="9"/><rect x="770" y="412" width="52" height="32" rx="9"/><rect x="770" y="480" width="52" height="32" rx="9"/><rect x="770" y="548" width="52" height="32" rx="9"/><rect x="770" y="616" width="52" height="32" rx="9"/>
  </g>
  <rect x="248" y="248" width="528" height="528" rx="72" fill="white" stroke="#B8D7FF" stroke-width="9"/>
  <rect x="292" y="292" width="440" height="440" rx="48" fill="#E9F5FF"/>
  <g stroke="#20C1D8" stroke-width="58" stroke-linecap="round" stroke-linejoin="round">
    <path d="M355 360L505 512L355 664"/><path d="M505 360L355 512L505 664"/>
  </g>
  <rect x="584" y="352" width="62" height="320" rx="24" fill="#0B4FB3"/>
  <rect x="712" y="352" width="62" height="320" rx="24" fill="#0B4FB3"/>
  <rect x="620" y="482" width="118" height="60" rx="24" fill="#20C1D8"/>
</svg>
"""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SVG_OUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    draw_png()
    write_svg()
    print(PNG_OUT)
    print(SVG_OUT)
