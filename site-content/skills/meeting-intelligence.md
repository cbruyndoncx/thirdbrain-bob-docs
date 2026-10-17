---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: meeting-intelligence — ThirdBrain BOB skill
  description: Turn meeting material into structured, execution-ready outputs before or after a meeting.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: meeting-intelligence
catLabel: productivity
area: foundational
desc: Analyzes meeting transcripts, notes, or recording-derived text to extract decisions, action items, blockers, open questions, sentiment, and follow-up emails.
summary: Turn meeting material into structured, execution-ready outputs before or after a meeting.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- source (Post-Meeting Analysis) — Transcript text, meeting notes, or recording-derived text
- context — loaded from your vault context
- profile — Company or client profile — anchors who the meeting is with.
- icp — ICP — informs decision-quality scoring for sales/prospect meetings.
- tone-of-voice — Tone of voice — register for follow-up drafts and summaries.
- source (Notetaker Transcript Ingest) — Folder holding notetaker exports (a synced cloud folder or a manual download dir), or the literal keyword 'fireflies' to fetch via the Fireflies API instead of reading files
- 'tool — Notetaker that produced the exports — sets capture_tool and destination subfolder (default: fireflies) (fireflies | otter | granola | fathom | read | zoom | teams | other)'
- 'dest — Vault-relative destination (default: {me.meetings}/NOTETAKER/{TOOL})'
- 'limit — Fireflies API route only — fetch only the N most recent transcripts (default: all)'
- goal — Meeting goal statement
- attendees — Attendee names and roles
- duration — Meeting duration (e.g., 30 min, 1 hour)
- target — Meeting target (person, company, or topic)
- date_context — Meeting date and any context
- source (Full Meeting-to-Execution Pipeline) — Transcript text, meeting notes, or recording-derived text
- context — loaded from your vault context
- client_kpi — Include client KPI update (only when context is client) (yes | no)
- source (Sales Call Debrief) — Call transcript, notes, or recording-derived text
- call_type — Type of sales call (defaults to discovery if unclear) (discovery | demo | proposal-review | negotiation | check-in | other)
- pre_call_objectives — Objectives set before the call (e.g., from a discovery-call prep)
- relationship_type — How the prospect entered the relationship — governs the commercial boundary check and how personal warmth is interpreted (cold | warm-intro | acquaintance | friend | former-colleague | community | existing-client | referral-partner | ecosystem)
- secondary_summary — Notetaker summary, CRM note, or prior framework output to grade against the transcript
- source (Discovery Opportunity Assessment) — Discovery call transcript, notes, or recording-derived text
- profile — Company or client profile — anchors whose commercial position the boundary check reasons from
outputs:
- agenda_md (markdown)
- analysis_md (markdown)
- assessment_md (markdown)
- briefing_md (markdown)
- debrief_md (markdown)
- full_md (markdown)
- meeting-intelligence (markdown)
- meeting_notes (markdown)
- prefer a permanent directory)
- '{me.meetings}/NOTETAKER/{TOOL}/{date} - {title}.md'
prompts:
- Extract action items from this meeting transcript
- Summarize this meeting and identify key decisions
- Run the full pipeline on this client meeting transcript
- Debrief this sales call and score my performance
- Review my calls from this week and show me patterns
- I just got off a discovery call with a friend of a friend — is there a business here?
- What should we actually sell this prospect, and what do we give away free?
- My notetaker says they're a champion — check that against the transcript
---
