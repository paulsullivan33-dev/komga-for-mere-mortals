# The neighbours

Outcome: where Komga sits among the
other tools that serve a comic and
book collection, characterised by
shape and center of gravity — not
benchmarked. The lab ran Komga only;
everything in this chapter is the
projects' own descriptions, and
`criteria.md` lists it as documented
only.

## Kavita

The closest neighbour: a free,
open-source server for comics, manga,
and e-books, with its own web reader,
OPDS support, user accounts, and
reading progress. Kavita's centre of
gravity is breadth — it treats EPUB
books as first-class citizens next to
comics, where Komga's heart is the
comic archive and its metadata
conventions. Households choose between
them on library shape and taste; a
collection of CBZ series with
ComicInfo leans Komga, a mixed shelf
leaning on e-books leans Kavita.
Either way, the organising-on-disk
rule of chapter 1 holds in spirit:
both build their libraries from your
folders.

## Calibre and calibre-web

**Calibre** is the e-book world's
library *manager* — it edits metadata,
converts formats, and keeps its own
managed library folder — with a
content server attached; **calibre-web**
is a web front end over a Calibre
library, OPDS included. The contrast
with Komga is a philosophy: Calibre
wants to own and improve the library
(copying books into its structure and
rewriting metadata in its database),
where Komga leaves your files where
they lie and describes them. For
prose e-books Calibre's conversion is
a real power Komga does not attempt;
for a comic archive collection, its
machinery is mostly beside the point.

## Ubooquity

An older, lightweight Java server for
comics and e-books: simple, small,
OPDS-speaking, happy to run on modest
hardware. Its development has been
quiet for years compared with Komga's
release pace — the lab's 1.30.0 is a
current, maintained line — and its
account and progress features are
thinner. It remains a fair choice for
a tiny, static collection on a tiny
machine.

## The specialists around the edges

- **Mylar** manages *acquiring* comic
  issues — watching for releases and
  filing them — which is the half of
  the workflow Komga deliberately does
  not do (chapter 1). The two compose:
  one files, the other serves.
- **Stump** is a newer, smaller
  OPDS-focused server some home labs
  have adopted; lighter than Komga,
  with a narrower feature set.
- **A plain file share plus a good
  reader app** is the zero-server
  neighbour: honest for one reader on
  one device, and the thing Komga
  replaces the moment a second device,
  a second reader, or a kept place
  enters the house.

Check: name the neighbour whose shape
matches the part of the problem Komga
does not solve for you — acquiring,
converting, or nothing at all — and
the chapter that drew that boundary.
If you can, you know what you bought
and what you did not.
