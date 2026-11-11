# Sources, tools and crawling

What to look for in recon, and where each thing goes. Record every one in the project's `docs/sources.md`, and give
each repo and tool its pinned line in `setup.bat` (`layout.md` → Setup), so another machine gets the same thing.

## `_external/`: other people's repos

Clone into `_external/<owner>/<repo>/`. Read them; never push to them. Kinds worth searching for:

| Kind | Why it helps | Examples of what to search for |
|---|---|---|
| Open-source server emulators | Packets, game rules, formulas, entity and spawn placements, database schemas | "<game> server emulator", "<game> private server source", community GitHub orgs |
| Reimplementations and engine remakes | How others rebuilt the client: rendering, formats, input | projects like OpenMW, OpenRA or OpenRCT2 for their games |
| Extractors and format specs | Archive layouts, model, texture and sound formats | "<game> extractor", "<format> spec", Kaitai Struct definitions, QuickBMS scripts |
| Protocol definitions and dissectors | Packet layouts, ciphers, handshakes | Wireshark dissectors, packet libraries, published packet logs |
| Data repositories | Item, monster, skill and map tables already parsed | community databases, datamine repos, wiki exports |
| Mod tools and SDKs | Loaders, editors, patching frameworks for the engine | the game's modding community, engine-wide mod loaders |
| Decompilation projects | Function names, structures and symbols someone already worked out | decomp projects, symbol and signature files for Ghidra or IDA |
| Engine-specific tools | Fast paths for the engine found in recon | Unity: AssetRipper, AssetStudio, Il2CppDumper; Unreal: FModel, UModel; Godot: GDRE Tools |
| Tools from the reverse-engineering community | Scripts and plugins for the target's language or packer | Ghidra scripts, IDA plugins, unpackers for a known packer |

Check each licence before using code from it (`boundaries.md`), and never use leaked proprietary source.

## `_data/crawled/`: sites

Crawl what holds values and descriptions the client doesn't: exact numbers, drop tables, formulas, quest text, how
mechanics behave.

| Kind | Holds |
|---|---|
| Wikis (fan wikis, Fandom, official wikis) | Mechanics, items, monsters, quests, maps, with values |
| Fan databases and calculators | Exact tables and formulas, often taken from the client |
| Official guides and manuals, archived versions | How systems are meant to work, UI and controls |
| Patch notes and changelogs | What changed when, so values match the version being studied |
| Forums and Q&A threads | Edge cases and tested behaviour |
| Web archives (the Wayback Machine) | Pages and sites that are gone |

How to crawl:

- One script per site in `tools/scripts/crawl_<site>.py` and a launcher `crawl_<site>.bat`.
- Check robots.txt and the terms first; send about one request a second; make the crawl resumable.
- Save the raw pages in `_data/crawled/<site>/raw/` and what you parse from them (CSV or JSON) beside them, with a
  crawl log.
- Convert what the project needs into its data files (`game/<part>/data/`, `layout.md` → Data) and write how
  systems work into `docs/findings/`, with the page URL and crawl date as the source. After that the crawl is only
  needed again to refresh it.
- Its launcher runs only when asked, and `setup.bat crawl` runs every crawl launcher.

## `_sdk/tools/`: third-party programs

Download into `_sdk/tools/<tool>/`, note the version and where it came from. Pick by what recon found:

| Need | Tools |
|---|---|
| Identify the compiler, packer, engine | Detect It Easy, a hex editor with templates (ImHex, 010 Editor) |
| Decompile native code | Ghidra, IDA Free, Binary Ninja, radare2 / Cutter |
| Decompile managed code | dnSpyEx or ILSpy (.NET), JADX or a Java decompiler, asar extraction (Electron) |
| Debug and trace locally | x64dbg, WinDbg, gdb or lldb; Process Monitor for file and registry access |
| Graphics | RenderDoc, apitrace, PIX: draw calls, textures, shaders |
| Network | Wireshark, for traffic between the client and our own local server |
| Instrumentation | Frida, for hooking functions in the local copy |
| Archives and assets | QuickBMS, the engine-specific tools above, Blender for models |

- This table is a starting point. Tools for an engine or format change often: when you have internet, search for what
  its community uses now before picking one.
- For anything done more than a few times, use the tool's scripted mode instead of its window: Ghidra's
  `analyzeHeadless` and scripts, IDA's batch mode, x64dbg and Frida scripts, `tshark` for Wireshark, RenderDoc's
  Python API, Blender with `--background --python`.
- Keep each tool's project or database in `_sdk/tools/<tool>/`, so an analysis runs once and later sessions reopen
  it (`methods.md`).

## `tools/`: our own tools

Write a tool when no existing one does the job, or when the job will run many times:

- `tools/<name>/` for anything bigger than one file: an archive extractor, a packet logger or proxy for our local
  server, a converter from extracted data into our own formats, a map or model viewer.
- `tools/scripts/` for one-file scripts: crawlers, parsers, a check that compares our values with the wiki's.
- Each tool reads from `_sdk/` or `_data/` and writes raw output to `_data/` or converted data files to the code
  folder's `data/`, through relative paths or an environment variable.
- Each tool that the user runs gets a launcher in the root and a row in `AGENTS.md`.
