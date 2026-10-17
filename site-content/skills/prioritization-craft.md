---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: prioritization-craft — ThirdBrain BOB skill
  description: Applies prioritization frameworks — RICE, ICE, Value vs Effort, Kano model — to rank options and say no gracefully. Use when the user needs 'RICE', 'ICE', 'Kano
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: prioritization-craft
catLabel: product-management
area: strategy
desc: Applies prioritization frameworks — RICE, ICE, Value vs Effort, Kano model — to rank options and say no gracefully.
summary: Applies prioritization frameworks — RICE, ICE, Value vs Effort, Kano model — to rank options and say no gracefully. Use when the user needs 'RICE', 'ICE', 'Kano', 'Value vs Effort', 'backlog prioritization', or 'prioritization decision'. For full PM workflows including PRDs and customer interviews, see product-manager-toolkit.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- request — The items to rank, what kind of thing they are, and the time horizon the ranking has to hold for.
- evidence — The usage, demand, revenue or dependency evidence behind each item — RICE is not reproducible without it, and a missing figure lowers Confidence rather than being guessed.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The items to triage and the deadline that makes a rough ordering preferable to an exact one.
- request — The items to place and what "value" means for this decision — revenue, retention, strategic position, or risk removed.
- request — The items to classify and the customer segment whose satisfaction the classification is about.
- customer-signal — What is known about how customers react to each item when present and when absent — the pairing Kano classification rests on, without which every item classifies as indifferent.
outputs:
- Decision frame, per-item Reach/Impact/Confidence/Effort scores with their assumptions, the ranked order, and what is explicitly not being done now.
- Each item assigned to a Kano category with the customer signal behind the assignment, and what the resulting satisfaction mix implies for sequencing.
- Per-item Impact/Confidence/Ease scores, the directional order they produce, and the caveat that the effort term is an estimate.
- The four quadrants with each item placed and justified, the quick wins called out, and the low-value items marked as non-goals.
- '{scope.knowledge-base.product}/prioritization-craft-{YYYY-MM-DD}.md'
prompts:
- Prioritize our feature backlog using RICE scoring
- Apply Value vs Effort analysis to these feature requests
- Help me say no to this feature request gracefully
- Run a Kano model analysis on our proposed features
---
