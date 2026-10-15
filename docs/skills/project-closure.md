---
description: Create a closure report that records final delivery status, performance, lessons learned, remaining handoffs, and formal sign-off.
title: project-closure
---

# project-closure

Create a closure report that records final delivery status, performance, lessons learned, remaining handoffs, and formal sign-off.

| | |
|---|---|
| **Area** | Project Delivery |
| **Category** | project management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Generates a project closure report with deliverable acceptance, lessons learned, performance summary, outstanding handoffs, and sign-off.

## How you ask

- “Generate a project closure report with lessons learned”
- “Create a deliverable acceptance and sign-off document”
- “Wrap up the project with a performance summary”
- “Document outstanding handoffs and post-mortem findings”

## Inputs

- project_charter — Approved charter — scope, objectives, constraints (from `project-charter`)
- wbs — Work breakdown structure — the deliverable tree (from `project-wbs`)
- schedule — Schedule — activities, durations, dependencies (from `project-schedule`)
- risk_register — Risk register — risks, scores, responses (from `project-risk`)
- request — What to produce
- profile — Company or client profile — delivery standards and project context.

## Outputs

- project-closure (markdown)
- project-closure-personal (markdown)
- {me.inbox}/project_closure.md
- {project-folder}/project_closure.md

