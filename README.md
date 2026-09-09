# Alternating Agent Development

[中文说明](README.zh-CN.md)

A shared development continuity skill for **Codex and Claude Code**: work in small verifiable units, preserve decisions and authorization, and hand off safely when switching agents or running low on quota.

The repository carries project memory. Each agent is a replaceable executor.

## What it does

- Checks task scope before starting; decomposes oversized work into recoverable units.
- Uses lightweight checkpoints during normal work and a consolidated handoff when switching.
- Saves a minimum recovery note first when quota or interruption risk is raised.
- Validates the real working tree against the previous handoff before resuming.
- Preserves user changes, verification gaps, decisions and authorization boundaries.
- Reuses each project's existing documentation through a small project mapping.

It does not synchronize working copies, obtain more quota, monitor token usage, or guarantee recovery of information never saved. It is an instruction workflow, not an automatic orchestration service.

## Install

Download or clone this repository **outside agent skill discovery folders**. With Python 3.10+ installed, run from this directory:

```sh
python install.py --dry-run
python install.py --agent both
```

Use `--agent codex` or `--agent claude` for one tool. No third-party Python packages are required. A different existing adapter is protected; review it before using `--replace-adapter`, which backs it up. Released protocol files are never silently overwritten with different content.

The installer writes:

```text
~/.agents/skills/alternating-agent-development/SKILL.md       Codex entry
~/.claude/skills/alternating-agent-development/SKILL.md       Claude entry
~/.agents/protocols/alternating-agent-development/releases/  shared protocol
```

Each tool gets **one discoverable entry**. Do not copy the entire repository into a skills folder: nested templates and versioned SKILL.md files can be discovered as duplicate skills. Custom tool discovery paths require manual adapter placement. Open a new session after installation.

## Use

In the intended project directory, say:

| Intent | Prompt |
|---|---|
| Resume | Please take over development. |
| Normal handoff | Enter closeout / handoff mode. |
| Quota pressure | Quota is low. Enter closeout / handoff mode. |
| First adoption | Set up this project's continuity workflow using the shared skill. |

Explicit invocation: `$alternating-agent-development` in Codex or `/alternating-agent-development` in Claude Code. Natural-language activation depends on the tool; project entry files provide another route to the protocol.

The first adoption inventories existing documents, establishes a project mapping and pins a protocol version. Projects keep business rules and current work; they do not need their own copy of the general workflow. On another machine, install the pinned version before resuming. An existing project pin takes precedence over the personal default.

Both handoff modes freeze expansion. Quota pressure makes recovery-first ordering particularly important: save the interruption location and last actual checks before attempting optional closure. A handoff may legitimately be partial or unverified.

## Protocol

```text
DISCOVER -> VALIDATE -> NORMAL
oversized work -> DECOMPOSE -> NORMAL
switch / quota -> CLOSEOUT -> HANDOFF -> next agent VALIDATE
```

The [1.0.0 protocol](releases/1.0.0/alternating-agent-development/SKILL.md) is the authority. Adapters contain only tool-specific discovery and invocation details. Future agents can use the shared project entry or add a thin adapter; native installation has only been exercised with Codex and Claude Code.

## Validation and feedback

See [validation and limitations](VALIDATION.md). We welcome Issues and pull requests with reproducible handoff failures, confusing instructions, new-tool adapters and evidence of unnecessary context cost. Please sanitize logs and use small fixtures; never post credentials, private conversations or business data.

To run packaging checks:

```sh
python -m unittest discover -s tests -v
```

Keep adopted release semantics stable. Propose changed behavior as a new version with migration notes and scenario evidence. Existing project pins must not silently change.

## License

MIT. See [LICENSE](LICENSE).
