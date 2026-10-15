---
description: Define a structured review rhythm for SME financial health. Works with simple data the owner already has — no dashboards, BI tools, or accountant required. Covers weekly pulse checks, monthly deep dives, and quarterly strategic reviews. Surfaces red flags with specific thresholds and produces ready-to-run meeting agendas.
title: financial-decision-cadence
---

# financial-decision-cadence

Define a structured review rhythm for SME financial health. Works with simple data the owner already has — no dashboards, BI tools, or accountant required. Covers weekly pulse checks, monthly deep dives, and quarterly strategic reviews. Surfaces red flags with specific thresholds and produces ready-to-run meeting agendas.

- **Area:** Finance
- **Category:** finance
- **Level:** beginner
- **Input:** data
- **Output:** spreadsheet
- **Setup:** none
- **Roles:** CEO / Founder, Finance Manager

Defines what financial metrics to review weekly, monthly, and quarterly, surfaces red flags and action triggers, and structures financial review meetings.

## How you ask

- “What should I be checking”
- “What are my warning signs”
- “Red flag metrics”

## Inputs

- company-profile — Company profile — sets the reporting entity for the review cadence.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- business-context — Brief description of the business if no profile file exists (revenue model, team size, cash position awareness)
- data — Current values for key metrics — cash balance, monthly burn/revenue, AR aging, largest client share, and gross margin. Can be pasted as plain text.
- review-type — Which cadence the agenda is for — weekly, monthly, or quarterly. Determines which metrics, red flags, and decision prompts the agenda pulls in. (weekly | monthly | quarterly)
- context — Any known issues or topics to include (e.g., "cash is tight", "Q2 close", "pricing review due")

## Outputs

- Decision cadence. Falls back to the scratch location (`output.scratch`) when no vault structure is present.
- agenda (markdown)
- red-flag-report (markdown)
- {scope.finance.analysis}/cadence.md
- {scope.finance.analysis}/review_{review-type}_{YYYY-MM-DD}.md
- {scope.finance.reports}/red_flag_check_{YYYY-MM-DD}.md

