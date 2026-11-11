# Boundaries

Reverse engineering for study, interoperability, preservation, modding and local play is widely practised; breaking
protections or harming a live service is not. These rules keep the project on the right side of that line. Copy the
rule text below into the project's `.claude/rules/boundaries.md` in M0.

When a request crosses one of these lines, say which one, don't do that part, and offer the route that gets the user
what they need without it (usually a local server or an offline copy).

## Rule text

```markdown
# Boundaries

- **Work on a copy.** The original lives in `_sdk/target/<version>/` and is never changed. A copy that needs a change
  (for example a server address pointed at 127.0.0.1) goes in `_sdk/patched/<version>/`, and every change is listed
  in `AGENTS.md`.
- **Reimplement, don't break in.** Study the files, the code and the behaviour. Never crack DRM or licence checks,
  bypass or disable anti-cheat, or defeat encryption that protects them. Encodings and ciphers the client and server
  use to talk to each other, and fixed file encodings, are formats: implementing them to interoperate is fine.
- **Local only.** Servers we write bind to 127.0.0.1 unless the user decides otherwise for their own network. Never
  connect our tools to the official servers, probe or scan them, impersonate them, or automate traffic against them.
  For protocol facts, use open-source servers and published logs.
- **Don't run protection or update code.** Don't start launchers or updaters that patch from the official servers, and
  don't load anti-cheat modules in a debugger.
- **Nothing proprietary in git.** The target's files, extracted assets, crawled pages and captures stay in `_sdk/`,
  `_data/` and `_external/`, which are git-ignored. Never force-add them, and never ship or share them. Our own data
  files (values, tables, placements, names, in our format) are committed; the target's art, sound and long texts
  are not.
- **Licences.** Code under permissive licences (MIT, BSD, Apache-2.0) may be ported with its copyright notice kept in
  the file. Code under copyleft licences (GPL, AGPL) is read for facts only unless this project uses the same
  licence. Leaked proprietary source code is never used.
- **Polite crawling.** Respect robots.txt and a site's terms, send at most about one request a second, make crawls
  resumable so nothing is fetched twice, and record each crawl in `docs/sources.md`. If a site forbids use for AI
  training, keep its pages for study only.
```

## Judgment calls

- **A debugger, tracer or memory viewer** on the local copy of a single-player game, or a client connected to our own
  local server: fine. On a client connected to official servers: no.
- **Patching the client** to reach `127.0.0.1`: fine, in `_sdk/patched/`. Patching out a licence check or anti-cheat:
  no.
- **Capturing traffic:** traffic between the original client and our own local server is fine. Capturing a session
  with the official service is the user's own call about their own account; never automate it, and prefer published
  logs.
- **Datamining** values from the target's files to rebuild its rules: fine. The raw dump stays in `_data/`; the
  values we use go into our own data files.
