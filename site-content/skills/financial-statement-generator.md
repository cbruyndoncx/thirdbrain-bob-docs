---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: financial-statement-generator — ThirdBrain BOB skill
  description: Assemble IFRS-compliant financial statements from a signed-off trial balance. Produces all four primary statements with prior-period comparatives. Source of tru
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: financial-statement-generator
catLabel: finance
area: finance
desc: Assembles the four IFRS financial statements from a signed-off trial balance as markdown notes in the books.
summary: Assemble IFRS-compliant financial statements from a signed-off trial balance. Produces all four primary statements with prior-period comparatives. Source of truth for management accounts, board reporting, and statutory filing.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- 'trial_balance — {books_root}/REPORTS/TB-{period_id}.md — must be status: signed-off'
- prior_trial_balance — Prior period TB for comparatives
- trial_balance — Trial balance used to assemble revenue, expenses, and profit from the trial balance
- prior_trial_balance — Prior trial balance used to assemble revenue, expenses, and profit from the trial balance
- current_sofp — Current sofp used to build cash flow from net profit with non-cash add-backs and working capital movements
- prior_sofp — Prior period SOFP for working capital movement calculation
- income_statement — Income statement used to build cash flow from net profit with non-cash add-backs and working capital movements
- current_sofp — Current sofp used to show movements in equity from opening to closing balance
- prior_sofp — Prior sofp used to show movements in equity from opening to closing balance
- income_statement — Income statement used to show movements in equity from opening to closing balance
- trial_balance — Trial balance used to generate all four statements in one run
- prior_trial_balance — Prior trial balance used to generate all four statements in one run
outputs:
- cash-flow-statement (markdown)
- income-statement (markdown)
- soce (markdown)
- sofp (markdown)
- statements-pack (markdown)
- '{scope.finance.reports}/cash-flow-{period_id}.md'
- '{scope.finance.reports}/income-{period_id}.md'
- '{scope.finance.reports}/soce-{period_id}.md'
- '{scope.finance.reports}/sofp-{period_id}.md'
- '{scope.finance.reports}/{statement_type}-{period_id}.md (four files)'
prompts:
- Period-end financial statements
- Management accounts
- Statutory accounts pack
---
