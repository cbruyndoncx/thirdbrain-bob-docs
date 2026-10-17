---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: trigger-event-scout — ThirdBrain BOB skill
  description: Continuous, entity-seeded buying-signal detection. Each cycle scans configured sources for events matching named signal definitions — each with positive/negativ
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: trigger-event-scout
catLabel: sales
area: sales
desc: Continuous buying-signal detection — watches a configured entity watchlist and source set for defined buying-signal events (project launches, tenders, exhibition…
summary: 'Continuous, entity-seeded buying-signal detection. Each cycle scans configured sources for events matching named signal definitions — each with positive/negative/edge-case examples — resolves the entities involved against a curated watchlist, scores fit and confidence separately, and emits qualifying hits as standard `type: lead` notes plus an inbox digest.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key]'
roles: '[]'
inputs:
- signal-records — Prior signal records — dedupe and trend base.
- config_id — Watchlist config to run
- since — Only consider signals after this date
- signal-config — Signal config (signals, entities, sources, thresholds)
- seen-log — Previously emitted signal hits (dedupe state)
- client_id — Restrict the sweep to one client's watchlists
- entities — Organizations to watch
- signal_types — Buying-signal events that count — tenders, launches, exhibitions
- sources — Where to look; defaults to the standard source set
- config_id — Config whose scoring or sources need adjusting
- false_positives — Signals that scored high but were not real buying windows
outputs:
- Lead note for a client-scoped config (config has `client_id`) — the client's prospect, not ours.
- Lead note for an own-company config (no `client_id`), one folder per lead.
- combined-digest (markdown)
- cycle-log (markdown)
- digest (markdown)
- signal-config (markdown)
- updated-config (markdown)
- '{client.leads}/{lead-id}.md'
- '{lead.root}/{lead-id}.md'
- '{me.inbox}/signals_all_{YYYY-MM-DD}.md'
- '{me.inbox}/signals_{customer_id}_{YYYY-MM-DD}.md'
- '{resource.research-signals}/kb/{customer_id}/cycle_{YYYY-MM-DD}.md'
- '{resource.research-signals}/{customer_id}.md'
prompts:
- Monitor buying signals
- Watch for leads
- Run a signal cycle
---
