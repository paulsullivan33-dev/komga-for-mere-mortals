# Reading progress

Outcome: your place in a book, kept by
the server — set, finished, and
read back, with the knock-on effects
on the series counts and the on-deck
shelf all shown from the lab's run.

## Progress is a per-book, per-user record

A book's record carries a
`readProgress` bundle: current page,
whether it is completed, and when it
was read. Before anyone reads, it is
absent — the lab's book 001 said
`readProgress: null`. It belongs to
the signed-in account: chapter 10's
two users looking at the same series
saw different read counts, because
each was looking at their own shelf of
progress laid over the shared
catalogue.

Setting progress is one API call —
the same one the web reader makes as
you turn pages, and OPDS apps make
through their own sync (transcript
`komga-lab/transcripts/t08-progress-and-search.txt`):

```
$ curl -s -X PATCH -u keeper@... \
    http://127.0.0.1:18090/api/v1/books/0S5KAHF72EN6M/read-progress \
    -d '{"page": 3, "completed": false}'
HTTP 204

$ GET /api/v1/books/0S5KAHF72EN6M
readProgress: {'page': 3, 'completed': False,
               'readDate': '2026-11-07T22:12:48Z', ...}
```

204 — done, nothing to say. Finishing
the book is the same call with the
last page and `completed: true`; the
record then reads page 6 of 6,
completed, with its read date. One
bookkeeping point the record makes
visible: `created` keeps the moment
you *started*, `lastModified` the last
change — Komga remembers that reading
took time, not only that it ended.

## What finishing does to the shelves

Progress is not a private note on the
book; the rest of the interface is
computed from it. The moment the lab
finished issue 1, the series record
moved:

```
booksCount 4   booksReadCount 1
booksUnreadCount 3   booksInProgressCount 0
```

(And mid-read, the same record had
shown the book as in progress — the
three counters plus the total always
agree, which makes them a cheap health
check on any series.) The **on-deck**
shelf — the "what next" list behind
both the web home page and the OPDS
On Deck feed — answered with exactly
the next unread book in the series:

```
$ GET /api/v1/books/ondeck
[('Clockwork Orchard 002', {})]
```

That `('... 002', {})` is the whole
value of the feature in one line: the
server knew issue 1 was finished, knew
issue 2 was next and untouched, and
offered it. Keep Reading is the twin
shelf — books in progress, at their
pages — and OPDS carries both feeds
(chapter 9), so a reading app and the
browser agree about where you stopped
because neither keeps its own copy:
the server is the record.

## The boundaries, stated plainly

- Progress syncs between *Komga's own
  doors* — web, API, OPDS — because
  they share the server's record. The
  Kobo and KOReader sync roles
  (chapter 10) extend that to those
  devices' own protocols; the lab ran
  no such device, so that extension is
  documented-only here.
- Deleting progress is the mirror
  call (`DELETE` on the same
  read-progress address, and a series
  can be marked read or unread whole);
  described from the API reference,
  not run by the lab.
- Progress says where you stopped,
  not what you thought. Ratings,
  reviews, and notes are not part of
  this record.

Check: PATCH one book to its last
page with `completed: true`, then read
the series record — `booksReadCount`
up by one, and the on-deck answer
naming the next book. If both moved,
your place is being kept where every
door can see it.
