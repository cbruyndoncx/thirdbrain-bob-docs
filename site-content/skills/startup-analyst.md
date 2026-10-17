---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: startup-analyst — ThirdBrain BOB skill
  description: Analyzes competitive landscapes, strategic positioning, and investment readiness for early-stage companies. Use when user needs a holistic startup assessment, c
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: startup-analyst
catLabel: product-management
area: strategy
desc: Analyzes competitive landscapes, strategic positioning, and investment readiness for early-stage companies.
summary: Analyzes competitive landscapes, strategic positioning, and investment readiness for early-stage companies. Use when user needs a holistic startup assessment, competitive analysis, or investor-readiness review, or mentions 'competitive landscape,' 'startup metrics,' 'pre-seed,' 'seed,' or 'Series A.' For dedicated TAM/SAM/SOM calculations, see market-sizing-analysis. For detailed financial models and projections, see startup-financial-modeling. This is the startup analysis methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Finance Manager]'
inputs:
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- startup-analyst (markdown)
- '{scope.knowledge-base.product}/startup-analyst-{YYYY-MM-DD}.md'
prompts:
- Assess our startup's investor readiness for a seed round
- Review our startup metrics against Series A benchmarks
- Map our competitive landscape and strategic positioning
- Evaluate our unit economics and runway
---
