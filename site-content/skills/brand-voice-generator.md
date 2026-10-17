---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: brand-voice-generator — ThirdBrain BOB skill
  description: Generate complete brand configuration files for a person, company, or client. Guides users through an interactive process to define brand identity and writing v
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: brand-voice-generator
catLabel: business
area: strategy
desc: Builds brand voice guidelines from existing content and turns them into a style system, and distils a founder's origin story into a 5-lens brand DNA.
summary: Generate complete brand configuration files for a person, company, or client. Guides users through an interactive process to define brand identity and writing voice, storing files in the appropriate vault location.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- profile — Company or client profile — entity and relationship context.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- design-spec — Brand design spec (read-only context). Owned/authored by the brand-system skill — this skill does NOT write it.
- tone-of-voice — Existing tone of voice guide.
- story — The founder's origin story, career arc, and personal texture (or a pointer to an existing founder-story note to read first)
- scope — Personal (`{me.profile-root}/brand/`), Company (`{company.brand}`), or client-id (`{client.brand}`)
- voice-source — At least one must already exist — this route reformats existing voice material and does not create it. Under the `personal` scope the same two files are read from the owner's profile root (`me.profile-root`); an input carries only the two key slots, so that third scope is stated here rather than declared.
- scope — `personal`, `company`, or a client-id under {company.clients}/
- slug — Persona filename slug
- install — `transitory` (pasted per conversation) or `persistent` (read at session start)
outputs:
- brand-config (json)
- brand-json (json)
- brand-json-client (json)
- founder-voice-dna (markdown)
- founder-voice-dna-client (markdown)
- founder-voice-dna-personal (markdown)
- persona (markdown)
- tone-of-voice (markdown)
- tone-of-voice-client (markdown)
- '{client.brand}/brand.json'
- '{client.brand}/founder-voice-dna.md'
- '{client.brand}/tone_of_voice.md'
- '{company.brand}/brand.json'
- '{company.brand}/config.json'
- '{company.brand}/founder-voice-dna.md'
- '{company.brand}/tone_of_voice.md'
- '{me.profile-root}/brand/founder-voice-dna.md'
- '{scope.personas}/{slug}.md'
prompts:
- Create brand voice guidelines from our existing blog posts
- Define our tone of voice for social media communications
- Build a style system based on our company's writing samples
- Analyze our content and extract consistent voice patterns
---
