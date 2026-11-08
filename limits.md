# Limits

Outcome: the honest boundary of the
tool, in one place. Komga is a
**server, not an editor** — nearly
every limit below is that sentence
applied. Each was either measured in
the lab or is stated in the project's
own material; `criteria.md` keeps the
two apart.

## It presents your files; it does not fix them

A bad scan stays bad. Missing pages
stay missing; a book whose pages are
in the wrong order inside the archive
is served in that order; a filename
that says nothing gives the book a
title that says nothing (chapter 12's
`title='Clockwork Orchard 003'` before
the ComicInfo arrived). The lab's
clearest exhibit is the text file in a
`.cbz` name: Komga catalogued it,
tested it, labelled it UNSUPPORTED
with its error comment — and left it
exactly where and what it was. Its
reply to a broken book is an honest
label, not a repair.

Two library settings gesture at
file-changing — `"convertToCbz"` and
`"repairExtensions"` — and both
default to **false** in the record the
lab was handed (chapter 6). They are
opt-in exceptions that prove the rule,
they rewrite files when enabled, and
this guide did not run them: any claim
about what conversion preserves or
loses would have to be measured, and
it was not. Enable them, if you ever
do, on a copy.

## Its metadata is inference, or imported, never verified

From filenames and folders, metadata
is inference (chapters 5 and 12);
from ComicInfo, it is import. Neither
is checked against the world. The
lab's invented writer, A. R. Fenwick,
now stands in the catalogue with the
same authority as any real credit —
Komga repeated what the file said.
It has no online lookup in its core
flow to correct or enrich a book
beyond what your files carry (some
imports — ISBN barcodes, Mylar files —
were named in the library settings and
not run here). Garbage filed is
garbage served, beautifully browsable.

## It does not read your comics

Page images are images. Search
(chapter 8) covers titles and
metadata; nothing in the server reads
the words or art inside the pages, so
there is no searching a story by its
contents, no automatic tagging of what
a page depicts. Likewise its analysis
is structural — type, page count,
dimensions, a cover thumbnail — not
judgement: it cannot tell a page is
duplicated, blurred, or someone else's
art.

## Reading happens where you read it

Komga's own web reader is one reader
(chapter 7). The library's reach into
apps is OPDS and the progress API —
standards, not magic: an app must
speak them, support the roles you
granted, and handle the formats your
files are in. A role-less account can
browse a catalog it cannot read from
(chapter 10), which is a feature with
sharp edges if you did not mean it.

## Smaller print, honestly stated

- **Java generations.** The 1.x line
  runs on Java 21; the announced 2.0
  raises the floor to Java 25, and a
  few image plug-ins already want
  Java 22 (the lab watched three
  switch off). The runtime is part of
  the install, and versions will move
  under this server over its life.
- **The web interface was not the
  lab's door.** Everything here was
  proved at the API level the
  interface uses. Screen-by-screen
  claims about the interface are not
  this guide's to make.
- **Performance at scale is
  unmeasured.** Four, then five books
  scanned in milliseconds say nothing
  about a hundred thousand: thumbnail
  generation, hashing, and the search
  index all cost per book, and large
  libraries live or die on hardware
  this lab did not test.
- **Security is transport-thin by
  default.** Accounts and roles are
  real (chapter 10), but basic auth
  over plain HTTP is a household-grade
  lock. The unclaimed-server window
  (chapter 4) is the sharp end: claim
  first, expose later, if at all.

Check: name three limits from this
chapter that apply to a library you
actually keep, and the chapter that
hands you each one's workaround —
filing, ComicInfo, or roles. If you
can, the tool's size is clear to you,
which is what makes it safe to run at
full strength.
