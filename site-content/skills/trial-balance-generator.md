---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: trial-balance-generator — ThirdBrain BOB skill
  description: Aggregate all posted journal entries for an accounting period into a structured trial balance. The trial balance is the foundation for financial statement prepa
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: trial-balance-generator
catLabel: finance
area: finance
desc: Aggregates all posted journal entries for a period into a trial balance — opening balances, period movements, and closing balances per account.
summary: Aggregate all posted journal entries for an accounting period into a structured trial balance. The trial balance is the foundation for financial statement preparation — every financial statement line is derived from it.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- period-record — Accounting period record — defines the range the trial balance covers.
- period_id — Accounting period ID, e.g. 2025-12
- period — {books_root}/PERIODS/{period_id}.md
- journals_folder — {books_root}/JOURNALS/ — scanned for posted JEs
- current_period_id — Current period id used to side-by-side trial balance with current and prior period, variance column
- prior_period_id — Prior period id used to side-by-side trial balance with current and prior period, variance column
- period_id — Period id used to check that total debits equal total credits; flag imbalances and draft JEs
outputs:
- comparative-trial-balance (markdown)
- trial-balance (markdown)
- validation-report (markdown)
- '{scope.finance.reports}/TB-{current_period_id}-comparative.md'
- '{scope.finance.reports}/TB-{period_id}-validation.md'
- '{scope.finance.reports}/TB-{period_id}.md'
prompts:
- Prepare period-end management accounts
- Generate financial statements
- Validate GL integrity
---
