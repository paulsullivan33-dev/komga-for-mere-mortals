# Your first run

Outcome: a running server that you
have **claimed** — the first
administrator account created, in the
exact way a person with no browser
session yet must do it — and a sign-in
proved with the API.

## Start it

Komga takes ordinary Spring-style
options on its command line. The lab's
start (transcript
`komga-lab/transcripts/t02-startup.txt`)
named three things: bind to this
machine only, listen on the lab's
port, and keep the config folder
inside the lab instead of the user's
home:

```
java -jar komga-1.30.0.jar \
  --server.address=127.0.0.1 \
  --server.port=18090 \
  --komga.config-dir=/path/to/lab/config
```

Leave `server.address` off for the
default (all interfaces) and
`server.port` at its default 25600 on
a real install; `--komga.config-dir`
defaults to a `.komga` folder in your
home. The banner confirms the version,
then the log builds the databases —
95 small migrations on a first run —
and ends with the two lines that mean
*ready*:

```
Tomcat started on port 18090 (http) with context path '/'
Started ApplicationKt in 57.514 seconds
```

The lab's first start took about a
minute; later starts are faster.
Opening `http://127.0.0.1:18090/` now
serves the web interface's page —
its title is simply `Komga`.

## A fresh server has no users — you claim it

There is no default password to look
up, and no account at all. Ask the API
who you are and it answers 401; ask to
create a user the ordinary way —
`POST /api/v1/users` — and it also
answers 401, because creating users is
an administrator's job and there is no
administrator yet (both attempts are
in transcript
`komga-lab/transcripts/t03-first-user.txt`,
kept because the dead end is the
lesson).

The real flow is the one the web
interface's first screen performs. A
fresh server shows that screen — "This
Komga server is not yet active, you
need to create a user account" — and
behind it sit two calls under
`/api/v1/claim`. First, the status:

```
$ curl -s http://127.0.0.1:18090/api/v1/claim
{"isClaimed":false}
```

Then the claim itself: an empty body,
with the chosen email and password
carried in two headers — the exact
call the interface's own code makes,
which the lab read out of the served
application bundle before trusting it:

```
$ curl -s -X POST http://127.0.0.1:18090/api/v1/claim \
    -H "X-Komga-Email: keeper@clockwork.example" \
    -H "X-Komga-Password: LabPass-1234!" \
    -H "Content-Type: application/json" -d '{}'
```

The answer is the new account, with
every role an administrator needs:

```json
{"id":"0S5KAGC0AERH9","email":"keeper@clockwork.example",
 "roles":["ADMIN","FILE_DOWNLOAD","KOBO_SYNC","KOREADER_SYNC",
          "PAGE_STREAMING","USER"],
 "sharedAllLibraries":true,"sharedLibrariesIds":[],
 "labelsAllow":[],"labelsExclude":[]}
```

And the status flips behind you:

```
$ curl -s http://127.0.0.1:18090/api/v1/claim
{"isClaimed":true}
```

Claiming is a one-time door: it exists
because zero users exist, and it is
gone once one does. That is also the
security note — a fresh, unclaimed
server left reachable on a network is
a server the first passer-by can
claim. Claim promptly, on first start.

## Sign in, and prove it

Komga accepts **HTTP basic auth** —
email and password on each request —
which is what scripts and OPDS apps
use. (The browser flow adds a session
on top; the account is the same.) One
detail of 1.30 that cost the lab a
call: the "who am I" endpoint lives
under the newer v2 API, not v1:

```
$ curl -s -u keeper@clockwork.example:LabPass-1234! \
    http://127.0.0.1:18090/api/v2/users/me
{"id":"0S5KAGC0AERH9","email":"keeper@clockwork.example", ...}
```

The same call with no credentials
answers 401. (The lab's first guess,
`/api/v1/users/me`, answers 404 with
"No endpoint GET /api/v1/users/me" —
Komga's error messages name the
missing endpoint plainly, a kindness
chapter 15 leans on.) The credentials
in this chapter are the lab's own,
invented for a fictional keeper on a
loopback port; yours should be a real
password, and the server should not be
exposed to the internet on basic auth
alone — it travels unencrypted over
plain HTTP.

Check: `GET /api/v1/claim` says
`{"isClaimed":true}`, and
`/api/v2/users/me` with your
credentials returns your account with
the ADMIN role. If both do, chapter 5
prepares a folder the scanner will
read well, and chapter 6 gives the
server its first library.
