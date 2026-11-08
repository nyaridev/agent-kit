# Rules and how they connect

The ADRs explain the architecture. The rules tell agents what to do while they work. Write them in phase 4.

## Where the rules go

| The project uses | Rules folder | How they load |
|---|---|---|
| Claude Code (it has `.claude/` or a `CLAUDE.md`, or the user works in Claude Code) | `.claude/rules/architecture/` | Claude Code loads every `.md` in `.claude/rules/`, subfolders included. `paths:` frontmatter limits a file to matching files. |
| Other agents only | `docs/rules/architecture/` | `AGENTS.md` lists each file and when to read it. |

Use one folder only. Never keep a copy of the same rule in two places.

## The rule files

Pick by the project's size (`SKILL.md` → Understand). Each file covers one topic and stays short, usually 20–60
lines. Use imperative sentences, with no explanations: the reasons are in the ADRs.

| File | Always? | What it holds |
|---|---|---|
| `overview.md` | yes, no `paths:` | The direction in 2–3 lines; the module table with allowed dependencies; a "where new things go" table; which file has each "How to add" recipe; "architecture changes need a new ADR in `docs/adr/`, and an update to `docs/adr/README.md` and these rules" |
| `code-organization.md` | yes, `paths:` = the source files | This project's size limit, section order and divider style, with a tiny skeleton file (`code-organization.md` in this skill) |
| `<module>.md` | medium and large projects | One module or layer: what it owns, what it may and may not depend on, its naming, and a **How to add** recipe |

### "How to add" recipes

They come from the third design pass. Each one is a few numbered steps that name the folders and files:

```markdown
## How to add a system

1. Create `src/systems/<name>/` with `<name>.ts` (the system) and `index.ts` (exports only).
2. Register it in `src/systems/registry.ts`.
3. Talk to other systems only through events in `src/core/events.ts`, never by importing them.
```

### Path-scoped rules (Claude Code)

A rule file that applies only to some files starts with `paths:` frontmatter, so it loads only while the agent works
on matching files:

```markdown
---
paths:
  - "src/systems/**"
---

# Systems
```

- `overview.md` has no `paths:`, so it always loads and can point to the other files.
- Use globs that match the real folders. Check them against the tree before writing them.

## Connecting the rules

1. **`AGENTS.md`** gets an `## Architecture` section (create `AGENTS.md` if it's missing):

   ```markdown
   ## Architecture

   <The direction in one sentence.> Read `docs/adr/README.md` first.

   | Rules | Applies to |
   |---|---|
   | `.claude/rules/architecture/overview.md` | everything |
   | `.claude/rules/architecture/code-organization.md` | `src/**` |
   ```

   It points to the files and doesn't repeat what they say.
2. **`CLAUDE.md`** (Claude Code projects): it must contain `@AGENTS.md`. Create it with that line, or add the line at
   the top of an existing one.
3. Check that every path you wrote in `AGENTS.md`, the overview and the rules exists.

## Replacing old rules

For an existing project that already has architecture, design, structure or code-style rules:

1. **Find them** in phase 1: rules folders, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/`,
   `.github/copilot-instructions.md`, `CONTRIBUTING.md`, and architecture docs in `docs/`.
2. **List them in phase 3:** each file or section, whether it's removed or replaced, and which points still hold and
   carry over into the new rules or an ADR.
3. **In phase 4,** write the new rules first. Then remove the old architecture files and sections, which git history
   keeps.
4. **Leave alone** whatever isn't architecture: commands, git, testing, deployment and tone rules stay where they are.
   A file that mixes both keeps its other sections.
5. **Old ADRs are never removed.** Mark them superseded (`adr.md`).
