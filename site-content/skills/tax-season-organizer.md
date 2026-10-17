---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: tax-season-organizer — ThirdBrain BOB skill
  description: One prompt to know exactly what's owed, to whom, by when — and produce the folder your accountant needs. Do the calculation, build the packet, never ask the own
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: tax-season-organizer
catLabel: finance
area: finance
desc: Computes quarterly estimated tax, tracks 1099-NEC contractor obligations, monitors VAT/sales-tax thresholds, and assembles a one-folder handoff packet for the accountant.
summary: One prompt to know exactly what's owed, to whom, by when — and produce the folder your accountant needs. Do the calculation, build the packet, never ask the owner to find the numbers themselves.
difficulty: intermediate
inputType: data
outputType: spreadsheet
requires: '[config]'
roles: '[Finance Manager]'
inputs:
- company-profile — Company profile — entity details used to frame the tax pack.
- jurisdiction — US, UAE, or UK/EU — read from the company profile (`company.profile`), ask once if missing
- period — Quarter being computed, e.g. Q2-2026 — inferred from today's date if not given
- entity_type — sole-prop / llc-sp / llc-c / s-corp / c-corp (US) or fze / fz-llc / mainland-llc (UAE)
- tax_year — Calendar year being reported
- period — YTD period to measure revenue against thresholds
- jurisdiction — Jurisdiction of the filing entity
- period — Fiscal year or period the packet covers
outputs:
- 1099-nec-tracker (markdown)
- handoff-packet (mixed)
- handoff-summary (markdown)
- quarterly-tax-summary (markdown)
- sales-tax-status (markdown)
- '{me.inbox}/tax-1099-nec-{YYYY-MM-DD}.md'
- '{me.inbox}/tax-quarterly-{YYYY-MM-DD}.md'
- '{me.inbox}/tax-sales-tax-{YYYY-MM-DD}.md'
- '{scope.finance.tax}/HANDOFF-{YYYY}-{period}/'
- '{scope.finance.tax}/HANDOFF-{YYYY}-{period}/00-summary.md'
prompts:
- What do I owe this quarter
- Do my taxes
- 1099 prep
---
