---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: free-tool-strategy — ThirdBrain BOB skill
  description: Expert guidance for engineering-as-marketing strategy. Build calculators, generators, and interactive tools for lead generation and SEO value. Plan and evaluate
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: free-tool-strategy
catLabel: marketing-strategy
area: marketing
desc: Builds calculators, generators, analyzers, and interactive tools for lead generation and SEO value.
summary: Expert guidance for engineering-as-marketing strategy. Build calculators, generators, and interactive tools for lead generation and SEO value. Plan and evaluate free tools that attract organic traffic and build brand awareness.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- profile — Scope-resolved business profile — business model and core product the tool has to feed. Caller resolves the path from the active scope.
- icp — Audience pains the candidate concepts are screened against for buyer fit.
- marketing-context — Positioning and channels used to judge whether a concept fits the way the business already goes to market.
- candidates — The competing tool concepts to screen. Two or more — a single concept belongs on the `single-tool` route.
- goal — Primary business goal for the tool. It decides which winner is recommended when two concepts score close — an SEO goal favours the concept with search demand and link pull, a lead-gen goal the one whose users match the buyer. (lead-gen | seo | brand-awareness | product-education)
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
- profile — Scope-resolved business profile — the product the tool has to create a natural path to.
- icp — Audience pains used to test whether the concept's users are the business's buyers.
- marketing-context — Positioning and channels the tool's landing page and CTA path have to stay consistent with.
- tool-concept — The single concept already chosen — what it does and for whom.
- tool-evaluation — Scorecard from the `idea-screen` route, read back so the concept's scoring carries into the spec instead of being re-argued.
- goal — Primary business goal for the tool. It sets what the MVP has to prove first and which measurement targets the spec carries. (lead-gen | seo | brand-awareness | product-education)
- profile — Scope-resolved business profile — used to judge whether the tool is core to the brand or merely useful.
- marketing-context — Positioning and differentiation used to test whether the tool is a strategic moat worth building custom.
- tool-concept — The concept whose implementation is being decided — what it does and what it must own.
- build-constraints — Dev capacity, budget, timeline, and any platform the user is locked into. Absent, the route records the constraint as unknown rather than assuming capacity exists.
- tool-spec — MVP scope from the `single-tool` route, read back so the build-or-buy call is made against a defined scope rather than a vague concept.
- profile — Scope-resolved business profile — the product the captured lead is being routed towards.
- icp — Audience definition used to judge whether the captured leads are the business's buyers.
- marketing-context — Channels and messaging the capture offer and CTA path have to match.
- tool-concept — The settled tool concept whose gating is unresolved — what it does and what output the user gets.
- goal — Primary business goal for the tool. It moves the gating recommendation directly — a pure SEO or brand goal points at an ungated tool, a lead-gen goal at gated or partially gated. (lead-gen | seo | brand-awareness | product-education)
- tool-spec — MVP scope from the `single-tool` route, read back so gating is designed against the tool's real output rather than a guess at it.
- profile — Business/client profile — model, audience, current offers
- icp — ICP file — target audience pains and triggers
- existing-offers — Brief description of current paid offers and lead magnets (if any)
outputs:
- 3-5 ranked offer concepts, each with format tag, value-ladder slot, ROI, stack with cost and time, AI-fit verdict, and RICE score.
- Gating choice with the reach-versus-capture tradeoff stated, the capture offer and CTA path, the qualifying question if one is used, and the measurement targets.
- Handoff brief for a dev team or agency — chosen build approach, the reason it beat the other two, and the data, integration, and maintenance assumptions it rests on.
- Requirements, explicit MVP scope boundaries, what is deliberately skipped, and the recommended build path.
- Scorecard per candidate, the kill reason for each rejected concept, and the one or two recommended winners.
- Strategy write-up carrying the build decision, its owners and milestone sequence, and the dependencies and risks the approach introduces.
- Strategy write-up for the screen — the chosen concept, why it matters to the audience and the business, what gets built first, and how success is measured.
- Tool thesis, audience and problem framing, lead capture logic and CTA path, and the assumptions and risks behind the scope.
- '{scope.marketing}/free-tools/free-tool-strategy-{YYYY-MM-DD}.md'
- '{scope.marketing}/free-tools/productized-offers-{YYYY-MM-DD}.md'
- '{scope.marketing}/free-tools/tool-brief-{tool-name}.md'
- '{scope.marketing}/free-tools/tool-evaluation-{tool-name}.md'
- '{scope.marketing}/free-tools/tool-spec-{tool-name}.md'
prompts:
- Build a free calculator tool for lead generation
- Evaluate this tool idea with a scorecard and scope the MVP
- Plan a free ROI calculator that captures leads
- Design an interactive tool for engineering-as-marketing
- Give me 5 productized AI offer ideas for my coaching business
- What audit/playbook offers could I build as a tripwire?
- Brainstorm AI-automated lead magnets across the value ladder
---
