# Agent Kit

Skills and templates for AI coding agents (Claude Code, and other agents that read `SKILL.md` skills). Copy the ones
you want into your own setup.

## Skills

| Skill | What it does |
|---|---|
| [`architect`](skills/architect/SKILL.md) | Plans a project's architecture in three passes, gets your approval, records it as ADRs in `docs/adr/`, writes the agent rules (`.claude/rules/architecture/`) and links them from `AGENTS.md`, then builds or migrates the project one approved milestone at a time. Keeps files under 1200 lines and organized in sections. |

## Install

Copy a skill's folder into your personal skills folder to use it in every project:

```bash
cp -r skills/architect ~/.claude/skills/
```

On Windows (PowerShell):

```powershell
Copy-Item -Recurse skills/architect "$HOME/.claude/skills/"
```

To use it in one project only, copy it into that project's `.claude/skills/` instead.

## Use

Ask for it in plain words ("plan the architecture for…", "clean up this project's structure") or run it directly:

```
/architect a 2D roguelike in Godot
/architect restructure this repo
```

It writes nothing until you approve the plan, and asks again before each milestone.
