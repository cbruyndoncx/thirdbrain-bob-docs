---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: jtbd-building — ThirdBrain BOB skill
  description: Use this skill when the team needs to understand the progress a customer is trying to make before choosing a solution.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: jtbd-building
catLabel: product-management
area: strategy
desc: Creates job stories, maps push/pull/anxiety/habit forces, identifies current workarounds, and turns JTBD research into design or messaging implications.
summary: Use this skill when the team needs to understand the progress a customer is trying to make before choosing a solution.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Product Manager]'
inputs:
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- interviews — Evidence to synthesize into jobs — interview notes or transcripts, support tickets, or observed behavior — including the triggering situation
- segment — User segment the research covers
- profile — Company or client profile — identity and stage.
- icp — ICP — target customer the strategy is for.
- offerings — Offerings catalogue — what is being strategised.
- marketing-context — Positioning, narrative, and competitive frame.
- interviews — Evidence the job story and forces rest on — interview notes or transcripts, support tickets, or observed behavior — including the triggering situation
- segment — User segment the decision affects
- decision — The product decision the JTBD brief must inform
- job_story — Draft job story, if one exists; otherwise the route drafts it from the evidence
- current_workarounds — What customers do today instead, if already known; otherwise taken from the evidence
- job_story — Validated or draft job story to derive messaging from
- audience — Target audience for the message
- channel — Channel or message context the copy is for
- forces — Push, pull, anxiety, and habit forces to address in copy
outputs:
- jtbd-messaging (markdown)
- jtbd-synthesis (markdown)
- solution-design (markdown)
- '{scope.knowledge-base.product}/jtbd-building-{YYYY-MM-DD}.md'
prompts:
- Create job stories for our project management feature
- Map the push/pull forces for our target customer segment
- Identify current workarounds our users employ
- Turn our JTBD research into design implications
---
