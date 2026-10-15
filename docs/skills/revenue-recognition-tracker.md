---
description: Track IFRS 15 revenue recognition across client contracts. Set up performance obligations, monitor completion progress, recognise revenue as obligations are satisfied, and maintain contract asset and liability balances.
title: revenue-recognition-tracker
---

# revenue-recognition-tracker

Track IFRS 15 revenue recognition across client contracts. Set up performance obligations, monitor completion progress, recognise revenue as obligations are satisfied, and maintain contract asset and liability balances.

| | |
|---|---|
| **Area** | Finance |
| **Category** | finance |
| **Level** | beginner |
| **Input** | data |
| **Output** | spreadsheet |
| **Setup** | [none] |
| **Roles** | [Finance Manager] |

Implements IFRS 15 revenue recognition by setting up performance obligations for a contract, tracking completion progress, and managing contract assets and liabilities.

## How you ask

- “New client contract”
- “Revenue recognition progress”
- “Bill a client”

## Inputs

- deal — Won deal driving the revenue contract setup.
- obligations — List of distinct promises with standalone selling prices
- obligation — Performance obligation to advance and recognise revenue against.
- progress_percentage — 0-100 for over-time; use 100 for point-in-time on satisfaction
- obligation — Performance obligation to reconcile billed vs recognised on.
- invoice — Client invoice issued against the obligation.
- period_id — Period id used to report all active contracts — recognised vs billed, contract asset/liability balances

## Outputs

- conversation
- performance-obligations (markdown)
- revenue-je (markdown)
- revenue-review (markdown)
- updated-obligation (markdown)
- user-specified output path for updated obligation
- {client.deals}/PO-{deal_id}-{NNN}.md
- {scope.finance.journals}/JE-{YYYY}-{NNN}.md

