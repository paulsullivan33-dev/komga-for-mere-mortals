# What Komga is

By the end of this chapter you can say,
in one sentence, what Komga does with a
folder of comics — and state the one
rule that decides whether your library
comes out tidy or tangled.

## The pile you already have

Comics and manga on a computer usually
live as archive files: a **CBZ** is an
ordinary zip archive of page images
with a different name, a **CBR** is the
same idea in the RAR format, and there
are also PDFs and e-book files. A small
collection is a folder per series with
numbered issues inside. A bigger one is
years of habits: some series nested two
folders deep, issue numbers written
three ways, a few files that are not
what their names claim.

Reading that pile means opening files
one at a time in whatever app is at
hand. Nothing shows you the whole
collection at once. Nothing shows
covers in a row. Nothing remembers that
you finished issue 2 on the tablet and
want issue 3 on the laptop.

**Komga** is a **media server** — a
program that runs on a machine you own,
reads that pile where it sits, and
serves it back to you as a library. In
the browser it looks like a small,
tidy bookshop of your own comics:
series with covers, books in order, a
reader that turns pages. To reading
apps it speaks **OPDS**, the standard
catalog format those apps browse and
download through (chapter 9). And it
keeps your place: which page, which
book finished, for each person with an
account (chapter 11).

It does not download comics, and it
does not sell or share anything. It
serves your files, to your accounts,
on your network. This guide's lab ran
**Komga 1.30.0**, the current release
at the time of writing, from the
project's own release page
(transcripts in `komga-lab/transcripts/`).

## The rule: the library on screen is the filing on disk

Komga builds its world out of what it
finds in your folders, and almost
nothing else. A folder becomes a
**series**. The archive files inside it
become its **books**, and the numbers
in their filenames become their order.
So:

> **Komga serves the library you file,
> exactly as you filed it — it reads
> your folders and filenames to build
> series and order, so the organising
> you do on disk is the organising you
> get on screen.**

The lab's fixture makes the rule
concrete. One folder named
`Clockwork Orchard` holding files named
`Clockwork Orchard 001.cbz` through
`004.cbz` became one series,
*Clockwork Orchard*, with books
numbered 1 to 4 (transcript
`komga-lab/transcripts/t05-series-and-books.txt`).
Nobody typed the series name or the
numbers into Komga; the folders and
filenames said them, and Komga
listened. Rename the folder and you
rename the series. Scatter a series
across two folders and you get two
series. Leave the numbers out of the
filenames and the order is whatever
the names sort into.

The same rule explains the honest
surprises. One of the lab's four files
was plain text with a `.cbz` name.
Komga catalogued it anyway — book 4,
present in the list — because the
filing said a book lives there; then
its analysis found text where an
archive should be and marked it
**UNSUPPORTED** with 0 pages (chapter 6
has the record). The rule cuts both
ways, and both ways are the same
sentence: what you filed is what you
get.

## Where it comes from

Komga is a free, open-source program
written mainly in Kotlin on the Spring
framework, distributed as a single jar
file that runs anywhere a suitable
Java does, and as a Docker image. The
project lives at github.com/gotson/komga
and its documentation at komga.org.
It has been developed since 2019 and
also handles PDF and EPUB books; this
guide's lab worked with CBZ comic
archives, the centre of its purpose.
One server can hold several
**libraries** — separate roots, one per
folder tree you point it at — and
several user accounts, each with its
own reading progress.

Check: say what Komga serves, where it
gets the series names and the book
order, and what happens to a series you
file in two folders. If you can, you
have this chapter — and the rule the
rest of the guide keeps pointing back
to.
