# 0001: Store todos in a JSON file

Status: Accepted
Date: 2025-03-02

## Context

One user, a few hundred todos at most.

## Decision

Keep todos in `todos.json` in the working directory.

## Consequences

No database to install; the file is easy to read and back up.
