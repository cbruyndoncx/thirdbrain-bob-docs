---
description: Create winning B2B proposals using proven frameworks (SPIN, MEDDIC, MEDDPICC, SPICED, Challenger Sale, Gap Selling, Value Selling) and value-focused messaging.
title: consultative-selling
---

# consultative-selling

Create winning B2B proposals using proven frameworks (SPIN, MEDDIC, MEDDPICC, SPICED, Challenger Sale, Gap Selling, Value Selling) and value-focused messaging.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Head of Sales] |

Applies SPIN, MEDDIC, MEDDPICC, SPICED, Challenger, Gap Selling, and Value Selling.

## How you ask

- “Generate a discovery question bank using SPIN selling”
- “Build an ROI calculator for our enterprise prospects”
- “Create an executive brief for the C-suite meeting”
- “Qualify this deal using the MEDDIC framework”

## Inputs

- request — The discovery task — which qualification framework to score against, the meeting being prepared for, and what is already known about the buyer.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Own or client business profile, read so questions are phrased in the buyer's language and the scorecard knows which services the deal is being qualified for.
- region-context — Regional business customs, calendar, and economic climate that decide which discovery questions land and when a meeting can realistically be held; produced by `regional-context`.
- prior-proposals — Earlier deliverables for the same prospect, read so the question bank does not re-ask what a previous round already answered.
- request — Which brief is wanted and the raw material for it — the prospect's stated challenge, discovery notes, and the meeting the brief has to open or follow up.
- profile — Own or client business profile supplying the services, credibility markers, and value framing the brief argues from.
- region-context — Geopolitical and economic climate used to open the brief by acknowledging the room and to pitch value as growth, efficiency, or certainty; produced by `regional-context`.
- prior-proposals — Previous briefs and question banks for the same prospect, read so the diagnostic brief builds on the recorded discovery rather than restating it.
- request — The engagement being proposed — service type, duration, deal size band, buyer level, and any commercial terms already agreed in discovery.
- profile — Own or client business profile supplying the delivering entity, service catalogue, and pricing posture the proposal commits to.
- region-context — Fiscal year timing, holidays, and regulatory environment that constrain the proposed timeline, currency, and contracting terms; produced by `regional-context`.
- prior-proposals — The diagnostic brief and qualification scorecard for this deal, read so the proposal stays consistent with the pain, gap, and decision criteria already recorded.
- request — The value case to quantify — current-state pain with hours or costs attached, expected future state, and the engagement fee the return is measured against.
- profile — Own or client business profile supplying the cost bases and service economics the ROI multiple is calculated from.
- region-context — Currency, labour cost, and inflation baseline so the quantified value is stated in figures the buyer's market recognises; produced by `regional-context`.
- prior-proposals — Discovery and diagnostic material for the same prospect, read so the ROI model reuses the pain figures already validated with the buyer.

## Outputs

- 300-500 word cold-outreach brief covering the challenge, cost of inaction, approach, expected outcome, and the discovery call being asked for.
- Complete formal proposal — executive summary, current state, gap, approach, timeline, investment, ROI analysis, and terms.
- Completed qualification scorecard with a score and supporting evidence per component, and the unqualified gaps still to be closed.
- Customised SPIN question bank grouped by situation, problem, implication, and need-payoff, each question labelled with the pain it is meant to surface.
- Post-discovery analysis of current state, quantified gap, and high-level approach, with every unverified figure labelled as an assumption.
- The proposal filed in the company proposals folder when scope is `company` (the company sells its own services to a prospect); on behalf of a client (scope = client-id) the proposal is `full-proposal` in that client's sales folder. Falls back to the scratch folder only when no scope is set.
- current-state annual cost, future-state annual value, annual gap, proposed fee, ROI multiple and percentage, and payback period, each line carrying its assumption. Returned in the conversation; fold it into a brief or proposal via the `brief` or `proposal` route to persist it.
- {client.sales}/proposals/{client-name}/diagnostic-brief-{client}-{YYYY-MM-DD}.md
- {client.sales}/proposals/{client-name}/discovery-questions-{client}-{YYYY-MM-DD}.md
- {client.sales}/proposals/{client-name}/executive-brief-{client}-{YYYY-MM-DD}.md
- {client.sales}/proposals/{client-name}/full-proposal-{client}-{YYYY-MM-DD}.md
- {client.sales}/proposals/{client-name}/qualification-{client}-{YYYY-MM-DD}.md
- {company.sales.proposals}/{client-name}/proposal-{client}-{YYYY-MM-DD}.md

