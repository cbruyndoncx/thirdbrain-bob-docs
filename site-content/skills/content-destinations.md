---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: content-destinations — ThirdBrain BOB skill
  description: Plan content backwards from business outcomes, not forwards from topics.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: content-destinations
catLabel: marketing-content
area: marketing
desc: Plans content backwards from business outcomes using the City Map framework — defining destinations (goals), signals (what carries people there), passengers (target…
summary: Plan content backwards from business outcomes, not forwards from topics.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- request — The mapping task — new build or quarterly reset — and any destinations, constraints, or business goals already known.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- existing-content — List of existing content pieces (blog posts, social content, videos) to classify by destination, signal, and funnel layer.
- request — The audit task — which content set to classify and which gaps matter most.
- previous-content-destinations-map — Content Destinations Map from a prior `full-map` or `audit-existing` run, read back to score each destination line against.
- performance-data — One month of metric data per destination line, scored on-track / stalling / exceeded against the map's defined success metrics.
- request — The review focus — which destinations or stops need the closest look this month.
outputs:
- Complete Content Destinations Map — Grand Central, destinations with metrics, signals/passengers/stops, timetable, distribution plan, and review cadence.
- Content Destinations Map built by classifying existing content against destinations, signals, and funnel layer, with content gaps identified and a gap-filling timetable.
- Per-destination status assessment (on track / stalling / exceeded), timetable adjustment recommendations, and experiment proposals for underperforming stops.
- '{client.marketing}/content-destinations-{YYYY-QN}.md'
prompts:
- Map our blog content to business goals using the city map framework
- What business outcome does each of these 17 blog posts serve?
- Create a content destinations map for Q2
- We're posting regularly but nothing is converting — help us connect content to outcomes
- Apply the Grace Andrews framework to our content plan
---
