---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: resolution-tracker — ThirdBrain BOB skill
  description: Track issue resolution status across the full [issue lifecycle](references/issue_lifecycle.md), measure time-to-resolve against [SLA targets](references/sla_tar
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: resolution-tracker
catLabel: operations
area: operations
desc: Tracks issue resolution status, measures time-to-resolve, and identifies resolution trends.
summary: Track issue resolution status across the full [issue lifecycle](references/issue_lifecycle.md), measure time-to-resolve against [SLA targets](references/sla_targets.md), and surface patterns across resolved issues — all from vault markdown issue records, without an external ticketing system.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- issue_id — Issue ID to update (e.g. ISS-2026-04-05-login-failure)
- new_status — State to move the issue into — open, investigating, resolved, verified, or closed. 'verified' requires evidence the fix held; 'closed' ends tracking. (open | investigating | resolved | verified | closed)
- action_taken — What was done — used as the resolution log entry
- resolved_by — Name of the acting person for this status update; ask when missing. When moving to resolved, this is the person who applied the fix. For verification, identify the independent reviewer rather than substituting the resolver.
- scope — Client ID (e.g. acme) or 'all' for portfolio-wide report
- period — Date range for the report (e.g. 2026-Q1, last-30-days). Defaults to all-time open issues.
- issue-records — Existing issue notes — the population the report summarises.
- scope — Client ID or 'all' for portfolio-wide analysis
- period — Date range to analyse (e.g. last-90-days, 2026-Q1). Defaults to last 90 days.
outputs:
- issue-report (markdown)
- trend-report (markdown)
- updated-issue-note (markdown)
- '{client.issues}/{issue_id}.md'
- '{company.reports}/issue_report_{YYYY-MM-DD}.md'
- '{company.reports}/issue_trends_{YYYY-MM-DD}.md'
prompts:
- Open issues
- Resolution SLA
- Issue retrospective
---
