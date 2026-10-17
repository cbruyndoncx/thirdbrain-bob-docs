---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: contract-clause-analyzer — ThirdBrain BOB skill
  description: 'Target Audience: PMC firms, engineering consultancies, quantity surveyors, and claims consultants managing FIDIC construction contracts in UAE/GCC.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: contract-clause-analyzer
catLabel: engineering
area: operations
desc: Analyze FIDIC contract clauses for risk allocation, obligations, notice periods, and deviations from standard conditions.
summary: 'Target Audience: PMC firms, engineering consultancies, quantity surveyors, and claims consultants managing FIDIC construction contracts in UAE/GCC.'
difficulty: expert
inputType: conversation
outputType: document
requires: '[mcp, api-key]'
roles: '[Operations Manager]'
inputs:
- contract-text — FIDIC contract clauses, Particular Conditions, or amendments to analyze
- edition — FIDIC edition (1999 or 2017) and book color (Red/Yellow/Silver)
- particular-conditions — Particular Conditions text to compare against standard FIDIC
- contract-text — Contract clauses to extract obligations from
outputs:
- deviation-matrix (markdown)
- obligations (markdown)
- risk-register (markdown)
- '{project-folder}/contract_clause_analysis.md'
- '{project-folder}/obligations_timeline.md'
- '{project-folder}/particular_conditions_deviations.md'
prompts:
- Analyze these FIDIC Red Book 2017 Particular Conditions for risk shifts
- Review Sub-Clauses 8.4, 13, and 20 for our contractor obligations
- Map all notice deadlines in this contract
- What are the Engineer's determination responsibilities under these clauses?
---
