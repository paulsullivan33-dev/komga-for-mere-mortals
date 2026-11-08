# Glossary

The terms, collected in one place.
Each is defined the way this guide
uses it.

**Acquisition link** — In an OPDS
feed, the link that downloads the
book's file itself, as opposed to a
link to another feed or an image.

**Analysis** — The step after a scan
opens each book: identify its real
type from its contents, count and
measure its pages, and generate its
thumbnail. Where a mislabelled file is
caught and marked.

**Basic auth** — HTTP's built-in
credential scheme: the account's email
and password sent with each request.
How scripts and OPDS apps sign in to
Komga.

**Book** — One archive file in the
catalogue: an issue, a volume, a
one-shot. Carries a media bundle (type,
status, page count) and a metadata
bundle (title, number, summary,
authors).

**CBZ / CBR** — The standard comic
archive formats: a CBZ is a zip
archive of page images; a CBR is the
same idea in the RAR format. Komga
reports a healthy CBZ's media type as
`application/zip`, because that is
what it is.

**Claim** — The one-time act of
creating a fresh server's first
account, through `/api/v1/claim`,
possible only while no user exists.
After the claim, the door is gone.

**ComicInfo** — A small XML file,
`ComicInfo.xml`, stored inside a comic
archive, carrying the book's metadata
(series, number, title, credits,
summary). Komga imports it on scan
when the library allows, which is the
default.

**Config folder** — The directory
holding everything the server knows
that is not your comics: the catalogue
database, tasks, sessions, search
index, logs. Set with
`--komga.config-dir`.

**Library** — One root folder plus its
settings (what to scan, what to
import, how often), as known to the
server. A server can hold several.

**Media status** — Analysis's verdict
on a book: READY for a book it could
open and count, UNSUPPORTED for one it
could not, with an error comment.

**Metadata** — The descriptive bundle
about a book or series — title,
number, summary, authors, publisher —
as distinct from the media facts.
Inferred from filenames, imported
from ComicInfo, or set by hand and
locked.

**On deck** — The server's "what to
read next" shelf: the next unread book
after your progress, computed from
read progress across a series.

**OPDS** — Open Publication
Distribution System: the standard
catalog format reading apps browse.
Komga serves the 1.2 (XML) feed at
`/opds/v1.2/catalog` and a 2.0 (JSON)
feed beside it.

**OPDS-PSE** — The page-streaming
extension to OPDS: one address per
page image, page numbers from 0, with
the page count stated in the feed, so
an app can read without downloading
the file.

**Page** — One image inside a book's
archive, in archive order. The unit
reading is made of.

**Read progress** — A per-user record
on a book: the page reached, whether
it is completed, and the dates. Set by
readers as they read; the shelves
(on deck, keep reading) are computed
from it.

**Role** — A permission on a user
account: USER, PAGE_STREAMING,
FILE_DOWNLOAD, ADMIN, and the sync
roles KOBO_SYNC and KOREADER_SYNC.
Roles decide which doors open for an
account.

**Scan** — The walk of a library's
root that matches folders to series
and files to books, then queues
analysis. Runs on library creation, on
a timer, and on request.

**Series** — One folder inside a
library's root, and the set of books
filed in it. Its name is the folder's
name until metadata says more.

**Sidecar** — A small companion file
beside the books — a series cover
image, a metadata file — that a scan
picks up and applies, counted
separately in the scan's report.

**Thumbnail** — The cover image the
server generates from a book's first
page during analysis, served as a
JPEG. A series shows its first book's
thumbnail by default.
