---
description: Designs AI-native product experiences, implements evals as product specs, and optimizes hybrid AI-plus-traditional architectures. Use when user mentions 'AI feature,' 'evals,' 'model improvements,' 'AI UX,' 'AI cost optimization,' or 'hybrid AI approach.' This is the AI product design methodology.
title: ai-product-patterns
---

# ai-product-patterns

Designs AI-native product experiences, implements evals as product specs, and optimizes hybrid AI-plus-traditional architectures. Use when user mentions 'AI feature,' 'evals,' 'model improvements,' 'AI UX,' 'AI cost optimization,' or 'hybrid AI approach.' This is the AI product design methodology.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Product Manager] |

Designs AI-native product experiences, implements evals as product specs, and optimizes hybrid AI-plus-traditional architectures.

## How you ask

- “Design an AI-native feature for our product”
- “Set up evals as product specs for our AI feature”
- “Optimize the cost of our hybrid AI architecture”
- “Improve the AI UX in our recommendation engine”

## Inputs

- request — The user problem the feature is meant to improve, plus the deterministic system, rule engine, or manual workflow that handles it today.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- quality-bar — Acceptable accuracy, latency, cost, and safety thresholds. Absent, the route proposes a bar and marks it as an assumption to confirm.
- request — The AI behaviour to be measured and the user outcome the evals are meant to protect.
- feature-spec — Spec from the `feature-design` route, read back so every eval case traces to a stated user outcome rather than to a model capability.
- quality-bar — Accuracy, latency, cost, and safety thresholds each eval case is scored against. Absent, the route derives a bar from the user outcome and flags it as unconfirmed.
- request — The architecture question — which work goes to a model, which stays deterministic, and what cost or portability pressure is forcing the decision.
- feature-spec — Spec from the `feature-design` route, read back so the architecture is judged against a fixed user outcome instead of being optimised in the abstract.
- quality-bar — Latency, cost-per-call, and safety limits the architecture has to hold. Absent, cost trade-offs are stated as ranges rather than decisions.

## Outputs

- Job to be done, the AI/non-AI split, fallback behaviour when the model is uncertain, quality bar, and the UX and rollout plan.
- Recommended hybrid boundary and pattern, model-routing and caching plan, cost estimate per 1000 calls, provider-portability position, and the monitoring to put in place.
- Runnable eval set — success, edge, and adversarial cases with inputs, expected outputs, and per-case quality bars — plus the pass condition that gates rollout.
- {scope.knowledge-base.product}/ai-product-patterns-architecture-{YYYY-MM-DD}.md
- {scope.knowledge-base.product}/ai-product-patterns-evals-{YYYY-MM-DD}.md
- {scope.knowledge-base.product}/ai-product-patterns-{YYYY-MM-DD}.md

