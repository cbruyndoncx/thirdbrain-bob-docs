---
description: Develop a project schedule with CPM analysis and PERT estimates, delivered as an SVG Gantt chart plus a structured JSON schedule. Use when user mentions 'project schedule,' 'Gantt chart,' 'critical path,' 'PERT estimate,' or 'develop schedule.' This is the scheduling methodology.
title: project-schedule
---

# project-schedule

Develop a project schedule with CPM analysis and PERT estimates, delivered as an SVG Gantt chart plus a structured JSON schedule. Use when user mentions 'project schedule,' 'Gantt chart,' 'critical path,' 'PERT estimate,' or 'develop schedule.' This is the scheduling methodology.

| | |
|---|---|
| **Area** | Project Delivery |
| **Category** | project management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Develop a project schedule with CPM analysis and PERT estimates, delivered as an SVG Gantt chart plus a structured JSON schedule.

## How you ask

- “Create a project schedule with critical path analysis”
- “Generate PERT estimates for our project activities”
- “Build a Gantt chart for our product launch timeline”
- “Calculate the critical path for our delivery milestones”

## Inputs

- wbs — Work breakdown structure — the deliverable tree (from `project-wbs`)
- request — What to produce
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- profile — Company profile — delivery standards and project context.
- profile_client — Client profile — used instead of the company profile for client engagements.

## Outputs

- gantt-chart (svg)
- schedule (markdown)
- schedule-data (json)
- {project-folder}/activities.json
- {project-folder}/gantt.svg
- {project-folder}/schedule.md

