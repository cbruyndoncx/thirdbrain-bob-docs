---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: journal-entry-poster — ThirdBrain BOB skill
  description: Generate balanced double-entry journal entries from vault source documents and post them to the general ledger. Every financial transaction — invoice issued, in
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: journal-entry-poster
catLabel: finance
area: finance
desc: Posts balanced journal entries to the GL from client invoices, supplier invoices, and payments.
summary: Generate balanced double-entry journal entries from vault source documents and post them to the general ledger. Every financial transaction — invoice issued, invoice received, payment sent, payment received — needs a posted JE before it appears in the trial balance and financial statements.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- invoice — Client sales invoice driving the AR/Revenue JE.
- coa — Chart of accounts for account-code lookup.
- invoice — Client invoice being paid.
- payment_amount — Amount received (supports partial payments)
- payment_date — Date payment was received
- supplier-invoice — Approved supplier invoice driving the Expense/AP JE.
- expense-mapping — Skill-internal mapping of supplier categories to expense GL codes (references/expense_account_mapping.md).
- supplier-invoice — Supplier invoice being paid — closes AP, debits bank.
- description — Plain-language description of the transaction
- 'lines — Debit/credit lines: account code, amount, description per line'
- 'period — Period ID: e.g. 2025-12'
- entry_type — manual | accrual | prepayment | reversal | opening
outputs:
- journal-entry (markdown)
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md'
prompts:
- Post the journal entry
- AR revenue entry
- AP expense entry
---
