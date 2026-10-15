---
description: Aggregate multiple relationship signals into a composite health score per client. Tracks trends over time, flags at-risk relationships early, and identifies expansion-ready accounts. The aggregation layer that sits on top of feedback, testimonials, communication, and deal data.
title: client-health-tracker
---

# client-health-tracker

Aggregate multiple relationship signals into a composite health score per client. Tracks trends over time, flags at-risk relationships early, and identifies expansion-ready accounts. The aggregation layer that sits on top of feedback, testimonials, communication, and deal data.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Head of Sales] |

Aggregates feedback signals (NPS, CSAT, testimonial willingness, response times, deal activity) into a composite client health score.

## How you ask

- “How is our relationship health with Acme Corp looking?”
- “Give me a portfolio health dashboard for all active clients”
- “Which clients are at risk right now? Show me the at-risk report”
- “Find expansion-ready clients we could upsell or ask for testimonials”
- “Show me the health trend for client bobbolt over the last 90 days”

## Inputs

- client_id — Client to score
- profile — Client profile — relationship baseline and history.
- marketing-context — Positioning context — frames expansion and retention angles.
- feedback-records — All feedback for this client — NPS and CSAT signal feeding the score.
- deal-activity — Deal records — activity recency and expansion signal.
- comms-threads — Communication threads — responsiveness signal.
- meeting-history — Meeting records — contact frequency signal.
- testimonials — Existing testimonials — advocacy signal.
- client_ids — Clients to include; defaults to every active client
- profile — Per-client profile (fanned across active clients) — portfolio context.
- score-history — Per-client score history (fanned across active clients) — previous score for the improved/declined comparison.
- threshold — Health score below which a client counts as at risk
- profile — Per-client profile — relationship history for risk scoring.
- score-history — Per-client score history — score trajectory that sets urgency.
- client_ids — Clients to assess for expansion signals; defaults to all active
- profile — Per-client profile — current spend and footprint for expansion analysis.
- client_id — Client whose health history is to be trended
- periods — How many historical snapshots to report; each comes from the score history, reconstructed from dated evidence only where the history does not reach back, and reported as unknown when neither exists
- profile — Per-client profile — baseline for trend comparison.
- score-history — The client's recorded score history — the primary source for every trend snapshot.

## Outputs

- Append-only score history, one row per scored client per run; trend and since-last-check comparisons read it.
- at-risk-report (markdown)
- expansion-report (markdown)
- health-score (markdown)
- health-trend-report (markdown)
- portfolio-dashboard (markdown)
- {client.profile-root}/health_score.md
- {client.profile-root}/health_score_history.md
- {company.reports}/at_risk_clients.md
- {company.reports}/client_health_portfolio.md
- {company.reports}/client_health_trend.md
- {company.reports}/expansion_opportunities.md

