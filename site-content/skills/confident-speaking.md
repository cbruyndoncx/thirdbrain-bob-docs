---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: confident-speaking — ThirdBrain BOB skill
  description: Structures presentations, verbal pitches, and talking points using the WHAT-SO WHAT-NOW WHAT framework. Use when user mentions 'presentation,' 'speaking,' 'pitc
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: confident-speaking
catLabel: human-resources
area: people
desc: Structures presentations, verbal pitches, and talking points using the WHAT-SO WHAT-NOW WHAT framework.
summary: Structures presentations, verbal pitches, and talking points using the WHAT-SO WHAT-NOW WHAT framework. Use when user mentions 'presentation,' 'speaking,' 'pitch,' 'talking points,' or 'difficult conversation.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder]'
inputs:
- request — The talk or pitch to structure, including topic and occasion.
- audience — Who is in the room and what decision authority they hold, so the hook and evidence are aimed at them.
- desired-action — The one thing the audience should do after the close; becomes the call to action.
- time-box — Length of the speaking slot. Sections are cut to fit this rather than the outline being padded out.
- evidence — Strongest available data point, example, or story. Absent, the route returns a prep-gap list instead of a finished outline.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The update to compress and the forum it is delivered in.
- audience — The executive or team receiving the update, used to set what can be assumed and what must be stated.
- core-message — The single point that survives if everything else is cut; becomes the headline.
- ask — What the listener has to decide, approve, or unblock.
- time-box — Maximum speaking time. Points are cut to fit rather than compressed into unreadable density.
- request — The conversation to prepare and why it is being had now.
- counterpart — The other party and the working relationship with them, which sets how direct the opening line can be.
- issue — The behaviour, decision, or conflict being raised, stated as the speaker will state it out loud.
- desired-outcome — What agreement or change the conversation is trying to reach; becomes the closing next step.
- likely-objections — Pushback the counterpart is expected to give. Absent, the route infers it and flags the inference.
outputs:
- Headline, three talking points, one explicit ask, and the questions most likely to come back.
- Opening line, issue statement, prepared responses to each anticipated objection, and the closing next step.
- Talk outline running hook, problem, solution, evidence, call to action, with per-section timings and anticipated questions with prepared answers.
- '{scope.knowledge-base.product}/confident-speaking-{YYYY-MM-DD}.md'
prompts:
- Structure a presentation using WHAT-SO WHAT-NOW WHAT
- Help me prepare talking points for a difficult conversation
- Create a verbal pitch for our product in 60 seconds
- Structure my keynote presentation for the conference
---
