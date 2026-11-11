---
name: reverse-engineer
description: Reverse engineer a game or app (the whole thing, one system, or only its assets or data) in a project laid out to grow into a full reverse-engineering effort. Sets up docs/adr/, findings and a research journal, _external/ for open-source references, _sdk/ for tools and the original copy, launchers, and agent rules; then works one approved milestone at a time, from recon to a local server emulator, an asset extractor or a rewrite. Use when the user wants to reverse engineer, decompile, datamine, extract assets or data from, document how a system works in, emulate the server of, make a local or private server for, or remake or port an existing game or app, even if they don't say "reverse engineering".
argument-hint: "[the game or app, and which part: all, a system, or assets]"
---

# Reverse engineer

Sets up a reverse-engineering project for a game or app and works through it one approved milestone at a time. The
project always has the layout of a full effort, even when the user wants one part, so that later work lands in a
place that already exists and nothing has to be moved.

## Principles

- **Fastest route to results.** Pick the route that gets something running and testable soonest, then build on it.
  For an online game that is usually a local server emulator for the original client (`references/routes.md`).
- **Nothing is learned twice.** Every finding is written down with its source and date, and every dead end goes in the
  journal, so the next session starts from facts instead of guesses.
- **The cheapest method that proves it.** Before any job that repeats, count what it will cost and pay the startup
  once: one process walks every item, never one launch per item. When a method turns out slow, stop and find a
  faster one, then record it so no session falls back to the slow way (`references/methods.md`).
- **Reimplement, don't break in.** Study files, code and behaviour; never crack DRM, bypass anti-cheat or touch live
  servers (`references/boundaries.md`).
- **The repo holds only your own work.** The target's files, extracted data, crawled pages, other people's repos and
  third-party tools stay in git-ignored folders.
- **Raw data in, our data out.** Crawled pages and extracted tables are raw material in `_data/`. What the project
  takes from them becomes our own data files in the code folder (values, tables, placements, in our format,
  committed) and docs on how each system works, so a fresh clone works without crawling anything
  (`references/layout.md` → Data).
- **Rebuildable on any machine.** `setup.bat` fetches the repos at their commits and the tools at their versions, and
  re-extracts what the code needs from the user's own copy of the target, checked against recorded hashes. Crawls run
  only when the user asks (`setup.bat crawl`). Nothing in the ignored folders is made by hand (`references/layout.md`
  → Setup).
- **One system at a time,** and every milestone needs the user's yes.

## Phases

| Phase | Files | Ends with |
|---|---|---|
| 1. Understand | read only | the target, the part wanted and the goal are known |
| 2. Plan | read only | the user approves the plan |
| 3. M0: scaffold | the project skeleton | the layout, rules and docs on disk |
| 4. M1: recon | findings, journal, sources | the system map, the route ADR, and the user's choice of route and language |
| 5. M2 and later | code, tools, data | one system per milestone, each done and approved before the next |

**Create or edit no file before the user approves the plan in phase 2.** Looking at the target (file names, sizes,
headers, strings) is fine.

## 1. Understand

Settle these from the request and, when the user gives a path, from a read-only look at the target:

- **The target:** name, version, platform, and whether it's a game or an app, single-player or online.
- **The part wanted:** all of it, one system (a file format, the network protocol, combat rules, a UI), or only its
  assets or data.
- **The goal:** study and documentation, a local server for the original client, extracted assets, a mod, or a
  rewrite.
- **The language** for new code, if the user named one.
- **What exists already:** an earlier project folder, community servers, extractors, wikis. If the project folder
  exists, read its `AGENTS.md`, `docs/` and journal first and continue from there instead of starting over. When it
  has no `.claude/rules/methods.md` or no system map in `docs/findings/overview.md` yet, add them as the first steps
  of the next milestone, and re-cut the remaining milestones from the map.

Ask only what you can't settle, in one message with options. Leave the route and the language open when recon must
decide them: they're asked at the end of M1.

## 2. Plan and get approval

Keep the plan to one screen (about 40–60 lines). Show in chat:

1. **Target and goal:** two or three lines.
2. **Route:** the one you recommend and why it's fastest, from `references/routes.md`. Mark it provisional when recon
   must confirm it.
3. **Layout:** the top-level tree (`references/layout.md`), with the folders this goal needs now and the ones that
   wait for later. Name the `game/` or `app/` subfolders the route will add.
4. **M0 steps,** numbered, since approval covers them.
5. **M1 recon:** one line on what it checks and that it ends with the route and language question.
6. **Later milestones:** one line each, marked as a sketch that M1 will refine.
7. **What needs the user:** a copy of the target (path, version), anything you can't fetch yourself.

