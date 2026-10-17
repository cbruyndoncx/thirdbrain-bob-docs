---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: currency-convert — ThirdBrain BOB skill
  description: Convert amounts between currencies using live exchange rates from the European Central Bank (via Frankfurter API).
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: currency-convert
catLabel: utilities
area: foundational
desc: Converts amounts between currencies using live ECB exchange rates via Frankfurter API.
summary: Convert amounts between currencies using live exchange rates from the European Central Bank (via Frankfurter API).
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- amount — Value to convert
- from_currency — Source currency code
- to_currency — Target currency code
- amounts — Values with their source currencies
- to_currency — Reporting currency to normalize to
- document — Document whose currency figures and stated rates are to be checked
outputs:
- conversation
- conversion-result (markdown)
- currency-table (markdown)
- validation-report (markdown)
prompts:
- Convert 1,500 EUR to USD at today's rate
- Create a multi-currency price table for EUR, USD, and GBP
- What's the current exchange rate for AUD to EUR?
- Convert our pricing to multiple currencies for the website
---
