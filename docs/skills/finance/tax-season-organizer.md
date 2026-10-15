---
description: One prompt to know exactly what's owed, to whom, by when — and produce the folder your accountant needs. Do the calculation, build the packet, never ask the owner to find the numbers themselves.
title: tax-season-organizer
---

# tax-season-organizer

One prompt to know exactly what's owed, to whom, by when — and produce the folder your accountant needs. Do the calculation, build the packet, never ask the owner to find the numbers themselves.

- **Area:** Finance
- **Category:** finance
- **Level:** intermediate
- **Input:** data
- **Output:** spreadsheet
- **Setup:** config
- **Roles:** Finance Manager

Computes quarterly estimated tax, tracks 1099-NEC contractor obligations, monitors VAT/sales-tax thresholds, and assembles a one-folder handoff packet for the accountant.

## How you ask

- “What do I owe this quarter”
- “Do my taxes”
- “1099 prep”

## Inputs

- company-profile — Company profile — entity details used to frame the tax pack.
- jurisdiction — US, UAE, or UK/EU — read from the company profile (`company.profile`), ask once if missing
- period — Quarter being computed, e.g. Q2-2026 — inferred from today's date if not given
- entity_type — sole-prop / llc-sp / llc-c / s-corp / c-corp (US) or fze / fz-llc / mainland-llc (UAE)
- tax_year — Calendar year being reported
- period — YTD period to measure revenue against thresholds
- jurisdiction — Jurisdiction of the filing entity
- period — Fiscal year or period the packet covers

## Outputs

- 1099-nec-tracker (markdown)
- handoff-packet (mixed)
- handoff-summary (markdown)
- quarterly-tax-summary (markdown)
- sales-tax-status (markdown)
- {me.inbox}/tax-1099-nec-{YYYY-MM-DD}.md
- {me.inbox}/tax-quarterly-{YYYY-MM-DD}.md
- {me.inbox}/tax-sales-tax-{YYYY-MM-DD}.md
- {scope.finance.tax}/HANDOFF-{YYYY}-{period}/
- {scope.finance.tax}/HANDOFF-{YYYY}-{period}/00-summary.md

