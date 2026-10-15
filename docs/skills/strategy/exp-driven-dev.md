---
description: Product experimentation — designs feature flag rollouts, selects primary and guardrail metrics, and structures data-driven shipping decisions. Use when user mentions 'feature flag,' 'guardrail metrics,' 'experiment design,' or 'statistical significance.' For marketing A/B tests with sample sizes and variant copy, see ab-test-setup.
title: exp-driven-dev
---

# exp-driven-dev

Product experimentation — designs feature flag rollouts, selects primary and guardrail metrics, and structures data-driven shipping decisions. Use when user mentions 'feature flag,' 'guardrail metrics,' 'experiment design,' or 'statistical significance.' For marketing A/B tests with sample sizes and variant copy, see ab-test-setup.

- **Area:** Strategy
- **Category:** product management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Product Manager

Product experimentation — designs feature flag rollouts, selects primary and guardrail metrics, and structures data-driven shipping decisions.

## How you ask

- “Design an A/B experiment with feature flags”
- “Select primary and guardrail metrics for our test”
- “Set up an experiment to test our new onboarding flow”
- “What's the statistical significance of these results?”

## Inputs

- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- exp-driven-dev (markdown)
- {scope.knowledge-base.product}/exp-driven-dev-{YYYY-MM-DD}.md

