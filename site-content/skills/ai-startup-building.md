---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-startup-building — ThirdBrain BOB skill
  description: Turn an AI startup idea into a concrete operating brief with explicit assumptions about AI fit, cost, latency, fallback behavior, and launch metrics.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-startup-building
catLabel: product-management
area: strategy
desc: Plans AI startup products with explicit AI-fit checks, MVP scope, model choice, cost budgets, fallback paths, and launch metrics.
summary: Turn an AI startup idea into a concrete operating brief with explicit assumptions about AI fit, cost, latency, fallback behavior, and launch metrics.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- ai-startup-building (markdown)
- '{scope.knowledge-base.product}/ai-startup-building-{YYYY-MM-DD}.md'
prompts:
- Plan an AI startup MVP with model choice and cost budget
- Scope a week-1 AI prototype with fallback paths
- Design an AI-native workflow for our startup product
- What AI model should we use and what will it cost?
---
