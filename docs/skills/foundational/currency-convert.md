---
description: Convert amounts between currencies using live exchange rates from the European Central Bank (via Frankfurter API).
title: currency-convert
---

# currency-convert

Convert amounts between currencies using live exchange rates from the European Central Bank (via Frankfurter API).

- **Area:** Foundational
- **Category:** utilities
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Finance Manager

Converts amounts between currencies using live ECB exchange rates via Frankfurter API.

## How you ask

- “Convert 1,500 EUR to USD at today's rate”
- “Create a multi-currency price table for EUR, USD, and GBP”
- “What's the current exchange rate for AUD to EUR?”
- “Convert our pricing to multiple currencies for the website”

## Inputs

- amount — Value to convert
- from_currency — Source currency code
- to_currency — Target currency code
- amounts — Values with their source currencies
- to_currency — Reporting currency to normalize to
- document — Document whose currency figures and stated rates are to be checked

## Outputs

- conversation
- conversion-result (markdown)
- currency-table (markdown)
- validation-report (markdown)

