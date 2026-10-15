---
description: Manage the full lifecycle of external audit findings — from fieldwork adjustments through management responses to the signed audit opinion. Ensures every finding is documented, responded to, and resolved before the opinion is issued.
title: audit-findings-tracker
---

# audit-findings-tracker

Manage the full lifecycle of external audit findings — from fieldwork adjustments through management responses to the signed audit opinion. Ensures every finding is documented, responded to, and resolved before the opinion is issued.

- **Area:** Finance
- **Category:** finance
- **Level:** beginner
- **Input:** data
- **Output:** spreadsheet
- **Setup:** none
- **Roles:** Finance Manager

Tracks audit adjustments, management letter points, and audit opinion status across an external audit engagement.

## How you ask

- “Proposed audit adjustment”
- “Management letter point”
- “Open findings”

## Inputs

- engagement — Active audit engagement record — finding is logged against it.
- finding_details — Description, account affected, proposed debit/credit, risk level
- engagement — Active audit engagement record.
- opinion_type — unmodified | qualified | adverse | disclaimer
- signed_date — Signed date used to record the final opinion type and sign-off date

## Outputs

- closed-engagement (markdown)
- conversation
- dashboard (markdown)
- management-letter (markdown)
- updated-engagement (markdown)
- {scope.finance.audit}/AUD-{YYYY}-management-letter.md
- {scope.finance.audit}/AUD-{YYYY}.md

