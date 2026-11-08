#!/usr/bin/env python3
"""Second-act fixture changes for the Komga lab (transcript t10).

1. Adds a new book, Clockwork Orchard 005.cbz (3 pages), as if a new
   issue had just been filed into the series folder.
2. Rebuilds Clockwork Orchard 003.cbz with the same 4 page images
   plus a ComicInfo.xml inside the archive, to test whether Komga
   reads embedded comic metadata.

Run after make_fixtures.py:  python3 add-issue-005.py
"""
import os
import zipfile

from make_fixtures import SERIES, SERIES_DIR, make_page

COMICINFO = """<?xml version="1.0" encoding="utf-8"?>
<ComicInfo>
  <Series>Clockwork Orchard</Series>
  <Number>3</Number>
  <Title>The Glass Greenhouse</Title>
  <Summary>The keeper builds a greenhouse of clock glass and plants a tree that ticks.</Summary>
  <Writer>A. R. Fenwick</Writer>
  <Publisher>Orchard Press</Publisher>
  <Year>2026</Year>
  <PageCount>4</PageCount>
</ComicInfo>
"""


def main():
    # 1. the new issue
    path5 = os.path.join(SERIES_DIR, f"{SERIES} 005.cbz")
    with zipfile.ZipFile(path5, "w", zipfile.ZIP_DEFLATED) as z:
        for p in range(1, 4):
            img = make_page(5, p, 3, (150, 84, 160))
            tmp = os.path.join(SERIES_DIR, "_p.png")
            img.save(tmp, "PNG")
            z.write(tmp, f"page-{p:02d}.png")
    os.remove(os.path.join(SERIES_DIR, "_p.png"))
    print(f"wrote {path5} ({os.path.getsize(path5)} bytes, 3 pages)")

    # 2. issue 003 rebuilt with ComicInfo.xml added
    path3 = os.path.join(SERIES_DIR, f"{SERIES} 003.cbz")
    with zipfile.ZipFile(path3, "w", zipfile.ZIP_DEFLATED) as z:
        for p in range(1, 5):
            img = make_page(3, p, 4, (58, 150, 84))
            tmp = os.path.join(SERIES_DIR, "_p.png")
            img.save(tmp, "PNG")
            z.write(tmp, f"page-{p:02d}.png")
        z.writestr("ComicInfo.xml", COMICINFO)
    os.remove(os.path.join(SERIES_DIR, "_p.png"))
    print(f"rewrote {path3} ({os.path.getsize(path3)} bytes, 4 pages + ComicInfo.xml)")


if __name__ == "__main__":
    main()
