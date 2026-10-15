---
description: Keeps hook configurations equivalent and maintainable across Claude Code, OpenAI Codex CLI, the Antigravity CLI (`agy`), Google Gemini CLI, and Goose. Authors new hooks from a single description, migrates between platforms, audits parity, and validates config syntax.
title: hook-authoring
---

# hook-authoring

Keeps hook configurations equivalent and maintainable across Claude Code, OpenAI Codex CLI, the Antigravity CLI (`agy`), Google Gemini CLI, and Goose. Authors new hooks from a single description, migrates between platforms, audits parity, and validates config syntax.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Authors and maintains equivalent hook configs across Claude Code, Codex, Antigravity CLI, Gemini CLI, and Goose.

## How you ask

- “Add a hook”
- “Keep hooks in sync”
- “Migrate hooks to Codex”

## Inputs

- event — Hook event (PreToolUse, PostToolUse, SessionStart, Stop)
- matcher — Regex matcher for the tool name or command
- command — Shell command to execute
- platforms — Target platforms (default Claude Code, Codex and Antigravity; Gemini CLI and Goose on request)
- vault_root — Path to vault root (defaults to current directory)
- source_path — Path to the source config file
- target_platform — Target platform (claude-code, codex, antigravity, gemini-cli, goose)
- config_path — Path to the config file to validate. validate-hooks.sh accepts no path argument: run it from the project root for its fixed Claude, Codex and Antigravity paths. Validate other paths and Gemini CLI or Goose configurations manually against the platform reference.

## Outputs

- .claude/settings.json, .codex/hooks.json, .agents/hooks.json, .gemini/settings.json, .agents/plugins/*/hooks/hooks.json
- Config snippet for the target platform, with migration notes for unsupported features
- Hooks present on one platform but missing on others, with fix commands
- Syntax check results, schema compliance, and common error fixes
- conversation
- hook-configs (json/toml)
- user-specified output path for migrated config

