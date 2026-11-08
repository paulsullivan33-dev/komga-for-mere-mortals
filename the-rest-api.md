# The REST API

Outcome: the door your scripts use —
how it authenticates, the handful of
endpoints this guide has already been
quietly using, and how search behaves —
all of it run against the lab server.

## Authentication, and the v1/v2 seam

Every API call carries **basic auth**:
the account's email and password
(chapter 4). No token to fetch, no
header ceremony:

```
curl -s -u keeper@clockwork.example:LabPass-1234! <url>
```

Wrong or missing credentials answer
401, and Komga's JSON errors say what
happened (`"status":401,
"error":"Unauthorized"`). Two shape
notes the lab learned by bumping into
them, worth more than a tidy fiction:

- The API lives mostly under
  `/api/v1/`, but **user management
  moved to `/api/v2/`** in this line:
  `/api/v2/users/me`, `POST
  /api/v2/users`. The v1 users
  collection no longer exists — `POST
  /api/v1/users` answers 404 even for
  an admin, and the error names the
  missing endpoint.
- **Responses differ by endpoint.**
  Catalogue lists (series, books,
  users under v1) arrive in a paged
  envelope — `content`, `totalElements`,
  `pageable`, and friends — while the
  v2 user list is a bare array. The
  `?unpaged=true` parameter flattens a
  paged endpoint to everything at
  once, which the lab used throughout
  its transcripts.

## The working set

The endpoints the chapters rely on,
each one exercised in the transcripts:

| Job | Call |
| --- | --- |
| Who am I | `GET /api/v2/users/me` |
| List series | `GET /api/v1/series?unpaged=true` |
| One series | `GET /api/v1/series/{id}` |
| A series' books | `GET /api/v1/series/{id}/books?unpaged=true` |
| One book | `GET /api/v1/books/{id}` |
| A book's pages | `GET /api/v1/books/{id}/pages` |
| One page | `GET /api/v1/books/{id}/pages/{n}` |
| A book's cover | `GET /api/v1/books/{id}/thumbnail` |
| Create a library | `POST /api/v1/libraries` |
| Rescan a library | `POST /api/v1/libraries/{id}/scan` |
| Mark progress | `PATCH /api/v1/books/{id}/read-progress` |

IDs are the opaque strings the server
hands back (`0S5KAHF6YEYSP` is the
lab's series). Keep them from
responses; do not construct them.
A book record is the full bundle —
identity, file path, size, media,
metadata, your read progress,
`fileHash` — and chapter 6 quoted one
in full.

## Search

Search is a parameter, not a separate
service — the config folder's Lucene
index (chapter 2) sits behind it. The
lab's pair of probes (transcript
`komga-lab/transcripts/t08-progress-and-search.txt`):

```
$ GET /api/v1/series?search=Orchard
['Clockwork Orchard']  totalElements: 1

$ GET /api/v1/series?search=Zeppelin
totalElements: 0
```

A word in the title finds the series;
a word in nothing finds nothing, with
a tidy empty page rather than an
error. Books search the same way
through `/api/v1/books?search=`.
Search covers catalogue fields —
titles, names, metadata — not the
words inside your page images;
Komga does not read your comics'
text, and chapter 16 keeps that
boundary plain.

## Writing back

The API is not read-only. This guide
has already written through it: a
library created, a scan requested
(202 — work accepted, done in the
queue), progress patched (204 — done,
nothing to say back). Metadata edits,
collections, read lists, and user
administration all live here too, each
behind the roles of chapter 10; the
parts this guide did not exercise are
listed as documented-only in
`criteria.md` rather than described as
if run. The full endpoint reference is
the project's own API documentation,
and the running server's behaviour —
as the v1/v2 seam shows — outranks
any guide, including this one.

Check: with your credentials, `GET
/api/v2/users/me` returns your
account, `GET /api/v1/series?search=`
plus a word from one of your series
titles returns exactly that series,
and the same search with a nonsense
word returns `totalElements: 0`. Three
small answers, and you hold the API.
