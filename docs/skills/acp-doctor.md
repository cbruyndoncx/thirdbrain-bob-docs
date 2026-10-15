---
description: The deep-dive counterpart to `bob-doctor`. Where `bob-doctor` answers "is this machine ready to run BOB at all?" (Layer 1, read-only), `acp-doctor` answers "why is the agent chat in Obsidian broken, and can it be fixed automatically?" — it validates the full chain from Node runtime through agent CLIs, the `acp-launch` launcher, login state, and the Agent Client plugin's configured paths, and (only when asked with `--fix`) repairs what is safe to repair.
title: acp-doctor
---

# acp-doctor

The deep-dive counterpart to `bob-doctor`. Where `bob-doctor` answers "is this machine ready to run BOB at all?" (Layer 1, read-only), `acp-doctor` answers "why is the agent chat in Obsidian broken, and can it be fixed automatically?" — it validates the full chain from Node runtime through agent CLIs, the `acp-launch` launcher, login state, and the Agent Client plugin's configured paths, and (only when asked with `--fix`) repairs what is safe to repair.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Diagnoses and repairs the Obsidian Agent Client / ACP agent stack — Node runtime, agent CLIs (claude, codex, agy for Antigravity, goose), the acp-launch auto-updating…

## How you ask

- “acp doctor — check my agents”
- “Claude Code stopped responding in Obsidian, can you diagnose it?”
- “Fix my acp setup and regenerate the launcher”
- “Run the agent handshake test and write a report”

## Inputs

- vault — Vault root (defaults to auto-detected root from CWD).

## Outputs

- diagnostic-note (markdown)
- launcher (bash)
- stdout (exit 0 = healthy, 1 = failures)
- stdout (per-agent handshake timing included)
- terminal-report (text)
- {me.inbox}/OPS-{date}-acp_doctor.md
- ~/bin/acp-launch (outside the vault)

