---
description: Authors the BOB Workspace plugin's `workspace.json` — the single file that composes the entire visible UI (dashboards, widgets, left-navigation, workbook groups, Base wiring, settings). This skill owns UI composition; its sibling bob-workspace-bootstrap owns the datamodel (YAML schema source → fileClasses → JSON Schemas) and writes no `workspace.json` at all — it defers all UI composition to this skill (and the plugin's native `Apply workspace template…` command for whole-template swaps).
title: bob-workspace-compose
---

# bob-workspace-compose

Authors the BOB Workspace plugin's `workspace.json` — the single file that composes the entire visible UI (dashboards, widgets, left-navigation, workbook groups, Base wiring, settings). This skill owns UI composition; its sibling bob-workspace-bootstrap owns the datamodel (YAML schema source → fileClasses → JSON Schemas) and writes no `workspace.json` at all — it defers all UI composition to this skill (and the plugin's native `Apply workspace template…` command for whole-template swaps).

| | |
|---|---|
| **Area** | Foundational |
| **Category** | obsidian |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Composes the BOB Workspace plugin UI by authoring its workspace.json — dashboards, widgets, navigation, workbook groups, Base wiring, and settings.

## How you ask

- “Add a dashboard to my workspace”
- “Add a widget to the CRM dashboard”
- “Set up my BOB Workspace UI from a template”

## Inputs

- vault_path — Absolute path to the user's vault root
- label — Human label shown in the switcher (prompt if omitted); also drives the file name workspace-<id>.json
- base — What to build from: an existing template file stem (workspace-minimal|crm|bob|cadence|emai.json — note the in-file `_template.id`s differ: minimal / crm-only / bob-workspace / cadence-classic / emai) to tailor, or 'datamodel' to build dashboards from the vault's entities. The bundled templates are NOT files: they are compiled into the plugin's `main.js` (from `src/bundled/templates.ts`) and seeded at load. `ls templates/*.json` finds only templates a user authored, so it is the wrong way to enumerate the bundled set and makes the bundled templates look deleted.
- element — What to add (dashboard / widget / nav-item / workbook-group / stat-card) and where
- target — JSON path of the element to change and the requested change

## Outputs

- console
- validation-report (text)
- workspace-config (json)
- workspace-template (json)
- {vault}/.obsidian/plugins/bob-workspace/templates/workspace-<id>.json
- {vault}/.obsidian/plugins/bob-workspace/workspace.json

