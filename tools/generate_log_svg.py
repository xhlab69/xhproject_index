from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "brand" / "logo.svg"

BLUE = "#064DA8"
DARK = "#242A33"
MUTED = "#29313B"


SVG = f"""<svg width="1254" height="1254" viewBox="0 0 1254 1254" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="44%" r="62%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="72%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F4F6F8"/>
    </radialGradient>
    <filter id="softShadow" x="-8%" y="-8%" width="116%" height="116%">
      <feDropShadow dx="0" dy="8" stdDeviation="7" flood-color="#0B1A33" flood-opacity=".18"/>
    </filter>
  </defs>

  <rect width="1254" height="1254" fill="url(#bg)"/>

  <g filter="url(#softShadow)">
    <g fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M435 338A252 252 0 0 1 755 274" stroke="{BLUE}" stroke-width="28"/>
      <path d="M423 554A252 252 0 0 1 755 714" stroke="{BLUE}" stroke-width="24"/>
      <path d="M858 347A252 252 0 0 1 776 724" stroke="{DARK}" stroke-width="26"/>
    </g>

    <g fill="{BLUE}">
      <rect x="767" y="283" width="27" height="27" rx="4"/>
      <rect x="818" y="318" width="24" height="24" rx="4"/>
    </g>
    <rect x="746" y="318" width="20" height="20" rx="4" fill="{DARK}"/>

    <g fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M285 519H415L452 452" stroke="{BLUE}" stroke-width="9"/>
      <path d="M293 565H443L509 488" stroke="{BLUE}" stroke-width="9"/>
      <path d="M361 612H441L524 531" stroke="{BLUE}" stroke-width="9"/>
      <circle cx="337" cy="519" r="13" fill="white" stroke="{BLUE}" stroke-width="8"/>
      <circle cx="284" cy="565" r="14" fill="white" stroke="{BLUE}" stroke-width="8"/>
      <circle cx="356" cy="612" r="13" fill="white" stroke="{BLUE}" stroke-width="8"/>

      <path d="M837 520H928" stroke="{DARK}" stroke-width="9"/>
      <path d="M804 566H974" stroke="{DARK}" stroke-width="9"/>
      <path d="M860 612H903" stroke="{DARK}" stroke-width="9"/>
      <circle cx="929" cy="520" r="13" fill="white" stroke="{DARK}" stroke-width="8"/>
      <circle cx="975" cy="566" r="15" fill="white" stroke="{DARK}" stroke-width="8"/>
      <circle cx="903" cy="612" r="13" fill="white" stroke="{DARK}" stroke-width="8"/>
    </g>

    <rect x="431" y="355" width="229" height="21" rx="4" fill="{BLUE}"/>
    <rect x="407" y="390" width="219" height="20" rx="4" fill="{BLUE}"/>

    <text x="535" y="530" text-anchor="middle" dominant-baseline="middle"
      font-family="Microsoft YaHei, SimHei, sans-serif" font-size="185" font-weight="900"
      fill="{BLUE}">夏</text>
    <text x="730" y="530" text-anchor="middle" dominant-baseline="middle"
      font-family="Microsoft YaHei, SimHei, sans-serif" font-size="185" font-weight="900"
      fill="{DARK}">侯</text>

    <path d="M517 623L610 711L710 600" stroke="{BLUE}" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>

    <g>
      <rect x="576" y="619" width="104" height="104" rx="11" fill="white" stroke="{BLUE}" stroke-width="9"/>
      <rect x="594" y="637" width="68" height="68" rx="5" fill="#0F4F9F"/>
      <g fill="{BLUE}">
        <rect x="592" y="588" width="8" height="17" rx="3"/><rect x="615" y="588" width="8" height="17" rx="3"/><rect x="638" y="588" width="8" height="17" rx="3"/><rect x="661" y="588" width="8" height="17" rx="3"/>
        <rect x="592" y="737" width="8" height="17" rx="3"/><rect x="615" y="737" width="8" height="17" rx="3"/><rect x="638" y="737" width="8" height="17" rx="3"/><rect x="661" y="737" width="8" height="17" rx="3"/>
        <rect x="546" y="635" width="18" height="8" rx="3"/><rect x="546" y="660" width="18" height="8" rx="3"/><rect x="546" y="685" width="18" height="8" rx="3"/>
        <rect x="692" y="635" width="18" height="8" rx="3"/><rect x="692" y="660" width="18" height="8" rx="3"/><rect x="692" y="685" width="18" height="8" rx="3"/>
      </g>
    </g>
  </g>

  <g filter="url(#softShadow)">
    <text x="627" y="842" text-anchor="middle" dominant-baseline="middle"
      font-family="Microsoft YaHei, SimHei, sans-serif" font-size="95" font-weight="900">
      <tspan fill="{BLUE}">夏侯</tspan><tspan fill="{DARK}">电子工坊</tspan>
    </text>
    <path d="M285 925H372M883 925H970" stroke="{BLUE}" stroke-width="3"/>
    <text x="627" y="925" text-anchor="middle" dominant-baseline="middle"
      font-family="Microsoft YaHei, SimHei, sans-serif" font-size="42" letter-spacing="14" fill="{MUTED}">
      嵌入式单片机开发
    </text>
  </g>
</svg>
"""


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(SVG, encoding="utf-8")
    print(OUT)
