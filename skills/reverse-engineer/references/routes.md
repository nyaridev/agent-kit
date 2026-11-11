# Routes and recon

## Picking a route

Choose the route that gets something running and testable soonest. Each one leaves the project ready for the next.

| Target and goal | Route | Why it's fastest | Grows into |
|---|---|---|---|
| Online game (MMO, multiplayer), whole game or a server system | **Server emulator first:** a local server in `game/server-emu/` that the original client connects to. Rules and values come from open-source servers, wiki crawls and the client's own data | The original client becomes the test harness: every mechanic can be checked against the real game, without writing a client | Our own `server/` from the emulator's rules and data, then our own `client/` |
| Single-player game, whole game | **Data first:** an extractor for its archives and formats, then a viewer, then `game/client/` rebuilt one system at a time | Assets and formats unlock everything else; each system can be compared with the original side by side | A full rewrite, a port, mods |
| Any game, assets only | **Extractor:** a tool in `tools/` that unpacks the archives into `_data/extracted/`, with each format written up in `docs/findings/` | Results on the first run | Formats documented, then a viewer, then a client |
| Any target, one system (a format, the protocol, combat rules, a UI) | **Study and harness:** findings for that system, plus the smallest tool or test that proves them (a parser, a packet decoder, a formula with the game's own numbers) | No code beyond what proves the facts | The same system in an emulator or a rewrite |
| App, standalone | **Feature map, then rebuild:** list its features from the UI, its files and its settings, then rebuild in `app/` | The original stays the reference for every screen | A full replacement |
| App with a server | **Server emulator first,** as for an online game | Same as above | Our own server and client |

When the user's goal differs (a mod, a translation, a speedrun tool), pick the route whose first milestone produces
what they asked for and say which route it grows into.

Always prefer existing community work over starting from zero: an open-source server, extractor or format spec can
save weeks. Check licences first (`boundaries.md`).

## Recon (M1)

Answer each question in `docs/findings/overview.md`, with how you found out. Work on `_sdk/target/` only and note
every dead end in the journal.

1. **What is it built with?** The engine and language from file names and headers. Some signs:
   - Unity: `UnityPlayer.dll`, `*_Data/`, `Assembly-CSharp.dll` (Mono) or `GameAssembly.dll` (IL2CPP).
   - Unreal: `*.pak`, `*.utoc`, `*.ucas`, `Engine/` folders.
   - Godot: `*.pck`, or a `.pck` embedded in the executable.
   - .NET: assemblies with CLR headers; Java: `*.jar`; Electron: `resources/app.asar`; Flutter: `flutter_assets/`.
   - Native code: the compiler and any packer, from a tool like Detect It Easy; Delphi, C++ and others leave clear
     strings and runtime names.
2. **What protects it?** Packers, anti-cheat drivers or DLLs, DRM, encrypted archives, an online-only login. Note
   each one and how the route avoids it; never plan around breaking one (`boundaries.md`).
3. **What are its files?** Archives and formats by their magic bytes and extensions; which ones have public
   extractors or specs; a first test that unpacks one file.
4. **How does it talk?** For online targets: the server addresses in its config or binary, the ports, whether the
   protocol is text or binary, and what the community has documented. Read published packet logs and open-source
   servers; don't probe live servers.
5. **What exists already?** Open-source servers and reimplementations, extractors, format specs, wikis and data
   sites (`sources.md`). Clone the useful repos into `_external/`, note each one's licence and what it's good for.
6. **What tools does the route need?** The external programs for `_sdk/tools/` and the small tools and scripts we
   write in `tools/`. For each program, note its batch, headless or scripting mode: most jobs will run many times
   (`methods.md`).
7. **How will the work be tested fast?** Whether the target can walk many cases in one run: a debug console, a
   command line, a scripting hook, a way to open any screen or map directly. Later milestones build their checks
   on it.

Then write `docs/adr/0002-route.md` (Proposed): the route, the options considered with their costs, and the
milestones it leads to. Ask the user to choose:

- **The route,** with your pick first, for example: server emulation only; emulation and then our own server and
  client; assets only; one system.
- **The language** for new code, unless they named one. Recommend from the work: a compiled, memory-safe language
  such as Rust for servers, clients and extractors that must be fast; Python for crawlers, parsers and one-off
  scripts; the target's own language when porting code closely; whatever the user already knows when speed of
  learning matters more.

## The system map (end of M1)

Recon ends with the target cut into systems, in `docs/findings/overview.md` → Systems. The milestones come from this
table, so the work is uncovered one part at a time instead of all at once:

```markdown
## Systems

| System | What it does | Needs | Size | Findings | Milestone |
|---|---|---|---|---|---|
| Archives | packs every asset and table | nothing | 41 archives, 2 layouts | `file-formats.md` | M2 |
| Login | handshake, account, character list | protocol framing | 9 packets | `protocol.md` | M3 |
| UI windows | the client's windows and what opens them | login, world entry | 194 windows in 12 families | not studied | M7–M9 |
```

- A **system** is a part that can be understood and tested on its own: one protocol area, one file format, one rule
  set, one family of screens.
- **Needs** gives the order: a milestone builds only on systems that are already done.
- **Size** is a count (packets, tables, screens, functions). It tells you when a system needs more than one
  milestone.
- The map is a first cut. Every milestone corrects it in its last step: new systems found, sizes fixed, rows split.

## Milestones after recon

One system per milestone, in the order the map's Needs column gives, so each one can be tested when it's done. Each
test is the cheapest one that proves the milestone, and a test over many cases runs in one session of the client,
never one launch per case (`methods.md`).

Every system milestone has the same three parts, in order:

1. **Study:** write the system's findings file first: its parts, its data, what is known and from where, what is
   still a guess. No code for a system before its findings exist.
2. **Build:** the smallest version that works end to end with one or two cases, then the remaining cases.
3. **Check,** and update the map and the tracker.

**Split a milestone** when it needs more than about 8 steps, covers more than one row of the map, or won't finish in
one session. Cut along the system's own seams: first the mechanism with a few cases end to end, then the rest in
families ("M7: the window framework and the 10 simplest windows; M8: inventory and shop windows; M9: the rest").
Never "M5: all the UI".

A system gets a findings file, not an ADR. ADRs are for decisions that are hard to undo, whichever milestone they
come up in.

A sketch for the server-emulator route:

| Milestone | Goal | Tested by |
|---|---|---|
| M2 | The data: extract the client's tables, crawl the wiki values the client doesn't hold, convert both into `server-emu/data/` | the counts and spot checks against the wiki |
| M3 | Login and entering the world | the original client reaches the world on `127.0.0.1` |
| M4 | Moving and seeing others on one map | walking in the original client |
| M5+ | One system each: chat, items, combat, NPCs and shops, quests… | each one in the original client |

When the emulator covers what the user needs, the rewrite (`server/`, then `client/`) reuses its rules and data.
Move that shared code into `shared/` in the milestone that first needs it in two places.
