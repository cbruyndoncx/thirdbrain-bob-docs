---
type: knowledge-base
title: "Howto — Run a Haiku Claude Agent via ACP in Obsidian"
status: final
created: 2026-04-26
modified: 2026-04-26
tags: [howto, acp, claude-agent, obsidian, haiku, userguide]
---

# Howto — Run a Haiku Claude Agent via ACP in Obsidian

Configure the locally-installed `claude-agent-acp` adapter to run as a separate Claude agent inside Obsidian's Agent Client plugin, pinned to Haiku, isolated from the default Claude Code instance.

This guide is self-contained — every command, env var, settings field, and config file you need is below.

## Why do this

- Cheap, fast model for low-stakes vault work (triage, formatting, lookups, quick rewrites)
- Runs alongside your default Sonnet/Opus instance without overriding global settings
- Isolated config dir means experimental tweaks (effort, permissions, allowed tools) don't bleed into your main agent

## Background — what the layers do

```
Obsidian Agent Client plugin (ACP client)
        │  spawns process, passes env vars + args
        ▼
claude-agent-acp (locally installed binary)
        │  thin ACP transport adapter; loads SDK
        ▼
Claude Agent SDK (same engine as Claude Code)
        │  reads CLAUDE_CONFIG_DIR/settings.json + env
        ▼
Anthropic API → Haiku 4.5
```

Key idea: the ACP adapter is **transport only**. Model selection, effort level, permissions, tool restrictions — all of that uses the **standard Claude Code env vars and settings.json**, exactly as if you were running Claude Code directly. No ACP-specific config language exists.

Precedence order (highest wins):

1. Environment variables (set in plugin env block)
2. `--model` CLI flag (if plugin allows passing args)
3. `model` field in settings.json (resolved via `CLAUDE_CONFIG_DIR`)
4. Account default

## Setup — 4 steps

### Step 1: Locate your `claude-agent-acp` binary

The path is whatever you installed. Common cases:

| Install method | Typical path |
|----------------|--------------|
| npm global | run `which claude-agent-acp` to find it (often `~/.npm-global/bin/claude-agent-acp` or `/usr/local/bin/claude-agent-acp`) |
| npm local in a project | `<project>/node_modules/.bin/claude-agent-acp` |
| Cloned from source | `node /path/to/claude-agent-acp/dist/index.js` |

Note this absolute path — you'll paste it into the Obsidian plugin in Step 3.

### Step 2: Create the isolated Haiku config dir

Run in WSL terminal:

```bash
mkdir -p /mnt/d/OBS/brncx-skills/99-TMP/claude-haiku-config
```

Then create `/mnt/d/OBS/brncx-skills/99-TMP/claude-haiku-config/settings.json` with this content:

```json
{
  "model": "haiku",
  "availableModels": ["haiku", "sonnet"],
  "effortLevel": "low",
  "env": {
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-4-5"
  }
}
```

What each field does:

| Field | Purpose |
|-------|---------|
| `model: "haiku"` | Active model when the session starts |
| `availableModels` | Restricts the `/model` picker. Drop `"sonnet"` for Haiku-only |
| `effortLevel: "low"` | Matches Haiku's fast/cheap intent (note: effort levels currently only affect Opus 4.7/4.6 and Sonnet 4.6 — harmless on Haiku) |
| `env.ANTHROPIC_DEFAULT_HAIKU_MODEL` | Pins the `haiku` alias to a specific model version so it doesn't drift on future Anthropic releases |

Optional fields you might add:

```json
{
  "permissions": {
    "allow": ["Read", "Glob", "Grep"],
    "deny": ["Bash"]
  },
  "statusLine": {
    "type": "command",
    "command": "echo '🟡 HAIKU AGENT'"
  }
}
```

### Step 3: Configure the Obsidian Agent Client plugin

Open Obsidian → **Settings → Community plugins → Agent Client → (your Claude agent entry, or add a new one)**.

| Field | Value |
|-------|-------|
| Name | `Claude Haiku` (or whatever you want shown in the picker) |
| Command / Path | the absolute path from Step 1 |
| Arguments | _(leave empty)_ |
| Working directory | usually your vault root: `/mnt/d/OBS/brncx-skills` |
| Environment variables | see env block below |

Env block — one `KEY=VALUE` per line:

```
CLAUDE_CONFIG_DIR=/mnt/d/OBS/brncx-skills/99-TMP/claude-haiku-config
ANTHROPIC_MODEL=haiku
```

Why both:
- `CLAUDE_CONFIG_DIR` — points the SDK at your isolated settings.json so this agent's tweaks don't leak into other Claude Code instances
- `ANTHROPIC_MODEL=haiku` — belt-and-braces; env wins over settings.json on precedence, so even if the config dir isn't picked up, Haiku is still active

### Step 4: Restart Obsidian and verify

Restart Obsidian (the plugin reads env at process spawn time). Open the Agent Client panel, start a session with the Haiku agent, and run:

| Command | What it confirms |
|---------|------------------|
| `/model` | Active model — should show Haiku |
| `/status` | Account info + which config file is loaded |

If the picker shows Sonnet/Opus instead of Haiku, the plugin isn't passing `CLAUDE_CONFIG_DIR` through. Two fallbacks:

**Fallback A — env-only.** Drop `CLAUDE_CONFIG_DIR` and rely on `ANTHROPIC_MODEL=haiku` alone. You lose the isolated settings.json, but the model pin works.

