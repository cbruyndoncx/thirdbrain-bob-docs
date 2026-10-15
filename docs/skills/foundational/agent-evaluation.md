---
description: 'Target Audience: Founders, operators, and team leads evaluating AI agent tools for knowledge work delegation.'
title: agent-evaluation
---

# agent-evaluation

Target Audience: Founders, operators, and team leads evaluating AI agent tools for knowledge work delegation.

- **Area:** Foundational
- **Category:** utilities
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Product Manager, Operations Manager

Evaluate AI agent tools against three structural dimensions (Persistent Memory, Inspectable Surfaces, Compounding Context) and generate calibrated delegation specs.

## How you ask

- “Evaluate this agent”
- “Should I use this tool”
- “Agent comparison”

## Inputs

- tool-name — Name of the agent tool being evaluated
- task-description — Specific task or workflow intended for delegation
- quality-definition — What 'good' looks like for this task
- tools — Comma-separated list of tool names to compare
- task-description — The task all tools will be evaluated against

## Outputs

- comparison (markdown)
- scorecard (markdown)
- {company.decisions}/agent-comparison-{YYYY-MM-DD}.md
- {company.decisions}/agent-eval-{tool-slug}-{YYYY-MM-DD}.md

