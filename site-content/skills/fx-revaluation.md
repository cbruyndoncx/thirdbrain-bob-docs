---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: fx-revaluation — ThirdBrain BOB skill
  description: Retranslate all open foreign currency monetary items at the period-end closing rate per IAS 21. Posts a net FX gain/loss journal entry for the period. Keeps the
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: fx-revaluation
catLabel: finance
area: finance
desc: Applies IAS 21 period-end foreign currency revaluation to receivables, payables, and cash balances.
summary: Retranslate all open foreign currency monetary items at the period-end closing rate per IAS 21. Posts a net FX gain/loss journal entry for the period. Keeps the balance sheet accurate when the company transacts in currencies other than AED.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- period_id — Period id used to retranslate all open FX monetary items at closing rate and post the gain/loss JE
- fx_rates — Closing FX rate table for the period.
- period_id — Period id used to report realised and unrealised FX gains/losses for the period by currency
outputs:
- conversation
- fx-revaluation-je (markdown)
- fx-summary (markdown)
- revaluation-summary (markdown)
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md'
prompts:
- FX revaluation
- Month-end revaluation
- Year-end revaluation
---
