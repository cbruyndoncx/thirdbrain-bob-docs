---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: revenue-recognition-tracker — ThirdBrain BOB skill
  description: Track IFRS 15 revenue recognition across client contracts. Set up performance obligations, monitor completion progress, recognise revenue as obligations are sat
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: revenue-recognition-tracker
catLabel: finance
area: finance
desc: Implements IFRS 15 revenue recognition by setting up performance obligations for a contract, tracking completion progress, and managing contract assets and liabilities.
summary: Track IFRS 15 revenue recognition across client contracts. Set up performance obligations, monitor completion progress, recognise revenue as obligations are satisfied, and maintain contract asset and liability balances.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- deal — Won deal driving the revenue contract setup.
- obligations — List of distinct promises with standalone selling prices
- obligation — Performance obligation to advance and recognise revenue against.
- progress_percentage — 0-100 for over-time; use 100 for point-in-time on satisfaction
- obligation — Performance obligation to reconcile billed vs recognised on.
- invoice — Client invoice issued against the obligation.
- period_id — Period id used to report all active contracts — recognised vs billed, contract asset/liability balances
outputs:
- conversation
- performance-obligations (markdown)
- revenue-je (markdown)
- revenue-review (markdown)
- updated-obligation (markdown)
- user-specified output path for updated obligation
- '{client.deals}/PO-{deal_id}-{NNN}.md'
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md'
prompts:
- New client contract
- Revenue recognition progress
- Bill a client
---
