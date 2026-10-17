---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Contract Clause Analyzer — BOB Workflow
  description: 'Target Audience: PMC firms, engineering consultancies, quantity surveyors, and claims consultants managing FIDIC construction contracts in UAE/GCC.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: contract-clause-analyzer
youtubeId: ''
published: ''
privacy: unlisted
title: Contract Clause Analyzer
thumbnail: ''
subtitle: FIDIC Clause Risk Analysis
inputs:
- label: contract-clauses.pdf
  icon: 📜
- label: particular-conditions.pdf
  icon: 📋
outputs:
- label: clause_analysis.md
  icon: 📊
- label: deviation_matrix.md
  icon: ⚠️
- label: obligations_timeline.md
  icon: 📅
steps:
- Identify edition and book color
- Clause-by-clause risk analysis
- Flag deviation from standard
- Map obligations and deadlines
- label: Review risk register
  actor: human
- Compile analysis report
trigger: '"Analyze these FIDIC Red Book 2017 Particular Conditions for risk shifts"'
timeSavings: ~2 days manual review → ~30 min automated (100× faster)
compounding: Each analysis builds a clause library — reusable across similar FIDIC projects
frequency: Per contract · per variation instruction
hook: 'The contract is signed.

  The risk it moved onto you is buried in clause 14.'
outcome: ''
benefits: []
cta: ''
difficulty: expert
primaryRoles:
- Operations Manager
pricingTier: pack-engineering-pro
category: engineering
filterGroup: engineering
area: operations
---

**Target Audience:** PMC firms, engineering consultancies, quantity surveyors, and claims consultants managing FIDIC construction contracts in UAE/GCC.
