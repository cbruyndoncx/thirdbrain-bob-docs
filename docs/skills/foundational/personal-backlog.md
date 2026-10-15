---
description: Live triage view of TaskNotes backlog. Computes ROI (impact/effort) and staleness using Obsidian Bases formulas — no scheduled regeneration, the views update as you edit tasks.
title: personal-backlog
---

# personal-backlog

Live triage view of TaskNotes backlog. Computes ROI (impact/effort) and staleness using Obsidian Bases formulas — no scheduled regeneration, the views update as you edit tasks.

- **Area:** Foundational
- **Category:** productivity
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder

Triage your TaskNotes backlog by ROI (impact/effort), staleness, and cluster.

## How you ask

- “Quick wins”
- “Stale or forgotten tasks”
- “Backlog ROI”

## Inputs

- vault_root — Vault root; auto-detected from {vault.core}/ or .obsidian/ when omitted
- --dry — Print proposed changes without writing
- vault_root — Vault root containing `output.tasks`
- vault_root — Vault root containing the skill reference; auto-detected when omitted
- vault_root — Vault root containing the TaskNotes backlog
- --vault — Vault root (default: auto-detected from {vault.core}/ or .obsidian/)
- --open — Open the generated page in the default browser
- --tasks-dir — Folder of markdown task files (default: nearest `output.tasks`)
- --role — Which assignee role the batch selects tasks for; defaults to agent, the only role an unattended batch can work. (agent | external | owner)
- --tasks-dir — Folder of markdown task files
- --today — Date stamp for the sheet (passed in, not read from the clock, so runs are reproducible)
- --out — Write the sheet here instead of stdout
- sheet — The answered decision-sheet TaskNote

## Outputs

- backlog-base (base)
- backlog-browser (html)
- batch-selection (text)
- daily-focus-report (markdown)
- decision-sheet (markdown)
- propagation-gaps (text)
- reference-findings (text)
- references/scoring-rubric.md
- rubric (markdown)
- stdout (or JSON with --json)
- stdout (or JSON with --json); exit 1 when findings exist
- stdout, or --out
- stdout; exit 1 when gaps exist
- updated-tasknotes (markdown)
- {me.inbox}/OPS-{YYYY-MM-DD}-daily-focus.md
- {output.tasks}/*.md
- {vault.attachments}/backlog-browser/backlog_tree.html
- {vault.bases}/Personal-Backlog.base

