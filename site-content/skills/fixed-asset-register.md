---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: fixed-asset-register — ThirdBrain BOB skill
  description: 'Manage the complete IAS 16 fixed asset lifecycle: acquisition, monthly depreciation, impairment, and disposal. Every fixed asset generates monthly depreciation '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: fixed-asset-register
catLabel: finance
area: finance
desc: Manages the IAS 16 fixed asset register and posts monthly depreciation, impairment, and disposal entries.
summary: 'Manage the complete IAS 16 fixed asset lifecycle: acquisition, monthly depreciation, impairment, and disposal. Every fixed asset generates monthly depreciation journal entries that feed the GL and trial balance.'
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- asset_details — Asset name, category, cost, acquisition date, useful life, depreciation method
- po_ref — loaded from your vault context
- period_id — Accounting period, e.g. 2025-12
- asset — {books_root}/ASSETS/FIXED/{asset}.md
- recoverable_amount — Higher of fair value less costs to sell and value in use (AED)
- disposal_date — Disposal date used to derecognise a disposed asset and calculate the gain or loss on disposal
- disposal_proceeds — Cash received (AED). 0 for scrapped assets.
- asset — Asset used to show the full depreciation schedule to end of useful life
outputs:
- conversation
- depreciation-journal-entries (markdown)
- disposal-je (markdown)
- fixed-asset (markdown)
- impairment-je (markdown)
- schedule (markdown)
- updated-asset (markdown)
- '{scope.finance.assets-fixed}/FA-{NNN}-{asset_name}.md'
- '{scope.finance.assets-fixed}/{asset}.md'
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md'
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md (one per asset)'
prompts:
- Fixed asset
- Monthly depreciation
- Impairment write-down
---
