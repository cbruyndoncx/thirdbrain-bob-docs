---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: period-close-orchestrator — ThirdBrain BOB skill
  description: Sequence and track the full financial period close. Creates the checklist, calls sub-skills in order, tracks completion of each step, and gates the period trans
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: period-close-orchestrator
catLabel: finance
area: finance
desc: Sequences and tracks the full period-end close — creates the close checklist, calls sub-skills in order, gates the hard close on all items signed off, and manages the…
summary: Sequence and track the full financial period close. Creates the checklist, calls sub-skills in order, tracks completion of each step, and gates the period transition from `in-progress` → `soft-closed` → `hard-closed`. The single command that runs a complete month-end or year-end.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- period_id — e.g. 2025-12
- 'close_type — monthly | quarterly | annual (default: monthly)'
- period_close — {books_root}/CLOSE/CLOSE-{YYYY}-{MM}.md
- period_close — Period close used to show completed, pending, and blocked items with % complete
- period_close — Period close used to set period status to soft-closed — blocks new JE posting, allows statement preparation
- period_close — Period close used to permanently lock the period after statements are signed off
- approver — Approver used to permanently lock the period after statements are signed off
outputs:
- conversation
- period-close (markdown)
- status-report (markdown)
- updated-period-close (markdown)
- '{scope.finance.close}/CLOSE-{YYYY}-{MM}.md'
prompts:
- Start a monthly close
- Check close status
- Soft-close a period
---
