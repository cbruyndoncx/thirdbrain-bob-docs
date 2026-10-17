---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: messaging-coherence — ThirdBrain BOB skill
  description: 'Govern and score a business''s messaging as one coherent system. This skill assembles a single messaging operating spec from the owner''s existing vault context, '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: messaging-coherence
catLabel: business
area: strategy
desc: Builds one messaging operating spec from vault context and scores whether published messaging stays on-spec across seven disciplines — positioning, distinction, promise,…
summary: Govern and score a business's messaging as one coherent system. This skill assembles a single messaging operating spec from the owner's existing vault context, then scores any published asset against that spec across seven disciplines and flags exactly where the message has drifted.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Marketing, Content Manager]'
inputs:
- phrase-bank — Approved phrases scored against the messaging spec.
- source (Build messaging spec) — What to build the spec for (company by default, or a named client)
- positioning — Positioning / competitive frame (from positioning-craft).
- tone-of-voice — Voice and narrative tone (from brand-voice-generator).
- offerings — Offer and promise inputs.
- icp — Target customer the message is for.
- source (Coherence audit) — Path(s) or pasted text of the asset(s) to score
- messaging-spec — The spec to score against (required — the audit cannot run without it).
- source (Drift fix) — The drifting asset plus its prior coherence-audit scorecard
- messaging-spec — The spec the rewrite must conform to — the same scope's spec the audit cited (a client audit reads the client spec).
outputs:
- coherence-scorecard (markdown)
- coherence-scorecard-client (markdown)
- drift-fix-guidance (markdown)
- drift-fix-guidance-client (markdown)
- messaging-spec (markdown)
- messaging-spec-client (markdown)
- '{client.knowledge-base}/marketing/coherence-audit-{YYYY-MM-DD}.md'
- '{client.knowledge-base}/marketing/drift-fix-{YYYY-MM-DD}.md'
- '{client.knowledge-base}/marketing/messaging-spec-{YYYY-MM-DD}.md'
- '{company.knowledge-base}/marketing/coherence-audit-{YYYY-MM-DD}.md'
- '{company.knowledge-base}/marketing/drift-fix-{YYYY-MM-DD}.md'
- '{company.knowledge-base}/marketing/messaging-spec-{YYYY-MM-DD}.md'
prompts:
- Is my messaging consistent
- Check messaging coherence
- Score this against our messaging spec
---
