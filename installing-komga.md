# Installing Komga

Outcome: a Komga jar on your machine
whose version and integrity you have
proved, ready to start — and an honest
account of which install routes this
guide ran and which it only read about.

## What Komga needs

Komga ships as a single **jar** — a
Java program in one file — so the real
requirement is a Java runtime new
enough to run it. The lab's machine
had OpenJDK 21:

```
$ java -version
openjdk version "21.0.12.1" 2026-08-18
```

and Komga 1.30.0 ran on it directly;
its startup log's first line says so
(transcript
`komga-lab/transcripts/t02-startup.txt`):

```
Starting ApplicationKt v1.30.0 using Java 21.0.12.1
```

The project has announced that the
future 2.0 line will raise the minimum
to Java 25. The 1.x line this guide
teaches is the one to install today,
and `java -version` on your machine is
the check that decides whether the jar
route is open to you. (Two honest
footnotes from the lab's startup log:
a few optional image-format plug-ins —
for HEIF, JPEG XL, and one WebP
reader — switch themselves off below
Java 22. Ordinary CBZ, CBR, PDF, and
EPUB books do not need them.)

## The route the lab used: the release jar

The project publishes each release on
its GitHub releases page — note the
address and the tag style, both of
which the lab verified by fetching
them: the repository is
`github.com/gotson/komga`, and its
release tags carry **no** leading `v`.
The lab downloaded two files from the
**1.30.0** release:

```
komga-1.30.0.jar          (127,123,335 bytes)
checksums_sha256.txt
```

and proved the jar against the
project's own sums before running it
(transcript
`komga-lab/transcripts/t00-version-and-checksum.txt`):

```
$ sha256sum komga-1.30.0.jar
cac820a26caf8c8cc2239351b5f7ac7c5ba13badfae5bb0ce2b2449f1dfd8ff3  komga-1.30.0.jar
```

The same value stands in the release's
`checksums_sha256.txt`. A jar whose sum
does not match its release's published
sum is not an install; it is a story
you stop and investigate. The download
is large — about 127 MB — because the
one file carries the whole server, web
interface included.

There is nothing to "install" beyond
that. Keep the jar in a folder of its
own, and chapter 4 starts it. The lab
kept the jar and its config folder
together in one scratch directory,
outside any system location.

## The other routes, documented only

- **Docker.** The project's image
  (`gotson/komga`, also mirrored on the
  GitHub registry) is the route most
  home servers use: one container, the
  config folder and your library
  folders mounted in, port 25600
  published. The project advises
  pinning the `1.x` tag rather than
  `latest` ahead of the 2.0 changes.
- **Your distribution or a package
  manager.** Community packages exist
  for several systems. They answer to
  the same two checks as the jar:
  version reported at startup, and the
  behaviour in chapter 4.

Whichever route you take, the jar's
filename and the startup banner are
the handshake: the banner prints the
version in its first lines, and this
guide's claims are tied to **1.30.0**.

Check: `java -version` prints 21 or
newer, and your jar's SHA-256 matches
the sum published with its release. If
both do, chapter 4 starts the server.
