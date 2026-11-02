#!/usr/bin/env python3
"""Puts a hook on one of your photos in your brand design. 1080 x 1350 PNG, no accounts, no cost.

Usage:
  python3 render_post.py --brand brand/brand.json --photo my-photos/laptop.jpg \
      --hook "Your content plan is not the problem." --highlight "Your week is." \
      --out posts/2026-11-20_my-topic/image.png [--placement bottom|top] [--focus "50% 20%"]

--hook is the plain part, --highlight the marked part after it (at least one of them).
Needs Google Chrome, Chromium or Microsoft Edge on the computer. Fonts come from Bunny Fonts.
"""
import argparse
import html
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_BRAND = {
    "paper": "#f9f7f4", "ink": "#151110", "accent": "#E07A4A",
    "headline_font": "Anton", "label_font": "Special Elite", "eyebrow": "", "handle": "",
}
CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def find_browser() -> str:
    for path in CHROME_PATHS:
        if os.path.exists(path):
            return path
    for name in ("google-chrome", "chromium", "chromium-browser", "microsoft-edge"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("No browser found. Please install Google Chrome, then run this again.")


def rgba(color: str, alpha: float) -> str:
    c = color.lstrip("#")
    return f"rgba({int(c[0:2], 16)},{int(c[2:4], 16)},{int(c[4:6], 16)},{alpha})"


def build_html(b: dict, photo: Path, hook: str, highlight: str, placement: str, focus: str) -> str:
    words = len(f"{hook} {highlight}".split())
    size = 104 if words <= 6 else 92 if words <= 10 else 80
    paper, ink, accent = b["paper"], b["ink"], b["accent"]
    family = "|".join(f.lower().replace(" ", "-") + ":400" for f in (b["headline_font"], b["label_font"]))
    # The shade follows the length of the hook, so hair and hands stay visible.
    chars_per_line = max(8, int(952 / (size * 0.46)))
    lines = max(1, -(-len(f"{hook} {highlight}".strip()) // chars_per_line))
    text_height = int(lines * size * 1.06)
    hl = f' <span class="hl">{html.escape(highlight)}</span>' if highlight else ""
    if placement == "top":
        shade = f'<div style="position:absolute;left:0;right:0;top:0;height:{130 + text_height + 110}px;background:linear-gradient(to bottom,{rgba(paper,.95)} 0%,{rgba(paper,.88)} 72%,{rgba(paper,0)} 100%)"></div>'
        shade += f'<div style="position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(to bottom,{rgba(ink,0)},{rgba(ink,.7)})"></div>'
        block = f'<div style="position:absolute;left:64px;right:64px;top:130px;color:{ink}"><h1>{html.escape(hook)}{hl}</h1></div>'
    else:
        shade = f'<div style="position:absolute;left:0;right:0;bottom:0;height:{118 + text_height + 240}px;background:linear-gradient(to bottom,{rgba(ink,0)} 0%,{rgba(ink,.62)} 30%,{rgba(ink,.88)} 58%,{rgba(ink,.93)} 100%)"></div>'
        shade += f'<div style="position:absolute;left:0;right:0;top:0;height:220px;background:linear-gradient(to bottom,{rgba(paper,.75)},{rgba(paper,0)})"></div>'
        block = f'<div style="position:absolute;left:64px;right:64px;bottom:118px;color:{paper}"><h1>{html.escape(hook)}{hl}</h1></div>'
    eyebrow = f'<div class="eyebrow">{html.escape(b["eyebrow"])}</div>' if b["eyebrow"] else ""
    handle = f'<div class="handle">{html.escape(b["handle"])}</div>' if b["handle"] else ""
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.bunny.net/css?family={family}">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:{paper}}}
body{{position:relative}}
img{{position:absolute;left:0;top:0;width:1080px;height:1350px;object-fit:cover;object-position:{html.escape(focus)}}}
h1{{font-family:"{b["headline_font"]}",Impact,sans-serif;font-weight:400;text-transform:uppercase;font-size:{size}px;line-height:1.06;text-wrap:balance}}
.hl{{background:linear-gradient(transparent 12%,{accent} 12%,{accent} 92%,transparent 92%);padding:0 12px;color:{ink};-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.eyebrow{{position:absolute;left:64px;top:60px;font-family:"{b["label_font"]}","Courier New",monospace;font-size:28px;letter-spacing:.16em;text-transform:uppercase;color:{ink}}}
.handle{{position:absolute;left:64px;bottom:44px;font-family:"{b["label_font"]}","Courier New",monospace;font-size:26px;letter-spacing:.08em;color:{paper}}}
</style></head><body>
<img src="{photo.resolve().as_uri()}" alt="">
{shade}{eyebrow}{block}{handle}
</body></html>"""


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--brand", required=True)
    p.add_argument("--photo", required=True)
    p.add_argument("--hook", default="")
    p.add_argument("--highlight", default="")
    p.add_argument("--out", required=True)
    p.add_argument("--placement", choices=["bottom", "top"], default="bottom")
    p.add_argument("--focus", default="50% 20%")
    a = p.parse_args()
    if not (a.hook or a.highlight):
        p.error("--hook or --highlight is required")
    brand = {**DEFAULT_BRAND, **json.loads(Path(a.brand).read_text(encoding="utf-8"))}
    photo = Path(a.photo)
    if not photo.exists():
        sys.exit(f"Photo not found: {photo}")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "page.html"
        page.write_text(build_html(brand, photo, a.hook, a.highlight, a.placement, a.focus), encoding="utf-8")
        subprocess.run([find_browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                        "--virtual-time-budget=5000", "--allow-file-access-from-files",
                        f"--user-data-dir={tmp}/profile", f"--screenshot={out.resolve()}", page.as_uri()],
                       check=True, capture_output=True)
    print(json.dumps({"image": str(out), "bytes": out.stat().st_size}))


if __name__ == "__main__":
    main()
