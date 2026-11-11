# Project layout

Every reverse-engineering project gets the same shape, whatever part the user wants first. Folders for later parts
are listed in `AGENTS.md` and ADR-0001 as "later" and created by the milestone that first needs them.

```
<project>/                     one git repo
├─ AGENTS.md  CLAUDE.md        the map, the target table, how to run things
├─ .gitignore  .gitattributes
├─ .claude/
│  ├─ settings.json            keeps agents from editing the original copy
│  └─ rules/                   agent rules (below)
├─ setup.bat                   rebuilds every git-ignored folder on a new machine (below)
├─ run_<thing>.bat …           launchers for everything that runs (below)
├─ docs/
│  ├─ README.md                index of the docs
│  ├─ adr/                     decisions: README.md (index, route, milestone tracker) + NNNN-<title>.md
│  ├─ findings/                how the target works, one file per system, each fact with its source
│  ├─ journal/                 the path taken: one dated entry per session, dead ends included
│  └─ sources.md               every repo, site, tool and data source used, and how to get it again
├─ tools/
│  ├─ <tool>/                  our own tools, one folder each (an extractor, a packet logger, a converter)
│  └─ scripts/                 one-file scripts (crawlers, parsers, quick checks)
├─ game/  or  app/             our reimplementation, shaped by the route (below), with its data files in <part>/data/
├─ _sdk/                       git-ignored: the target and third-party programs
│  ├─ target/<version>/        the original, copied, never changed
│  ├─ patched/<version>/       a changed copy, only if the route needs one; every change listed in AGENTS.md
│  └─ tools/                   third-party programs (Ghidra, a debugger, asset viewers) and their projects
├─ _data/                      git-ignored: raw material gathered from the target and the web
│  ├─ extracted/<version>/     assets, tables and code dumps pulled from the target's files
│  ├─ crawled/<site>/          saved pages from wikis and fan sites, and what was parsed from them
│  └─ captures/                traces and logs recorded locally (debugger, graphics or packet traces)
└─ _external/<owner>/<repo>/   git-ignored: other people's repos we read (open-source servers, extractors)
```

## The code folder

Use `game/` for a game and `app/` for an app. Its subfolders follow the route (`routes.md`):

| Target | Subfolders |
|---|---|
| Online game | `server-emu/`: a server that speaks the original protocol, so the original client plays on it locally. Later `server/` and `client/`: our own rewrite. `shared/` once two of them use the same rules or data code |
| Single-player game | `client/`: our rewrite, built system by system |
| App without a server | the app directly in `app/` |
| App with a server it needs | `server-emu/` first, then `client/`, as for an online game |
| Assets or one system only | no code folder yet; the work lives in `tools/` and `docs/findings/` until a rewrite starts |

Each subfolder is a project of its own (its own build file), so a rewrite in another language sits beside the
emulator without touching it. Each keeps its data files in its own `data/`; once two parts read the same data, it
moves to `shared/data/`.

## Data: raw in, ours out

| Kind | Where | In git | How another machine gets it |
|---|---|---|---|
| Raw: crawled pages, parsed crawl tables | `_data/crawled/<site>/` | no | not needed; `setup.bat crawl` fetches it again on request |
| Raw: tables, text and assets extracted from the target | `_data/extracted/<version>/` | no | `setup.bat` runs the extract scripts on the user's copy |
| Ours: values, tables, placements, formulas, names, in our own format | `game/<part>/data/` | yes | it's in the clone |
| Ours: how each system works and the values it uses | `docs/findings/` | yes | it's in the clone |

- A converter in `tools/` turns raw data into our data files, and each file says where it came from in a header or
  a `source` field: the script, the raw source, its date. Re-run the converter rather than editing its output.
- Our data files hold facts in our own schema. The target's assets (models, textures, sounds, music) and long texts
  (dialogue, quest text, descriptions) stay in `_data/extracted/`, and the code loads them from there at run time.
- When a crawl adds something new, convert it into the data files and docs in the same milestone, so the crawl is
  never needed again to build or run the project.

## .gitignore

Write it before anything else, so that nothing heavy or proprietary is ever staged:

```gitignore
# The target, third-party tools, gathered data and other people's repos (docs/sources.md says how to get them again)
/_sdk/
/_data/
/_external/

# Build output and local state
target/
node_modules/
__pycache__/
*.log
.env
.claude/settings.local.json
```

Add the build folders of the languages the project uses. Never use `git add -f` on an ignored path.

## .gitattributes

Windows' `cmd` misreads batch files with LF line endings: lines run together and commands fail with errors like
`'xyz' is not recognized`. Keep launchers in CRLF on every machine:

