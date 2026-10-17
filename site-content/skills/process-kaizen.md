---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: process-kaizen — ThirdBrain BOB skill
  description: 'Target Audience: business owners, operations leads, and consultants who have already mapped a process with `business-baseline` and want to continuously improve '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: process-kaizen
catLabel: business
area: strategy
desc: Runs AI-powered Kaizen continuous improvement on a single business process that business-baseline has already mapped.
summary: 'Target Audience: business owners, operations leads, and consultants who have already mapped a process with `business-baseline` and want to continuously improve it — reduce waste, standardize, and build a team improvement habit — using the Japanese Kaizen discipline.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Operations Manager]'
inputs:
- process-ref — The target process — a type:process note path or {client-id}/{process-id}. Must already exist (produced by business-baseline).
- process-ref — The target type:process note (must exist).
- scope-ref — The team / org / client the suggestion system serves.
- process-ref — The type:process note the Kaizen event targets — needed only for the Kaizen-event charter, which is keyed to that process. Without it the route still runs the suggestion system and metrics, and asks which process the event is for before writing a charter.
outputs:
- gemba-walk-guide (markdown)
- gemba-walk-guide-company (markdown)
- kaizen-artifacts (markdown)
- kaizen-artifacts-company (markdown)
- kaizen-event-charter (markdown)
- kaizen-event-charter-company (markdown)
- suggestion-register (markdown)
- waste-findings (markdown)
- waste-findings-company (markdown)
- '{client.business-baseline.waste}/{process-id}-{category}.md'
- '{client.business-baseline}/kaizen/{process-id}-gemba-walk.md'
- '{client.business-baseline}/kaizen/{process-id}-kaizen-event.md'
- '{client.business-baseline}/kaizen/{process-id}-{5s|pdca|standard-work}.md'
- '{company.process-audits}/{process-id}-{category}.md'
- '{company.processes}/kaizen/{process-id}-gemba-walk.md'
- '{company.processes}/kaizen/{process-id}-kaizen-event.md'
- '{company.processes}/kaizen/{process-id}-{5s|pdca|standard-work}.md'
- '{output.tasks}/kaizen-suggestion-{slug}.md'
prompts:
- Kaizen my process
- Reduce waste in X
- Run a waste audit
---
