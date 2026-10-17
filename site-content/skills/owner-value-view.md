---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: owner-value-view — ThirdBrain BOB skill
  description: Give a business owner an honest, indicative answer to "what is my company worth — and what would move the number?" from figures they already have or can estimat
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: owner-value-view
catLabel: finance
area: finance
desc: Gives a business owner an indicative "what is my company worth, and what moves the number" valuation from their own figures.
summary: Give a business owner an honest, indicative answer to "what is my company worth — and what would move the number?" from figures they already have or can estimate in minutes. Output is a football-field range across five valuation methods plus a value-driver sensitivity table, so the owner sees both the number *and* the levers.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[CEO / Founder, Finance Manager]'
inputs:
- inputs_json — inputs.json per scripts/value_business.py --schema (revenue, normalized EBITDA/EBIT, net debt, sector multiple, etc.)
- client_id — If provided, the run uses the client's books and writes to the client's `{scope.finance.analysis}`; else the company's
- trial_balance — Signed-off TB or accounts-review Normalized Earnings Bridge; auto-fills normalized EBITDA/EBIT
- inputs_json — Inputs json used to emphasise the sensitivity table — which lever (margin, multiple, owner-dependency, growth) moves value most
outputs:
- driver_report (markdown)
- value_view (markdown)
- '{scope.finance.analysis}/owner_value_view_{YYYY-MM}.md'
- '{scope.finance.analysis}/value_drivers_{YYYY-MM}.md'
prompts:
- What's my business worth
- Value my company
- What would I sell for
---
