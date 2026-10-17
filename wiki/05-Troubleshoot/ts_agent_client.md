---
type: knowledge-base
title: "Troubleshooting — Agent Client"
status: final
created: 2026-04-28
modified: 2026-07-12
tags: [troubleshooting, agent-client, acp]
---

# Troubleshooting — Agent Client

> **Folder names below are the default (numbered) layout that BOB ships with.** A workspace
> with its own context pack names the folders differently — `uv run 00-CORE/Agents/skills/context-pack/scripts/resolve_context.py --key skills.root`
> prints the real path for the key named in each case.

## First stop: run the ACP doctor

Before debugging by hand, run the doctor — it checks the whole stack in one pass (Node/WSL runtime, agent CLIs, ACP adapters, login state, and whether the plugin's configured paths actually exist):

```bash
uv run 00-CORE/Agents/skills/acp-doctor/scripts/acp_doctor.py              # diagnose, with a fix hint per failure
uv run 00-CORE/Agents/skills/acp-doctor/scripts/acp_doctor.py --handshake  # also live-test each adapter (slower)
uv run 00-CORE/Agents/skills/acp-doctor/scripts/acp_doctor.py --fix        # repair what can safely be repaired
```

Run it inside WSL (Windows) or a normal terminal (macOS/Linux), from anywhere inside the vault. Exit 0 = healthy. Logins are the one thing it cannot fix for you — it prints the exact login command to run.

---

## Agent worked yesterday, broken today (updates / moved paths)

The most common cause: an agent CLI or adapter was updated or reinstalled, and the plugin still points at the old path. The doctor flags this as `command does not exist`.

**Durable fix:** switch every agent to the auto-updating launcher — command `~/bin/acp-launch` with the agent name as the argument (`claude`, `codex`, `gemini`, …) — so the configured path never changes again. See [[agent-client-installation]] section 3.

---

## Agent Client panel won't open

1. Verify the plugin is installed and enabled: **Settings → Community plugins → Agent Client**
2. Open via Command Palette (`Ctrl+P`) → type `Agent Client: Open`
3. If missing entirely, re-run BRAT: **Settings → BRAT → Check for updates**

Full setup guide: [[agent-client-installation]]

---

## "API key invalid" / 401 error

1. Copy `.env.example` → `.env` in the vault root
2. Add your API key: `ANTHROPIC_API_KEY=sk-ant-...`
3. Restart Obsidian

> CLI tools (Claude Code, Codex, Gemini CLI) use your subscription login — no `.env` key needed for the main provider.

---

## WSL mode not working (Windows)

1. **Settings → Agent Client** → enable **WSL Mode**
2. Use Linux-style paths for Node.js and agent executables (e.g. `/usr/local/bin/node`)
3. Verify Node is installed inside WSL: open WSL terminal → `node --version`

See [[agent-client-installation]] for full path configuration.

---

## BOB hangs or times out

| Cause | Fix |
|-------|-----|
| No internet | Check connection |
| Provider outage | Check provider's status page; try a different model in the panel's model selector |
| Wrong model selected | Switch to a smaller/faster model (e.g. Haiku) to test |
| Large vault scan | Give it 30–60 seconds on first run |

---

## Related

- [[agent-client-installation]] — Full ACP plugin setup
- [[ts_install]] — Node.js / CLI tool not found
- [[ts_skills]] — BOB can't find skills
