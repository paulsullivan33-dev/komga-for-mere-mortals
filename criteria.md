# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** The limits chapter names what the
   tool cannot do: it is a server, not an editor — it will not
   fix bad scans, wrong page order, missing pages, or metadata
   a filename cannot support, only present what is filed,
   labelled as honestly as the UNSUPPORTED book in the lab;
   metadata from filenames and folder layout is inference, and
   metadata from ComicInfo is unverified import — the lab ran
   that import and watched invented facts land with full
   authority; its conversion and repair options exist but
   default off, rewrite files when enabled, and were not run
   here, so no conversion or transcoding quality is claimed;
   it does not read the words or art inside pages, so search
   is catalogue search only; and reading itself happens in
   clients — OPDS apps and browsers — of which Komga's own
   web reader is one option, proved here at the API level
   rather than clicked through.
8. **The one rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *Komga serves the library
   you file, exactly as you filed it: it reads your folders
   and filenames to build series and order, so the organising
   you do on disk is the organising you get on screen* —
   before any procedure depends on it, and later chapters point
   back to it where the rule bites: the series that is really
   two folders, the book catalogued by its extension and
   judged by its contents, and the metadata an archive gains
   only when the file itself carries it.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is an Ubuntu 24.04 sandbox with OpenJDK
21.0.12.1. Komga **1.30.0** was the project's official release
jar (`komga-1.30.0.jar`, 127,123,335 bytes, from
`github.com/gotson/komga/releases/download/1.30.0/` — the
repository is gotson/komga and its tags carry no leading `v`),
verified against the release's own `checksums_sha256.txt`
(SHA-256 `cac820a26caf8c8cc2239351b5f7ac7c5ba13badfae5bb0ce2b2449f1dfd8ff3`,
matching). It ran from the lab's scratch folder with its config
folder inside the lab, bound to 127.0.0.1 port 18090. The lab
is in `komga-lab/`: a fixture generator
(`make_fixtures.py`, Pillow) that draws one fictional series,
*Clockwork Orchard* — three CBZ issues of 6, 5, and 4 generated
PNG pages, plus a fourth `.cbz` that is plain text on purpose;
a second script (`add-issue-005.py`) that later files a 3-page
issue 005 and rebuilds issue 003 with a `ComicInfo.xml` inside;
and the transcripts in `komga-lab/transcripts/`. All accounts,
names, and firms in the fixtures are invented.

Run for real, with transcripts as evidence:

- Version and integrity (t00): the jar's SHA-256 matched the
  release's published sum; `java -version` recorded.
- Startup (t02): banner `Version: 1.30.0`; `Starting
  ApplicationKt v1.30.0 using Java 21.0.12.1`; 95 database
  migrations applied to a fresh SQLite catalogue in the config
  folder; `Tomcat started on port 18090`; `Started
  ApplicationKt in 57.514 seconds`. The log also records three
  image plug-ins (HEIF, JPEG XL, one WebP reader) disabling
  themselves below Java 22; the limits chapter says so.
- Fixtures (t01): the generator's page record — issue page
  sizes and CBZ byte counts — which later transcripts check
  the server against.
- The first administrator (t03): before any user existed,
  `GET /api/v1/users/me` and an unauthenticated `POST
  /api/v1/users` both answered 401. The web interface's claim
  flow — found by reading the served application bundle —
  worked exactly as the interface calls it: `GET
  /api/v1/claim` answered `{"isClaimed":false}`; `POST
  /api/v1/claim` with `X-Komga-Email` / `X-Komga-Password`
  headers and an empty body answered 200 with the new account
  (roles ADMIN, FILE_DOWNLOAD, KOBO_SYNC, KOREADER_SYNC,
  PAGE_STREAMING, USER; `sharedAllLibraries: true`); the claim
  status then read `true`. Basic auth proved against
  `GET /api/v2/users/me` (200 with credentials, 401 without);
  the lab's first guess, `/api/v1/users/me`, answered 404 with
  "No endpoint GET /api/v1/users/me", and the transcript
  keeps it.
- Library and scan (t04): `POST /api/v1/libraries` with only a
  name and root answered 200 with the full default record
  (`scanInterval EVERY_6H`, `scanOnStartup false`,
  `importComicInfo*` true, `convertToCbz false`,
  `repairExtensions false`, `seriesCover FIRST`). Creation
  triggered a scan; the log records `Scan for extensions:
  [cbz, zip, cbr, rar, pdf, epub]` and `Scanned 1 series,
  4 books, and 0 sidecars`. An explicit
  `POST /api/v1/libraries/{id}/scan` answered 202 and
  rescanned.
