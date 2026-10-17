---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: catalog-reply — ThirdBrain BOB skill
  description: Match a natural-language product request against the JSON index produced by catalog-csv-ingest. Return the strongest match, price, currency, unit, and stock sta
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: catalog-reply
catLabel: sales
area: sales
desc: Answer product catalogue questions from an imported catalogue index with matched product, current price, currency, and optional stock.
summary: Match a natural-language product request against the JSON index produced by catalog-csv-ingest. Return the strongest match, price, currency, unit, and stock state with the source catalogue and import date.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[catalog-csv-ingest]'
roles: '[]'
inputs:
- query — Customer or operator product request
- catalogue_index — catalogue-index.json emitted by catalog-csv-ingest
outputs:
- Matched product, price, availability, source, and confidence
- prefer a permanent directory)
prompts: []
---
