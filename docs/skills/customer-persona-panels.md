---
description: 'Run lightweight synthetic audience research inside the vault. This version is interactive first: the model does the persona generation and persona-by-persona response work directly in the current agent runtime. `uv` scripts are used only for deterministic helpers such as validation, analysis, and routing saved outputs.'
title: customer-persona-panels
---

# customer-persona-panels

Run lightweight synthetic audience research inside the vault. This version is interactive first: the model does the persona generation and persona-by-persona response work directly in the current agent runtime. `uv` scripts are used only for deterministic helpers such as validation, analysis, and routing saved outputs.

| | |
|---|---|
| **Area** | Research |
| **Category** | research |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [install] |
| **Roles** | [Head of Marketing] |

Builds synthetic customer persona panels and runs lightweight concept or message tests in the current agent environment.

## How you ask

- “Generate a client-scoped persona panel for this buying committee.”
- “Ask our saved panel what would stop them buying this offer.”
- “Concept-test these three messages and save the comparison report.”

## Inputs

- tone-of-voice — Brand voice used to render persona reactions.
- icp — Ideal customer profile — who the output targets.
- marketing_context — Positioning and messaging context.
- offerings — Offerings catalogue — what is being sold.
- request — Market, audience, or buying context to model.
- output_scope — Whether the panel is temporary, company-internal, or client-specific. (tmp | company | client)
- client_id — Required when output_scope is client.
- question — The exact research question for the panel.
- panel_dir — Existing panel folder containing manifest.json and persona JSON files.
- output_scope — Whether the study output is temporary, company-internal, or client-specific. (tmp | company | client)
- concepts — The concepts, messages, offers, or feature bundles to compare.
- panel_dir — Existing panel folder when reusing a panel.

## Outputs

- Folder containing manifest.json and persona files, or equivalent company/client path.
- Folder containing results.json, summary.json, results.csv, report.md, and optional charts.
- prefer a permanent directory)
- results (json)
- reusable-client-panel (json-bundle)
- scoped-study (mixed-report-bundle)
- {client.research}/persona-panels/{panel-id}/
- {company.marketing}/research/{study-id}/ or {client.research}/{study-id}/ or {client.projects}/{project}/

