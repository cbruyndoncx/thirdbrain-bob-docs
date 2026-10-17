---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: strategic-sourcing — ThirdBrain BOB skill
  description: Guides purchasing optimization from spend visibility through supplier relationship management. For business owners, procurement managers, and operations leads w
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: strategic-sourcing
catLabel: operations
area: operations
desc: Sourcing strategy and supplier selection — spend analysis, Kraljic matrix, RFI/RFP/RFQ templates, TCO calculations, BATNA negotiation prep, and initial supplier…
summary: Guides purchasing optimization from spend visibility through supplier relationship management. For business owners, procurement managers, and operations leads who manage ongoing vendor relationships and purchasing categories.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- supplier_profiles — Supplier profiles scanned when sourcing or comparing vendors.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
outputs:
- strategic-sourcing (markdown)
- '{company.reports}/strategic-sourcing/strategic-sourcing-{descriptor}.md'
prompts:
- Run a spend analysis on our IT services category
- Classify our top 20 suppliers using the Kraljic matrix
- Generate an RFP for cloud hosting migration
- Calculate TCO for switching from Vendor A to Vendor B
- Prepare a negotiation brief for our logistics contract renewal
- Build a quarterly supplier scorecard for our three key vendors
- Review this SaaS contract against standard terms
- Create a full strategic sourcing plan for our marketing services spend
---