**Fallback B — wrap in a shell script.** If the plugin doesn't expose an env block at all, create `/mnt/d/OBS/brncx-skills/99-TMP/SCRIPTS/claude-agent-acp-haiku.sh`:

```bash
#!/usr/bin/env bash
export CLAUDE_CONFIG_DIR=/mnt/d/OBS/brncx-skills/99-TMP/claude-haiku-config
export ANTHROPIC_MODEL=haiku
exec /absolute/path/to/claude-agent-acp "$@"
```

Make it executable: `chmod +x /mnt/d/OBS/brncx-skills/99-TMP/SCRIPTS/claude-agent-acp-haiku.sh`

Point the plugin's Command field at the script instead of the binary.

## Run two agents side-by-side

Duplicate the agent entry in the Obsidian plugin. Same binary path, different env block:

| Agent | `CLAUDE_CONFIG_DIR` | `ANTHROPIC_MODEL` | Use for |
|-------|---------------------|-------------------|---------|
| Default Sonnet/Opus | _(unset — uses your normal config)_ | _(unset)_ | Real work |
| Haiku | `…/99-TMP/claude-haiku-config` | `haiku` | Quick tasks, triage, lookups |

Each runs as a separate ACP server process — fully isolated, no cross-contamination.

## Full env var reference

These are the env vars the Claude Agent SDK / Claude Code reads. Set any of them in the Obsidian plugin's env block:

| Variable | Effect |
|----------|--------|
| `ANTHROPIC_MODEL` | Active model alias or full ID (`haiku`, `sonnet`, `opus`, `claude-haiku-4-5`, `claude-opus-4-7[1m]`, etc.) |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | What the `haiku` alias resolves to |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | What the `sonnet` alias resolves to |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | What the `opus` alias resolves to |
| `CLAUDE_CONFIG_DIR` | Path to a folder containing settings.json (isolates from default config) |
| `CLAUDE_CODE_EFFORT_LEVEL` | `low` / `medium` / `high` / `xhigh` / `max` / `auto` (Opus 4.7/4.6, Sonnet 4.6 only) |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model used by spawned subagents |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT` | Set `1` to remove 1M context options from picker |
| `DISABLE_PROMPT_CACHING` | Set `1` to disable prompt caching globally |
| `DISABLE_PROMPT_CACHING_HAIKU` | Set `1` to disable prompt caching for Haiku only |
| `ANTHROPIC_BASE_URL` | Custom API endpoint (LLM gateway, Bedrock proxy, etc.) |
| `ANTHROPIC_CUSTOM_MODEL_OPTION` | Adds a custom entry to the `/model` picker |

Deprecated: `ANTHROPIC_SMALL_FAST_MODEL` — use `ANTHROPIC_DEFAULT_HAIKU_MODEL` instead.

## Full settings.json reference

Fields you can add to the settings.json under `CLAUDE_CONFIG_DIR`:

```json
{
  "model": "haiku",
  "availableModels": ["haiku", "sonnet"],
  "effortLevel": "low",
  "env": {
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-4-5"
  },
  "permissions": {
    "allow": ["Read", "Glob", "Grep", "Edit"],
    "deny": ["Bash(rm *)", "Bash(git push *)"]
  },
  "modelOverrides": {
    "claude-haiku-4-5": "your-custom-id-or-arn"
  },
  "statusLine": {
    "type": "command",
    "command": "/path/to/statusline-script.sh"
  }
}
```

| Field | Purpose |
|-------|---------|
| `model` | Initial model on session start |
| `availableModels` | Allowlist for the `/model` picker; merges across user/project/managed settings |
| `effortLevel` | Default reasoning effort |
| `env` | Extra env vars applied when this config is loaded |
| `permissions.allow` / `permissions.deny` | Tool allowlist / denylist (supports patterns like `Bash(git push *)`) |
| `modelOverrides` | Map Anthropic model IDs to provider-specific IDs (Bedrock ARNs, Vertex names) |
| `statusLine` | Custom status line shown above the prompt |

## Model alias quick reference

| Alias | Resolves to (Anthropic API) |
|-------|------------------------------|
| `haiku` | Claude Haiku 4.5 |
| `sonnet` | Claude Sonnet 4.6 |
| `opus` | Claude Opus 4.7 |
| `sonnet[1m]` | Sonnet 4.6 with 1M context |
| `opus[1m]` | Opus 4.7 with 1M context |
| `opusplan` | Opus in plan mode → Sonnet in execution |
| `default` | Resolves to your account's tier default |
| `best` | Currently equivalent to `opus` |

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `/model` shows Sonnet/Opus, not Haiku | Plugin not passing env. Use Fallback B (shell-script wrapper) |
| Picker is empty / picker shows wrong models | Check `availableModels` in settings.json — array might be too restrictive |
| Adapter fails to start | Run the binary path manually in a terminal — confirms it works outside Obsidian |
| Settings changes don't apply | Restart Obsidian — the ACP server only reads config at spawn time |
| Both agents share state | They shouldn't if `CLAUDE_CONFIG_DIR` is different — verify by running `/status` in each |
| Effort level setting ignored | Effort only affects Opus 4.7/4.6 and Sonnet 4.6 — Haiku doesn't support it |

## References

- Claude Code model configuration: https://code.claude.com/docs/en/model-config
- claude-agent-acp repo: https://github.com/agentclientprotocol/claude-agent-acp
- ACP protocol spec: https://agentclientprotocol.com
