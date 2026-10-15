---
description: Assemble the IFRS Notes to the Financial Statements pack. Pulls from the signed-off trial balance and the four primary statements (SOFP, Income, Cash Flow, SOCE) to produce one `fs-notes` note covering all required disclosures.
title: fs-notes-generator
---

# fs-notes-generator

Assemble the IFRS Notes to the Financial Statements pack. Pulls from the signed-off trial balance and the four primary statements (SOFP, Income, Cash Flow, SOCE) to produce one `fs-notes` note covering all required disclosures.

- **Area:** Finance
- **Category:** finance
- **Level:** beginner
- **Input:** data
- **Output:** spreadsheet
- **Setup:** none
- **Roles:** Finance Manager

Assembles the IFRS Notes to the Financial Statements from a signed-off trial balance and the four primary statements.

## How you ask

- “Year-end statutory accounts”
- “Quarterly board pack disclosures”
- “IFRS-compliant full pack”

## Inputs

- trial_balance — {books_root}/REPORTS/TB-{period_id}.md — must be status: signed-off
- financial_statements — Wikilinks to all 4 financial-statement notes for the period (sofp, income, cash-flow, soce)
- period_id — Period id used to produce a single fs-notes note covering all required IFRS disclosures for the period
- prior_period_id — Prior period for comparatives (IAS 1 requirement)
- fs_notes — Fs notes used to validate the notes pack against the four statements before promotion to status:approved

## Outputs

- fs-notes (markdown)
- review-checklist (markdown)
- {scope.finance.reports}/notes-{period_id}-review.md
- {scope.finance.reports}/notes-{period_id}.md

