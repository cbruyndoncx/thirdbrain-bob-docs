---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: sales-enablement — ThirdBrain BOB skill
  description: Build pre-sale assets that move prospects toward a decision — webinar outlines, lead magnets, scopes of work, and contract summaries.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: sales-enablement
catLabel: sales
area: sales
desc: Creates pre-sale assets including webinar outlines, lead magnet structures, scope of work documents, and plain-language contract summaries.
summary: Build pre-sale assets that move prospects toward a decision — webinar outlines, lead magnets, scopes of work, and contract summaries.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- request — Webinar topic, the goal it serves (educate, generate leads, convert, launch, partner), the target audience, and the slot length available.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company background used to write the credibility segment of the opening and to keep the host's claims true.
- offerings — Services and pricing the pitch block transitions into, so the offer named on the webinar is one that actually exists.
- tone-of-voice — Writing style for the registration page, hook, and email copy the outline drafts.
- request — Topic, target audience segment, and the promise the asset has to deliver, plus any format or production constraint already fixed.
- profile — Company background supplying the authority the asset trades on and the audience it already reaches.
- offerings — Paid offering the asset's final-page CTA and nurture sequence point at, so the magnet leads somewhere real.
- tone-of-voice — Writing style for the landing page headline, bullets, and delivery email.
- request — Project details, client requirements, deliverables, timeline, and the commercial terms already agreed — the material the SOW formalises rather than decides.
- source-materials — Proposal excerpt, requirements document, or brief supplied by the caller, read so scope, milestones, and pricing in the SOW match what was actually quoted instead of being reconstructed.
- profile — Legal and trading identity of the provider party named in the SOW.
- offerings — Real service definitions and rates, so in-scope deliverables and the investment section match what is actually sold.
- tone-of-voice — Writing style for the narrative sections — overview and objective — while the commercial clauses stay literal.
- contract — The agreement to translate — service agreement, NDA, partnership, or vendor contract. Without it the route does not run; this skill summarises a real document and does not draft one.
- request — What the summary is for and which side is being advised, plus any clause the caller already wants checked.
- profile — Own trading identity, used to tell which named party in the contract is the reader's side.
- tone-of-voice — Writing style for the plain-language rewrite; the quoted clause references stay verbatim regardless.
outputs:
- Formal SOW — overview, in-scope and out-of-scope lists, milestone and payment table, acceptance criteria, assumptions and dependencies, change-management process, investment, and signature block.
- Full webinar structure — registration and reminder copy, timed opening, three teaching blocks with interaction prompts, offer transition, pitch, seeded Q&A, and the attendee and no-show follow-up sequences.
- One recommended asset with its type, promise, delivery format, landing-page hook, section-by-section content outline, design notes, nurture topics, the non-obvious reason prospects stall, and the tradeoff against the rejected alternative.
- Plain-language summary of obligations, money, timeline, exit and dispute terms, confidentiality and IP, plus a red-flag list for legal review, a key-dates table, and the standing note that the summary does not replace legal advice.
- '{company.sales}/sales-enablement-{descriptor}.md'
prompts:
- Create a lead magnet outline for our target audience
- Draft a scope of work document for this project
- Write a plain-language contract summary for the client
- Build a webinar outline for our pre-sale pipeline
---
