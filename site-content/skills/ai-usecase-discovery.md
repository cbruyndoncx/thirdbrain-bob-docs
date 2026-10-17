---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-usecase-discovery — ThirdBrain BOB skill
  description: Discover, evaluate, and prioritize AI use cases for a target business domain. Produces a filtered shortlist and a BOB Integration Map showing which ThirdBrain B
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-usecase-discovery
catLabel: research
area: research
desc: Discovers and prioritizes AI use cases for a business domain or client vertical.
summary: Discover, evaluate, and prioritize AI use cases for a target business domain. Produces a filtered shortlist and a BOB Integration Map showing which ThirdBrain BOB skills cover each use case.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- request — Target domain and optional client context
outputs:
- ai-usecase-discovery-client (markdown)
- ai-usecase-discovery-resources (markdown)
- '{client.research}/ai-usecase-discovery-{domain}-{YYYY-MM-DD}.md'
- '{resource.research}/ai-usecase-discovery-{domain}-{YYYY-MM-DD}.md'
prompts:
- Discover AI use cases for a procurement and supply chain client in the UAE
- What AI opportunities exist for an HR consulting firm with 50 employees?
- Build a skill roadmap for field service management — what can BOB cover?
- Find AI use cases in logistics that we could offer a 3PL client
---
