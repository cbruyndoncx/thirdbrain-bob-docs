---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-charter — ThirdBrain BOB skill
  description: Generates formal project charters, updates existing charters, and extracts scope, objectives, stakeholders, milestones, budget, and approval sections from proje
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-charter
catLabel: project-management
area: project-delivery
desc: Generates formal project charters, updates existing charters, and extracts scope, objectives, stakeholders, milestones, budget, and approval sections from project briefs…
summary: Generates formal project charters, updates existing charters, and extracts scope, objectives, stakeholders, milestones, budget, and approval sections from project briefs or stakeholder conversations. Use when the user mentions 'project charter,' 'authorize project,' 'project kickoff,' 'formalize project,' or 'draft a charter.' This is the project charter methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Product Manager]'
inputs:
- transcript — Project brief, kickoff conversation, or call notes the charter is drafted from; supplies purpose, objectives, scope, stakeholders, budget, and timeline.
- project-context — Tailoring decisions read back from `project-context` — charter depth, delivery approach, and priority principles that shape how each section is written.
- profile — Company or client profile supplying the sponsoring organization, delivery standards, and industry context behind the assumptions. For client scope, resolves to the client profile instead (`client.profile`).
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- existing-charter — Charter already in the project folder; its approved content is preserved and the revision is merged into it rather than replacing it.
- transcript — Conversation or note carrying the change — new stakeholders, revised budget, moved milestones — that the existing charter is updated with.
- project-context — Tailoring decisions read back from `project-context`, so the revision stays at the depth the charter was originally written to.
- profile — Company or client profile used to check that revised roles and standards still match the delivering organization. For client scope, resolves to the client profile instead (`client.profile`).
- project-name — Name of the project being authorized. The route refuses to proceed without it rather than inventing one.
- transcript — Partial brief or fragment of a conversation, where one exists, used to fill whichever sections it covers; everything it does not cover is marked TBD.
- profile — Company or client profile used to supply the sponsoring organization and delivery standards that would otherwise also be TBD. For client scope, resolves to the client profile instead (`client.profile`).
outputs:
- Charter draft carrying the confirmed core facts, with budget, timeline, and unidentified stakeholders marked TBD and the gap list stated rather than filled with invented figures.
- Complete charter — purpose and justification, SMART objectives, in/out scope, assumptions, constraints, high-level risks, milestones, budget summary, stakeholder roles with PM authority, and the approval table.
- Revised charter with new information merged in, superseded content either updated or dated-off, and the approval table reset where a re-approval is required.
- '{project-folder}/project_charter.md OR {me.inbox}/project_charter.md'
prompts:
- Create a project charter for our website redesign
- Draft a formal charter from this project brief
- Authorize the project with scope, objectives, and milestones
- Update our existing project charter with new stakeholders
---
