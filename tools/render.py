"""Render the World Chronicle broadsheet from stories.json.

Build-time tool only: it builds a square 1024x1024 front page from
stories.json (local fonts in tools/fonts/), screenshots it with Playwright +
Chromium, and writes assets/entry.png inside the competition limits
(1024x1024, 1 MiB). The submitted program (main.ts) only copies that file,
so the entry itself needs no network and is trivially deterministic.

Layout follows the reviewer's structure: masthead + big date, one lead with
a schematic Gulf map (confirmed locations only, no trajectories, time labels
and attribution on the map), six main stories, verified briefs, a numbers
line, a ticker and a sources footer. One fact sentence per story; nothing
is squeezed into unreadably small type.

Usage:  python3 tools/render.py [--data stories.json] [--out assets/entry.png]
"""

import argparse
import hashlib
import json
import os
import sys
from html import escape as esc

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

PAGE_W, PAGE_H = 1024, 1024
MAX_SIDE = 1024
MAX_BYTES = 1_048_576

# Schematic Gulf coastline, approximate lon/lat. Drawn from the map's own
# shape, not traced from any image. The map is labelled schematic.
ARAB_COAST = [
    (48.2, 29.8), (49.0, 28.5), (50.0, 27.5), (50.8, 26.3), (51.5, 25.4),
    (52.5, 24.9), (54.0, 24.3), (55.0, 24.5), (56.0, 25.8), (56.6, 26.5),
]
IRAN_COAST = [
    (56.6, 26.5), (56.0, 26.9), (54.5, 26.9), (53.0, 27.3), (51.5, 28.0),
    (50.0, 29.2), (48.8, 29.9), (48.2, 29.8),
]


