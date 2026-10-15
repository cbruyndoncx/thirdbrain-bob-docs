---
description: Audit B2B SaaS product pages through a product marketing lens. Use this skill for page-level evaluation, not for a full-site SEO audit or a general CRO sweep.
title: product-page-audit
---

# product-page-audit

Audit B2B SaaS product pages through a product marketing lens. Use this skill for page-level evaluation, not for a full-site SEO audit or a general CRO sweep.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing content |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Product Manager] |

Audits B2B SaaS product, feature, and solution pages with a weighted product marketing rubric.

## How you ask

- “Audit our product page for conversion and messaging”
- “Review our SaaS feature page against product marketing best practices”
- “Score our solution page for persona fit and CTA strategy”
- “Analyze our landing page for value proposition clarity”

## Inputs

- url — URL of the product, feature or solution page to audit; pasted copy or screenshots can stand in for a live page
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- product-page-audit (markdown)
- {scope.marketing}/content/product-page-audit-{YYYY-MM-DD}.md

