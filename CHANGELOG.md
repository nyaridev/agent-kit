# Changelog

## Unreleased

- Repo: README banners (`assets/brand/`, dark and light) and a shorter README.
- `reverse-engineer`: first version. Plan first, then M0 scaffold (one repo; `docs/adr`, `findings`, `journal`,
  `sources.md`; git-ignored `_sdk/`, `_data/`, `_external/`; `.claude/rules` and root launchers), M1 recon ending with
  the route and language question, then one approved milestone at a time. Boundaries: local only, no DRM or anti-cheat
  bypass, nothing proprietary in git.
- `reverse-engineer`: rebuildable on any machine. `setup.bat` fetches `_external/` repos at pinned commits and
  `_sdk/tools/` at pinned versions, reruns the scripts that make `_sdk/patched/` and `_data/`, and checks the user's copy
  of the target against hashes in `docs/sources.md`; nothing in the ignored folders is made by hand. Commits only when
  asked. Launchers are ASCII with CRLF line endings (`.gitattributes`), since `cmd` misreads LF files, and are tested
  through `cmd`.
- `reverse-engineer`: raw data in, our data out. Crawled and extracted data stays raw in `_data/`; converters turn what
  the project uses into committed data files in `game/<part>/data/` (values, tables, placements, names) and docs, so a
  clone works without crawling. Crawls run only with `setup.bat crawl`; art, sound and long texts are re-extracted
  from the user's copy, never committed.
- `reverse-engineer`: the cheapest method that proves it (`references/methods.md`). Before a job that repeats, the
  agent counts its cost and pays the startup once (one session walks every screen, file or packet, never one launch
  per item), tries 3 items first, and uses the cheapest check that can prove the milestone. A slow method is stopped
  and replaced. Projects get `.claude/rules/methods.md`, a table of the fastest known way to do each recurring job;
  recon notes each tool's headless mode and how the target can be tested in one run; lessons that fit any target are
  offered as a row for the skill itself. New test case `many-screens-check`.
- `reverse-engineer`: recon ends with a system map (`docs/findings/overview.md` → Systems: each system, what it
  needs, its size), and the milestones after it come from the map, one system each in dependency order: study and
  findings first, then the smallest working version, then the rest. A milestone over about 8 steps, or a system with
  many cases, is split into several. Phase 5 is now "M2 and later".
- `architect`: a milestone is at most about 8 steps; a large system is split into several milestones along its seams.
- `architect`: the same method rules for building (`references/methods.md`): designs are checked for parts that can
  be tested without starting the whole program, every milestone names its check, and faster methods are recorded in
  the project's `AGENTS.md` → Working methods and offered for the skill. New test case `many-screens-check`.
- `architect`: first version. Three-pass design, approval before any file is written, ADRs and overview in
  `docs/adr/`, path-scoped architecture rules linked from `AGENTS.md`, one approved milestone at a time, a size check
  you can opt into, file size limits (1000/1200 lines) and section order for code.
- `architect`: the plan fits on one screen (full rule paths, M0 steps only, reasoning goes into the ADRs), ADRs get a
  "Later" consequence, and scaffolds leave no empty section dividers. Three test cases in `evals/`.
- `architect`: only files under about 40 lines may skip dividers; the next milestone's steps come with the report, so
  one reply approves it. Two more test cases: a vague request, and an existing project with old ADRs and rules.