Flag anything in the target that falls under `references/boundaries.md` (anti-cheat, DRM, an always-online login)
and say how the route avoids it. Ask for approval, revise until it comes, and treat it as covering M0 only.

## 3. M0: scaffold

Follow `references/layout.md`:

1. `git init` in the project root; write `.gitignore` first, so nothing heavy is ever staged, and `.gitattributes`,
   which keeps launchers in the CRLF line endings Windows needs.
2. `AGENTS.md` (target table, folder map with the later slots, run table, rules table) and `CLAUDE.md`.
3. `.claude/rules/` (boundaries, research, methods, code) and `.claude/settings.json`.
4. `docs/`: `README.md`, `adr/README.md` with the milestone tracker, `adr/0001-scope-and-layout.md`, `findings/`,
   the first journal entry, `sources.md` (`references/records.md`).
5. The git-ignored folders: `_sdk/`, `_data/`, `_external/`. Copy the target into `_sdk/target/<version>/` when the
   user gave a path. Copy it, never move it, and ask first if it's large (several GB). Record the version and the
   SHA-256 of its main files in `docs/sources.md`.
6. `setup.bat`: checks the requirements and the target copy, with empty sections for repos, tools and data that later
   milestones fill (`references/layout.md` → Setup). Make it ASCII with CRLF line endings, then run it through `cmd`
   to check it passes.
7. Done checks (below), then report with a suggested commit message and show M1's steps. Commit only when the user
   asked you to.

Other launchers come with the thing they start, so M0 adds none besides `setup.bat` unless something can already run.

## 4. M1: recon

Follow `references/routes.md` → Recon. Find out how the target is built (engine, language, packers, protections),
its file formats, how it talks to servers, and what other people have already published (open-source servers,
extractors, format docs, wikis: `references/sources.md`). Clone what helps into `_external/`, and record each in
`docs/sources.md` and `setup.bat`. List the third-party programs the route needs for `_sdk/tools/`, each with its
batch or headless mode, and download them only after the user says yes, through `setup.bat`, so another machine gets
the same versions.

M1 ends with:

- `docs/findings/overview.md`: what the target is made of, each fact with its source, and the **system map**: the
  target cut into systems, with what each needs and how big it is (`references/routes.md` → The system map);
- `docs/adr/0002-route.md` with status **Proposed**: the recommended route, the options considered, and the
  milestones that follow from the map, one system each, in dependency order;
- one question to the user: which route, and which language for new code (unless already given), with your pick
  first.

When the user answers, mark ADR-0002 **Accepted**, update the tracker with the milestones, and show the next
milestone's steps.

## 5. M2 and later: one system per milestone

Each milestone takes one row of the system map (one system, one tool, one data source) and has numbered steps:
study the system and write its findings first, then build the smallest version that works end to end, then the
rest, then check. A milestone that needs more than about 8 steps, or covers a system with many cases, is split into
several before it starts (`references/routes.md` → Milestones after recon). Never build the whole target, or a whole
large system, in one go.

1. Before each milestone, show its steps and wait for a yes. Say how it will be tested: the cheapest check that
   proves it, and for a check over many items, the count, the time for one and the single run that covers them all
   (`references/methods.md`).
2. Work only inside the milestone. Note anything else on the tracker's "Later" list.
3. Record as you go (`references/records.md`): a journal entry for the session, each fact in `docs/findings/`, each
   new source in `docs/sources.md` and `setup.bat`, and an ADR for each decision that's hard to undo. Turn the raw
   data a milestone uses into data files in the code folder with a converter, not by hand.
4. Watch the cost as you go. When a step is mostly startup, or you wait on it a third time, or the user says it's
   slow, stop and find a faster method before continuing, then put it in `.claude/rules/methods.md`.
5. Give each runnable thing a launcher in the root (`references/layout.md` → Launchers) and a row in `AGENTS.md`.
6. **Done checks:** the launchers you added run through `cmd` (ASCII, CRLF); `setup.bat` covers everything new in `_sdk/`, `_data/` and
   `_external/` and still passes; the journal entry and findings are written; the methods rule has every job that
   was done twice; the tracker shows the milestone done and the system map is corrected; `git status` shows nothing from `_sdk/`, `_data/` or
   `_external/`; no source file is over 1200 lines.
7. Report what changed, what didn't work, what was slow and what replaced it, and a suggested commit message. Commit
   only when the user asked you to. A lesson that would help on any target goes in as one line for the skill
   (`references/methods.md` → Improving this skill). In the same message, show the next milestone's numbered steps
   and ask for a yes.

When something contradicts the route or a recorded finding, stop: write it in the journal, propose a fix or a
superseding ADR, and get a yes before working around it.
