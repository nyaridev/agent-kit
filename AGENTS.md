# AGENTS.md — Agent Kit

Guide for AI agents (Claude Code, Cursor, Codex…) working in this repo. In Claude Code, the workspace and category
rules load from the `CLAUDE.md` files above this folder; this file covers only what's specific here.

## What this is

Portable agent skills and templates that anyone can copy into their own setup. Nothing here is installed: it's the
source that gets copied out (`README.md` → Install).

## Layout

| Path | What |
|---|---|
| `skills/<name>/SKILL.md` | One skill: frontmatter (`name`, `description`) and its workflow |
| `skills/<name>/references/` | Details the skill reads when a step needs them |
| `CHANGELOG.md` | What changed, per skill |
| `assets/brand/` | The README's banners, dark and light |

## Rules

- **Universal.** Skills are shared with other people, so they name no machine, user, drive, workspace folder or
  personal project. Paths are relative to the project the skill works in (`docs/adr/`, `.claude/rules/`).
- **Self-contained.** A skill folder works when copied alone: it links only to files inside itself.
- **Short `SKILL.md`.** Keep the workflow in `SKILL.md` (under about 200 lines) and move details into `references/`.
- **The description triggers the skill.** It says what the skill does and when to use it, with the words a user would
  say.
- A change to a skill gets a line in `CHANGELOG.md` and, when it changes what users see, an update to `README.md`.
