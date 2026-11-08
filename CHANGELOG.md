# Changelog

## Unreleased

- `architect`: first version. Three-pass design, approval before any file is written, ADRs and overview in
  `docs/adr/`, path-scoped architecture rules linked from `AGENTS.md`, one approved milestone at a time, a size check
  you can opt into, file size limits (1000/1200 lines) and section order for code.
- `architect`: the plan fits on one screen (full rule paths, M0 steps only, reasoning goes into the ADRs), ADRs get a
  "Later" consequence, and scaffolds leave no empty section dividers. Three test cases in `evals/`.
