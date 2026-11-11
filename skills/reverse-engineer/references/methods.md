# Methods: the cheapest way that proves it

Most time in reverse engineering is lost to slow loops, not hard problems: a program started once per item, a binary
analysed again every session, a screenshot taken where a log line would do. Pick the method before you start the
work, and change it as soon as it turns out slow.

## Before a job that repeats

This applies when the same step will run more than about 5 times (files, screens, packets, functions, pages), or when
one step takes more than about 10 seconds.

1. **Count.** Items × time for one = the total. Say it in one line before you start: "194 screens × 13 s = 42 min".
2. **Find the fixed cost.** What is paid on every item that could be paid once: starting the program, loading its
   data, logging in, analysing the binary, compiling, opening a connection, one tool call per item.
3. **Pay it once.** One process, session or script walks every item: open, check, close, next. Never one launch per
   item, and never one command per item when a script can loop.
4. **Try 3, then all.** Run 3 items, time them, fix what breaks, then run the rest.
5. **Write results to a file,** one line per item (id, pass or fail, detail), in `_data/captures/`. A crash then
   resumes where it stopped, and only the failures need a closer look.
6. **Stop on a pattern.** When the first items all fail the same way, fix that before running the rest.

## The cheapest check

Use the lowest step that can show the thing is right, and go higher only for what it can't show:

| Step | Check | Shows |
|---|---|---|
| 1 | Read the data or the code (search, parse, diff) | a value, a layout, a missing entry |
| 2 | Call the function directly with the target's own bytes and compare with the known answer | a parser, a cipher, a formula |
| 3 | Run it headless: the tool's command line, the server without the client, a recorded capture replayed | a handler, an extractor, a converter |
| 4 | One live session driven by a script: one launch, every case walked in the same process, a log line per case | how the original client reacts |
| 5 | The user's eyes, on one list of everything to look at | what only a person can judge |

A screenshot is step 5 for whoever reads it. Take one only where a log, a dump or a state query can't answer.

## When a method is too slow

Signs: most of each item's time is startup; you wait on the same step a third time; you send the same command again
with one argument changed; a run will take more than a few minutes; the user says it's slow.

Stop and look for a faster way before going on. Spend up to about a tenth of what the slow run would cost, in this
order:

1. **The project's methods rule and journal:** is it already solved here?
2. **The tool's own batch, headless, scripting or watch mode:** its `--help`, its docs.
3. **Another tool built for the job** (`sources.md`). Tools for an engine or format change often: when you have
   internet, search for what its community uses now instead of trusting what you remember.
4. **Our own harness in `tools/`,** when it saves more time than it takes to write. A job that will come back in
   later milestones almost always does.
5. **A smaller job:** only what changed since the last run, or the slow step's output cached in `_data/`.
6. **In parallel,** when the items don't depend on each other and the tool is safe to run twice at once.

Time the old way and the new way on the same 3 items, keep the faster one, and record it (below).

| Slow | Fast |
|---|---|
| Starting the program once per screen, widget, map or item | One launch and a driver that opens, checks and closes each in turn in the same process |
| A decompiler's window, one function at a time | One headless analysis, kept; a script exports every function or the ones that match (Ghidra's `analyzeHeadless`, IDA's batch mode) |
| Analysing the binary again each session | The tool's project or database kept in `_sdk/tools/` and reopened |
| One command per archive or file | An extractor that walks the folder and skips what is already done |
| Restarting the client to test each packet or handler | Captured packets replayed against the server in a test; the client only for the last check |
| Rebuilding the server for each data change | Data files read at start or on a reload command |
| A screenshot to read a value | A log line, a dump, the data file |
| Reading a large dump from top to bottom | Search it or index it first, read only the hits |
| Fetching a site page by page | Its API or export dump when it has one, then a resumable crawler |
| One tool call per item | One script that loops and prints a summary table |
| Asking the user to check items one at a time | One list they check in one pass |

## The project's methods rule

M0 copies the rule text below into `.claude/rules/methods.md`, with the table's header only (the row shown is an example). It has no `paths:`, so
every session loads it. Add a row the second time a job is done, and replace the row as soon as a faster way is
measured, in the same step. A method the user corrects is recorded at once, before the work goes on.

```markdown
# Methods

The fastest known way to do each recurring job here. Use the row. When you find a faster way, time both and replace
the row in the same step.

- **Count before you loop.** Before a job with more than about 5 items, or a step over about 10 seconds, say the
  total (items × time for one) and how much of it is startup.
- **Pay startup once.** One process, session or script walks every item: open, check, close, next. Never one launch
  per item, and never one command per item when a script can loop.
- **Try 3, then all.** Time 3 items, fix what breaks, then run the rest. One result line per item goes to a file in
  `_data/captures/`, so a crash resumes where it stopped.
- **Cheapest check that proves it:** read the data or code; call the function directly; run it headless; one
  scripted live session; the user's eyes on one list.
- **Too slow?** When a step is mostly startup, you wait on it a third time, or the user says it's slow: stop and find
  a faster way first (the tool's batch or headless mode, another tool, our own harness in `tools/`).

| Job | Method | Cost | Instead of |
|---|---|---|---|
| Check every UI screen | `check_ui.bat`: one client launch, each screen opened and closed in turn, log in `_data/captures/ui-check.log` | 1–2 s a screen | one launch per screen, 13 s each |
```

## Improving this skill

A lesson that isn't about this target (it would have helped on any target) belongs in the skill too:

1. Put it in the milestone report as one line: "For the skill: <slow way> → <fast way>".
2. On the user's yes, add it as a row to the Slow/Fast table above, in the skill folder this file was loaded from.
   Write it for any project: no target names, paths or machine details.
3. Say which file you changed. An installed skill may be a copy, and the user may want the row in its source too.
