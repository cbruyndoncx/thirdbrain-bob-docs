---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: food-label-compliance — ThirdBrain BOB skill
  description: Extract all text with font metadata, measure x-heights, check allergen emphasis, validate nutrition declarations, and produce a scored compliance report with PD
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: food-label-compliance
catLabel: compliance
area: operations
desc: Validates food product label PDFs against country-specific labeling regulations.
summary: Extract all text with font metadata, measure x-heights, check allergen emphasis, validate nutrition declarations, and produce a scored compliance report with PDF output.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- label — Label artwork or text to check
- market — Country or region the label ships into
- label — Label to check
- domain — The single compliance domain to audit — mandatory, font, nutrition, allergen, date, quantity, or language (the `--domain` values of `validate_label.py`) — instead of running the full label check. (mandatory | font | nutrition | allergen | date | quantity | language)
- markets — Markets to check the same label against
outputs:
- compliance-pdf (pdf)
- compliance-report (markdown)
- domain-compliance-pdf (pdf)
- domain-compliance-report (markdown)
- multi-country-pdf (pdf)
- multi-country-report (markdown)
- '{client.deliverables}/food-label-compliance/label_compliance_{YYYY-MM-DD}.md'
- '{client.deliverables}/food-label-compliance/label_compliance_{YYYY-MM-DD}.pdf'
prompts:
- Validate this food label PDF against EU regulations
- Check if the allergens are properly emphasised on this label
- Is the font size on this label large enough for EU compliance?
- Audit this label for the Dutch market
- Check nutrition table format against EU 1169/2011
---
