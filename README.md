# Komga for Mere Mortals

A comic collection on a hard drive is
easy to start and hard to live with.
Folders multiply. Issue numbers hide
inside filenames in three different
styles. Your reading app wants the
files one way, your tablet another,
and nothing remembers which issue you
stopped at. **Komga** takes over the
serving: it is a program you run on
your own machine that scans the comic
folders you already have, builds a
library from them, and offers that
library to your browser and your
reading apps — with covers, series,
order, and your place kept for you.

One rule governs everything it does,
and this guide states it in chapter 1
and keeps pointing back to it: **Komga
serves the library you file, exactly
as you filed it. It reads your folders
and filenames to build its series and
their order, so the organising you do
on disk is the organising you get on
screen.** A tidy folder tree becomes a
tidy library. A messy one becomes a
messy library with a nice cover on it.
Komga does not move, rename, or repair
your files; the filing is yours, the
serving is its.

The lab behind this guide ran the real
thing: **Komga 1.30.0**, the official
jar from the project's GitHub
releases, checked against the
release's own SHA-256 sums and run on
OpenJDK 21. Against a small fictional
series the lab generated itself —
*Clockwork Orchard*, three numbered
issues of drawn pages, plus one file
that is plain text wearing a `.cbz`
name — the lab claimed the fresh
server exactly the way its web
interface does, created a library,
watched the scan find 1 series and 4
books, and proved the page counts
(6, 5, and 4) matched the generated
files. It read a page back through the
API and found it byte-for-byte
identical to the page inside the
archive; downloaded the whole first
issue through OPDS and found the file
byte-for-byte identical to the one on
disk; marked a book read and watched
the series counts move; added a second
user with no special roles and watched
that user get 403 where the roles said
no; and finally dropped in a new issue
and a `ComicInfo.xml`, rescanned, and
watched the new book appear and the
old book gain a real title, a summary,
and a writer. The text file in a
`.cbz` name stayed in the catalogue
the whole time as an unsupported book
with 0 pages — the lab kept it in
every count rather than tidying it
away.

What the lab could not do, it did not
fake. Nobody clicked through the web
interface: every step the interface
would take was done with the same API
call the interface itself makes, and
the transcripts show the calls. The
Docker route, other operating systems,
and e-book formats beyond the comic
archives are described from the
project's documentation and labelled
documented-only. `criteria.md` keeps
the full ledger.

## What this guide covers

- [**What Komga is**](what-komga-is.md) —
  the pile of files, the server that
  serves it, and the one rule
- [**The moving parts**](the-moving-parts.md) —
  the config folder, the scanner,
  libraries, series, books and pages,
  and the three doors in
- [**Installing Komga**](installing-komga.md) —
  the jar and Java the lab used, the
  Docker route, and the checks every
  install must pass
- [**Your first run**](your-first-run.md) —
  starting the server, claiming it with
  the first administrator account, and
  signing in
- [**Organising on disk**](organising-on-disk.md) —
  one folder per series, numbers in
  filenames, and what the scanner
  makes of them
- [**Libraries and scanning**](libraries-and-scanning.md) —
  pointing Komga at a folder, what a
  scan does, and reading its results
- [**Reading in the browser**](reading-in-the-browser.md) —
  the web interface, thumbnails, and
  the page stream the reader lives on
- [**The REST API**](the-rest-api.md) —
  basic auth, the series and book
  endpoints, and search
- [**OPDS and reading apps**](opds-and-reading-apps.md) —
  the catalog feed, downloading a book
  through it, and page streaming for
  apps
- [**Users and access**](users-and-access.md) —
  a second account, the roles, and
  what each role actually stops
- [**Reading progress**](reading-progress.md) —
  marking pages and books read, and
  the on-deck shelf
- [**Metadata and ComicInfo**](metadata-and-comicinfo.md) —
  what filenames can and cannot say,
  and the metadata file that changes
  the picture
- [**Running it for real**](running-it-for-real.md) —
  the config folder, the port, the
  settings, and what a backup is
- [**Real jobs**](real-jobs.md) — a new
  issue filed and scanned in, metadata
  added to an old issue, and a reader
  given an account
- [**The neighbours**](the-neighbours.md) —
  Kavita, Calibre, Ubooquity, and the
  other shapes a comic server takes
- [**Limits**](limits.md) — a server,
  not an editor: what it will not fix,
  convert, or fetch for you
- [**Troubleshooting**](troubleshooting.md) —
  the book that will not open, the
  series that split in two, and the
  login that goes nowhere
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Finding or downloading comics — Komga
serves a collection you already have
and has no part in building it.
Editing scans or fixing metadata
inside your files: chapter 12 shows
the one metadata file Komga reads,
and chapter 16 is plain about the
rest. Running a public service for
strangers: every example here binds to
the machine it runs on or a home
network, and accounts are for a
household, not the internet.

## How to use this guide

Read chapter 1 for the rule and
chapter 2 for the map of parts;
chapter 4 gets a server claimed and a
library scanned, and chapters 5 and 6
teach you to read what the scan made
of your folders. Chapter 5 is the one
to read before you point Komga at a
real collection, not after: the
library on screen will be the folders
on disk, wearing a cover. The lab's
generated comics live in
`komga-lab/fixtures/`, its generator
scripts beside them, and every claim's
evidence in `komga-lab/transcripts/`;
its distilled commands are
`examples/commands.txt` and its notes
`examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Calibre for Mere Mortals](https://paulsullivan33-dev.github.io/calibre-for-mere-mortals/)
- [Docker for Mere Mortals](https://paulsullivan33-dev.github.io/docker-for-mere-mortals/)
- [Java for Mere Mortals](https://paulsullivan33-dev.github.io/java-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/komga-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/komga-for-mere-mortals/blob/main/LICENSE-CODE).
