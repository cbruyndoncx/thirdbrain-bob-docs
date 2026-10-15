---
description: Generate team status updates and standup summaries by pulling data from project management tools or analyzing meeting transcripts.
title: team-status-generator
---

# team-status-generator

Generate team status updates and standup summaries by pulling data from project management tools or analyzing meeting transcripts.

- **Area:** Foundational
- **Category:** productivity
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Product Manager, Operations Manager

Generate team status updates and standup summaries from project management tools (Linear, Jira, Asana) or meeting transcripts.

## How you ask

- “Generate a standup summary from our Linear board”
- “What did the team accomplish this sprint?”
- “Create a team status update from our Jira tickets”
- “Compile a progress report from this week's PM data”

## Inputs

- source (Team Status Generator) — Where team state comes from: tasknotes, tasks-plugin, card-board, linear, jira, asana, transcript, slack, or agent-logs
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set

## Outputs

- sprint-report (markdown)
- standup-summary (markdown)
- status (markdown)
- {company.meetings}/{YYYY-MM-DD}_standup-summary.md
- {company.reports}/sprint-{sprint-id}-report.md
- {company.reports}/status-{YYYY-MM-DD}.md

