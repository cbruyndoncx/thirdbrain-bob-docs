---
description: Aggregates milestones, risks, budget, resource signals, and PM artifacts to generate executive project status reports with derived RAG health. Use when the user mentions 'project status report,' 'status update,' 'project health,' 'executive summary,' 'RAG status,' or 'how is the project going.' This is the project status methodology.
title: project-status
---

# project-status

Aggregates milestones, risks, budget, resource signals, and PM artifacts to generate executive project status reports with derived RAG health. Use when the user mentions 'project status report,' 'status update,' 'project health,' 'executive summary,' 'RAG status,' or 'how is the project going.' This is the project status methodology.

| | |
|---|---|
| **Area** | Project Delivery |
| **Category** | project management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder] |

Aggregates milestones, risks, budget, resource signals, and PM artifacts to generate executive project status reports with derived RAG health.

## How you ask

- “Generate a project status report for the executive team”
- “What's the overall health of our project?”
- “Create a RAG status update with risks and milestones”
- “How is the project tracking against our baseline?”

## Inputs

- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- status-report-yyyy-mm-dd (markdown)
- {project-folder}/status_report_YYYY-MM-DD.md

