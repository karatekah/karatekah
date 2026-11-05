"""Build a GitHub-compatible banner with the user's Unicode samurai drawing."""
from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
art = (ROOT / "assets" / "samurai.txt").read_text(encoding="utf-8").splitlines()
assert art and all(len(line) <= 60 for line in art)
lines = "\n".join(f'<tspan x="830" y="{44+i*13.0:.1f}" textLength="{len(line)*8.0:.1f}" lengthAdjust="spacingAndGlyphs" fill="{"#e1be80" if i < 8 else "#e9d5bc"}">{escape(line.replace(" ", "⠀"))}</tspan>' for i, line in enumerate(art))
banner = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-labelledby="title desc">
<title id="title">Karatekah — Crimson Dojo</title>
<desc id="desc">Karatekah. Samurai character art. Full stack development, cybersecurity and cloud. Made by: Ҝ卂尺卂ㄒ乇Ҝ卂卄</desc>
<defs>
<linearGradient id="ink" x2="1" y2=".5"><stop stop-color="#101117"/><stop offset="1" stop-color="#1c1018"/></linearGradient>
<linearGradient id="sun" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#9b3445"/><stop offset="1" stop-color="#572131"/></linearGradient>
<pattern id="texture" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".5" fill="#e2bc89" fill-opacity=".13"/></pattern>
<clipPath id="clip"><rect width="1200" height="420" rx="12"/></clipPath>
</defs>
<g clip-path="url(#clip)">
<rect width="1200" height="420" fill="url(#ink)"/>
<rect x="730" width="470" height="420" fill="url(#texture)"/>
<circle cx="930" cy="191" r="157" fill="none" stroke="#ae5460" stroke-opacity=".2"/>
<circle cx="930" cy="191" r="142" fill="url(#sun)"/>
<path d="M815 85A151 151 0 0 1 1068 252" stroke="#d6b36d" stroke-opacity=".5" fill="none"/>
<path d="M0 419H1200" stroke="#873540" stroke-width="2"/>
<g font-family="Segoe UI,Arial,sans-serif">
<text x="44" y="49" font-size="15" fill="#d6b36d" font-family="Consolas,Courier New,monospace">karatekah@github:~$ <tspan fill="#d1c1c7">./welcome</tspan></text>
<text x="39" y="153" font-size="64" font-weight="600" fill="#f4ece3">Ҝ卂尺卂ㄒ乇Ҝ卂卄</text>
<text x="44" y="212" font-size="28" font-weight="600" fill="#f4ece3">Built with discipline.</text>
<text x="44" y="250" font-size="19" fill="#d5c4cd">Full stack development · Cybersecurity · Cloud</text>
<text x="44" y="291" font-size="15" fill="#a99aa8">Terminal tools · Web applications · Open source</text>
<path d="M44 329H575" stroke="#53303b"/>
<path d="M44 329H98" stroke="#d6b36d" stroke-width="2"/>
<text x="44" y="372" font-size="17" fill="#e0be7e">Made by: Ҝ卂尺卂ㄒ乇Ҝ卂卄</text>
</g>
<text font-family="Segoe UI Symbol,Consolas,monospace" xml:space="preserve" font-size="18">{lines}</text>
<text x="930" y="379" text-anchor="middle" fill="#cb9497" font-size="12" font-family="Consolas,Courier New,monospace">[ discipline in every line ]</text>
</g>
<rect x=".5" y=".5" width="1199" height="419" rx="11.5" fill="none" stroke="#61313e" stroke-opacity=".5"/>
</svg>'''
ET.fromstring(banner)
(ROOT / "assets" / "hero.svg").write_text(banner, encoding="utf-8")
print("Built assets/hero.svg — full samurai v2")
