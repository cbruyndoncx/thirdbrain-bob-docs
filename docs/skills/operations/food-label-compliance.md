---
description: Extract all text with font metadata, measure x-heights, check allergen emphasis, validate nutrition declarations, and produce a scored compliance report with PDF output.
title: food-label-compliance
---

# food-label-compliance

Extract all text with font metadata, measure x-heights, check allergen emphasis, validate nutrition declarations, and produce a scored compliance report with PDF output.

- **Area:** Operations
- **Category:** compliance
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Validates food product label PDFs against country-specific labeling regulations.

## How you ask

- “Validate this food label PDF against EU regulations”
- “Check if the allergens are properly emphasised on this label”
- “Is the font size on this label large enough for EU compliance?”
- “Audit this label for the Dutch market”
- “Check nutrition table format against EU 1169/2011”

## Inputs

- label — Label artwork or text to check
- market — Country or region the label ships into
- label — Label to check
- domain — The single compliance domain to audit — mandatory, font, nutrition, allergen, date, quantity, or language (the `--domain` values of `validate_label.py`) — instead of running the full label check. (mandatory | font | nutrition | allergen | date | quantity | language)
- markets — Markets to check the same label against

## Outputs

- compliance-pdf (pdf)
- compliance-report (markdown)
- domain-compliance-pdf (pdf)
- domain-compliance-report (markdown)
- multi-country-pdf (pdf)
- multi-country-report (markdown)
- {client.deliverables}/food-label-compliance/label_compliance_{YYYY-MM-DD}.md
- {client.deliverables}/food-label-compliance/label_compliance_{YYYY-MM-DD}.pdf

