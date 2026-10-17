---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: variation-order-analyzer — ThirdBrain BOB skill
  description: 'Target Audience: Quantity surveyors, contract administrators, project directors, and claims consultants managing FIDIC variation orders in UAE/GCC construction '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: variation-order-analyzer
catLabel: engineering
area: operations
desc: Assess variation order entitlement, apply FIDIC valuation methodologies, calculate cost and schedule impact, and structure defensible valuations.
summary: 'Target Audience: Quantity surveyors, contract administrators, project directors, and claims consultants managing FIDIC variation orders in UAE/GCC construction projects.'
difficulty: expert
inputType: conversation
outputType: document
requires: '[mcp, api-key]'
roles: '[Operations Manager]'
inputs:
- variation-request — Variation order request, instruction, or scope change description
- original-scope — Relevant original contract scope, specifications, or drawings
- variation-details — Scope of variation work, quantities, resources required
- schedule-of-rates — Contract Schedule of Rates and Prices
- variations — List of variations with status, values, and approval state
outputs:
- entitlement-report (markdown)
- register (markdown)
- valuation-report (markdown)
- '{project-folder}/variation_register.md'
- '{project-folder}/vo_entitlement_{number}.md'
- '{project-folder}/vo_valuation_{number}.md'
prompts:
- Is this scope change a variation or part of the original contract?
- Value this variation order using FIDIC Red Book 2017 rates
- Update the variation register with VO-015
- The Contractor claims this is a variation — assess entitlement
---
