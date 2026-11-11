# Milestones

The plan from phase 3 is carried out as milestones M0, M1, M2… Each one is a stopping point the user approves.

## Shape of a milestone

- **One goal:** one system or one concern ("Save system", "Split the renderer"). Never two systems at once.
- **Numbered steps**, each small enough to review: a few files and one visible result.
- **Small enough for one session:** about 8 steps at most. Split a system that needs more, or that has many cases
  of one kind, along its own seams: first the mechanism with a few cases end to end, then the rest in groups, each
  its own milestone ("M3: screen framework and the 5 simplest screens; M4: shop and inventory screens"). Never one
  milestone for the whole project or a whole large system.
- **Order:** foundations first, so a milestone never depends on a later one.
- **A named check:** how the milestone is proved done, by the cheapest check that can prove it (`methods.md`). A
  check over many cases is one run that walks them all, never one launch per case.

```markdown
### M2: Inventory

1. Create `src/inventory/` with the skeleton from the code-organization rule.
2. Move item logic out of `src/player.ts` into `src/inventory/inventory.ts`.
3. Point `shop.ts` and `hud.ts` at the new module.
4. Done checks.

Checked by: the inventory tests while working; the whole suite once at the end.
```

## M0

| Project | M0 is |
|---|---|
| New | **Scaffold:** the folder tree; an entry point that runs; each module as a header comment plus only the sections it already has code for; the ADRs, overview and rules from phase 4; the checks, if chosen. |
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
4. **Too slow?** When a step is mostly startup, or you wait on it a third time, or the user says it's slow, stop and
   find a faster method (`methods.md`), then record it in `AGENTS.md` → Working methods.
5. **Done checks**, at the end of every milestone:
   - it builds or runs;
   - the tests pass, or the manual check the user agreed to;
   - the automated checks pass, if they were chosen;
   - no file is over 1200 lines;
   - `docs/adr/README.md` is updated: the milestone is marked done and the next one's steps are listed.
6. **Report:** what changed, what was skipped and why, what was slow and what replaced it, and a suggested commit
   message. The milestone is a safe point to roll back to. Commit only if the user asked you to.
7. **Ask** about the next milestone by showing its numbered steps in the same message, not by asking whether to list
   them.

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
