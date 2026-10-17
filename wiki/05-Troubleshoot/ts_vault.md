---
type: knowledge-base
title: "Troubleshooting — Vault & Obsidian"
status: final
created: 2026-04-28
modified: 2026-04-28
tags: [troubleshooting, vault, obsidian]
---

# Troubleshooting — Vault & Obsidian

## Vault folders missing (00-CORE, 10-ME, etc.)

You opened the wrong folder. Obsidian must be pointed at the **vault root** — the folder that contains `CLAUDE.md`.

1. **File → Open vault → Open folder as vault**
2. Navigate to the folder containing `CLAUDE.md`, `getting_started.md`, `00-CORE/`, etc.
3. Select that folder (not a subfolder inside it)

---

## "Trust author and enable plugins" prompt skipped

If you clicked "No" or dismissed the prompt, plugins are disabled:

1. **Settings → Community plugins**
2. Toggle **Enable community plugins** ON
3. Restart Obsidian if plugins still don't appear

---

## Dataview queries show no results

- Dataview plugin must be installed and enabled
- Queries depend on frontmatter `type:` fields — check the note has correct frontmatter
- Run BRAT's **Check for updates** if Dataview is missing

---

## Excalidraw / Canvas files won't open

- These require specific plugins (Excalidraw, JSON Canvas support)
- Run **Settings → BRAT → Check for updates** to install missing plugins
- Canvas is built into Obsidian 1.1+ — update if needed (**Help → Check for updates**)

---

## Obsidian opens a second window instead of the existing vault

The vault name in Advanced URI or CLI commands must match exactly (case-sensitive) what Obsidian has registered.

Check registered name: **Settings → About → Vault name**

---

## Related

- [[getting_started]] — Opening the vault for the first time
- [[ts_install]] — Plugin installation issues
- [[MOC-troubleshoot]] — All troubleshooting areas
