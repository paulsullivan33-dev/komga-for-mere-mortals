# Metadata and ComicInfo

Outcome: a clear line between the
metadata Komga *infers* from your
filing and the metadata it *reads*
when a book carries its own — with the
lab's before-and-after on the same
book as the proof.

## The inference you start with

Metadata is the descriptive bundle —
title, number, summary, authors,
publisher. With no help, Komga infers
all of it from chapter 5's sources:
the folder names the series, the
filename names the book and numbers
it, and everything else is honestly
empty. Book 003's record before this
chapter's experiment (transcript
`komga-lab/transcripts/t05-series-and-books.txt`):

```
title='Clockwork Orchard 003'  summary=''  authors=[]
```

That is not a failure; it is the
truth about a bare archive. But a
library of bare archives is a library
of filenames, and real collections
want more: a story title, a writer, a
summary for the series page. There are
two places that "more" can live —
typed into Komga, or filed inside the
book. The durable one is inside the
book, and its name is ComicInfo.

## ComicInfo.xml: the book carries its facts

**ComicInfo** is a small XML file,
`ComicInfo.xml`, stored *inside* the
CBZ alongside the pages, describing
the book: series, number, title,
summary, writer and other credits,
publisher, dates, even a page count.
It is a community convention older
than Komga, written by tagging tools
and some publishers, and Komga reads
it because the library record from
chapter 6 said so by default:
`"importComicInfoBook":true`,
`"importComicInfoSeries":true`.

The lab's experiment (script
`komga-lab/add-issue-005.py`, transcript
`komga-lab/transcripts/t10-new-issue-and-comicinfo.txt`)
rebuilt issue 003 with the same four
pages plus this file:

```xml
<ComicInfo>
  <Series>Clockwork Orchard</Series>
  <Number>3</Number>
  <Title>The Glass Greenhouse</Title>
  <Summary>The keeper builds a greenhouse of clock glass
           and plants a tree that ticks.</Summary>
  <Writer>A. R. Fenwick</Writer>
  <Publisher>Orchard Press</Publisher>
  <Year>2026</Year>
  <PageCount>4</PageCount>
</ComicInfo>
```

One rescan later, the same book read:

```
title='The Glass Greenhouse'
summary='The keeper builds a greenhouse of clock glass ...'
authors=[{'name': 'A. R. Fenwick', 'role': 'writer'}]
pages=4   status=READY
```

Three details matter. The **page count
did not change**: `ComicInfo.xml`
inside the archive is metadata, not a
page — the analysis counts images.
The facts **propagated upward**: the
series record gained publisher
`Orchard Press` and the writer, because
series metadata is aggregated from its
books. And the change was **picked up
by an ordinary rescan**: editing the
file changed it, the scan noticed, the
analysis re-ran. No re-import, no
special command.

## Which source wins, and the locks

Notice the `Lock` fields riding along
in every metadata record chapter 6
showed — `titleLock`, `summaryLock`,
and the rest. A field set by hand in
Komga, or marked locked, is not
overwritten by the next scan's
inference or import; an unlocked field
is refreshed from the file. That is
the whole reconciliation rule, and it
is why the inside-the-book route is
the durable one: facts in the file
survive a rebuilt database, while
facts typed into one server's database
live only there — though typed facts,
locked, win on that server.

A measured caution to end on: Komga
imports what a ComicInfo *says*, with
no way to know whether it is right.
The lab's invented writer is now
indistinguishable, in the catalogue,
from a real credit. Metadata quality
is a filing problem like any other —
which is chapter 1's rule wearing a
different coat.

Check: add a `ComicInfo.xml` with a
title and writer to one of your CBZs,
rescan its library, and read the
book's record. The new title and
author, with the page count unmoved,
mean the import did what this chapter
claims.