def load_data(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def font_css():
    fonts = os.path.join(HERE, "fonts")
    return """
@font-face { font-family: 'Chronicle Display'; font-style: normal;
  font-weight: 400 900; src: url('file://%s/PlayfairDisplay.ttf'); }
@font-face { font-family: 'Chronicle Text'; font-style: normal;
  font-weight: 200 800; src: url('file://%s/Newsreader.ttf'); }
@font-face { font-family: 'Chronicle Text'; font-style: italic;
  font-weight: 200 800; src: url('file://%s/Newsreader.ttf'); }
@font-face { font-family: 'Chronicle Label'; font-style: normal;
  font-weight: 100 900; src: url('file://%s/Inter.ttf'); }
""" % (fonts, fonts, fonts, fonts)


def style_block():
    return """
* { box-sizing: border-box; margin: 0; padding: 0; }
.sheet { width: 1024px; height: 1024px; background: #f6f2e8; color: #1b1b1b;
  font-family: 'Chronicle Text', Georgia, serif; padding: 14px 26px;
  overflow: hidden; position: relative; }
.topline { display: flex; justify-content: space-between;
  font-family: 'Chronicle Label', sans-serif; font-size: 13px; font-weight: 800;
  letter-spacing: 1.6px; text-transform: uppercase;
  border-bottom: 1px solid #222; padding-bottom: 4px; margin-bottom: 5px; }
.nameplate { text-align: center; border-bottom: 4px double #111;
  padding-bottom: 7px; }
.nameplate h1 { font-family: 'Chronicle Display', Georgia, serif;
  font-size: 48px; font-weight: 900; letter-spacing: 2px; line-height: 1;
  text-transform: uppercase; color: #101c2e; }
.nameplate .motto { font-family: 'Chronicle Display', Georgia, serif;
  font-style: italic; font-size: 11px; letter-spacing: 3px;
  text-transform: uppercase; color: #4a5a70; margin-top: 1px; }
.dateline { text-align: center; font-family: 'Chronicle Label', sans-serif;
  font-size: 17px; font-weight: 800; letter-spacing: 3px;
  text-transform: uppercase; padding: 4px 0 3px 0;
  border-bottom: 1px solid #111; }
.leadrow { display: flex; gap: 14px; padding: 7px 0 6px 0;
  border-bottom: 2px solid #111; }
.leadtext { flex: 1; }
.kicker { font-family: 'Chronicle Label', sans-serif; font-size: 11px;
  font-weight: 800; letter-spacing: 2px; color: #8c2f26;
  text-transform: uppercase; }
.leadtext h2 { font-family: 'Chronicle Display', Georgia, serif;
  font-size: 28px; font-weight: 900; line-height: 1.05; margin: 3px 0 4px 0;
  color: #101c2e; }
.leadtext .dek { font-family: 'Chronicle Text', Georgia, serif;
  font-style: italic; font-size: 15px; line-height: 1.3; color: #333; }
.leadtext .body { font-size: 13px; line-height: 1.32; margin-top: 6px; }
.mapbox { width: 280px; flex: none; border: 1px solid #33505e;
  background: #eef2ee; padding: 4px 6px 4px 6px; }
.mapbox .maptitle { font-family: 'Chronicle Label', sans-serif; font-size: 11px;
  font-weight: 800; letter-spacing: 1.6px; text-transform: uppercase;
  color: #1f2a37; margin-bottom: 2px; }
.mapbox .mapnote { font-family: 'Chronicle Label', sans-serif; font-size: 9px;
  color: #555; margin-top: 2px; line-height: 1.3; }
.numline { border-bottom: 2px solid #111; padding: 5px 0;
  font-family: 'Chronicle Label', sans-serif; font-size: 11px;
  letter-spacing: 0.3px; color: #333; white-space: nowrap; }
.numline b { color: #8c2f26; font-weight: 800; }
.numline .val { font-family: 'Chronicle Display', Georgia, serif;
  font-size: 15px; font-weight: 900; color: #8c2f26; }
.sectionhead { font-family: 'Chronicle Label', sans-serif; font-size: 11px;
  font-weight: 800; letter-spacing: 2.2px; text-transform: uppercase;
  border-bottom: 2px solid #111; padding: 5px 0 3px 0; margin-bottom: 4px; }
.maingrid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2px 16px;
  border-bottom: 2px solid #111; padding-bottom: 5px; margin-bottom: 2px; }
.main .tag { font-family: 'Chronicle Label', sans-serif; font-size: 10px;
  font-weight: 800; letter-spacing: 1.6px; color: #8c2f26;
  text-transform: uppercase; }
.main h3 { font-family: 'Chronicle Display', Georgia, serif; font-size: 16px;
  font-weight: 800; line-height: 1.1; margin: 2px 0 3px 0; color: #101c2e; }
.main p { font-size: 13px; line-height: 1.3; color: #333; }
.briefgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 3px 20px;
  padding-top: 1px; }
.brief .tag { font-family: 'Chronicle Label', sans-serif; font-size: 9px;
  font-weight: 800; letter-spacing: 1.4px; color: #8c2f26;
  text-transform: uppercase; }
.brief b { font-family: 'Chronicle Display', Georgia, serif; font-size: 14px;
  font-weight: 800; line-height: 1.12; display: block; color: #101c2e; }
.brief span { font-size: 12px; line-height: 1.22; color: #333; }
.tape { font-family: 'Chronicle Label', sans-serif; font-size: 13px;
  font-weight: 600; background: #1f2a37; color: #f2f5f8; padding: 6px 10px;
  letter-spacing: 0.3px; margin-top: 5px; white-space: nowrap;
  overflow: hidden; }
.footbar { position: absolute; left: 26px; right: 26px; bottom: 12px;
  border-top: 3px double #111; padding-top: 6px;
  font-family: 'Chronicle Label', sans-serif; font-size: 10px; font-weight: 600;
  letter-spacing: 0.7px; text-transform: uppercase; color: #333;
  display: flex; justify-content: space-between; }
"""


def project(lon, lat, width, height):
    x = (lon - 47.0) / (58.0 - 47.0) * width
    y = (30.6 - lat) / (30.6 - 24.0) * height
    return round(x, 1), round(y, 1)


def gulf_map_svg(lead):
    w, h = 268, 156
    coast = ARAB_COAST + IRAN_COAST[1:]
    points = " ".join(
        "%s,%s" % project(lon, lat, w, h) for lon, lat in coast
    )
    dots = []
    for mark in lead["markers"]:
        x, y = project(mark["lon"], mark["lat"], w, h)
        dots.append(
            '<circle cx="%s" cy="%s" r="4" fill="#8c2f26" stroke="#fff" '
            'stroke-width="1.2"/>' % (x, y)
        )
    # Hand-placed labels, one per dot, kept clear of each other.
    labels = (
        '<text x="30" y="41" font-family="Inter, sans-serif" font-size="10" '
        'font-weight="700" fill="#1f2a37">ALI AL SALEM, KUWAIT</text>'
        '<text x="76" y="130" font-family="Inter, sans-serif" font-size="10" '
        'font-weight="700" fill="#1f2a37">SHEIKH ISA, BAHRAIN</text>'
        '<text x="201" y="102" font-family="Inter, sans-serif" font-size="10" '
        'font-weight="700" fill="#1f2a37" text-anchor="end">QESHM ISLAND</text>'
        '<text x="266" y="152" font-family="Inter, sans-serif" font-size="10" '
        'font-weight="700" fill="#1f2a37" text-anchor="end">STRAIT OF HORMUZ</text>'
        '<text x="58" y="62" font-family="Inter, sans-serif" font-size="10" '
        'font-weight="700" fill="#33505e">PERSIAN GULF</text>'
    )
    return (
        '<svg width="%s" height="%s" viewBox="0 0 %s %s">'
        '<rect x="0" y="0" width="%s" height="%s" fill="#eef2ee"/>'
        '<polygon points="%s" fill="#cfe0ea" stroke="#33505e" '
        'stroke-width="1.4"/>'
        "%s%s</svg>" % (w, h, w, h, w, h, points, "".join(dots), labels)
    )


def section_lead(data):
    lead = data["lead"]
    return """<div class="leadrow">
<div class="leadtext">
<div class="kicker">%s</div>
<h2>%s</h2>
<div class="dek">%s</div>
<div class="body">%s</div>
</div>
<div class="mapbox">
<div class="maptitle">%s</div>
%s
<div class="mapnote">%s</div>
</div>
</div>""" % (
        esc(lead["kicker"]),
        esc(lead["headline"]),
        esc(lead["dek"]),
        esc(lead["body"]),
        esc(lead["map_title"]),
        gulf_map_svg(lead),
        esc(lead["attribution"]),
    )


def section_numbers(numbers):
    parts = []
    for value, label in numbers:
        parts.append(
            '<span class="val">%s</span> %s' % (esc(value), esc(label))
        )
    return (
        '<div class="numline"><b>BY THE NUMBERS</b> &nbsp;—&nbsp; %s</div>'
        % " &nbsp;·&nbsp; ".join(parts)
    )


def section_mains(mains):
    parts = []
    for main in mains:
        parts.append(
            """<div class="main"><div class="tag">%s</div>
<h3>%s</h3><p>%s</p></div>"""
            % (esc(main["region"]), esc(main["headline"]), esc(main["fact"]))
        )
    return (
        '<div class="sectionhead">Main stories</div>'
        '<div class="maingrid">%s</div>' % "".join(parts)
    )


def section_briefs(briefs):
    parts = []
    for brief in briefs:
        parts.append(
            """<div class="brief"><span class="tag">%s</span>
<b>%s</b><span>%s</span></div>"""
            % (
                esc(brief["region"]),
                esc(brief["headline"]),
                esc(brief["fact"]),
            )
        )
    return (
        '<div class="sectionhead">Verified briefs</div>'
        '<div class="briefgrid">%s</div>' % "".join(parts)
    )


def build_page(data):
    return """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<style>%s%s</style></head>
<body><div class="sheet">
<div class="topline"><span>%s</span><span>%s</span></div>
<div class="nameplate"><h1>%s</h1><div class="motto">%s</div></div>
<div class="dateline">%s</div>
%s
%s
%s
%s
<div class="tape">%s</div>
<div class="footbar"><span>%s</span><span>%s</span></div>
</div></body></html>""" % (
        font_css(),
        style_block(),
        esc(data["date_label"]),
        esc(data["paper"]),
        esc(data["paper"]),
        esc(data["tagline"]),
        esc(data["date_label"]),
        section_lead(data),
        section_numbers(data["numbers"]),
        section_mains(data["mains"]),
        section_briefs(data["briefs"]),
        esc(data["ticker"]),
        esc(data["footer"]["count"]),
        esc(data["footer"]["sources"]),
    )


def render_html_to_png(html_path, png_path):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(
            viewport={"width": PAGE_W, "height": PAGE_H},
            device_scale_factor=1,
        )
        page.goto("file://" + html_path)
        page.evaluate("() => document.fonts.ready")
        page.wait_for_timeout(400)
        overflow = page.evaluate(
            "() => document.querySelector('.sheet').scrollHeight"
        )
        page.screenshot(path=png_path)
        browser.close()
    return overflow


def save_within_limits(src_path, dst_path):
    from PIL import Image

    with Image.open(src_path) as im:
        if im.size != (MAX_SIDE, MAX_SIDE):
            im = im.resize((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        im.save(dst_path, format="PNG", optimize=True)
    size = os.path.getsize(dst_path)
    if size > MAX_BYTES:
        with Image.open(src_path) as im:
            rgb = im.convert("RGB")
            if rgb.size != (MAX_SIDE, MAX_SIDE):
                rgb = rgb.resize((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
            rgb.save(dst_path, format="JPEG", quality=88, optimize=True)
        size = os.path.getsize(dst_path)
    with open(dst_path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    return size, digest


def main():
    from PIL import Image

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default=os.path.join(ROOT, "stories.json"))
    parser.add_argument("--out", default=os.path.join(ROOT, "assets", "entry.png"))
    args = parser.parse_args()

    data = load_data(args.data)
    build_dir = os.path.join(HERE, "build")
    os.makedirs(build_dir, exist_ok=True)
    html_path = os.path.join(build_dir, "page.html")
    raw_png = os.path.join(build_dir, "page.png")

    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(build_page(data))
    print("wrote %s" % html_path)

    overflow = render_html_to_png(html_path, raw_png)
    print("sheet scrollHeight: %s (page is %s)" % (overflow, PAGE_H))
    if overflow > PAGE_H:
        print("WARNING: content overflows the page by %s px" % (overflow - PAGE_H))

    with Image.open(raw_png) as probe:
        print("raw render: %sx%s" % probe.size)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    size, digest = save_within_limits(raw_png, args.out)
    with Image.open(args.out) as final:
        dims = final.size
    print(
        "final: %s  %sx%s  %d bytes  sha256 %s"
        % (args.out, dims[0], dims[1], size, digest)
    )
    if size > MAX_BYTES:
        print("ERROR: over the 1 MiB limit", file=sys.stderr)
        return 1
    if dims[0] > MAX_SIDE or dims[1] > MAX_SIDE:
        print("ERROR: over the 1024x1024 limit", file=sys.stderr)
        return 1
    print("OK: within limits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
