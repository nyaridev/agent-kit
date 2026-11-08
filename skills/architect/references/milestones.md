# Milestones

The plan from phase 3 is carried out as milestones M0, M1, M2… Each one is a stopping point the user approves.

## Shape of a milestone

- **One goal:** one system or one concern ("Save system", "Split the renderer"). Never two systems at once.
- **Numbered steps**, each small enough to review: a few files and one visible result.
- **Order:** foundations first, so a milestone never depends on a later one.

```markdown
### M2: Inventory

1. Create `src/inventory/` with the skeleton from the code-organization rule.
2. Move item logic out of `src/player.ts` into `src/inventory/inventory.ts`.
3. Point `shop.ts` and `hud.ts` at the new module.
4. Done checks.
```

## M0

| Project | M0 is |
|---|---|
| New | **Scaffold:** the folder tree; an entry point that runs; empty module skeletons in the section layout; the ADRs, overview and rules from phase 4; the checks, if chosen. |
| Existing | **Baseline:** confirm it builds or runs and its tests pass, before anything moves; add the files over 1000 lines to the tracker; set up the checks, if chosen. No behavior changes. |

## M1 and later

- **New project:** build one system per milestone, in dependency order.
- **Existing project:** move one system per milestone onto the new structure.
  - Behavior stays the same while code moves. A migration milestone adds no features.
  - Oversized files are split in the milestone of the system that owns them.

## The loop

1. **Ask first.** Before each milestone after M0, show its steps and wait for a yes. The user may reorder, cut or
   split steps.
2. **Stay inside the milestone.** No changes outside it. Anything you notice elsewhere goes on the tracker's
   "Later" list.
3. **Off the plan?** When something comes up that the plan didn't cover, stop and propose an ADR change before going
   on.
4. **Done checks**, at the end of every milestone:
   - it builds or runs;
   - the tests pass, or the manual check the user agreed to;
   - the automated checks pass, if they were chosen;
   - no file is over 1200 lines;
   - `docs/adr/README.md` is updated: the milestone is marked done and the next one's steps are listed.
5. **Report:** what changed, what was skipped and why, and a suggested commit message. The milestone is a safe point
   to roll back to. Commit only if the user asked you to.
6. **Ask** about the next milestone.

## Automated checks

Ask in phase 3, with your pick first:

| Option | What | Fits |
|---|---|---|
| None | The rules only | small projects, short-lived tools |
| Size check | A tiny script in the project's own language or shell: fails on files over 1200 lines, warns over 1000 | most projects |
| Size and boundaries | The size check, plus failing on imports the module table forbids (the stack's linter when it has an import-boundary rule, otherwise a small script) | large projects, several contributors |
| Hooked in | Either check, also run in CI or a pre-commit hook | projects that already have CI or hooks |

The check lives in the project (`scripts/check-architecture.*` or the stack's usual place), is listed in `AGENTS.md`
under the project's commands, and runs in every milestone's done checks.
