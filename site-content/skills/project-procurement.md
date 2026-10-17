---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-procurement — ThirdBrain BOB skill
  description: Generate a procurement management plan with make-or-buy analysis, vendor evaluation, and contract recommendations. Use when user mentions 'procurement plan,' 'm
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-procurement
catLabel: project-management
area: project-delivery
desc: Generate a procurement management plan with make-or-buy analysis, vendor evaluation, and contract recommendations.
summary: Generate a procurement management plan with make-or-buy analysis, vendor evaluation, and contract recommendations. Use when user mentions 'procurement plan,' 'make or buy analysis,' 'vendor selection,' 'evaluate vendors,' or 'contract types.' Supports agile/hybrid and outcome-based contracting approaches.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- request — What to produce
outputs:
- procurement-plan (markdown)
- '{project-folder}/procurement_plan.md OR {me.inbox}/procurement_plan.md'
prompts:
- Create a procurement management plan for our project
- Run a make-or-buy analysis for this component
- Evaluate vendors for our upcoming contract
- Recommend contract types for our agile delivery
---
