---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: market-sizing-analysis — ThirdBrain BOB skill
  description: Calculates TAM, SAM, and SOM using top-down, bottom-up, and value theory methodologies. Use when the user needs 'market size numbers', 'TAM', 'SAM', 'SOM', 'mar
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: market-sizing-analysis
catLabel: product-management
area: strategy
desc: Calculates TAM, SAM, and SOM using top-down, bottom-up, and value theory methodologies.
summary: Calculates TAM, SAM, and SOM using top-down, bottom-up, and value theory methodologies. Use when the user needs 'market size numbers', 'TAM', 'SAM', 'SOM', 'market sizing', 'addressable market', or 'market-sizing methodology'. For broader startup competitive analysis, see startup-analyst. For financial projections and runway, see startup-financial-modeling.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Finance Manager]'
inputs:
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company or client profile — identity and stage.
- icp — ICP — target customer the strategy is for.
- offerings — Offerings catalogue — what is being strategised.
- marketing-context — Positioning, narrative, and competitive frame.
outputs:
- market-sizing-analysis (markdown)
- market-sizing-analysis-company (markdown)
- '{client.knowledge-base.product}/market-sizing-analysis-{YYYY-MM-DD}.md'
- '{company.knowledge-base.product}/market-sizing-analysis-{YYYY-MM-DD}.md'
prompts:
- Calculate the TAM, SAM, and SOM for our market opportunity
- Size the addressable market for our B2B SaaS product
- Run a bottom-up market sizing analysis for our niche
- How big is the market opportunity for this idea?
---
