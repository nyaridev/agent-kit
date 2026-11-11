# ADR-0001: Study the whole game, in the standard reverse-engineering layout

Status: Accepted
Date: 2026-03-01

## Context
The user wants to run Skyrift locally and learn how it works.

## Decision
One repo; `_sdk/`, `_data/` and `_external/` git-ignored; `game/` shaped by the route chosen after recon.

## Options considered
Separate repos per part: more setup, nothing gained yet.

## Consequences
Later parts land in folders that already have a place.
