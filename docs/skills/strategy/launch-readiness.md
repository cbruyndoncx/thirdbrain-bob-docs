---
description: 'Produce an objective, decision-quality assessment of whether a product is ready to launch. This skill covers three complementary angles: a structured go/no-go checklist across all functions, a dependency tracker with owners and live status, and a rollback plan that pre-answers "what do we do if this goes wrong." Together they remove the guesswork from launch day decisions.'
title: launch-readiness
---

# launch-readiness

Produce an objective, decision-quality assessment of whether a product is ready to launch. This skill covers three complementary angles: a structured go/no-go checklist across all functions, a dependency tracker with owners and live status, and a rollback plan that pre-answers "what do we do if this goes wrong." Together they remove the guesswork from launch day decisions.

- **Area:** Strategy
- **Category:** product management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Product Manager

Assesses launch readiness with go/no-go checklists, dependency tracking, risk assessment, and rollback plans.

## How you ask

- “Run a go/no-go check for the ThirdBrain starter tier launch”
- “Are we ready to launch? Walk me through the checklist”
- “Map all our launch dependencies and flag what's blocking”
- “Create a rollback plan for next week's release”
- “What do we do if the launch goes wrong?”
- “Prepare a launch readiness pack for the client review”

## Inputs

- request — What to produce
- product-context — Product definition, feature scope, target market.
- launch-scope — Type of launch: full GA, limited beta, feature release, market expansion, etc.
- product-context — Product and workstream context.
- team-context — Teams or owners involved (engineering, marketing, legal, ops, etc.)
- product-context — Architecture and deployment context (`company.products`)
- go-no-go-checklist — Identified risks from route-a (`company.products`)

## Outputs

- Fallback checklist, used when no product context is available.
- dependency-tracker (markdown)
- go-no-go-checklist (markdown)
- prefer a permanent directory)
- rollback-plan (markdown)
- {product.root}/launch-readiness/dependency_tracker_{YYYY-MM-DD}.md
- {product.root}/launch-readiness/go_no_go_{YYYY-MM-DD}.md
- {product.root}/launch-readiness/rollback_plan_{YYYY-MM-DD}.md

