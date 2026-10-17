---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skill-gap-analysis — ThirdBrain BOB skill
  description: Audit skill coverage against business use cases, identify gaps, and resolve them systematically.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skill-gap-analysis
catLabel: utilities
area: foundational
desc: Analyzes use case lists against installed skills to identify coverage gaps, groups partial matches into new skills, creates missing skills, and scores them.
summary: Audit skill coverage against business use cases, identify gaps, and resolve them systematically.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- use-cases — Use-case list to map — a vault note, a pasted list, or the existing skill_use_case_mapping.md
outputs:
- Coverage table plus the grouped proposal table (new skill or extension per theme, with the use cases it covers).
- Phase 5 — one per new skill; extended skills are edited in place.
- Phase 7 qms-quality scorecard, one per skill created in the run, scored against the rubric matching the skill's output type.
- skill-use-case-mapping (markdown)
- '{company.knowledge-base}/skill_use_case_mapping.md'
- '{company.qms.scores}/{skill-name}.md'
- '{skills.root}/{skill-name}/'
prompts:
- Audit our skill coverage against this list of use cases
- Find gaps in our skill library for marketing workflows
- Map these business needs to existing skills and identify what's missing
- Score partial skill matches and group them into new skill proposals
---
