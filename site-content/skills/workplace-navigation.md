---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: workplace-navigation — ThirdBrain BOB skill
  description: Use this skill when the user needs a concrete plan for handling a difficult work dynamic, not just general advice.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: workplace-navigation
catLabel: human-resources
area: people
desc: Drafts conversation scripts, recommends boundary-setting language, prepares escalation notes, and helps resolve difficult colleague dynamics and team conflicts.
summary: Use this skill when the user needs a concrete plan for handling a difficult work dynamic, not just general advice.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- situation — The working relationship or dynamic that needs repair
- scope — `self` (default, nothing saved unless asked), `company`, or a client-id under {company.clients}/ — sets where a saved brief goes
- situation — Where a boundary is being crossed
- desired_state — What the arrangement should look like instead
- situation — Issue that first-line handling has not resolved
- prior_attempts — What has already been tried; may be empty for safety cases
outputs:
- Escalation brief with documented instances and impact; saved only at company or client scope, or when the user asks.
- Navigation brief with the boundary statement; saved only at company or client scope, or when the user asks.
- Navigation brief with the conversation plan; saved only at company or client scope, or when the user asks.
- '{scope.hr}/workplace-navigation-boundary-{case-slug}-{YYYY-MM-DD}.md'
- '{scope.hr}/workplace-navigation-escalation-{case-slug}-{YYYY-MM-DD}.md'
- '{scope.hr}/workplace-navigation-repair-{case-slug}-{YYYY-MM-DD}.md'
prompts:
- difficult colleague
- team conflict
- toxic dynamics
- workplace politics
- blocking behavior
- escalation path.
---
