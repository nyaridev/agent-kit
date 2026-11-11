---
tags: [skill-creator]
max_turns: 50
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Earlier in this chat you proposed this plan and I've read it:

---
Target: Hollowmere, a single-player 3D adventure game (Windows, version 1.0.3), my copy is in ../hollowmere-install.
Goal: extract its models, textures and sounds so I can study them. Maybe a full remake later.

Route: assets only, with an extractor in tools/ (provisional, recon confirms the archive format).

Layout:
  AGENTS.md CLAUDE.md .gitignore .claude/
  docs/ (adr, findings, journal, sources.md)
  tools/ (extractor later, scripts/)
  _sdk/ _data/ _external/ (git-ignored)
  game/client/ later, if the remake happens

M0 Scaffold:
  1. git init and .gitignore
  2. AGENTS.md and CLAUDE.md
  3. .claude/rules and settings.json
  4. docs: README, adr/README with the tracker, 0001 scope and layout, first journal entry, sources.md
  5. copy the game into _sdk/target/1.0.3/
  6. setup.bat, so the project can be rebuilt on another machine
M1 Recon: engine, archive formats, existing extractors; ends with the route and language question.
---

Approved, go ahead with M0. The project folder is empty.
