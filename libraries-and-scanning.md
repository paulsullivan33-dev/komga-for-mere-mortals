# Libraries and scanning

Outcome: a library created on the
folder you prepared, a scan run and
understood, and the catalogue read
back with its numbers checked against
the files on disk.

## Create the library

A **library** is a name, a root folder,
and a page of settings. The web
interface has a form for it; the lab
used the API call the form sends
(transcript
`komga-lab/transcripts/t04-library.txt`):

```
$ curl -s -u keeper@clockwork.example:... \
    -X POST http://127.0.0.1:18090/api/v1/libraries \
    -H "Content-Type: application/json" \
    -d '{"name": "Clockwork Library",
         "root": "/home/.../komga-lab/fixtures/library"}'
```

The 200 response is the whole library
record, and its defaults are worth
reading once, because they are the
server's posture in miniature:

- `"scanInterval":"EVERY_6H"` and
  `"scanOnStartup":false` — rescans
  happen on a timer, not constantly;
  chapter 13 returns to this.
- `"importComicInfoBook":true` and its
  siblings — embedded metadata is
  welcome (chapter 12).
- `"scanCbx":true,"scanPdf":true,
  "scanEpub":true` — all book kinds on.
- `"convertToCbz":false` and
  `"repairExtensions":false` — Komga
  will not rewrite your files unless
  you ask it to. Remember this in
  chapter 16.
- `"seriesCover":"FIRST"` — a series
  shows its first book's cover until
  told otherwise.

Creating the library starts a scan by
itself: by the time the lab asked for
the series list seconds later, the
series was already there.

## What a scan does — and a rescan on demand

The scan walks the root, matches
folders to series and files to books,
then queues each new or changed book
for **analysis**: open it, identify
its real type from its contents, count
and measure its pages, make a
thumbnail. The log narrates both halves;
its summary line is the one to look
for:

```
Scanned 1 series, 4 books, and 0 sidecars in 2.607672ms
```

Asking for another scan — after filing
new books, or fixing a name — is one
call, answered 202 (accepted; the work
happens in the task queue):

```
$ curl -s -X POST -u keeper@... \
    http://127.0.0.1:18090/api/v1/libraries/0S5KAHEBJEPPY/scan
HTTP/1.1 202
```

## Read the catalogue back, and check it

Trust, then verify — the series record
reports its own counts:

```
"booksCount":4,"booksReadCount":0,"booksUnreadCount":4
```

And the book list is the real proof
(transcript
`komga-lab/transcripts/t05-series-and-books.txt`,
distilled to the fields that matter):

```
'Clockwork Orchard 001' number=1 size=160.5 KiB mediaStatus=READY       mediaType=application/zip pagesCount=6
'Clockwork Orchard 002' number=2 size=134.6 KiB mediaStatus=READY       mediaType=application/zip pagesCount=5
'Clockwork Orchard 003' number=3 size=106.7 KiB mediaStatus=READY       mediaType=application/zip pagesCount=4
'Clockwork Orchard 004' number=4 size=132 B     mediaStatus=UNSUPPORTED mediaType=text/plain      pagesCount=0
```

Three things to see in that table.
First, the generated files' page
counts — 6, 5, 4 — came back exactly.
The scanner is not estimating; it
opened the archives and counted.
Second, each healthy book's media type
is `application/zip` whatever the file
is named: a CBZ *is* a zip, and the
analysis says so. Third, book 004:
132 bytes of plain text, sniffed as
`text/plain`, status **UNSUPPORTED**,
comment `ERR_1001`, 0 pages — yet
still numbered, sized, and listed. A
scan does not drop what it cannot
read; it catalogues it and labels it.
Chapter 15 starts from that label when
a real book of yours wears it.

Check: create a library on a small
folder, then compare the book list
against the folder: one series per
folder, one book per file, numbers
matching the filenames, and every
media status READY — or a label you
can explain. That comparison *is* the
scan, understood.
