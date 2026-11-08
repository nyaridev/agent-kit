# Changelog

## Unreleased

- `architect`: first version. Three-pass design, approval before any file is written, ADRs and overview in
  `docs/adr/`, path-scoped architecture rules linked from `AGENTS.md`, one approved milestone at a time, a size check
  you can opt into, file size limits (1000/1200 lines) and section order for code.
- `architect`: the plan fits on one screen (full rule paths, M0 steps only, reasoning goes into the ADRs), ADRs get a
  "Later" consequence, and scaffolds leave no empty section dividers. Three test cases in `evals/`.
- `architect`: only files under about 40 lines may skip dividers; the next milestone's steps come with the report, so
  one reply approves it. Two more test cases: a vague request, and an existing project with old ADRs and rules.
