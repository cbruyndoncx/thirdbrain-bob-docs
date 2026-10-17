---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: exp-driven-dev — ThirdBrain BOB skill
  description: Product experimentation — designs feature flag rollouts, selects primary and guardrail metrics, and structures data-driven shipping decisions. Use when user men
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: exp-driven-dev
catLabel: product-management
area: strategy
desc: Product experimentation — designs feature flag rollouts, selects primary and guardrail metrics, and structures data-driven shipping decisions.
summary: Product experimentation — designs feature flag rollouts, selects primary and guardrail metrics, and structures data-driven shipping decisions. Use when user mentions 'feature flag,' 'guardrail metrics,' 'experiment design,' or 'statistical significance.' For marketing A/B tests with sample sizes and variant copy, see ab-test-setup.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Product Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- exp-driven-dev (markdown)
- '{scope.knowledge-base.product}/exp-driven-dev-{YYYY-MM-DD}.md'
prompts:
- Design an A/B experiment with feature flags
- Select primary and guardrail metrics for our test
- Set up an experiment to test our new onboarding flow
- What's the statistical significance of these results?
---
