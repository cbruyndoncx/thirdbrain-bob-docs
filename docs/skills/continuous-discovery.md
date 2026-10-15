---
description: Run this skill when the user needs a repeatable discovery operating system, not a one-off interview summary.
title: continuous-discovery
---

# continuous-discovery

Run this skill when the user needs a repeatable discovery operating system, not a one-off interview summary.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Product Manager] |

Implements continuous discovery habits including weekly customer contact, opportunity solution trees, and assumption testing.

## How you ask

- “Set up a continuous discovery habit for our product team”
- “Create an opportunity solution tree for our onboarding problem”
- “Design an assumption test for our biggest product risk”
- “Plan weekly customer contact cadence for our product trio”

## Inputs

- request — The cadence question — setting up the weekly rhythm, or running this week's interview/synthesis/decision cycle.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The outcome and the opportunities or interview findings to map into a solution tree.
- request — The solution or assumption set to test, and any evidence already collected.

## Outputs

- Assumption test plan and results — assumptions ranked by risk, test method chosen, evidence collected, and the resulting build/test-more/pivot decision.
- Opportunity Solution Tree — outcome, ranked opportunities, candidate solutions, and the assumptions each solution depends on.
- Weekly operating plan — trio participation, interview schedule, synthesis session output, and the build/test-more/pivot call for the week.
- {scope.knowledge-base.product}/continuous-discovery-{YYYY-MM-DD}.md

