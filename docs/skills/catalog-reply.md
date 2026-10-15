---
description: Match a natural-language product request against the JSON index produced by catalog-csv-ingest. Return the strongest match, price, currency, unit, and stock state with the source catalogue and import date.
title: catalog-reply
---

# catalog-reply

Match a natural-language product request against the JSON index produced by catalog-csv-ingest. Return the strongest match, price, currency, unit, and stock state with the source catalogue and import date.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [catalog-csv-ingest] |
| **Roles** | [] |

Answer product catalogue questions from an imported catalogue index with matched product, current price, currency, and optional stock.

## Inputs

- query — Customer or operator product request
- catalogue_index — catalogue-index.json emitted by catalog-csv-ingest

## Outputs

- Matched product, price, availability, source, and confidence
- prefer a permanent directory)

