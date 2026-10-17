---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: bob-workspace-compose — ThirdBrain BOB skill
  description: Authors the BOB Workspace plugin's `workspace.json` — the single file that composes the entire visible UI (dashboards, widgets, left-navigation, workbook groups
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: bob-workspace-compose
catLabel: obsidian
area: foundational
desc: Composes the BOB Workspace plugin UI by authoring its workspace.json — dashboards, widgets, navigation, workbook groups, Base wiring, and settings.
summary: Authors the BOB Workspace plugin's `workspace.json` — the single file that composes the entire visible UI (dashboards, widgets, left-navigation, workbook groups, Base wiring, settings). This skill owns UI composition; its sibling bob-workspace-bootstrap owns the datamodel (YAML schema source → fileClasses → JSON Schemas) and writes no `workspace.json` at all — it defers all UI composition to this skill (and the plugin's native `Apply workspace template…` command for whole-template swaps).
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- vault_path — Absolute path to the user's vault root
- label — Human label shown in the switcher (prompt if omitted); also drives the file name workspace-<id>.json
- 'base — What to build from: an existing template file stem (workspace-minimal|crm|bob|cadence|emai.json — note the in-file `_template.id`s differ: minimal / crm-only / bob-workspace / cadence-classic / emai) to tailor, or ''datamodel'' to build dashboards from the vault''s entities. The bundled templates are NOT files: they are compiled into the plugin''s `main.js` (from `src/bundled/templates.ts`) and seeded at load. `ls templates/*.json` finds only templates a user authored, so it is the wrong way to enumerate the bundled set and makes the bundled templates look deleted.'
- element — What to add (dashboard / widget / nav-item / workbook-group / stat-card) and where
- target — JSON path of the element to change and the requested change
outputs:
- console
- validation-report (text)
- workspace-config (json)
- workspace-template (json)
- '{vault}/.obsidian/plugins/bob-workspace/templates/workspace-<id>.json'
- '{vault}/.obsidian/plugins/bob-workspace/workspace.json'
prompts:
- Add a dashboard to my workspace
- Add a widget to the CRM dashboard
- Set up my BOB Workspace UI from a template
---
