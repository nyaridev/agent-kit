# skyrift-re

Reverse engineering Skyrift (Windows), a small online co-op game: run it locally and document how it works.
Decisions in `docs/adr/` (start with `docs/adr/README.md`), facts in `docs/findings/`, what was tried in
`docs/journal/`.

| | |
|---|---|
| Target | Skyrift, version 1.2 (copy in `_sdk/target/1.2/`) |
| Built with | not known yet (M1) |
| Route | decided at the end of M1 |

## Folders

| Folder | What | Rules |
|---|---|---|
| `docs/` | ADRs, findings, journal, sources | `.claude/rules/research.md` |
| `tools/` | our own tools | `.claude/rules/code.md` |
| `game/` | later: shaped by the route | |
| `_sdk/`, `_data/`, `_external/` | git-ignored | `.claude/rules/boundaries.md` |