```gitattributes
* text=auto
*.bat text eol=crlf
*.cmd text eol=crlf
*.sh text eol=lf
```

## AGENTS.md

```markdown
# <Project name>

Reverse engineering <target> (<platform>): <the goal in one sentence>. Decisions in `docs/adr/` (start with
`docs/adr/README.md`), facts in `docs/findings/`, what was tried in `docs/journal/`.

| | |
|---|---|
| Target | <name>, version <x> (copy in `_sdk/target/<version>/`) |
| Built with | <engine, language, packer>, or "not known yet (M1)" |
| Route | <route> (ADR-0002), or "decided at the end of M1" |
| Data | our data files (`game/<part>/data/`) and what made them; raw data in `_data/` |
| Protocol | for online targets: what is known, or "not known yet" |

## Folders

| Folder | What | Rules |
|---|---|---|
| `docs/` | ADRs, findings, journal, sources | `.claude/rules/research.md` |
| `tools/` | our own tools | `.claude/rules/code.md` |
| `game/server-emu/` | later: local server for the original client | |
| `_sdk/`, `_data/`, `_external/` | git-ignored: the target, gathered data, other people's repos | `.claude/rules/boundaries.md` |

## Run

| Launcher | What it does |
|---|---|
| `setup.bat` | after a fresh clone: fetches the repos and tools, rebuilds the data (needs your copy of the target) |
| `run_server_emu.bat` | (example) starts the local server and the original client |

## Rules

| File | Applies to |
|---|---|
| `.claude/rules/boundaries.md` | everything |
| `.claude/rules/research.md` | everything |
| `.claude/rules/methods.md` | everything |
| `.claude/rules/code.md` | `tools/**`, `game/**` |
```

Keep the target table current: it's the first thing every session reads. `CLAUDE.md` holds one line, `@AGENTS.md`.

## .claude/

### rules/

| File | Loads | Holds |
|---|---|---|
| `boundaries.md` | always (no `paths:`) | The rule text from `boundaries.md` in this skill |
| `research.md` | always (no `paths:`) | Read `docs/findings/` and the latest journal entries before researching anything; how to write a finding, a journal entry and a source (`records.md`); never record a guess as a fact |
| `methods.md` | always (no `paths:`) | The rule text from `methods.md` in this skill: how to cost a repeated job, and the table of the fastest known way to do each recurring job here |
| `code.md` | `paths:` = the code folders | Size limits (aim for 1000 lines or fewer per file, split along a clear seam above 1000, always split above 1200), one job per file, sections in the order header, imports, constants, types, state, helpers, public API, entry point, each under a short divider comment; read game data from the part's `data/` folder and assets from `_data/extracted/` through a relative path or an environment variable, never a path on one machine |
| `<part>.md` | `paths:` = that folder | Added with the part (`server-emu.md`, `extractor.md`): what it owns, how it's tested, and a **How to add** recipe (a packet handler, an archive format, a map) |

Rules are short and imperative. The reasons live in the ADRs.

### settings.json

```json
{
  "permissions": {
    "deny": ["Edit(/_sdk/target/**)", "Write(/_sdk/target/**)"]
  }
}
```

A leading `/` anchors the path at the folder the session was opened in, which is the project root for this file.

## Setup: the same project on any machine

A fresh clone plus `setup.bat` must give the same project: the same repos at the same commits, the same tool
versions, and the same data. Everything in the git-ignored folders comes from one of three places:

| Where it comes from | Examples | Recorded in |
|---|---|---|
| Fetched | `_external/` repos, `_sdk/tools/` programs | `setup.bat` (URL, commit or version) and `docs/sources.md` (licence, what it's for) |
| Made by our scripts | `_sdk/patched/`, `_data/extracted/`, decompiler output | the script in `tools/`, called by `setup.bat` or its launcher |
| Supplied by the user | `_sdk/target/<version>/` | `docs/sources.md`: the version, where it came from, SHA-256 of its main files |
| Crawled, only on request | `_data/crawled/` | the crawl script and `docs/sources.md`; `setup.bat crawl` runs them |

Rules:

- Nothing in `_sdk/`, `_data/` or `_external/` is made or changed by hand. A patch to the client is a script; a fix to
  extracted data is a step in the converter.
- Pin everything: a commit for each repo, a versioned download URL for each tool, the toolchain versions our code
  needs (`rust-toolchain.toml`, `.python-version`, or a line in `AGENTS.md`).
- Local settings files (server config, passwords, paths) are git-ignored; commit a `<name>.example` beside each, and
  `setup.bat` copies it when the real one is missing.
- Crawls run only with `setup.bat crawl` or their own launchers: what the project uses from them is already in its
  data files and docs, sites change, and fetching them again on every machine is impolite. A site may have changed
  since, so a new crawl can differ; the crawl date in `docs/sources.md` says which one the data files came from.
- `setup.bat` is safe to run again: it skips whatever is already there.

```bat
@echo off
rem Rebuilds everything git doesn't hold, after a fresh clone or on a new machine: _external\ (other people's repos at
rem the commits we used), _sdk\tools\ (third-party programs), then _sdk\patched\ and _data\extracted\ (made by our
rem scripts from your copy). "setup.bat crawl" also re-crawls the sites; the data files in git don't need it.
rem Safe to run again: it skips what is already there. Needs git; curl and tar come with Windows 10 and later.
setlocal
cd /d "%~dp0"
where git >nul 2>nul || (echo git is required: https://git-scm.com & pause & exit /b 1)

rem -- The target: your own copy, never downloaded (docs\sources.md has its hashes) --
if not exist "_sdk\target\<version>\<main file>" (
  echo Copy your install of <target> <version> into _sdk\target\<version>\ and run this again.
  pause & exit /b 1
)

rem -- Requirements for our code --
rem where cargo >nul 2>nul || (echo Rust is required: https://rustup.rs & pause & exit /b 1)

rem -- Repos in _external\: URL, folder, commit --
rem call :repo https://github.com/<owner>/<repo> <owner>\<repo> <commit>

rem -- Tools in _sdk\tools\: folder, versioned download URL of a .zip --
rem call :tool <tool> https://<versioned release URL>.zip

rem -- Local settings from their examples --
rem if not exist game\server-emu\config.toml copy game\server-emu\config.example.toml game\server-emu\config.toml

rem -- Made by our scripts from your copy --
rem call extract_all.bat

rem -- Crawls: only with "setup.bat crawl" --
if /i "%~1"=="crawl" (
  rem call crawl_wiki.bat
  echo Crawls done.
)

echo Setup done.
pause
exit /b 0

:repo
if exist "_external\%~2\.git" exit /b 0
git clone --quiet %1 "_external\%~2" && git -C "_external\%~2" checkout --quiet %3 || echo FAILED: %1
exit /b 0

:tool
if exist "_sdk\tools\%~1" exit /b 0
if not exist "_sdk\tools" mkdir "_sdk\tools"
curl -L --fail -s -o "_sdk\tools\%~1.zip" %2 && mkdir "_sdk\tools\%~1" && tar -xf "_sdk\tools\%~1.zip" -C "_sdk\tools\%~1" || echo FAILED: %1
if exist "_sdk\tools\%~1.zip" del "_sdk\tools\%~1.zip"
exit /b 0
```

M0 writes it with the sections commented out; each milestone that adds a repo, tool, script or settings file adds its
line in the same step. A tool with no direct download (an installer, a licence) gets an `echo` that says what to
install by hand and where. On macOS or Linux, write `setup.sh` with the same sections.

## Launchers

Everything that runs gets a launcher in the root, so the user can test it with a double-click and an agent can run
it the same way. Name it after what it does: `run_<thing>.bat`, `extract_<what>.bat`, `crawl_<site>.bat`,
`check.bat`. On macOS or Linux, write `.sh` files with the same names instead.

```bat
@echo off
rem Starts the local server emulator and the original client from _sdk\target\<version>.
rem The client connects to 127.0.0.1 only. Closing this window stops the server.
cd /d "%~dp0game\server-emu"
where cargo >nul 2>nul || (echo Rust is required: https://rustup.rs & pause & exit /b 1)
cargo run -- --client "%~dp0_sdk\target\<version>" || pause
```

- The `rem` lines say what it does, what it needs and how to stop it.
- It changes to its own folder first (`%~dp0`), so it works from anywhere.
- It checks its requirements and says how to install what's missing.
- It pauses on failure so the error stays readable.
- It is plain ASCII with CRLF line endings: no box-drawing characters, dashes or other non-ASCII text, which `cmd`
  misreads. `.gitattributes` keeps clones in CRLF, but a file you just wrote is LF until you convert it, for example
  with `python -c "import sys; p=sys.argv[1]; d=open(p,'rb').read().replace(b'\r\n',b'\n'); open(p,'wb').write(d.replace(b'\n',b'\r\n'))" setup.bat`.
- Test it through `cmd` (`cmd /c "setup.bat < nul"`), not by reading it.
- A check over many cases (every screen, every archive, every packet) is one launcher that starts the program once
  and walks them all, writing a result line per case (`methods.md`). It takes an optional list of cases, so a
  re-run can cover only the failures.
- Each launcher gets a row in `AGENTS.md` → Run.
