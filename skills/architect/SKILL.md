---
name: architect
description: Plan a project's architecture, record it as ADRs in docs/adr/, wire it into the agent rules, then build or migrate it one approved milestone at a time. Use when starting a new project, when asked to design, plan, restructure, clean up or improve the architecture or structure of an existing project, when writing or updating ADRs, or when a codebase has grown messy and needs a clear direction.
argument-hint: "[what to build, or what to restructure]"
---

# Architect

Turns a project idea or an existing codebase into a clear architecture: a few ADRs, a short set of rules that agents
follow, and a milestone plan that is built one approved milestone at a time.

## Principles

- **Clear over clever.** One direction, stated in one sentence, that a newcomer can follow without asking.
- **As small as the project.** The smallest architecture that holds the project's real scope. No layers, patterns or
  extension points for needs nobody has named.
- **One system at a time.** Design, build and migrate one system per milestone. Never leave two half-done.
- **Every rule earns its place.** If a rule wouldn't change what an agent writes, drop it. Reasons live in the ADRs;
  rules only say what to do.
- **The project's other rules stay.** This skill owns architecture and code-organization rules only. Commands, git,
  testing and style rules are left as they are.

## Phases

| Phase | Files | Ends with |
|---|---|---|
| 1. Understand | read only | the scope and size are known |
| 2. Design, in three passes | read only | a draft in your head |
| 3. Present | read only | the user approves the plan |
| 4. Record | docs and rules | ADRs, overview and rules on disk |
| 5. Build | code | each milestone done and approved before the next |

**Create or edit no file before the user approves in phase 3.** Reading, searching and counting lines are fine.

## 1. Understand

- **New project:** from the request, settle what it does, its platform and stack, who uses it, and its rough size.
- **Existing project:** read the README, `AGENTS.md`/`CLAUDE.md`, every rules folder (`.claude/rules/`,
  `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`), `docs/`, any existing ADRs, the folder tree,
  the package manifests, and the line counts of the largest source files. Note what the code does well and what hurts.
- **Size the project.** It decides how much you write:

  | Size | Looks like | ADRs | Rule files |
  |---|---|---|---|
  | Small | a script or single-purpose tool, a handful of files | 1 | 1–2 |
  | Medium | an app or game with a few systems | 1–3 | 2–4 |
  | Large | many systems, several contributors or packages | one per real decision | one per topic |

  When the request and the code don't make the size clear, ask the user one question about scope (with options:
  what it must do now, what is planned next) instead of guessing big.

## 2. Design in three passes

Do all three passes before showing anything.

1. **First pass: the design.** The modules or layers and what each owns; which may depend on which; where state
   lives; how data flows; the folder layout and naming; how files are organized inside
   (`references/code-organization.md`). Use the stack's own conventions and whatever the project already does well
   before inventing anything.
2. **Second pass: the critique.** For each part, name what it gains, what it costs, and what would break it. Cut
   anything that serves no current or clearly planned need. Check that every new file has one obvious home, that the
   layers fit the project's size, and that a newcomer could follow it.
3. **Third pass: the future.** Walk three realistic future additions through the design (a new feature, a new system
   or screen, a new data source or platform). Each must land in one obvious place without touching unrelated modules.
   When one doesn't, fix the design. Add an extension point only where a named need requires it. These walkthroughs
   become the "How to add" recipes in the rules.

Settle on one recommended design. Don't hand the user a menu: other options go in each ADR's "Options considered".

## 3. Present and get approval

The user has to read and judge this plan, so keep it to one screen: about 40 lines for a small project, 80 for a large
one. A long plan hides the decisions that matter. The reasoning from the three passes goes into the ADRs in phase 4,
not into this message. Show in chat:

1. **Direction:** one sentence, then up to 3 lines of summary.
2. **Folder tree:** the top two levels, with a short comment on each.
3. **Decisions:** one line per ADR: title, the decision, and its main trade-off.
4. **Rules:** one line per rule file, by its full path (`.claude/rules/architecture/overview.md`…): what it covers and
   which files it applies to. Always include `overview.md` and `code-organization.md` (`references/rules-wiring.md`).
5. **Replacements** (existing projects): the architecture or design rules and docs that will be removed, and what from
   them is kept in the new rules (`references/rules-wiring.md` → Replacing old rules). A short table works well.
6. **Milestones:** M0 with its numbered steps, since approval covers it. Later milestones get one line each with their
   goal; their steps are shown before each one starts (`references/milestones.md`).
7. **Future needs the user named** (sync, multiplayer…): one line each on where they will land. Leave the other
   walkthroughs for the ADRs.
8. **Automated checks:** ask which option the user wants (`references/milestones.md` → Automated checks), with your
   pick first.

Add assumptions only when they change the design, at most three lines. Ask for approval. Revise and show the plan again until the user approves it. Approval covers phase 4 and M0. Every
later milestone needs its own yes.

## 4. Record

- ADRs and the overview: `references/adr.md`. Each decision is its own `docs/adr/NNNN-<title>.md`, and
  `docs/adr/README.md` is the one general file (summary, ADR index, milestone tracker).
- Rules and how they connect to `AGENTS.md`: `references/rules-wiring.md`.
- Replace old architecture rules as shown in phase 3. Never delete an ADR: mark the old one superseded.

## 5. Build, one milestone at a time

Follow `references/milestones.md`:

1. Before each milestone after M0, show its steps and wait for a yes.
2. Do the steps in order. Touch only the system this milestone is about.
3. Finish with the done checks: it builds or runs, tests pass, checks pass if chosen, and the tracker is updated.
4. Report what changed and suggest a commit message. In the same message, show the next milestone's numbered steps
   and ask for a yes, so the user can approve it in one reply.

When the work turns up something the plan didn't cover, stop. Propose an ADR change (a new ADR, or a superseding one)
and get a yes before coding around it. When the user changes direction, update the ADRs and rules first, then the code.

## Code organization

Every file written in phase 5 follows `references/code-organization.md`: the size limit (aim for 1000 lines or fewer,
never more than 1200), one responsibility per file, and a fixed section order with short divider comments. Phase 4
writes the project's version of it into the rules.
