# Records: ADRs, findings, journal, sources, methods

Five kinds of record, so that no session has to rediscover what an earlier one learned:

| Record | Answers | Changes |
|---|---|---|
| `docs/adr/` | What did we decide, and why? | A new ADR supersedes an old one; old ones stay |
| `docs/findings/` | How does the target work? | Kept current: corrected when something better is found |
| `docs/journal/` | What did we try, and what happened? | Append only: one entry per session |
| `docs/sources.md` | Where did each thing come from, and how do we get it again? | One row per source |
| `.claude/rules/methods.md` | What is the fastest known way to do each recurring job here? | Kept current: a faster method replaces the row (`methods.md`) |

## ADRs

`docs/adr/NNNN-<short-title>.md`, numbered from 0001. One decision each, under a page.

```markdown
# ADR-0002: <Decision as a short sentence>

Status: Proposed | Accepted | Superseded by ADR-NNNN
Date: YYYY-MM-DD

## Context
What we know (link the findings) and what forces the decision.

## Decision
What we do, in a few lines.

## Options considered
Each option with its main cost, and why it lost.

## Consequences
What gets easier, what gets harder, and what it leaves for later.
```

- **ADR-0001, scope and layout** (written in M0): what part of the target this project covers now, the full layout
  with the folders that wait for later, and what stays out of git.
- **ADR-0002, route** (written in M1): see `routes.md`.
- Later ADRs: anything hard to undo (a protocol library, a data format of our own, how the client is patched to
  reach a local server).
- Never delete an ADR. To change one, write a new one and set the old status to `Superseded by ADR-NNNN`.

`docs/adr/README.md` is the general file: the project in three lines, the ADR index (number, decision, status), and
the milestone tracker:

```markdown
## Milestones

| Milestone | Goal | Status |
|---|---|---|
| M0 | Scaffold | done |
| M1 | Recon | in progress |

### M1 steps
1. [x] Identify the engine and packer
2. [ ] Find community servers and extractors

### Later
- Things noticed outside the current milestone.
```

## Findings

`docs/findings/<system>.md`, one file per system or topic (`overview.md`, `file-formats.md`, `protocol.md`,
`combat.md`, `items.md`), listed in `docs/README.md`. They describe the target, not our code.

Each finding says what is true, where it was found, when, and how sure we are:

```markdown
## Archive header

`*.dat` archives start with `NTFS` + a u32 file count, then a table of (id u32, offset u32, size u32).
- Source: hex of `data/items.dat`, confirmed by unpacking all 41 archives with `tools/extract` (2026-03-14).
- Status: confirmed
```

- **Status** is `confirmed` (checked against the target), `from <source>` (a wiki or a community server says so, not
  checked yet), or `guess` (a reasoned guess, to be tested). Never write a guess as a fact.
- Give the source exactly: a file and offset, a function address, a packet, a URL with its date, a repo path and
  commit. Someone must be able to check it again.
- When two sources disagree, keep both with their sources and say which one wins and why.
- Write a finding as soon as you learn it, even if nothing uses it yet: that's what makes it useful to the next
  system.

## Journal

`docs/journal/YYYY-MM-DD-<topic>.md`, one entry per session (or per milestone step when a session is long).

```markdown
# 2026-03-14: unpacking the item archives (M2, step 1)

Goal: unpack `data/items.dat`.

- Tried zlib on the whole file: failed, the header isn't compressed.
- Found the file table at 0x10 (findings/file-formats.md, "Archive header").
- Each entry is zlib on its own: worked for 40 of 41 archives.
- Dead end: `sounds.dat` uses another layout; left for later (tracker).

Next: write the extractor as `tools/extract/`.
```

- Record what didn't work and why, as carefully as what did. Dead ends are the most expensive things to rediscover.
- Note how long the slow steps took ("194 screens, 13 s each with one launch per screen; 1–2 s each in one
  session"). The faster method goes into `.claude/rules/methods.md`; the journal keeps how it was found.
- Move every lasting fact into `docs/findings/`; the journal links to it.
- Before starting work, read the last few entries and the findings for the system you're touching.

## Sources

`docs/sources.md` says what each thing outside git is, where it came from and why we use it; `setup.bat` fetches or
rebuilds it (`layout.md` → Setup). Every row here has its line there, apart from the target; crawls run only with `setup.bat crawl`.

```markdown
## Repos (`_external/`)

| Repo | Commit | Licence | Used for |
|---|---|---|---|
| github.com/<owner>/<repo> | `abc1234` (2026-03-10) | MIT | packet definitions; ported with notice |

## Sites (`_data/crawled/`)

| Site | Crawled | Rules | Saved as | Made by |
|---|---|---|---|---|
| <wiki URL> | 2026-03-12, 1,204 pages | robots.txt allows; 1 request/s | `_data/crawled/<site>/` | `tools/scripts/crawl_wiki.py` |

## Tools (`_sdk/tools/`)

| Tool | Version | From | Used for |
|---|---|---|---|
| Ghidra | 11.x | its GitHub releases | decompiling the client |

## Target and data

- Target: <name> <version>, where it came from (the user's own copy, a store, an installer and its date).
- SHA-256 of its main files, so another machine can check it has the same build:

  | File | SHA-256 |
  |---|---|
  | `<main executable>` | `…` |

- `_data/extracted/<version>/`: made by `extract_all.bat`.
- `_data/crawled/<site>/`: raw only; what we use from it is in `game/<part>/data/` and `docs/findings/`.
- `game/<part>/data/<file>`: made by `<converter>` from `<raw source>` on `<date>`.
```
