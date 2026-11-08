#!/usr/bin/env python3
"""Generate the fictional comic fixtures for the Komga lab.

Creates, under fixtures/library/:
  Clockwork Orchard/Clockwork Orchard 001.cbz  (6 pages)
  Clockwork Orchard/Clockwork Orchard 002.cbz  (5 pages)
  Clockwork Orchard/Clockwork Orchard 003.cbz  (4 pages)
  Clockwork Orchard/Clockwork Orchard 004.cbz  (NOT a zip - plain text,
                                                the deliberately odd file)

Every page is an original generated image: coloured panels, simple
shapes, and printed text. No copied art, no real people or titles.
Run:  python3 make_fixtures.py
"""
import os
import zipfile

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "fixtures", "library")
SERIES_DIR = os.path.join(LIB, "Clockwork Orchard")
SERIES = "Clockwork Orchard"

# (issue number, page count, accent colour)
ISSUES = [
    (1, 6, (196, 84, 44)),
    (2, 5, (44, 110, 196)),
    (3, 4, (58, 150, 84)),
]

PAGE_W, PAGE_H = 800, 1100


def font(size):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # older Pillow
        return ImageFont.load_default()


def make_page(issue, page, pages, accent):
    img = Image.new("RGB", (PAGE_W, PAGE_H), (246, 242, 232))
    d = ImageDraw.Draw(img)
    # border and two simple "panels"
    d.rectangle([20, 20, PAGE_W - 20, PAGE_H - 20], outline=(30, 30, 30), width=6)
    d.rectangle([60, 120, PAGE_W - 60, 520], fill=accent)
    d.ellipse([300, 200, 500, 400], fill=(250, 220, 90), outline=(30, 30, 30), width=4)
    d.rectangle([60, 580, PAGE_W - 60, 980], fill=(225, 225, 215),
                outline=(30, 30, 30), width=4)
    # a little "clockwork tree": trunk, branches, gears as circles
    d.rectangle([385, 760, 415, 960], fill=(110, 72, 40))
    for cx, cy, r in [(330, 700, 70), (470, 680, 85), (400, 590, 60)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(90, 90, 90), width=8)
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(90, 90, 90))
    d.text((60, 45), f"{SERIES}", fill=(20, 20, 20), font=font(44))
    d.text((60, 1000), f"Issue {issue:03d} - page {page} of {pages}",
           fill=(20, 20, 20), font=font(36))
    d.text((90, 620), "The orchard keeper winds the trees at dawn.",
           fill=(40, 40, 40), font=font(28))
    return img


def main():
    os.makedirs(SERIES_DIR, exist_ok=True)
    for issue, pages, accent in ISSUES:
        cbz_path = os.path.join(SERIES_DIR, f"{SERIES} {issue:03d}.cbz")
        with zipfile.ZipFile(cbz_path, "w", zipfile.ZIP_DEFLATED) as z:
            for p in range(1, pages + 1):
                img = make_page(issue, p, pages, accent)
                name = f"page-{p:02d}.png"
                tmp = os.path.join(HERE, "_page.png")
                img.save(tmp, "PNG")
                z.write(tmp, name)
                print(f"{os.path.basename(cbz_path)} <- {name} "
                      f"({os.path.getsize(tmp)} bytes)")
        os.remove(os.path.join(HERE, "_page.png"))
        print(f"wrote {cbz_path} ({os.path.getsize(cbz_path)} bytes, {pages} pages)")

    odd = os.path.join(SERIES_DIR, f"{SERIES} 004.cbz")
    with open(odd, "w", encoding="utf-8") as f:
        f.write("This file is named .cbz but it is plain text, not a zip archive.\n")
        f.write("The lab keeps it to record how Komga treats a book it cannot open.\n")
    print(f"wrote {odd} ({os.path.getsize(odd)} bytes, deliberately not a zip)")


if __name__ == "__main__":
    main()
