---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: bank-reconciliation — ThirdBrain BOB skill
  description: Reconcile GL cash balances to bank statements. Identifies timing differences (deposits in transit, unpresented cheques) and unrecorded items (bank charges, inte
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: bank-reconciliation
catLabel: finance
area: finance
desc: Reconciles GL cash account balances to bank statements by matching deposits, unpresented cheques, and unrecorded bank charges.
summary: Reconcile GL cash balances to bank statements. Identifies timing differences (deposits in transit, unpresented cheques) and unrecorded items (bank charges, interest). Required as part of period-end close before the trial balance is signed off.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- bank_account — Bank account master record with currency, GL code, and IBAN.
- period_id — Period id used to match GL cash account to bank statement and identify all reconciling items
- bank_statement_balance — Closing balance per bank statement, in the bank account's currency
- reconciliation — Draft reconciliation note awaiting approver sign-off.
- approver — Approver used to update status to approved once all differences are explained
outputs:
- approved-reconciliation (markdown)
- bank-reconciliation (markdown)
- '{scope.finance.bank}/BRECON-{YYYY}-{MM}-{account_id}.md'
prompts:
- Bank reconciliation
- Cash balance discrepancy
- Bank statement doesn't match
---
