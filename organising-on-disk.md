# Organising on disk

Outcome: a folder layout the scanner
turns into the library you meant —
because, per chapter 1's rule, the
layout is not preparation for the
library; it *is* the library, in its
first form.

## One folder per series

The scanner (chapter 2) treats each
folder directly inside a library's
root as one series, and the files
inside it as that series' books. The
layout that works is the plain one the
lab used:

```
library/
  Clockwork Orchard/
    Clockwork Orchard 001.cbz
    Clockwork Orchard 002.cbz
    Clockwork Orchard 003.cbz
    Clockwork Orchard 004.cbz
```

One scan later that tree was one
series named `Clockwork Orchard` —
the folder's name, exactly — with
books 1 to 4 (transcript
`komga-lab/transcripts/t05-series-and-books.txt`).
Nothing was configured, mapped, or
tagged. The folder did the work.

The consequences to plan around:

- **A series filed in two folders is
  two series.** Two folders whose
  names differ by a suffix, a year, or
  a spelling drift will not be merged.
  Merge them on disk, then rescan.
- **A folder of mixed books is one
  mixed series.** Loose one-off books
  belong in a folder of their own, or
  in the library's configured
  one-shots arrangement — not scattered
  at the root, where each may become
  its own tiny series.
- **The root is a shelf, not a
  series.** Books belong one level
  down, inside their series folder.

## Numbers live in filenames

A book's **number** — its place in the
series — is read from its filename.
The lab's files carried their numbers
as `001`, `002`, `003`, and Komga's
catalogue shows `number: 1`, `2`, `3`,
and a matching `numberSort` for
ordering. Three practical notes:

- **Pad your numbers.** `002` sorts
  before `010` in every tool ever
  written; `2` and `10` do not. Komga
  reads the numeric value, and padding
  keeps the disk, the catalogue, and
  every other program in agreement.
- **One style per series.** Volumes,
  chapters, and specials each have
  their fans' conventions. Whatever you
  choose, a series whose filenames
  follow one pattern reads cleanly;
  chapter 12 covers the metadata file
  that can override a filename when a
  name truly cannot carry the facts.
- **The rest of the filename is the
  title until told otherwise.** With
  nothing else to go on, book 1's title
  in the catalogue was the filename
  without its extension:
  `Clockwork Orchard 001`.

## Names the scanner believes

File extensions choose whether a file
is a book at all. The lab's scanner
logged the list it was looking for:

```
Scan for extensions: [cbz, zip, cbr, rar, pdf, epub]
```

A `.cbz` by any other extension is
invisible, and a file *with* the right
extension is a book — which is how the
lab's plain-text `Clockwork Orchard
004.cbz` entered the catalogue. The
extension gets a file catalogued; the
contents decide whether it can be
read, and that second judgement
belongs to the analysis step in the
next chapter.

Keep names honest for a different
reason too: Komga shows file paths to
administrators (and, the lab noted,
hides them from ordinary users — the
reader account in chapter 10 saw an
empty `url` where the admin saw the
full path). The path is part of the
record. Names you would be happy to
read aloud in the catalogue are the
right names on disk.

Check: pick one real series folder and
read its filenames as the scanner
will — folder name as the series
title, a number in every filename,
padding consistent. If you can predict
the catalogue from the listing, the
rule is working for you instead of on
you.
