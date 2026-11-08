# Reading in the browser

Outcome: how the web interface shows
the library and reads a book — and the
proof, taken at the API level the
interface itself uses, that the page
you are shown is the page inside your
file, unchanged.

An honesty note first, in this guide's
own rule: the lab did not click
through the web interface. It fetched
what the interface fetches — pages,
thumbnails, book records — through the
same endpoints, and checked the bytes.
What the screens look like is the
project's own presentation; what they
serve is measured here.

## What the interface is built from

The server's root address serves the
interface — the lab's fetch returned
its page with `<title>Komga</title>`
and the application bundle behind it
(transcript
`komga-lab/transcripts/t03-first-user.txt`). Everything
on screen is an API result rendered:
the shelf is the series list of
chapter 6, a series page is its book
list, and the covers are **thumbnails**
the analysis made — a JPEG rendered
from page 1:

```
$ curl -s -u keeper@... -o thumb.jpg \
    http://127.0.0.1:18090/api/v1/books/0S5KAHF72EN6M/thumbnail
HTTP 200  content-type image/jpeg  9977 bytes  (218x300)
```

(transcript
`komga-lab/transcripts/t11-thumbnail-opds2-settings.txt`).
A series wears its first book's
thumbnail by default — the
`"seriesCover":"FIRST"` setting from
chapter 6 — so the cover of your
series is the cover of the issue you
filed first. File accordingly.

## The page stream

Reading is pages, fetched one at a
time. A book's page list names each
page's file, type, and dimensions —
for the lab's first issue, the six
generated PNGs at 800×1100, with byte
sizes matching the generator's own
record exactly (transcript
`komga-lab/transcripts/t06-page-image.txt`):

```
{"number":1,"fileName":"page-01.png","mediaType":"image/png",
 "width":800,"height":1100,"sizeBytes":31402}
```

Fetching page 1 returns the image
itself:

```
$ curl -s -u keeper@... \
    http://127.0.0.1:18090/api/v1/books/0S5KAHF72EN6M/pages/1
HTTP 200  Content-Type: image/png  Content-Length: 31402
```

The lab compared hashes: the served
page and the `page-01.png` inside the
CBZ on disk are the *same bytes*
(SHA-256 `688ccb3e…ad8` both ways).
Komga does not recompress, resize, or
improve your pages on the way through
the ordinary page endpoint; it opens
the archive and hands the page over.
What the reader adds is presentation —
page turns, spreads, reading
direction, zoom — in the browser, on
top of the stream. Readers who want
the file itself use the download the
FILE_DOWNLOAD role guards (chapters 9
and 10).

Two boundaries of the stream, both
measured. Ask for a page of the
UNSUPPORTED book 004 and the answer is
404 with a plain message, "Book
analysis failed" — there are no pages
to give. And ask for a page with no
credentials and the answer is 401:
the reader is behind the account, like
everything else.

The web reader is one way to read —
the house way, always available,
nothing to install. It is not the only
way, and for a tablet on a couch it is
often not the best way; that is what
OPDS (next-but-one chapter) is for.

Check: fetch one page of a real book
through the API and compare its byte
size with the page inside the archive
on disk. Equal sizes — and a thumbnail
that is visibly page 1 — mean the
chain from file to screen is the one
this chapter describes.
