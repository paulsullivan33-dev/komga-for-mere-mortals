# Running it for real

Outcome: the lab's throwaway start
turned into a server you can live
with — the settings that matter, where
everything lives, and what a backup
and a password rescue actually involve.

## The start, made permanent

The lab started Komga by hand with
three options (chapter 4). A standing
install keeps the same shape and lets
your service manager — systemd, a
container runtime, your NAS's app
store — hold the command:

```
java -jar komga-1.30.0.jar \
  --server.port=25600 \
  --komga.config-dir=/srv/komga/config
```

(the lab's loopback bind and port
18090 were lab choices; 25600 is the
default port). Settings come from
three places, in the project's Spring
style: command-line options like the
above, environment variables
(`SERVER_PORT` for `server.port`), and
an optional `application.yml` in the
config folder for anything finer. The
configuration reference on komga.org
is the full list; the honest subset
this guide verified is the start line,
the port, the address, and the config
dir.

The **server settings** screen in the
web interface covers the running
server's own options; the lab proved
the door exists and opens for an
administrator (`GET /api/v1/settings`
answered 200, transcript
`komga-lab/transcripts/t11-thumbnail-opds2-settings.txt`)
and changed nothing there — settings
you did not watch change are not
described here as if tried.

## What lives where

From chapter 2's map, the operational
version:

- **Your comics**: wherever you filed
  them. Komga reads them in place. A
  backup of the library *files* is a
  backup of those folders, by whatever
  tool backs up the rest of your disk.
- **The config folder**: the
  catalogue, users, progress, search
  index, logs. Back *this* up and a
  restored server remembers everything
  except the files themselves — which
  it will find again at their recorded
  paths.
- **The jar**: replaceable from the
  release page, checksum and all
  (chapter 3). Upgrading is, in shape,
  stop, swap jar, start — the config
  folder's databases migrate
  themselves at startup, as the lab's
  95 first-run migrations suggest.
  Take the config backup *before* the
  swap; migrations do not run
  backwards.

The scan timer belongs here too: the
lab's library record carried
`"scanInterval":"EVERY_6H"` and
`"scanOnStartup":false`, so a standing
server notices new filings on its
interval, not instantly. If your habit
is "file it, read it now," either
lower the interval, enable scan on
startup, or keep the rescan call from
chapter 6 in your pocket — all three
are settings, not surgery.

## The password rescue, documented only

Komga's command-line extras run
alongside a normal start: the project
documents `--list-users` to print the
accounts in the database, and
`--email=<user> --newpassword=<text>`
to reset a forgotten password. The lab
did not need either — its passwords
were written down in its own
transcripts — so both are named here
as documented-only, from the project's
CLI guide, and the honest drill is to
try `--list-users` on your own install
before the day you need the reset.

Check: stop your server, copy the
config folder somewhere safe, and
start it again. If the library, the
users, and your place in the book you
were reading are all still there, you
hold both halves of the backup story:
files in their folders, state in the
config folder.
