# Real jobs

Outcome: three ordinary jobs, whole —
a new issue joining a running library,
metadata arriving for a book that had
none, and a reader joining the server —
each one assembled from chapters you
have already read, each one run by the
lab.

## Job 1: a new issue arrives

The steady-state job of every comic
server: issue 5 comes out (or is found,
or is finally scanned), and the
library should simply have it.

1. **File it where it belongs**: into
   the series folder, with the series'
   naming pattern — the lab wrote
   `Clockwork Orchard 005.cbz`, 3
   pages, beside its siblings (script
   `komga-lab/add-issue-005.py`).
2. **Rescan the library** (chapter 6):

   ```
   POST /api/v1/libraries/0S5KAHEBJEPPY/scan  →  202
   ```

   On a standing server the scan timer
   would find it within the interval;
   the call is for "now."
3. **Verify in the catalogue**:

   ```
   Scanned 1 series, 5 books, and 0 sidecars
   'Clockwork Orchard 005' status=READY pages=3
   ```

The new book slotted in as number 5
by its filename, the series grew, and
nobody touched a setting. The job is
chapter 1's rule as a workflow: the
work happens at the filing cabinet,
and Komga's part is to notice.

## Job 2: a book gains its metadata

Issue 3 had lived as a filename
(chapter 12). The job: give it a real
title, a summary, and its writer —
durably, inside the file.

1. **Write `ComicInfo.xml`** with the
   book's facts and add it to the CBZ
   (the lab's script rebuilt the
   archive with the same pages plus
   the XML).
2. **Rescan** — the same call as job 1.
   The changed file is re-analysed.
3. **Verify**: the book's record gains
   `title='The Glass Greenhouse'`, the
   summary, and
   `authors=[{'name': 'A. R. Fenwick',
   'role': 'writer'}]`; the series
   record gains the publisher; the page
   count stays 4, because metadata is
   not a page.

The contrast inside the same rescan
is the lesson: issue 005 arrived with
no ComicInfo and kept its filename for
a title. Inference fills what it can;
the file carries the rest.

## Job 3: a reader joins

The household job: someone gets an
account of their own, so their place
is kept separately from yours
(chapter 10).

1. **Create the account** as an
   administrator, `POST /api/v2/users`,
   choosing the roles on purpose —
   the lab's plain reader got USER
   only, deliberately.
2. **Decide the sharing** before
   handing the password over:
   `sharedAllLibraries` starts true;
   narrow it if the server holds
   shelves the reader should not see.
3. **Verify as the reader**: sign in,
   browse the catalog (200), and —
   because the lab withheld the roles —
   confirm a page fetch and a file
   download refuse (403). A reader who
   should read in apps needs
   PAGE_STREAMING; one who should take
   files away needs FILE_DOWNLOAD. Add
   roles deliberately, and the
   verification turns green on purpose
   rather than by default.

Each job ends in the catalogue, not on
the command line: a count moved, a
title changed, a role answered. That
is the habit this guide is really
teaching — Komga is a server, so its
truth is always one query away, and
every job above ends by asking.

Check: run job 1 on your own server
with any new file, and verify by the
series' book count and the new book's
page count. If the numbers on screen
match the file you filed, you can do
all three jobs — the other two are
the same shape.
