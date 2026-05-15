from pathlib import Path
import math
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "project-images" / "stm32_wifi_smart_clock_materials.png"

W, H = 1920, 1080
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def rounded(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, content, size, fill, bold=False, anchor=None):
    draw.text(xy, content, font=font(size, bold), fill=fill, anchor=anchor)


def wrap_pixels(draw, content, fnt, max_width):
    lines = []
    current = ""
    for ch in content:
        if ch == "\n":
            if current:
                lines.append(current.rstrip())
            current = ""
            continue
        trial = current + ch
        if draw.textlength(trial, font=fnt) > max_width and current:
            lines.append(current.rstrip())
            current = ch.lstrip()
        else:
            current = trial
    if current:
        lines.append(current.rstrip())
    return lines


def draw_wrapped(draw, xy, content, size, fill, bold=False, max_width=220, line_height=None, max_lines=2):
    fnt = font(size, bold)
    line_height = line_height or int(size * 1.35)
    lines = wrap_pixels(draw, content, fnt, max_width)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines[-1] and draw.textlength(lines[-1] + "...", font=fnt) > max_width:
            lines[-1] = lines[-1][:-1]
        lines[-1] += "..."
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_height
    return y


def gradient_bg():
    img = Image.new("RGB", (W, H), "#eef6ff")
    pix = img.load()
    c1 = (239, 247, 255)
    c2 = (246, 251, 255)
    for y in range(H):
        t = y / (H - 1)
        r = int(c1[0] * (1 - t) + c2[0] * t)
        g = int(c1[1] * (1 - t) + c2[1] * t)
        b = int(c1[2] * (1 - t) + c2[2] * t)
        for x in range(W):
            pix[x, y] = (r, g, b)
    return img


def draw_circuit_pattern(draw):
    color = "#d6e7f8"
    nodes = [(110, 170), (230, 170), (230, 255), (380, 255), (1510, 160), (1660, 160),
             (1660, 260), (1800, 260), (1190, 910), (1335, 910), (1335, 990),
             (1510, 990), (165, 880), (315, 880), (315, 980), (465, 980)]
    for i in range(0, len(nodes), 4):
        pts = nodes[i:i + 4]
        if len(pts) == 4:
            draw.line([pts[0], pts[1], pts[2], pts[3]], fill=color, width=3, joint="curve")
            for x, y in pts:
                draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill="#c2daf4")

    for x in range(80, W, 145):
        draw.line((x, H - 62, x + 48, H - 62), fill="#d9eafd", width=2)
        draw.ellipse((x + 52, H - 66, x + 60, H - 58), fill="#c5def7")


def icon_mcu(draw, x, y):
    rounded(draw, (x + 18, y + 22, x + 122, y + 92), 8, "#1aa36f", "#0e7e55", 2)
    rounded(draw, (x + 50, y + 42, x + 90, y + 74), 5, "#12323e")
    for i in range(9):
        px = x + 25 + i * 10
        draw.line((px, y + 15, px, y + 22), fill="#6b7280", width=3)
        draw.line((px, y + 92, px, y + 101), fill="#6b7280", width=3)
    text(draw, (x + 70, y + 111), "STM32", 16, "#0f3d34", True, "mm")


def icon_wifi(draw, x, y):
    rounded(draw, (x + 26, y + 26, x + 112, y + 92), 8, "#1e50ae", "#123d8d", 2)
    for i in range(4):
        draw.rectangle((x + 39 + i * 16, y + 37, x + 47 + i * 16, y + 76), fill="#d8e6ff")
    cx, cy = x + 70, y + 102
    for r in (22, 38, 54):
        draw.arc((cx - r, cy - r, cx + r, cy + r), 205, 335, fill="#17b4d8", width=4)
    draw.ellipse((cx - 5, cy - 5, cx + 5, cy + 5), fill="#17b4d8")


def icon_oled(draw, x, y):
    rounded(draw, (x + 16, y + 24, x + 124, y + 92), 9, "#0f172a", "#2241a8", 3)
    text(draw, (x + 70, y + 47), "12:30", 24, "#7ef9ff", True, "mm")
    text(draw, (x + 70, y + 75), "WiFi OK", 14, "#93c5fd", False, "mm")


def icon_rtc(draw, x, y):
    rounded(draw, (x + 22, y + 24, x + 118, y + 94), 8, "#2563eb", "#1d4ed8", 2)
    draw.ellipse((x + 69, y + 42, x + 105, y + 78), fill="#cbd5e1", outline="#64748b", width=2)
    rounded(draw, (x + 34, y + 42, x + 62, y + 74), 5, "#111827")
    text(draw, (x + 48, y + 59), "RTC", 13, "#ffffff", True, "mm")


