---
type: knowledge-base
title: "BOB User Manual — 13. Strategy & Management"
description: "How BOB supports strategic planning, decision-making, market analysis, management reporting, and the link from strategy to execution"
status: draft
created: 2026-08-07
modified: 2026-08-07
tags: [bob, user-manual, wiki]
---

# 13. Strategy & Management

BOB treats strategy as structured, searchable data — not a slide deck you forget after the offsite. Strategy notes, decisions, and planning artifacts live as first-class vault entities, linked to the meetings and projects they drive.

This chapter covers: how decisions are captured; the tools BOB provides for strategic analysis and planning; management reporting rhythms; and how strategy connects downward to projects, campaigns, and daily work.

---

## 13.1 Strategy artifacts — what BOB stores

Two entity types anchor this module.

**Strategy notes** hold directional thinking: market positioning, where-to-play choices, growth bets, and annual priorities. They are authored notes, not generated summaries. BOB can draft them with you, but you own the content.

**Decision-log entities** are first-class records. Every significant decision — a new market, a pricing change, a hire above budget, a product pivot — deserves its own note with the date, the options considered, the reasoning, and the outcome. This is not optional: decisions logged in meeting notes get lost. A decision-log entry makes the reasoning searchable six months later.

| Entity | What it captures | Linked to |
|--------|-----------------|-----------|
| Strategy note | Directional choices, positioning, growth priorities | OKR notes, project notes, campaigns |
| Decision-log | Date, options, rationale, outcome, owner | Meeting note where the decision was made |

---

## 13.2 Decision support

BOB offers three different modes of decision support. Choose the one that fits the decision.

| Skill | When to use it |
|-------|---------------|
| `ask-boardroom` | You want a panel of perspectives — multiple advisor voices debating the options before you choose |
| `decision-frameworks` | You want a specific analytical framework applied: expected value, regret minimisation, pre-mortem |
| `ask-zeus` | You want 1:1 coaching that draws on your personal vault context |

### Using `ask-boardroom`

Describe the decision and the options you're considering. BOB assembles a virtual panel — each advisor brings a different lens (operator, investor, customer, contrarian). The panel debates the options; you read the positions and decide. Useful for high-stakes, low-reversibility choices where you want to stress-test your thinking before committing.

### Using `decision-frameworks`

Name the framework or describe the decision type. BOB applies the structure and walks you through it:

| Framework | Best for |
|-----------|---------|
| Expected value | Decisions where you can quantify outcomes and probabilities |
| Regret minimisation | Long-range, identity-level choices |
| Pre-mortem | Before committing — surface failure modes in advance |

After running either skill, log the decision in a decision-log entity. Include the framework used and the key trade-offs. Future-you will thank you.

---

## 13.3 Market and competitive analysis

| Skill | What it produces |
|-------|-----------------|
| `market-sizing-analysis` | TAM, SAM, SOM — using top-down, bottom-up, and value-theory methods |
| `competitive-battlecard` | Sales-ready one-pager: positioning vs. a named competitor, win themes, trap questions, talk tracks |
| `research-company` | Full company intelligence report: competitive positioning, industry signals, USP analysis, AI/automation angles |
| `deep-research` | Multi-source research report with citations — OpenAI, DeepSeek, or Perplexity back-end |

`market-sizing-analysis` and `research-company` are your starting points for a new market or a new competitive threat. Use `competitive-battlecard` when your sales team needs a quick-reference tool for a specific competitor. Use `deep-research` when you need cited, multi-source analysis — it requires an API key.

### Research workflow

| Step | What you do | What BOB does | Where it's saved |
|------|-------------|---------------|-----------------|
| 1. Define the question | State the market, competitor, or topic | Clarifies scope; confirms source method | — |
| 2. Run the analysis | Approve the scope | Researches, structures, and writes the report | Vault — `{resource.root}` |
| 3. Link findings | Tag the note as a strategy input | — | — |
| 4. Decide | Use the output in `ask-boardroom` or `decision-frameworks` | — | Decision-log entity |

---

## 13.4 Planning rhythms

BOB supports structured annual and quarterly planning through two skills and one recurring playbook suite.

### OKRs

`okr-frameworks` writes OKRs, aligns team goals, and creates a measurement framework for quarterly tracking. Give it your priorities for the period and it returns draft Objectives with Key Results, scored for specificity and measurability. Edit them before finalising — the draft is a starting point, not a mandate.

`kpi-dashboard-design` designs the dashboard that tracks those KPIs. It selects metrics, defines thresholds, and specifies the visualisation layout. The output is a design brief; `operating-dashboard` then builds the canvas.

### Annual and quarterly planning

The `plan-to-perform` value chain maps the full planning cycle:

