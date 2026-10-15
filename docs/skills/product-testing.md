---
description: 'Design product tests, run moderated user testing sessions, and produce clear go/no-go recommendations. Built for SME contexts: 5-user studies, no lab required, minimal overhead.'
title: product-testing
---

# product-testing

Design product tests, run moderated user testing sessions, and produce clear go/no-go recommendations. Built for SME contexts: 5-user studies, no lab required, minimal overhead.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Product Manager] |

Creates test plans, user testing scripts, feedback collection templates, and test result reports for product validation.

## How you ask

- “Product tests”
- “User testing sessions”
- “Structured feedback”

## Inputs

- client_product — Client product identity. Read when the request is client-scoped and the note exists.
- profile — Company or client profile — entity and relationship context.
- client-profile — Client profile — context for whose product is being tested.
- product-record — Product record — what is under test.
- product — Product, feature, or prototype to test
- stage — Product maturity the test plan targets — concept, prototype, beta, or pre-launch. Sets the method mix and what counts as a pass. (concept | prototype | beta | pre-launch)
- constraints — Timeline, participant availability, or budget constraints
- test-plan — Completed test plan (route-a output or equivalent)
- tasks — Specific tasks or scenarios to cover if not in the test plan
- session-notes — Raw notes or observation logs from user testing sessions
- test-plan — Original test plan with success criteria

## Outputs

- prefer a permanent directory)
- temporary-product-testing (markdown)
- test-plan (markdown)
- test-results-report (markdown)
- user-test-script (markdown)
- {product.root}/testing/test_plan_{YYYY-MM-DD}.md
- {product.root}/testing/test_results_{YYYY-MM-DD}.md
- {product.root}/testing/user_test_script_{YYYY-MM-DD}.md

