# The moving parts

Outcome: a map of the pieces inside
every running Komga — what it keeps,
what it reads, and the three doors
other programs talk to it through — so
later chapters can name a part instead
of waving at the whole.

## The server and its config folder

Komga is one process: the jar, a Java
runtime, and a **config folder**
holding everything the server knows
that is not your comics. On its first
start the lab's server created, inside
the folder it was told to use
(transcript
`komga-lab/transcripts/t02-startup.txt`):

- `database.sqlite` — the catalogue:
  libraries, series, books, metadata,
  users, reading progress.
- `tasks.sqlite` — the queue of work
  (scans, analysis, thumbnails).
- `sessions.sqlite` — web sign-ins.
- `lucene/` — the search index.
- `logs/` — its own log files.

Your comic files are **not** copied
into the config folder. The database
holds descriptions of them — names,
page counts, sizes, a hash — and the
paths to them. Delete the config
folder and the library is gone but the
comics are untouched; delete a comic
file and the next scan notices it
missing. Chapter 13 covers what a
backup therefore is.

## The scanner

The **scanner** walks a library's root
folder and builds the catalogue from
what it finds. On the lab's library its
log line reads (transcript
`komga-lab/transcripts/t04-library.txt`):

```
Scan for extensions: [cbz, zip, cbr, rar, pdf, epub]
Scanned 1 series, 4 books, and 0 sidecars in 2.6ms
```

Folders become series, matching files
become books, and **sidecars** — small
companion files, like a series cover
image sitting beside the books — are
picked up too. After the walk, queued
tasks **analyse** each book: open the
archive, count and measure its pages,
note its real type from its contents
(not its name), and generate a
**thumbnail** from its first page.
Analysis is where the lab's text file
in a `.cbz` name was caught: catalogued
by the scan, marked UNSUPPORTED by the
analysis.

## Libraries, series, books, pages

The catalogue's four nouns:

- A **library** is one root folder
  plus its settings — what to scan,
  what to import, how often.
- A **series** is one folder inside
  the root, holding books that belong
  together. Chapter 1's rule lives
  here.
- A **book** is one archive file: an
  issue, a volume, a one-shot. It
  carries two bundles of facts: its
  **media** (type, status, page count)
  and its **metadata** (title, number,
  summary, authors).
- A **page** is one image inside the
  book's archive, in archive order.

## The three doors

Everything that uses Komga comes
through one of three doors, all on the
same port (25600 by default; the lab
used 18090):

- The **web interface**, served at the
  root address — the bookshop view and
  the reader, for people in a browser.
- The **REST API** under `/api/` —
  the same calls the web interface
  itself makes, available to your
  scripts. Most of this guide's lab
  work went through this door
  (chapter 8).
- The **OPDS feeds** under `/opds/` —
  the catalog in the standard format
  reading apps speak, in both its 1.2
  (XML) and 2.0 (JSON) dialects
  (chapter 9).

Behind all three doors sit **users and
roles** (chapter 10): an account says
who is asking, and its roles say
whether it may stream pages, download
files, or administer the server.

Check: name the four catalogue nouns
in order, say which file in the config
folder holds the catalogue, and name
the three doors. If you can, the rest
of the guide has somewhere to hang.