def icon_dht(draw, x, y):
    rounded(draw, (x + 36, y + 22, x + 104, y + 98), 9, "#22c55e", "#15803d", 2)
    for row in range(4):
        for col in range(3):
            draw.ellipse((x + 51 + col * 14, y + 36 + row * 12,
                          x + 57 + col * 14, y + 42 + row * 12), fill="#0f5132")
    draw.rectangle((x + 48, y + 98, x + 54, y + 110), fill="#475569")
    draw.rectangle((x + 68, y + 98, x + 74, y + 110), fill="#475569")
    draw.rectangle((x + 88, y + 98, x + 94, y + 110), fill="#475569")


def icon_buttons(draw, x, y):
    for i, c in enumerate(["#ef4444", "#f59e0b", "#22c55e", "#3b82f6"]):
        bx = x + 25 + i * 24
        rounded(draw, (bx, y + 38, bx + 18, y + 78), 5, "#e5e7eb", "#94a3b8", 2)
        draw.ellipse((bx - 1, y + 29, bx + 19, y + 49), fill=c, outline="#1f2937", width=2)
    text(draw, (x + 70, y + 102), "SET  UP  OK", 13, "#475569", True, "mm")


def icon_buzzer(draw, x, y):
    draw.ellipse((x + 38, y + 28, x + 102, y + 92), fill="#111827", outline="#334155", width=3)
    draw.ellipse((x + 54, y + 44, x + 86, y + 76), fill="#374151")
    for r in (18, 31):
        draw.arc((x + 93 - r, y + 60 - r, x + 93 + r, y + 60 + r), -45, 45, fill="#0ea5e9", width=3)


def icon_led(draw, x, y):
    draw.line((x + 70, y + 81, x + 70, y + 110), fill="#475569", width=4)
    draw.line((x + 54, y + 88, x + 54, y + 110), fill="#475569", width=4)
    draw.polygon([(x + 47, y + 72), (x + 93, y + 72), (x + 83, y + 92), (x + 57, y + 92)],
                 fill="#facc15", outline="#ca8a04")
    draw.ellipse((x + 47, y + 36, x + 93, y + 78), fill="#fde68a", outline="#ca8a04", width=2)
    for p in [(x + 42, y + 34), (x + 98, y + 34), (x + 70, y + 19)]:
        draw.line((x + 70, y + 36, p[0], p[1]), fill="#f59e0b", width=3)


def icon_power(draw, x, y):
    rounded(draw, (x + 35, y + 35, x + 105, y + 82), 8, "#ffffff", "#94a3b8", 3)
    draw.rectangle((x + 51, y + 24, x + 61, y + 35), fill="#64748b")
    draw.rectangle((x + 79, y + 24, x + 89, y + 35), fill="#64748b")
    draw.line((x + 105, y + 58, x + 130, y + 58), fill="#2563eb", width=5)
    text(draw, (x + 70, y + 102), "5V / 3.3V", 14, "#475569", True, "mm")


def icon_stlink(draw, x, y):
    rounded(draw, (x + 38, y + 24, x + 102, y + 96), 8, "#dc2626", "#991b1b", 2)
    rounded(draw, (x + 49, y + 42, x + 91, y + 77), 5, "#ffffff")
    text(draw, (x + 70, y + 60), "ST", 20, "#dc2626", True, "mm")
    draw.rectangle((x + 61, y + 96, x + 79, y + 109), fill="#9ca3af")


def icon_wires(draw, x, y):
    colors = ["#ef4444", "#2563eb", "#f59e0b", "#22c55e"]
    for i, c in enumerate(colors):
        yy = y + 32 + i * 16
        draw.arc((x + 23, yy - 22, x + 117, yy + 22), 8, 172, fill=c, width=4)
    rounded(draw, (x + 32, y + 84, x + 108, y + 109), 4, "#e5e7eb", "#94a3b8", 2)
    for i in range(8):
        draw.line((x + 40 + i * 8, y + 88, x + 40 + i * 8, y + 106), fill="#cbd5e1", width=2)


def icon_case(draw, x, y):
    draw.polygon([(x + 36, y + 40), (x + 104, y + 28), (x + 120, y + 82), (x + 52, y + 96)],
                 fill="#dbeafe", outline="#60a5fa")
    draw.polygon([(x + 36, y + 40), (x + 52, y + 96), (x + 30, y + 82), (x + 18, y + 28)],
                 fill="#bfdbfe", outline="#60a5fa")
    rounded(draw, (x + 54, y + 48, x + 100, y + 74), 5, "#111827")
    text(draw, (x + 77, y + 61), "12:30", 12, "#7ef9ff", True, "mm")


ICONS = [
    icon_mcu,
    icon_wifi,
    icon_oled,
    icon_rtc,
    icon_dht,
    icon_buttons,
    icon_buzzer,
    icon_led,
    icon_power,
    icon_stlink,
    icon_wires,
    icon_case,
]


