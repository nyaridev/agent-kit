# ADRs and the overview

All architecture docs live in `docs/adr/`:

```
docs/adr/
├─ README.md                    the overview: summary, ADR index, milestone tracker
├─ 0001-<kebab-title>.md        one file per decision
└─ 0002-<kebab-title>.md
```

## Writing an ADR

- **One decision per ADR.** "Use a layered layout" and "store saves as JSON" are two ADRs.
- **Numbers** are four digits, start at `0001`, and are never reused. The file name is the number plus a short
  kebab-case title: `0003-event-bus-between-systems.md`.
- **Keep it short:** usually 20–60 lines. The ADR explains why; the rules say what to do.
- **Status:**
  - `Accepted`: what the user approved in phase 3. ADRs are written straight as Accepted.
  - `Superseded by ADR-NNNN`: replaced by a later decision. Its text stays as it was, and the new ADR says
    `Supersedes ADR-NNNN`.
  - `Deprecated`: no longer applies, and nothing replaced it.
- **Never delete or rewrite an ADR.** To change a decision, write a new ADR and mark the old one superseded. Fixing a
  typo or a broken link is fine.
- **Existing ADRs elsewhere** (`doc/decisions/`, `architecture/`…): move them into `docs/adr/` with their numbers and
  dates, and continue the numbering after the highest one.

### Template

```markdown
# ADR-NNNN: <Title>

**Status:** Accepted
**Date:** YYYY-MM-DD
**Supersedes:** ADR-NNNN <!-- omit when it supersedes nothing -->

## Context

What problem or need forces this decision, and the constraints (stack, size, team, deadlines). 3–8 lines.

## Decision

What we do, stated plainly. Name the folders, modules and dependency rules it creates.

## Options considered

- **<Option>:** why not, in one line.
- **<Option>:** why not, in one line.

## Consequences

- **Easier:** what this makes simple.
- **Harder:** what it costs, and what to watch for.
- **Rules:** the rule files that apply it (`.claude/rules/architecture/<file>.md`).
```

## The overview: `docs/adr/README.md`

The one file to read first. It describes the architecture **as it is now**, so it's rewritten when the architecture
changes, unlike the ADRs.

```markdown
# Architecture

<What the project is, in one line. The direction in one sentence.>

## Shape

<The folder tree, top two levels, a short comment on each.>

## Modules

| Module | Owns | May depend on |
|---|---|---|
| `core/` | game rules and state | nothing |
| `ui/` | screens and widgets | `core/` |

## Decisions

| ADR | Title | Status |
|---|---|---|
| [0001](0001-layered-layout.md) | Layered layout | Accepted |

## Milestones

| Milestone | Goal | Status |
|---|---|---|
| M0 | Scaffold | done |
| M1 | Save system | in progress |
| M2 | Inventory | planned |

### M1: Save system

- [x] 1. Move save code from `main.py` into `core/save/`
- [ ] 2. Split `core/save/store.py` (1340 lines) into `store.py` and `migrate.py`
- [ ] 3. Point callers at the new module

### Later

- Things found during the work that belong to another milestone, one line each.

## Rules

Where the architecture rules live (`.claude/rules/architecture/`), with one line on each file.
```

- Only the current milestone's steps are listed. When a milestone is done, mark it `done` in the table and remove its
  step list.
- Keep the overview short (about a screen or two). Details belong in the ADRs and rules.
