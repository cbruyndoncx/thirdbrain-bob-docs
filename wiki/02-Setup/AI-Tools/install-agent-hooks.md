---
type: knowledge-base
title: Install the frontmatter hooks for Claude Code, Codex and Antigravity
status: final
created: 2026-09-26
modified: 2026-09-26
tags: [setup, hooks, claude-code, codex, antigravity, vault-validator]
description: Per-machine install of the frontmatter-validation hook for the three coding agents, with the verification steps
---

# Install the frontmatter hooks

Every note an agent writes with its file tools is checked right after the write, and the
failures go back to the agent so it can fix the note in the same turn. The write itself is never
undone. Two checks run:

- **Schema** (`validate_frontmatter.py`): type and required fields, checked against the generated
  JSON Schema for the note's `type:`.
- **Data model guard** (`datamodel_guard.py --no-report`): links resolve, lifecycle rules, the
  note's location, and uniqueness of `client_id` and email. A hook run does not rewrite
  `datamodel-guard-latest.md`. Run the guard by hand, or on a schedule, when you want that
  report.

Hooks are **per machine**. They live in dot-folders (`.claude/`, `.codex/`, `.agents/`), which
Obsidian Sync does not sync, so every new laptop needs this page once. Scripts that write notes
themselves (`uv run …`) are not seen by any hook. They must self-validate, as
[[CONVENTIONS.md]] requires.

## What runs

One adapter serves all three agents:
`{skills.root}/vault-validator/scripts/agent_hook.py --agent <claude|codex|antigravity>`.
It takes the written Markdown paths from the agent's payload and runs both sibling checks on
them. It then returns any failure in the form that agent reads.

| Agent | Config file (vault root) | Event | Matcher | How a failure reaches the model |
|---|---|---|---|---|
| Claude Code | `.claude/settings.json` | `PostToolUse` | `Write\|Edit\|MultiEdit` | exit 2, message on stderr |
| Codex | `.codex/hooks.json` | `PostToolUse` | `apply_patch\|Edit\|Write` | `{"decision":"block","reason":…}` |
| Antigravity | `.agents/hooks.json` | `PreToolUse` + `PostInvocation` | `write_to_file\|replace_file_content\|multi_replace_file_content` | `injectSteps` ephemeral message |

Antigravity sends no file path to `PostToolUse`. The adapter therefore records the target at
`PreToolUse` and validates once the tool calls finish (`PostInvocation`). The pending list lives
in `$XDG_RUNTIME_DIR/vault-validator-agent-hook/`.

Agent shells do not expand key notation, so the config files carry **literal absolute paths**.
Below, `<vault>` is the vault root and `<skills>` is `<vault>/00-CORE/Agents/skills` on the
default layout. Use `resolve_context.py --key skills.root` to find the real path.

## Prerequisites

- `uv` on `PATH` in the shell the agent uses (`uv --version`).
- The vault schema tree exists: `<vault>/00-CORE/Schemas/json-schema/`. Without it the validator
  prints a `SKIP` line and passes. That is expected in an MCP-only workspace.

## Claude Code

Create or merge `<vault>/.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "uv run --quiet \"$CLAUDE_PROJECT_DIR/00-CORE/Agents/skills/vault-validator/scripts/agent_hook.py\" --agent claude --vault \"$CLAUDE_PROJECT_DIR\"",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

Restart Claude Code in the vault. Run `/hooks` and check that the `PostToolUse` entry is listed.

## Codex

1. The `hooks` feature must be on. `codex features list | grep hooks` should show `stable true`.
   Older builds need `[features] codex_hooks = true` in `~/.codex/config.toml`.
2. The vault must be a trusted project in `~/.codex/config.toml`
   (`[projects."<vault>"] trust_level = "trusted"`).
3. Create `<vault>/.codex/hooks.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "apply_patch|Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "uv run --quiet <skills>/vault-validator/scripts/agent_hook.py --agent codex --vault <vault>",
            "timeout": 60,
            "statusMessage": "Validating frontmatter"
          }
        ]
      }
    ]
  }
}
```

4. **Trust the hook.** Start `codex` in the vault, run `/hooks` and mark the new hook trusted.
   Codex skips new or changed hooks until they are trusted, and it records trust against the
   hook's hash. Editing the command means trusting it again.

## Antigravity CLI (`agy`)

The vault must be listed under `trustedWorkspaces` in `~/.gemini/antigravity-cli/settings.json`.
Then create `<vault>/.agents/hooks.json`:

```json
{
  "vault-frontmatter": {
    "PreToolUse": [
      {
        "matcher": "write_to_file|replace_file_content|multi_replace_file_content",
        "hooks": [
          {
            "type": "command",
            "command": "uv run --quiet <skills>/vault-validator/scripts/agent_hook.py --agent antigravity --event pre --vault <vault>",
            "timeout": 30
          }
        ]
      }
    ],
    "PostInvocation": [
      {
        "type": "command",
        "command": "uv run --quiet <skills>/vault-validator/scripts/agent_hook.py --agent antigravity --event postinv --vault <vault>",
        "timeout": 60
      }
    ]
  }
}
```

Run `/hooks` in `agy` and check that `vault-frontmatter` is listed. The `PreToolUse` handler
returns `{"decision": "ask"}`, which defers to the normal approval flow. It must not return `{}`:
agy 1.2.13 treats that as a hard deny and blocks every file write (found 2026-09-29).

## Verify

The adapter's own tests need no agent:

```bash
cd <skills>/vault-validator && uv run scripts/test_agent_hook.py
```

A live check per agent: ask it to create `00-CORE/TaskNotes/Tasks/zz-hook-probe.md` with the
frontmatter `type: task` and nothing else. A working hook reports `'status' is a required
property` back to the agent in the same turn. Delete the probe note afterwards. Do not probe in
`99-TMP/`, because the validator skips that folder.

A dry run of the Claude Code path, without an agent:

```bash
echo '{"tool_input":{"file_path":"<vault>/<some typed note>.md"}}' \
  | uv run --quiet <skills>/vault-validator/scripts/agent_hook.py --agent claude --vault <vault>; echo "exit=$?"
```

Exit 0 means pass (or skip). Exit 2 means the note failed, and the reason is on stderr.

## Troubleshooting

- **Nothing happens on write.** Check that the config file sits at the vault root the agent was
  started in. For Codex, check that the hook is trusted in `/hooks`. For Antigravity, check that
  the workspace is trusted.
- **Every write takes a few seconds.** Both checks start through `uv`. On this laptop (WSL,
  vault on DrvFs) a passing write measured 6.7 s on 2026-09-26. The first run is slower still,
  because it builds the environments. Keep `uv`'s cache on the Linux filesystem (the default
  `~/.cache/uv`).
- **`SKIP: … no generated JSON Schemas`.** This workspace has no schema tree, for example when
  skills are served over MCP. Validation is unavailable there by design.
- **Temporarily silence failures.** `SCHEMA_VALIDATION=warn` in the agent's environment prints
  violations without failing.

## Related

- [[vault-validator]] skill: the validator, the adapter, and the foreground
  `frontmatter_watcher.py` backstop for writes that no hook sees.
- [[hook-authoring]] skill: authoring and porting hooks between agents.
- [[FRONTMATTER-REQUIRED.md]]: required fields per `type:`.
