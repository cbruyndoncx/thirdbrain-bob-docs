---
description: Defines explicit craft levels, recommends what to polish vs defer, and produces quality-versus-speed decision briefs with refactor trade-offs. Use when user asks about 'quality vs speed,' 'craft quality,' 'what to polish,' 'refactor or ship,' or 'details matter.' For binary go/no-go shipping decisions with reversibility analysis, see ship-decisions. This is the quality-speed methodology.
title: quality-speed
---

# quality-speed

Defines explicit craft levels, recommends what to polish vs defer, and produces quality-versus-speed decision briefs with refactor trade-offs. Use when user asks about 'quality vs speed,' 'craft quality,' 'what to polish,' 'refactor or ship,' or 'details matter.' For binary go/no-go shipping decisions with reversibility analysis, see ship-decisions. This is the quality-speed methodology.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Product Manager] |

Defines explicit craft levels, recommends what to polish vs defer, and produces quality-versus-speed decision briefs with refactor trade-offs.

## How you ask

- “Should we polish this feature or ship it now?”
- “Create a quality-vs-speed decision brief for this release”
- “Define explicit craft levels for our product areas”
- “Should we refactor this code or ship the feature first?”

## Inputs

- decision — What is shipping, and what quality is being traded for speed
- scope — Area under consideration for rework
- pain_evidence — Evidence the current state is costing something
- period — Period the retrospective covers
- incidents — Specific events to examine

## Outputs

- launch-decision (markdown)
- quality-retrospective (markdown)
- refactor-decision (markdown)
- source-client (markdown)
- {client.knowledge-base.product}/quality-speed-{YYYY-MM-DD}.md
- {company.knowledge-base.product}/quality-speed-{YYYY-MM-DD}.md