ITEMS = [
    ("核心主控", "STM32F103C8T6 最小系统板", "x1", "负责定时器、按键、显示与串口控制"),
    ("联网模块", "ESP8266 WiFi 模块", "x1", "常见 ESP-01S 串口版，支持联网校时"),
    ("显示模块", "0.96 寸 IIC OLED 显示屏", "x1", "显示时间、日期、联网状态"),
    ("时钟保持", "DS3231 RTC 时钟模块", "x1", "断电后保持时间，成品更稳定"),
    ("环境拓展", "DHT11 / DHT22 温湿度模块", "x1", "增加桌面温湿度显示卖点"),
    ("人机交互", "独立按键模块 / 轻触按键", "x3-4", "设置时间、模式切换、确认返回"),
    ("提示模块", "有源蜂鸣器模块", "x1", "闹钟、按键反馈、联网异常提示"),
    ("状态指示", "LED 指示灯模块", "x1-2", "WiFi、同步、报警状态提示"),
    ("供电材料", "5V USB 供电线 + 3.3V 电源模块", "x1", "给 STM32 与 WiFi 稳定供电"),
    ("下载调试", "ST-Link V2 下载器", "x1", "程序下载、在线调试、烧录固件"),
    ("连接固定", "杜邦线 + 面包板 / 洞洞板", "若干", "免焊调试，后期可转洞洞板固定"),
    ("外观成品", "亚克力底板 / 3D 打印外壳", "x1", "让项目看起来像可购买实物"),
]


def draw_card(draw, idx, x, y, w, h):
    tag, name, qty, desc = ITEMS[idx]
    rounded(draw, (x + 5, y + 8, x + w + 5, y + h + 8), 8, "#cbdcf0")
    rounded(draw, (x, y, x + w, y + h), 8, "#ffffff", "#d6e6f7", 2)
    rounded(draw, (x + 20, y + 24, x + 154, y + 158), 8, "#eef6ff", "#d8e9fb", 1)
    ICONS[idx](draw, x + 17, y + 31)

    rounded(draw, (x + 182, y + 22, x + 296, y + 56), 8, "#eaf2ff", "#cbdffd")
    text(draw, (x + 239, y + 39), tag, 18, "#1e50ae", True, "mm")
    rounded(draw, (x + w - 80, y + 22, x + w - 24, y + 56), 8, "#1e50ae")
    text(draw, (x + w - 52, y + 39), qty, 16, "#ffffff", True, "mm")

    text_x = x + 182
    text_w = w - 206
    y0 = y + 70
    y0 = draw_wrapped(draw, (text_x, y0), name, 23, "#111827", True, text_w, 31, 2)
    draw_wrapped(draw, (text_x, y0 + 6), desc, 16, "#475569", False, text_w, 24, 2)


def main():
    img = gradient_bg()
    draw = ImageDraw.Draw(img)
    draw_circuit_pattern(draw)

    rounded(draw, (96, 64, 1824, 202), 8, "#ffffff", "#d7e7f9", 2)
    rounded(draw, (96, 64, 116, 202), 0, "#1e50ae")
    text(draw, (154, 106), "项目材料图", 28, "#1e50ae", True)
    text(draw, (154, 160), "基于 STM32 与 WiFi 的物联网智能时钟系统设计", 46, "#0f172a", True)
    text(draw, (1764, 108), "STM32  |  WiFi  |  OLED", 24, "#2563eb", True, "ra")
    text(draw, (1764, 154), "大学生购买实物参考清单 · 现成模块方案", 21, "#64748b", False, "ra")

    card_w, card_h = 410, 186
    gap_x, gap_y = 32, 28
    start_x, start_y = 96, 250
    for idx in range(len(ITEMS)):
        row = idx // 4
        col = idx % 4
        draw_card(draw, idx, start_x + col * (card_w + gap_x), start_y + row * (card_h + gap_y), card_w, card_h)

    footer_y = 920
    rounded(draw, (96, footer_y, 1824, 1018), 8, "#e8f3ff", "#c7def8", 2)
    text(draw, (132, footer_y + 39), "购买提示", 26, "#1e50ae", True)
    tips = [
        "WiFi 模块优先选 ESP-01S/ESP8266 串口模块，注意 3.3V 稳定供电。",
        "OLED 建议选 4 针 IIC 版本，接线少、适合课程设计快速调试。",
        "若主打“成品实物”，建议加 RTC、蜂鸣器和外壳，展示效果更完整。",
    ]
    for i, tip in enumerate(tips):
        tx = 300 + i * 500
        draw.ellipse((tx, footer_y + 34, tx + 12, footer_y + 46), fill="#1e50ae")
        draw_wrapped(draw, (tx + 24, footer_y + 20), tip, 18, "#334155", False, 430, 26, 2)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, quality=96)
    print(OUT)


if __name__ == "__main__":
    main()
