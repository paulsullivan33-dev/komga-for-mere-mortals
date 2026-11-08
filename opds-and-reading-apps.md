# OPDS and reading apps

Outcome: the catalog your reading apps
browse — its address, its shape, a
book downloaded through it byte-for-
byte, and the page-streaming dialect
apps use to read without downloading.

## What OPDS is, in one paragraph

**OPDS** (Open Publication Distribution
System) is a standard way for a server
to publish a browsable catalog of
books: feeds of entries, each entry a
book or a doorway to another feed, with
links to cover images, to the book
file itself, and to its pages. A
reading app — on a tablet, a phone, an
e-reader — is pointed at one catalog
address, signs in, and from then on
your library is simply *there* in the
app. Komga serves OPDS because comics
are mostly read somewhere other than
the server's own browser tab.

## The catalog

Komga's OPDS 1.2 catalog lives at:

```
http://127.0.0.1:18090/opds/v1.2/catalog
```

(same host and port as everything
else; 25600 on a default install).
With the lab keeper's basic-auth
credentials it answered 200,
`Content-Type: application/atom+xml`,
and a root feed of doorways (transcript
`komga-lab/transcripts/t07-opds.txt`):
**Keep Reading**, **On Deck**, **All
series**, **Latest series**, **Latest
books**, **All libraries**, and more.
With no credentials it answered 401 —
OPDS apps are given the account email
and password, and they present them
the same way `curl -u` does.

Following **All series** to the lab's
one series gave its book feed, and
each healthy book's entry carried the
links an app lives on:

```
<link type="application/zip"
      rel="http://opds-spec.org/acquisition"
      href=".../opds/v1.2/books/0S5KAHF72EN6M/file/Clockwork%20Orchard%20001.cbz"/>
<link type="image/jpeg" rel="http://opds-spec.org/image"
      href=".../opds/v1.2/books/0S5KAHF72EN6M/thumbnail"/>
<link pse:count="6" type="image/png"
      rel="http://vaemendis.net/opds-pse/stream"
      href=".../opds/v1.2/books/0S5KAHF72EN6M/pages/{pageNumber}"/>
```

Note the count in passing: the series
feed listed **3 entries, not 4**. The
UNSUPPORTED text file is in the
catalogue (chapter 6) but is not
offered to reading apps — there is
nothing an app could open.

## Downloading through OPDS

The acquisition link is the book file.
The lab followed it:

```
HTTP 200  content-type application/zip  164401 bytes
```

and hashed the result against the
fixture on disk:

```
63ee36ad…cbf3  via-opds.cbz
63ee36ad…cbf3  Clockwork Orchard 001.cbz   (on disk)
```

Identical. An OPDS download is your
file, whole — the same posture as the
page stream in chapter 7, at file
granularity. This is the transfer the
FILE_DOWNLOAD role guards: chapter
10's role-less reader was refused
here with 403 while still allowed to
browse the catalog with 200.

## Page streaming (OPDS-PSE)

Apps that read without downloading use
the third link: the **OPDS-PSE** page
stream, one image per address, page
numbers starting at **0** — where the
REST API counts from 1. The feed even
states the page count (`pse:count="6"`),
so an app knows the book's length
before fetching a page. The lab
fetched PSE page 0 and hashed it
against REST page 1: same bytes again.
Two dialects, one stream of your
pages, nothing re-encoded on the way.

Komga also serves an **OPDS 2.0**
catalog — JSON instead of XML — linked
from the 1.2 feed as its `alternate`;
the lab fetched `/opds/v2/catalog` and
got its navigation JSON back
(transcript
`komga-lab/transcripts/t11-thumbnail-opds2-settings.txt`). Newer apps may prefer it; the 1.2
feed is the one with the widest
support, and everything this chapter
proves was proved on 1.2.

Check: point a `curl -u` at your
`/opds/v1.2/catalog`, follow the series
link, and download one book through
its acquisition link. If the byte
count matches the file on disk, your
reading apps will meet the same
library you filed.
