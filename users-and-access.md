# Users and access

Outcome: a second account created the
way an administrator does it, and the
**roles** — Komga's whole access
system — proved at the endpoints where
each one bites.

## One server, several readers

A Komga server is a household tool:
one catalogue, one account per reader,
each account keeping its own reading
progress (chapter 11) and its own
view of what is shared with it. The
administrator from chapter 4 is simply
the first account, with all roles. The
lab created a second, deliberately
plain account — an administrator's
call under the v2 API (transcript
`komga-lab/transcripts/t09-second-user.txt`):

```
$ curl -s -u keeper@...(admin) -X POST \
    http://127.0.0.1:18090/api/v2/users \
    -d '{"email":"reader@clockwork.example",
         "password":"ReaderPass-1234!","roles":[]}'
HTTP 201
{"id":"0S5KAX62TEKWE","email":"reader@clockwork.example",
 "roles":["USER"],"sharedAllLibraries":true,
 "sharedLibrariesIds":[], ...}
```

Two defaults to notice. An account
created with no roles still gets
**USER** — the right to sign in and
read what is shared. And
`sharedAllLibraries` starts **true**:
a new account sees every library
until an administrator narrows it to
named libraries (`sharedLibrariesIds`)
or sharing labels. On a family server
that may be exactly right; on anything
wider, set the sharing before you hand
the password out, not after.

## The roles, and where each one bites

The administrator's role list from
chapter 4 is the full menu: `ADMIN`,
`FILE_DOWNLOAD`, `PAGE_STREAMING`,
`KOBO_SYNC`, `KOREADER_SYNC`, and
`USER`. The lab's reader had only
USER — and the differences were not
cosmetic:

| Attempt, as the role-less reader | Answer |
| --- | --- |
| Browse the OPDS catalog | 200 |
| List the series | 200 |
| Fetch a page (`/pages/1`) | **403** — no PAGE_STREAMING |
| Download a file via OPDS | **403** — no FILE_DOWNLOAD |
| Create a library | **403** — no ADMIN |
| List the users | **403** — no ADMIN |

Browse-but-cannot-read is a coherent
posture — a catalogue a child or a
guest can look through — and it fell
out of two role checkboxes, not a
configuration file. The sync roles
gate the Kobo and KOReader progress
sync doors; this guide did not run a
sync device, so those two are named
here and listed documented-only in
`criteria.md`.

Two quieter differences in the same
transcript. The reader's view of the
series had `"url":""` where the
admin's record carried the full file
path: **paths are an administrator's
detail**, hidden from ordinary
accounts. And the reader's series
counts showed `booksReadCount: 0` at
the moment the admin's showed 1 —
progress is per account, which the
next chapter uses.

What roles are not: they are
permissions, not encryption or a
network boundary. Basic auth over
plain HTTP still shows credentials to
anyone who can watch the wire, so a
server beyond your own network belongs
behind HTTPS or a tunnel — a transport
decision this guide flags and does not
make for you.

Check: create a plain account, sign in
as it, and try the three doors of the
table — catalog 200, a page 403, a
library creation 403. When the answers
match the roles you granted, you
understand the access system well
enough to run a household on it.
