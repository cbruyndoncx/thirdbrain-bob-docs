---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: root-cause-analysis — ThirdBrain BOB skill
  description: Diagnose why problems happened and define what needs to change so they stop happening.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: root-cause-analysis
catLabel: operations
area: operations
desc: Diagnoses root causes of customer issues, service failures, and recurring problems using a 5-Whys framework, fishbone diagrams, and pattern matching.
summary: Diagnose why problems happened and define what needs to change so they stop happening.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- 'problem-statement — Brief description of the issue: what happened, who was affected, when'
- problem-statement — Description of the current issue
- issue-records — Reference to vault issue records, support logs, or incident history if available
- root-cause — Root cause identified from five-whys or pattern-check output
- systemic-flag — Whether the issue was classified as systemic
outputs:
- corrective-action-plan (markdown)
- five-whys-analysis (markdown)
- pattern-assessment (markdown)
- '{company.qms.root}/rca-{YYYY-MM-DD}-corrective-action.md'
- '{company.qms.root}/rca-{YYYY-MM-DD}-pattern-check.md'
- '{company.qms.root}/rca-{YYYY-MM-DD}.md'
prompts:
- Why something went wrong
- Recurring issues
- Systemic vs one-off
---
