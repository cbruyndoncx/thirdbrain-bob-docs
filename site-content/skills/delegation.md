---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: delegation — ThirdBrain BOB skill
  description: Identify what the founder should stop doing and build a framework to hand it off — moving them from Doer to Delegator to Director.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: delegation
catLabel: human-resources
area: people
desc: Audits founder time allocation, sorts tasks into four delegation buckets (Only You, Teach Someone, Hire For, Eliminate), builds handoff plans with 'good enough'…
summary: Identify what the founder should stop doing and build a framework to hand it off — moving them from Doer to Delegator to Director.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Operations Manager]'
inputs:
- client_company_overview — Client company profile — name, industry, size, offering, key contacts. Read when the request is client-scoped; the route asks the user when absent.
- context — Founder's current situation — team size, role, hours worked, pain points
- 'scope — `company`, or a client-id under the client root (`client.root`) — a string with one reserved value, not a closed set. Decides where the output is written: company processes or that client''s processes.'
- profile — Company profile — stage and team context for the delegation audit.
- task — The specific task or responsibility to hand off
- delegate — Who will take over (name/role). If unknown, skill recommends.
- prior_audit — Link to the previous delegation audit
outputs:
- delegation_audit (markdown)
- handoff_plan (markdown)
- review (markdown)
- '{scope.processes}/delegation/delegation_audit_{YYYY-MM-DD}.md'
- '{scope.processes}/delegation/delegation_review_{YYYY-MM-DD}.md'
- '{scope.processes}/delegation/{task-slug}_handoff_{YYYY-MM-DD}.md'
prompts:
- Delegate
- Bottleneck
- Doing too much
---