- Series and books (t05): one series, *Clockwork Orchard*,
  from the folder name; books numbered 1–4 from the
  filenames, with media exactly as generated — 001 READY
  `application/zip` 6 pages, 002 READY 5 pages, 003 READY
  4 pages — and 004, the text file, catalogued as a book but
  UNSUPPORTED, media type sniffed as `text/plain`, 0 pages,
  comment `ERR_1001`.
- Pages (t06): the page list for book 001 matches the
  generator's six PNGs (800×1100, byte sizes identical);
  `GET /books/{id}/pages/1` answered 200 `image/png`,
  31,402 bytes, SHA-256 identical to the page inside the CBZ
  on disk. A page request for the unsupported book answered
  404 "Book analysis failed"; without credentials, 401.
- OPDS (t07): `GET /opds/v1.2/catalog` with basic auth
  answered 200 `application/atom+xml` with the root feed
  (Keep Reading, On Deck, All series, Latest series, Latest
  books, All libraries); without credentials, 401. The
  series feed listed 3 book entries — the unsupported book is
  not offered — each with a thumbnail link, an
  `application/zip` acquisition link, and an OPDS-PSE stream
  link stating `pse:count` 6, 5, 4. Downloading book 001
  through its acquisition link returned 164,401 bytes
  byte-identical (SHA-256) to the fixture on disk. The PSE
  page 0 fetch was byte-identical to the REST page 1 fetch.
- Search and progress (t08): `?search=Orchard` found the
  series (1), `?search=Zeppelin` found none (0). `PATCH
  /books/{id}/read-progress` answered 204; the book's
  readProgress went from null to page 3 (not completed) to
  page 6 completed; the series counts moved to
  `booksReadCount 1, booksUnreadCount 3`; `GET
  /api/v1/books/ondeck` then offered *Clockwork Orchard 002*.
- Users and roles (t09): user creation lives under v2 —
  `POST /api/v1/users` answered 404 even as admin.
  `POST /api/v2/users` as admin answered 201 with a reader
  holding only the USER role and `sharedAllLibraries: true`.
  As that reader: series list 200 (with the file path hidden
  — `"url":""` where the admin sees the path — and its own
  read counts at 0), OPDS catalog 200, page fetch 403,
  OPDS file download 403, library creation 403, user list
  403. The admin's user list answered with both accounts.
- A new issue and ComicInfo (t10): after filing issue 005
  (3 pages) and rebuilding issue 003 with a `ComicInfo.xml`,
  one rescan logged `Scanned 1 series, 5 books`; book 005
  appeared READY with 3 pages, and book 003 gained title
  "The Glass Greenhouse", the filed summary, and writer
  A. R. Fenwick, its page count unchanged at 4 — the XML was
  not counted as a page. The series record aggregated the
  writer, summary, and publisher Orchard Press (t11).
- Thumbnails, OPDS 2, settings (t11): a book thumbnail
  answered 200 `image/jpeg`, 9,977 bytes, 218×300 — generated
  from page 1. `GET /opds/v2/catalog` answered with its JSON
  navigation. `GET /api/v1/settings` as admin answered 200
  (opened, nothing changed).

Documented only — described from the project's documentation,
its served interface code, or the records above, not run, and
the text does not claim otherwise:

- The Docker install route and any platform other than this
  Linux sandbox; the distribution and community packages.
- Clicking through the web interface: every interface action
  in this guide was performed with the API call the interface
  itself makes. The reader's on-screen presentation,
  thumbnail regeneration (endpoint seen in the served bundle,
  not called), and the server settings screen (opened via its
  API, nothing changed) are described, not exercised.
- The command-line extras `--list-users` and the
  `--newpassword` reset.
- The KOBO_SYNC and KOREADER_SYNC roles and their device
  sync; deleting read progress and marking a whole series
  read or unread; collections, read lists, and metadata
  editing by hand in the interface.
- Library options the lab left at their defaults and did not
  exercise: `convertToCbz`, `repairExtensions`, EPUB and PDF
  books (the scanner lists them; no fixture used them), CBR
  files, one-shots configuration, sharing labels and
  per-library sharing changes, scan intervals other than the
  observed default, and sidecar files (the scans reported 0).
- The neighbouring tools in chapter 15 are characterised,
  not benchmarked, and the announced 2.0 line (including its
  Java 25 minimum) is reported from the project's blog, not
  tested.

Fixtures are this guide's own and deliberately generic: one
invented orchard, one invented writer, one invented press. No
example is modelled on any real person, network, service or
organisation. Two lab accidents are kept in the record rather
than tidied away: the first download of the jar was reported
complete prematurely by the shell while the transfer was
still running, so the lab re-verified the finished file's
size and SHA-256 against the release's sums before use
(t00); and the first-user transcript (t03) preserves the
401 and 404 dead ends that taught the guide where the claim
flow and the v2 users API actually live.
