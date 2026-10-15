---
description: Writes canonical YAML schema source files to `{vault.schemas.source}/` based on what the vault already contains (templates + frontmatter census). The BOB Workspace plugin's settings UI then takes those YAML files and regenerates fileClasses, JSON Schemas, and DATAMODEL sections via its built-in `regenerateSchemaOutputs` pipeline. This skill is the upstream half — the plugin owns the downstream half.
title: bob-workspace-bootstrap
---

# bob-workspace-bootstrap

Writes canonical YAML schema source files to `{vault.schemas.source}/` based on what the vault already contains (templates + frontmatter census). The BOB Workspace plugin's settings UI then takes those YAML files and regenerates fileClasses, JSON Schemas, and DATAMODEL sections via its built-in `regenerateSchemaOutputs` pipeline. This skill is the upstream half — the plugin owns the downstream half.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | obsidian |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Bootstraps the BOB Workspace plugin datamodel by scanning vault templates and frontmatter and writing canonical YAML schema source files to {vault.schemas.source}/.

## How you ask

- “Bootstrap the minimum BOB Workspace schemas for this existing vault.”
- “Dry-run the schema proposal without writing any YAML.”
- “Extend the current setup only for uncovered entity types.”
- “Diagnose which vault entities are missing from the current workspace UI.”

## Inputs

- vault_path — Absolute path to the user's vault root
- templates_path — Path to existing templates folder; auto-detected if omitted
- vault_path — Absolute path to the user's vault root (minimum route must have run first)
- base_route — Which route's proposal to render (minimum | extend); defaults to minimum
- entities — Explicit list of entity slugs to generate Bases for; if omitted, generates for all YAML source files lacking a matching .base

## Outputs

- added-yaml-source (yaml)
- bases (base)
- diagnostic-report (markdown)
- merge-report (markdown)
- prefer a permanent directory)
- proposal-report (markdown)
- updated-yaml-source (yaml)
- yaml-source (yaml)
- {vault.bases}/
- {vault.schemas.source}/

