---
description: Install MCP servers into any AI coding CLI — single-server or bulk-install Anthropic's curated bundles.
title: mcp-add
---

# mcp-add

Install MCP servers into any AI coding CLI — single-server or bulk-install Anthropic's curated bundles.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [config] |
| **Roles** | [] |

Add MCP (Model Context Protocol) servers to AI coding clients — install individual servers or bulk-install Anthropic's official 21 curated bundles (63 unique servers…

## How you ask

- “Show me the available MCP bundles before installing anything.”
- “Dry-run the small-business MCP bundle for Codex.”
- “Install this single MCP server into Claude Code after showing me the command.”
- “Verify which servers from the sales bundle are registered.”

## Inputs

- bundle — Bundle name, e.g. anthropic-small-business
- client — Target AI coding CLI, e.g. 'claude code', codex, goose
- dry-run — Preview the install without writing config
- server — Server name and endpoint URL or stdio command
- client — Target AI coding CLI
- scope — global or project — project writes .mcp.json into the current working directory
- request — No arguments needed — lists the full catalog
- request — No arguments needed — lists the deduplicated server catalog
- bundle — Bundle name to inspect

## Outputs

- bundle-contents (console)
- bundle-list (console)
- cli-mcp-config (json)
- per-server lines plus a Installed/Skipped/Failed summary block
- per-server lines plus a Installed/Skipped/Failed summary block` — install-summary (console)
- server-catalog (console)
- stdout
- the target CLI's MCP config file (paths in references/cli-config-paths.md)

