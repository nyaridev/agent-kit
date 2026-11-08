---
tags: [skill-creator]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Earlier in this chat you looked at my todo CLI and proposed this, and I've read it:

---
Direction: split todo.py into a CLI layer over a storage module, keeping the JSON file format.

Folder tree:
  todo/
    cli.py      argparse and printing only
    store.py    load, save, add, done on todos.json
  tests/

ADRs:
  - Move docs/decisions/0001 and 0002 into docs/adr/ with their numbers.
  - 0003 CLI over a store module: supersedes 0002 (everything in todo.py). Trade-off: two files instead of one.

Rules (.claude/rules/architecture/):
  overview.md (always): direction, module table, where new things go, how to add a command
  code-organization.md (todo/**, tests/**): 1000/1200 line limits, section order, divider style

Replacements:
  - .claude/rules/structure.md (architecture: "everything in todo.py") is removed; nothing carries over.
  - .claude/rules/testing.md (how to run tests) stays as it is.
  - CLAUDE.md keeps its content and gets @AGENTS.md; a new AGENTS.md gets the Architecture section.

Milestones:
  M0 Baseline: tests pass before anything moves, record docs and rules, no behavior change
  M1 Store module: move load/save/add/done into todo/store.py
  M2 CLI module: move argparse into todo/cli.py, keep `python todo.py` working
---

Approved. No automated checks for this one, it's tiny.

Input files: todo.py, tests/test_todo.py, CLAUDE.md, .claude/rules/structure.md, .claude/rules/testing.md, docs/decisions/0001-json-file-storage.md, docs/decisions/0002-single-file.md
