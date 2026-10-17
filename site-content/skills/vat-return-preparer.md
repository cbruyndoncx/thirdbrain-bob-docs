---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: vat-return-preparer — ThirdBrain BOB skill
  description: Prepare UAE VAT returns by aggregating output VAT on sales and input VAT on purchases, reconciling to GL balances, and flagging errors before FTA filing. Covers
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: vat-return-preparer
catLabel: finance
area: finance
desc: Multi-jurisdiction VAT and indirect tax return preparation — aggregates output and input tax, reconciles GL accounts, and produces jurisdiction-specific return entities.
summary: Prepare UAE VAT returns by aggregating output VAT on sales and input VAT on purchases, reconciling to GL balances, and flagging errors before FTA filing. Covers FTA Form 201 — the standard UAE VAT return for quarterly filers.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- period_id — VAT period, e.g. 2025-Q4 (Oct–Dec 2025)
- trn — FTA Tax Registration Number
- jurisdiction — uae (default, company books only) | uk | india | ksa | belgium | netherlands. REQUIRED when books_root is overridden — the uae default must not carry over to a client root.
- invoices_folder — Client sales invoices for the period — source of output VAT.
- supplier_invoices_folder — Supplier invoices for the period — source of input VAT.
- vat_return — Draft VAT return note to reconcile against the GL.
- trial_balance — Period trial balance — provides VAT control account balances.
- vat_return — Draft VAT return to lint for common FTA errors before filing.
outputs:
- reconciliation-note (markdown)
- review-checklist (markdown)
- vat-return (markdown)
- '{scope.finance.tax-vat}/VAT-{YYYY}-Q{N}-recon.md'
- '{scope.finance.tax-vat}/VAT-{YYYY}-Q{N}-review.md'
- '{scope.finance.tax-vat}/VAT-{YYYY}-Q{N}.md'
prompts:
- Prepare a VAT return
- Reconcile tax accounts
- Review filing readiness
---
