---
description: Create a deliverable-oriented WBS that is concrete enough to estimate, assign, validate, and hand downstream to scheduling or risk work.
title: project-wbs
---

# project-wbs

Create a deliverable-oriented WBS that is concrete enough to estimate, assign, validate, and hand downstream to scheduling or risk work.

| | |
|---|---|
| **Area** | Project Delivery |
| **Category** | project management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Generates a deliverable-oriented Work Breakdown Structure with work-package dictionary fields, effort rollups, and optional canvas output.

## How you ask

- “Create a Work Breakdown Structure for our website redesign”
- “Decompose the project scope into deliverable-based packages”
- “Build a WBS with effort rollups for estimation”
- “Validate our WBS against the 100% rule”

## Inputs

- project_charter — Approved charter — scope, objectives, constraints (from `project-charter`)
- request — What to produce
- profile — Company profile — delivery standards and project context.
- profile_client — Client profile — used instead of the company profile for client engagements.

## Outputs

- project-wbs (markdown)
- wbs-canvas (canvas)
- {project-folder}/wbs.canvas
- {project-folder}/wbs.md

