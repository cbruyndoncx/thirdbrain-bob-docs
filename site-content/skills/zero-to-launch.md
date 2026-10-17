---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: zero-to-launch — ThirdBrain BOB skill
  description: Use this skill to turn an idea into a tightly scoped prototype plan that can actually ship, not to brainstorm every possible feature.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: zero-to-launch
catLabel: product-management
area: strategy
desc: Turns ideas into prototype briefs, scopes week-1 MVPs, prioritizes requirements, maps full user flows, and creates launch-ready implementation plans.
summary: Use this skill to turn an idea into a tightly scoped prototype plan that can actually ship, not to brainstorm every possible feature.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- request — The idea, feature, or prototype to scope — problem, target user, and build horizon (week-1 MVP, prototype sprint, or broader concept plan).
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- The launch-ready prototype brief — Core Job, Success Criteria, Wedge, AI-First Assessment, Complete Experience, Week-1 MVP Scope, Deferred Scope, and Validation Plan.
- '{scope.knowledge-base.product}/zero-to-launch-{YYYY-MM-DD}.md'
prompts:
- Turn my idea into a prototype brief and MVP scope
- What should I build first for this product concept?
- Map the full user flow for my app idea
- Create a launch-ready implementation plan from this concept
---
