---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ct-return-preparer — ThirdBrain BOB skill
  description: Prepare UAE Corporate Tax returns and period-end CT provisions. Adjusts accounting net income for CT add-backs and deductions, splits free zone qualifying vs no
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ct-return-preparer
catLabel: finance
area: finance
desc: Prepares corporate tax returns in EmaraTax, HMRC, ZATCA, FPS Finance, and Belastingdienst workflows.
summary: Prepare UAE Corporate Tax returns and period-end CT provisions. Adjusts accounting net income for CT add-backs and deductions, splits free zone qualifying vs non-qualifying income, applies the small business relief threshold, and computes net CT payable.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- tax_year — Financial year, e.g. 2025
- accounting_net_income — Net profit per signed financial statements (AED)
- entity_type — mainland | free-zone-qualifying | free-zone-non-qualifying
- jurisdiction — uae (default, company books only) | uk | india | ksa | belgium | netherlands. REQUIRED when books_root is overridden — the uae default must not carry over to a client root.
- income_statement — Signed income statement for the tax year — basis for accounting net income.
- ct_return — Draft CT return note to split into qualifying vs non-qualifying income.
- revenue_breakdown — Description of income sources and counterparties
- ct_return — Draft CT return to lint for common EmaraTax errors before filing.
outputs:
- ct-return (markdown)
- freezone-analysis (markdown)
- review-checklist (markdown)
- '{scope.finance.tax-ct}/CT-{YYYY}-freezone.md'
- '{scope.finance.tax-ct}/CT-{YYYY}-review.md'
- '{scope.finance.tax-ct}/CT-{YYYY}.md'
prompts:
- Corporate tax return
- CT provision
- Taxable income
---
