# Code organization

These rules apply to every source file. In phase 2, pick the project's concrete version: the section order for its
language and one divider style. In phase 4, write that version into the project's `code-organization.md` rule.

## File size

| Lines in the file | What to do |
|---|---|
| up to 1000 | Fine. |
| 1001–1200 | Split it when a clear seam makes it easier to maintain. If you keep it whole, say why in your report. |
| over 1200 | Always split it. |

- Split along responsibilities (one system, feature or layer per file), never into arbitrary halves or a `utils2`.
  Update every import and caller in the same step.
- Generated code and pure data tables are exempt. The rule file names them.
- Before adding to a file that's already over 1000 lines, split it first or put the new code in its own file.

## One job per file

- Each file does one thing, and its name says what. Group files in folders by feature or module.
- Entry points (`main`, `index`, `init`) wire things together and hold no logic of their own.

## Section order

Order a file from what it needs, through what it holds, to what it does:

1. **Header:** 1–3 lines on what the file is for.
2. **Imports and dependencies.**
3. **Constants and config:** named values, never magic numbers in function bodies.
4. **Types:** classes, structs, enums, type aliases.
5. **State:** module-level variables, grouped and commented by purpose.
6. **Private helpers.**
7. **Public API:** what other files use.
8. **Setup and exports:** initialization, the entry point, the export or return.

Leave out the sections a file doesn't need. Where the language has its own idiomatic order, follow it and keep the
spirit (a Luau module returns its table last; Rust puts `#[cfg(test)] mod tests` at the bottom; Python ends with
`if __name__ == "__main__":`).

## Section dividers

- Mark each section with a short divider comment in one style for the whole project:

  ```
  -- ── Constants ─────────────────────────────
  # ── State ─────────────────────────────────
  // ── Public API ────────────────────────────
  ```

- Files under about 100 lines may skip dividers.
- Inside a long section, group related functions under a smaller sub-heading comment.

## Comments and naming

- Comment why, not what, in one short line. Give each public function a one-line doc comment.
- No commented-out code, no stray debug output.
- Variables live in the narrowest scope that works. Module state lives only in the State section.
- Names follow the language's conventions, and the same thing has the same name everywhere.

## Skeleton

Put a skeleton like this, in the project's language, in its `code-organization.md` rule:

```lua
-- Inventory: holds a player's items and enforces stack limits.

-- ── Dependencies ──────────────────────────
local Signal = require(script.Parent.Signal)

-- ── Constants ─────────────────────────────
local MAX_STACK = 99

-- ── State ─────────────────────────────────
local Inventory = {}
local itemsByPlayer = {}

-- ── Private helpers ───────────────────────
local function clampStack(count)
	return math.clamp(count, 0, MAX_STACK)
end

-- ── Public API ────────────────────────────
--- Adds `count` of `itemId` to the player's inventory.
function Inventory.add(player, itemId, count)
	-- ...
end

return Inventory
```
