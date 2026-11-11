# Methods: the cheapest way that proves it

A milestone is slow when its loop is slow: the whole suite run after every edit, the app restarted for each change,
one launch per screen to look at. Pick how the work will be checked before starting it, and change the method as soon
as it turns out slow.

## Design for a fast check

In the second design pass, ask of each module: can it be checked without starting the whole program?

- Logic sits in modules a test can call directly; the entry point and the UI only wire them together.
- Anything with many cases of one kind (screens, levels, commands, importers) is listed in one place, so one run can
  walk them all.
- Slow or outside things (network, disk, clock, a device) sit behind one module a test can replace.

When the design can't give a fast check for a part, say so in the ADR's "Harder" line.

## Before a job that repeats

This applies when the same step will run more than about 5 times (files, tests, screens, modules to move), or when
one step takes more than about 10 seconds.

1. **Count.** Items × time for one = the total. Say it in one line before you start: "60 screens × 12 s = 12 min".
2. **Find the fixed cost.** What is paid on every item that could be paid once: starting the app, building, booting
   a test runner or an emulator, loading data, one tool call per item.
3. **Pay it once.** One process, session or script walks every item: open, check, close, next. Never one launch per
   item, and never one command per item when a script can loop.
4. **Try 3, then all.** Run 3 items, time them, fix what breaks, then run the rest.
5. **Write results to a file,** one line per item (id, pass or fail, detail), outside the source tree. Only the
   failures need a closer look.
6. **Stop on a pattern.** When the first items all fail the same way, fix that before running the rest.

## The cheapest check

Use the lowest step that can show the change is right, and go higher only for what it can't show:

| Step | Check | When |
|---|---|---|
| 1 | Type check, lint, compile | after every edit |
| 2 | The tests of the module you touched | after every step |
| 3 | The whole suite and the automated checks | once, in the milestone's done checks |
| 4 | One run of the program driven by a script: one launch, every case walked in the same process, a log line per case | what tests can't reach (rendering, wiring, start-up) |
| 5 | The user's eyes, on one list of everything to look at | what only a person can judge |

## When a method is too slow

Signs: most of each item's time is startup; you wait on the same step a third time; you send the same command again
with one argument changed; a run will take more than a few minutes; the user says it's slow.

Stop and look for a faster way before going on. Spend up to about a tenth of what the slow run would cost, in this
order:

1. **The project's own notes:** `AGENTS.md` → Working methods, and its commands.
2. **The tool's own modes:** a test filter, watch mode, incremental build, hot reload, headless run (its `--help`,
   its docs).
3. **Another tool the stack already has** for the job. Tooling changes often: when you have internet, check the
   stack's current docs instead of trusting what you remember.
4. **A small harness or script of our own,** when it saves more time than it takes to write.
5. **A smaller job:** only what changed, or the slow step's output cached.
6. **In parallel,** when the items don't depend on each other.

Time the old way and the new way on the same 3 items, keep the faster one, and record it (below).

| Slow | Fast |
|---|---|
| Starting the app once per screen, level or case | One launch and a driver that opens, checks and closes each in turn in the same process |
| The whole suite after every edit | The touched module's tests while working, the whole suite once at the done checks |
| A full rebuild and restart for each change | Incremental build, watch mode or hot reload |
| Reading every file to understand a codebase | The tree, the manifests, line counts and a search first; then only the files a decision depends on |
| Moving files one at a time, testing after each | One system moved in one step, its tests run once |
| One tool call per item | One script that loops and prints a summary table |
| A screenshot to read a value | A log line, a test assertion, a state dump |
| Asking the user to check items one at a time | One list they check in one pass |

## Recording a method in the project

This skill leaves the project's command and testing rules as they are, so it only adds to them. The second time a
job is done, and whenever a faster way is measured or the user corrects one, add or replace a row in `AGENTS.md` →
`## Working methods` (create the section when the project has no such table):

```markdown
## Working methods

The fastest known way to do each recurring job. When you find a faster way, time both and replace the row.

| Job | Method | Cost | Instead of |
|---|---|---|---|
| Check every screen | `npm run screens`: one launch, each screen opened and closed in turn, log in `tmp/screens.log` | 1–2 s a screen | one launch per screen, 12 s each |
```

## Improving this skill

A lesson that isn't about this project (it would have helped on any project) belongs in the skill too:

1. Put it in the milestone report as one line: "For the skill: <slow way> → <fast way>".
2. On the user's yes, add it as a row to the Slow/Fast table above, in the skill folder this file was loaded from.
   Write it for any project: no project names, paths or machine details.
3. Say which file you changed. An installed skill may be a copy, and the user may want the row in its source too.
