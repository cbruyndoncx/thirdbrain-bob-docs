---
description: 'Target Audience: PMC firms, engineering consultancies, quantity surveyors, and claims consultants managing FIDIC construction contracts in UAE/GCC.'
title: contract-clause-analyzer
---

# contract-clause-analyzer

Target Audience: PMC firms, engineering consultancies, quantity surveyors, and claims consultants managing FIDIC construction contracts in UAE/GCC.

| | |
|---|---|
| **Area** | Operations |
| **Category** | engineering |
| **Level** | expert |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [mcp, api-key] |
| **Roles** | [Operations Manager] |

Analyze FIDIC contract clauses for risk allocation, obligations, notice periods, and deviations from standard conditions.

## How you ask

- “Analyze these FIDIC Red Book 2017 Particular Conditions for risk shifts”
- “Review Sub-Clauses 8.4, 13, and 20 for our contractor obligations”
- “Map all notice deadlines in this contract”
- “What are the Engineer's determination responsibilities under these clauses?”

## Inputs

- contract-text — FIDIC contract clauses, Particular Conditions, or amendments to analyze
- edition — FIDIC edition (1999 or 2017) and book color (Red/Yellow/Silver)
- particular-conditions — Particular Conditions text to compare against standard FIDIC
- contract-text — Contract clauses to extract obligations from

## Outputs

- deviation-matrix (markdown)
- obligations (markdown)
- risk-register (markdown)
- {project-folder}/contract_clause_analysis.md
- {project-folder}/obligations_timeline.md
- {project-folder}/particular_conditions_deviations.md

## Seen in these workflows

- [Contract Clause Analyzer](../workflows/contract-clause-analyzer.md)