| Stage | Skills / playbooks |
|-------|--------------------|
| Assess current state | `business-baseline`, `owner-priority-system`, `market-sizing-analysis` |
| Strategise | `strategy-frameworks`, `growth-engine`, `growth-scaling-playbook` |
| Plan | `okr-frameworks` + [[Plan my next 12 months]] playbook |
| Budget | `startup-financial-modeling` |
| Execute | `ship-decisions`, `delegation` |
| Review | `business-pulse`, `weekly-review`, `vault-maturity-score` |

For a quarterly reset, run the [[Quarterly Replan]] playbook. It chains assessment, OKR review, and replanning into a single guided workflow.

### `strategy-frameworks`

When a decision requires a formal strategic canvas — where-to-play/how-to-win, beachhead market selection, crossing-the-chasm positioning — use `strategy-frameworks`. It applies the chosen framework and produces a written analysis. Outputs link to the relevant strategy note.

---

## 13.5 Management reporting

Management reporting connects strategy to daily numbers. Three skills serve different time horizons.

| Skill | Time horizon | What it produces |
|-------|-------------|-----------------|
| `business-pulse` | Weekly | A snapshot of the business: pipeline health, cash position, open issues, team capacity |
| `operating-dashboard` | Ongoing | A JSON Canvas file showing live business state across all modules |
| `kpi-dashboard-design` | Setup | The design spec for a KPI dashboard — run once, revisit quarterly |

### `business-pulse` workflow

| Step | What you do | What BOB does | Where it's saved |
|------|-------------|---------------|-----------------|
| 1. Trigger the pulse | Ask for the weekly business pulse | Reads the vault: pipeline, tasks, financials, open issues | — |
| 2. Review the output | Check the snapshot | — | Vault — `{company.management}` |
| 3. Act on flags | Follow up on red items | — | Task notes |

**Good practice:** run `business-pulse` on the same day each week. Consistent timing makes the outputs comparable over time.

### `operating-dashboard`

The dashboard is a canvas file generated from `business-baseline` source data. Refresh it after any significant change — a new client, a strategic pivot, a headcount change. It does not auto-update; you trigger the refresh.

---

## 13.6 How strategy links downward

A strategy note that doesn't connect to execution is decoration. BOB's data model is designed to close the gap.

| Strategy artifact | Links to |
|-------------------|---------|
| Strategy note | OKR notes, project notes, campaign briefs |
| Decision-log | Meeting note (where the decision was made), project note (if it changes scope) |
| OKR | Tasks in `{output.tasks}`, sprint plans |
| KPI | `operating-dashboard`, `business-pulse` output |

When you create a project or a campaign, link it to the strategy note that motivated it. When you close a decision, link the decision-log entry to the meeting where it was discussed. These links make the vault navigable — six months later you can trace why a project exists and what decision authorised it.

`ship-decisions` sits at the boundary between strategy and execution. Use it when a product or process change is ready to ship and you need a structured go/no-go: it applies reversibility analysis (one-way versus two-way doors) and surfaces the technical-debt trade-offs.

---

## 13.7 Skills serving this module

| Skill | Value chain stage |
|-------|------------------|
| `market-sizing-analysis` | assess |
| `business-baseline` | assess |
| `owner-priority-system` | assess |
| `strategy-frameworks` | strategise |
| `growth-engine` | strategise |
| `okr-frameworks` | plan |
| `startup-financial-modeling` | budget |
| `ship-decisions` | execute |
| `ask-boardroom` | cross-cutting (decide) |
| `decision-frameworks` | cross-cutting (decide) |
| `competitive-battlecard` | cross-cutting (market) |
| `research-company` | cross-cutting (market) |
| `deep-research` | cross-cutting (market) |
| `kpi-dashboard-design` | cross-cutting (reporting) |
| `operating-dashboard` | cross-cutting (reporting) |
| `business-pulse` | review |

**Playbooks:** [[Plan my next 12 months]], [[Quarterly Replan]], [[Business Owner Operating System]], [[Weekly Business Review]], [[Growth opportunity mapping]]

---

## 13.8 Good practices

- Log decisions in decision-log entities, not in meeting notes. Meeting notes scroll away; decision-log entries are searchable forever.
- Link strategy notes to the projects and campaigns they drive. Without links, strategy and execution live in separate silos.
- Run `ask-boardroom` before committing to a one-way-door decision. The cost is one prompt; the benefit is stress-tested reasoning on record.
- Refresh `operating-dashboard` after significant changes, not on a fixed schedule. A stale dashboard is worse than no dashboard — it creates false confidence.
- Keep OKRs short. Three objectives, three key results each. More than that and the quarter becomes unmanageable.

Previous: [[12-hr-people|12. HR & People]]
