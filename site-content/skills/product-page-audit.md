---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: product-page-audit — ThirdBrain BOB skill
  description: Audit B2B SaaS product pages through a product marketing lens. Use this skill for page-level evaluation, not for a full-site SEO audit or a general CRO sweep.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: product-page-audit
catLabel: marketing-content
area: marketing
desc: Audits B2B SaaS product, feature, and solution pages with a weighted product marketing rubric.
summary: Audit B2B SaaS product pages through a product marketing lens. Use this skill for page-level evaluation, not for a full-site SEO audit or a general CRO sweep.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- url — URL of the product, feature or solution page to audit; pasted copy or screenshots can stand in for a live page
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- product-page-audit (markdown)
- '{scope.marketing}/content/product-page-audit-{YYYY-MM-DD}.md'
prompts:
- Audit our product page for conversion and messaging
- Review our SaaS feature page against product marketing best practices
- Score our solution page for persona fit and CTA strategy
- Analyze our landing page for value proposition clarity
---
