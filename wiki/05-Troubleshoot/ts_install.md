---
type: knowledge-base
title: "Troubleshooting — Installation"
status: final
created: 2026-04-28
modified: 2026-04-28
tags: [troubleshooting, installation, setup]
---

# Troubleshooting — Installation

## "claude: command not found"

```bash
source ~/.bashrc    # reload PATH (Linux/WSL)
source ~/.zshrc     # reload PATH (macOS)
```

If still missing, reinstall: `npm install -g @anthropic-ai/claude-code`

---

## "node: command not found" / npm missing

| OS | Fix |
|----|-----|
| macOS | `brew install node` |
| Linux / WSL | `sudo apt install nodejs npm` |
| Windows | Download from [nodejs.org](https://nodejs.org/) |

Minimum version: Node 18+, npm 9+. Check with `node --version`.

---

## Plugins not loading in Obsidian

1. When opening the vault, click **"Trust author and enable plugins"** — if you clicked "No", plugins are disabled globally
2. Go to **Settings → Community plugins** → toggle **Enable community plugins** ON
3. Plugins are not auto-installed — run BRAT's **"Check for updates"** (see Step 3 in [[getting_started]])

---

## uv / uvx not found

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
uv --version
```

---

## Related

- [[getting_started]] — Full installation guide
- [[ts_agent_client]] — Agent Client won't start
- [[ts_skills]] — Skills not loading after install
