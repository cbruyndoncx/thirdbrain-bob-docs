---
description: Reconcile GL cash balances to bank statements. Identifies timing differences (deposits in transit, unpresented cheques) and unrecorded items (bank charges, interest). Required as part of period-end close before the trial balance is signed off.
title: bank-reconciliation
---

# bank-reconciliation

Reconcile GL cash balances to bank statements. Identifies timing differences (deposits in transit, unpresented cheques) and unrecorded items (bank charges, interest). Required as part of period-end close before the trial balance is signed off.

- **Area:** Finance
- **Category:** finance
- **Level:** beginner
- **Input:** data
- **Output:** spreadsheet
- **Setup:** none
- **Roles:** Finance Manager

Reconciles GL cash account balances to bank statements by matching deposits, unpresented cheques, and unrecorded bank charges.

## How you ask

- “Bank reconciliation”
- “Cash balance discrepancy”
- “Bank statement doesn't match”

## Inputs

- bank_account — Bank account master record with currency, GL code, and IBAN.
- period_id — Period id used to match GL cash account to bank statement and identify all reconciling items
- bank_statement_balance — Closing balance per bank statement, in the bank account's currency
- reconciliation — Draft reconciliation note awaiting approver sign-off.
- approver — Approver used to update status to approved once all differences are explained

## Outputs

- approved-reconciliation (markdown)
- bank-reconciliation (markdown)
- {scope.finance.bank}/BRECON-{YYYY}-{MM}-{account_id}.md

