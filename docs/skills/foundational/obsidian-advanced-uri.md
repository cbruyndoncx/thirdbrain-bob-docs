---
description: Use this skill for Advanced URI features that `obsidian-cli` does not cover.
title: obsidian-advanced-uri
---

# obsidian-advanced-uri

Use this skill for Advanced URI features that `obsidian-cli` does not cover.

- **Area:** Foundational
- **Category:** obsidian
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** 

Generates Obsidian Advanced URI commands for URI-only actions.

## How you ask

- “Open this canvas file in Obsidian”
- “Switch to my work workspace in Obsidian”
- “Run search and replace inside this note via URI”
- “Open the Obsidian settings page for community plugins”

## Inputs

- vault-name — Vault the URI targets, emitted as the `vault=` parameter rather than left to Obsidian's active-vault default.
- canvas-file — Vault-relative location of the `.canvas` file the command opens; URL-encoded into `filepath=`.
- canvas-target — Node id or viewport coordinates to bring into view once the canvas opens. Absent, the canvas opens at its saved view.
- environment — Shell the returned command has to survive. The choice changes the emitted wrapper and whether every `&` is escaped. (native | wsl)
- request — Which canvas the user wants open and what they need in view when it lands.
- vault-name — Vault whose settings pane is opened; a settings URI without it can land in the wrong vault.
- setting-id — Settings tab identifier passed as `settingid=` — a built-in tab name or a community plugin id.
- setting-section — Case-sensitive section name within the tab, when the user needs a specific block rather than the tab head.
- request — Which settings surface the user is trying to reach and why, so an unconfirmed tab id is not guessed.
- vault-name — Vault holding the file to be edited; a mutation URI must never rely on the active-vault default.
- filepath — Vault-relative location of the single file the replacement is applied to.
- search-text — Literal text to match, URL-encoded into `search=`. Its exactness decides whether the mutation hits or silently misses.
- replace-text — Replacement text written in place of every match, URL-encoded into `replace=`.
- request — The edit the user wants made, including whether the target file is currently open and unsaved.
- vault-name — Vault whose workspace or bookmark set is being switched.
- workspace-name — Name of the workspace or bookmark to activate, exactly as saved in Obsidian.
- target-kind — Which named object is being opened. The choice selects the URI parameter and changes what happens to the current layout. (workspace | bookmark)
- request — The layout or saved view the user wants to land in.
- vault-name — Vault whose plugin configuration is changed; plugin state is per-vault.
- plugin-id — Community plugin identifier to act on. Required for enable and disable; omitted when updating every plugin at once.
- plugin-action — What to do to the plugin. The choice decides which URI parameter is emitted and whether one plugin or all of them are touched. (enable | disable | update)
- request — The plugin state change the user is after, so an unconfirmed plugin id is not invented.
- vault-name — Vault the file write is directed at; a write URI must never rely on the active-vault default.
- filepath — Vault-relative location of the file to open or write.
- write-mode — How the URI treats an existing file. The choice is the difference between adding to a note and destroying its contents. (open | new | append | prepend | overwrite)
- content — Text written into the file, URL-encoded into `data=`. Absent, the command only opens the file.
- request — The edit the user wants and the reason `obsidian-cli` cannot do it, which this route has to state before falling back.

## Outputs

- The canvas-opening command with its one-line explanation of what appears on screen.
- The fallback write command, the reason the CLI was bypassed, and the verification step for the change.
- The plugin state-change command and the check that confirms the resulting state.
- The replacement command, the no-undo warning, and the verification command that confirms the change landed.
- The settings-navigation command and the tab or section it lands on.
- The workspace or bookmark command and the layout it activates.
- prefer a permanent directory)

