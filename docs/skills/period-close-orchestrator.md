---
description: Sequence and track the full financial period close. Creates the checklist, calls sub-skills in order, tracks completion of each step, and gates the period transition from `in-progress` → `soft-closed` → `hard-closed`. The single command that runs a complete month-end or year-end.
title: period-close-orchestrator
---

# period-close-orchestrator

Sequence and track the full financial period close. Creates the checklist, calls sub-skills in order, tracks completion of each step, and gates the period transition from `in-progress` → `soft-closed` → `hard-closed`. The single command that runs a complete month-end or year-end.

| | |
|---|---|
| **Area** | Finance |
| **Category** | finance |
| **Level** | beginner |
| **Input** | data |
| **Output** | spreadsheet |
| **Setup** | [none] |
| **Roles** | [Finance Manager] |

Sequences and tracks the full period-end close — creates the close checklist, calls sub-skills in order, gates the hard close on all items signed off, and manages the…

## How you ask

- “Start a monthly close”
- “Check close status”
- “Soft-close a period”

## Inputs

- period_id — e.g. 2025-12
- close_type — monthly | quarterly | annual (default: monthly)
- period_close — {books_root}/CLOSE/CLOSE-{YYYY}-{MM}.md
- period_close — Period close used to show completed, pending, and blocked items with % complete
- period_close — Period close used to set period status to soft-closed — blocks new JE posting, allows statement preparation
- period_close — Period close used to permanently lock the period after statements are signed off
- approver — Approver used to permanently lock the period after statements are signed off

## Outputs

- conversation
- period-close (markdown)
- status-report (markdown)
- updated-period-close (markdown)
- {scope.finance.close}/CLOSE-{YYYY}-{MM}.md

