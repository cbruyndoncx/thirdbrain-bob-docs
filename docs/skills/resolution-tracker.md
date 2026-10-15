---
description: Track issue resolution status across the full issue lifecycle, measure time-to-resolve against SLA targets, and surface patterns across resolved issues — all from vault markdown issue records, without an external ticketing system.
title: resolution-tracker
---

# resolution-tracker

Track issue resolution status across the full issue lifecycle, measure time-to-resolve against SLA targets, and surface patterns across resolved issues — all from vault markdown issue records, without an external ticketing system.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Tracks issue resolution status, measures time-to-resolve, and identifies resolution trends.

## How you ask

- “Open issues”
- “Resolution SLA”
- “Issue retrospective”

## Inputs

- issue_id — Issue ID to update (e.g. ISS-2026-04-05-login-failure)
- new_status — State to move the issue into — open, investigating, resolved, verified, or closed. 'verified' requires evidence the fix held; 'closed' ends tracking. (open | investigating | resolved | verified | closed)
- action_taken — What was done — used as the resolution log entry
- resolved_by — Name of the acting person for this status update; ask when missing. When moving to resolved, this is the person who applied the fix. For verification, identify the independent reviewer rather than substituting the resolver.
- scope — Client ID (e.g. acme) or 'all' for portfolio-wide report
- period — Date range for the report (e.g. 2026-Q1, last-30-days). Defaults to all-time open issues.
- issue-records — Existing issue notes — the population the report summarises.
- scope — Client ID or 'all' for portfolio-wide analysis
- period — Date range to analyse (e.g. last-90-days, 2026-Q1). Defaults to last 90 days.

## Outputs

- issue-report (markdown)
- trend-report (markdown)
- updated-issue-note (markdown)
- {client.issues}/{issue_id}.md
- {company.reports}/issue_report_{YYYY-MM-DD}.md
- {company.reports}/issue_trends_{YYYY-MM-DD}.md

