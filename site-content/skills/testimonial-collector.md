---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: testimonial-collector — ThirdBrain BOB skill
  description: Manage the full lifecycle of client testimonials — from initial request through approval to tracking where each testimonial is used. Creates `testimonial` entit
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: testimonial-collector
catLabel: sales
area: sales
desc: Manages the full testimonial lifecycle — request, remind, capture, approve, and track usage across marketing materials and proposals.
summary: Manage the full lifecycle of client testimonials — from initial request through approval to tracking where each testimonial is used. Creates `testimonial` entities in the vault for systematic reuse across proposals, marketing, and sales.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing]'
inputs:
- client_id — Client being asked
- respondent — Person to request the testimonial from
- project_ref — Project the testimonial should speak to
- profile — loaded from your vault context
- tone-of-voice — loaded from your vault context
- contact-details — loaded from your vault context
- testimonial_ref — Outstanding request to chase
- channel — Where the reminder is sent — email, linkedin, whatsapp, or in-person. Match the channel the original request went out on. (email | linkedin | whatsapp | in-person)
- respondent — Who gave the testimonial
- content — The testimonial text as given — verbatim, not paraphrased
- format — Form the testimonial arrived in — written, video, linkedin-recommendation, or case-study-quote. Determines how it is stored and where it can be reused. (case-study-quote | linkedin-recommendation | video | written)
- testimonial_ref — Testimonial awaiting sign-off
- permission_level — how far the testimonial may be attributed and reused; see Phase 4 (anonymized | internal-only | public)
- client_id — Restrict the audit to one client; defaults to all
- existing-testimonials — Existing testimonials for this client — the population being audited.
- testimonial_ref — Testimonial being used
- used_in — Assets the testimonial now appears in
- client_id — Client whose existing feedback should be reviewed
- source_scope — Named source scope such as meetings, feedback notes, emails, or delivery notes
outputs:
- testimonial-approval (markdown)
- testimonial-audit-report (markdown)
- testimonial-backfill-report (markdown)
- testimonial-capture (markdown)
- testimonial-followup (markdown)
- testimonial-request (markdown)
- testimonial-usage (markdown)
- '{client.testimonials}/testimonial_backfill_{YYYY-MM-DD}.md'
- '{client.testimonials}/testimonial_{YYYY-MM-DD}.md'
- '{company.reports}/testimonial_audit.md'
prompts:
- Send a testimonial request to our main contact at Acme Industries after the rebrand project
- Follow up on the testimonial we requested from Sarah two weeks ago
- The client just sent their testimonial over email, capture it in the vault
- Run a testimonial audit across all clients and show me gaps
- Mark the Acme testimonial as approved for website and proposal use
---
