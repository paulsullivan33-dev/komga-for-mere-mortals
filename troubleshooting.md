# Troubleshooting

Outcome: the failures this guide's own
lab met or deliberately built, each
with the observation that identifies
it and the move that fixes it — plus
the general method: in Komga, the
catalogue and the log will usually
tell you which layer is speaking.

## The method: ask the server what it thinks

Almost every problem below is a
mismatch between the folder on disk
and the catalogue in the database.
Two questions separate them, and both
have been this guide's refrain:
`GET /api/v1/series/{id}/books` — what
the catalogue holds — against
`ls` — what the disk holds. And the
server log narrates its side: scans
report their counts, analysis reports
its verdicts, startup reports its
version and port. Read the layer that
disagrees.

## "I can't sign in / there's no account"

- **Fresh server, login screen, no
  credentials exist.** The server is
  unclaimed. `GET /api/v1/claim` will
  say `{"isClaimed":false}`; claim it
  (chapter 4) rather than hunting for
  a default password — there is none.
- **401 on every call.** Wrong email
  or password, or credentials sent to
  an endpoint that moved: `/api/v1/
  users/me` answers 404 in 1.30 — the
  address is `/api/v2/users/me`
  (chapter 8). Komga's error JSON names
  the missing endpoint; read it before
  blaming the password.
- **403, but the password is right.**
  The account lacks the role for that
  door (chapter 10's table): pages
  want PAGE_STREAMING, downloads want
  FILE_DOWNLOAD, administration wants
  ADMIN. Roles are the fix, not the
  password.

## "The book is there but won't open"

Check its media status in the book
list. **UNSUPPORTED** with a comment
like `ERR_1001` means analysis opened
the file and found something else —
the lab's case was plain text in a
`.cbz` name, sniffed as `text/plain`.
The extension catalogues; the contents
decide. Rebuild or replace the file
itself (Komga will not — chapter 16),
then rescan. A page request against
such a book answers 404, "Book
analysis failed," which is the same
verdict at the reading door.

## "My series is two series" (or one series too many)

Chapter 1's rule, wearing a frown.
Two folders — a spelling drift, a year
suffix, a nested extra level — are two
series, and no setting merges them.
Fix the folders on disk into one,
rescan, and let the catalogue follow.
The mirror fault, unrelated books
sharing one folder, is the same fix in
the other direction.

## "The new issue never appeared"

Walk the chain: is the file inside the
series folder, with an extension the
scanner lists (`cbz, zip, cbr, rar,
pdf, epub`)? Has a scan run since —
check the log for the `Scanned N
series, M books` line and compare M
with the folder, or force one with the
rescan call (chapter 6); a standing
server may simply be inside its
`EVERY_6H` interval. Is the book
present but with surprising metadata?
Then the scan worked and the naming
did not — chapter 5.

## "The cover is wrong"

A series wears its first book's cover
by default (`seriesCover: FIRST`), and
a book's thumbnail is generated from
its page 1 at analysis. A wrong cover
usually means the filing put a
different book first, or page 1 is not
the cover inside the archive — both
are file-side facts. Regenerating
thumbnails exists in the interface and
API; the lab saw the endpoint in the
served bundle but did not run it, so
it is named here, not taught.

## "It won't start"

Read the first lines, not the last:
the banner prints the version, and
`Starting ApplicationKt v1.30.0 using
Java 21.0.12.1` proves the jar met a
Java. An older Java fails there, in
the open. A port already in use fails
at the Tomcat lines — move
`server.port` or free the port. A
config folder the process cannot
write fails at the database lines —
the folder is the server's home, and
it must be writable by the user the
server runs as.

Check: for one real symptom, name the
layer talking — claim, roles, media
status, folders, scan, or startup —
and the one query or log line that
proves it. That is the whole method;
the entries above are its worked
examples.
