---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Earlier in this chat you set up my reverse-engineering project for Skyrift with the reverse-engineer skill (server
emulator route, Rust). M0 to M3 are done: the original client logs in to our local server and enters the world. The
project folder isn't mounted in this session, so plan only and write no files.

Next is M4: make sure every one of the client's 180 UI windows opens against our server without an error (the window
ids are in our data file, and the server can tell the client to open a window by id). The client takes about 12
seconds to start. Show me M4's steps and how you'll test it.
