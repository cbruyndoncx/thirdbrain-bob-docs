---
description: Map, diagnose, and optimize business operations through progressive visual analysis.
title: business-baseline
---

# business-baseline

Map, diagnose, and optimize business operations through progressive visual analysis.

- **Area:** Strategy
- **Category:** business
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Operations Manager

Maps and diagnoses business operations with Business Maps, Bow-Tie Funnels, and Process Swimlanes.

## How you ask

- “Run a business baseline on my operations" · "Map my business and identify bottlenecks" · "Create a bow-tie funnel for my SaaS product" · "Give me an Excalidraw swimlane I can drag around”

## Inputs

- kpi-registry — Canonical KPI definitions and thresholds.
- process-definitions — Documented processes — the maps being diagnosed.
- client-kpi-registry — Client KPI registry when scoped to a client.
- client-id — Client folder name under {company.clients}/
- business-type — Business archetype for inference patterns (auto-detected if omitted) (agency | coach | course-creator | creator | ecommerce | enterprise-b2b | franchise | local | manufacturing | multi-channel-retail | nonprofit | real-estate | saas | service-provider | technical-services)
- profile — Company or client profile — identity and stage.
- icp — ICP — target customer the strategy is for.
- offerings — Offerings catalogue — what is being strategised.
- marketing-context — Positioning, narrative, and competitive frame.
- process — Process name to expand (e.g. 'Lead Gen', 'Onboarding', 'Fulfillment')
- process-note — Path to the `type: process` source note (client or company scope)
- orientation — Layout direction (default horizontal, unchanged behavior). horizontal = lanes are rows, steps flow left→right. vertical = lanes are columns with a top label, steps flow top→bottom — use for LONG processes (e.g. 16 steps) that run off the right edge horizontally; the canvas gets tall (expected). Two-way arrow binding holds identically in both. Vertical writes a distinct {process-id}-swimlane-vertical.excalidraw.md so it never clobbers the horizontal diagram. (horizontal | vertical)
- no-archive — Skip archiving an existing diagram before regeneration (default false — archive first)
- no-bands — Suppress stage bands (default false). When steps carry a `stage:` field and orientation is vertical, consecutive same-stage steps are grouped into labelled full-width bands behind the lanes; --no-bands renders the plain sequence. Bands are vertical-only — horizontal ignores stage regardless.
- business-type — One of the 15 archetype slugs (auto-detected from baseline if a session exists) (agency | coach | course-creator | creator | ecommerce | enterprise-b2b | franchise | local | manufacturing | multi-channel-retail | nonprofit | real-estate | saas | service-provider | technical-services)
- scope — 'company' (default — this vault's own business) or a client-id for a client-scoped registry
- chain-matrix — Archetype × value-chain applicability — pre-fills the Step 2 relevance cuts and asserts every `core` chain carries a KPI. A chain marked `—` must not receive one.
- chains — One or more journey value-chain ids to score, e.g. `service-to-renew`, `deliver-to-satisfaction`. The two meta-chains (infrastructure, operating-controls) have no journey stages and cannot be scored.
- business-type — Archetype packs supplying the stage→evidence mapping; repeatable. Chains the archetype does not operate score ⚪ not-applicable instead of 🔴. Stages with no row in the selected packs fall back to the packs of archetypes that DO run that chain, named in the report. (agency | coach | course-creator | creator | ecommerce | enterprise-b2b | franchise | local | manufacturing | multi-channel-retail | nonprofit | real-estate | saas | service-provider | technical-services)
- kpi-packs — Archetype KPI packs — the `Computed from` column is the stated stage→evidence-entity mapping this route reads.
- chain-matrix — Archetype × value-chain applicability. Separates ⚪ *not applicable — this archetype does not run the chain* from ⚪ *applicable but no KPI declares an evidence source*, and bounds the cross-archetype fallback. Read whenever `business-type` is supplied.
- answers — The owner's answers to the five intake questions (see workflows/sme_instant_audit.md). Free text — capture their words, do not reformat into jargon.
- business-type — Archetype used to pick which failure patterns to test against; skip if unknown rather than guessing. (agency | coach | course-creator | creator | ecommerce | enterprise-b2b | franchise | local | manufacturing | multi-channel-retail | nonprofit | real-estate | saas | service-provider | technical-services)

## Outputs

- Each swimlane migrated into a structured `type: process` note — the source of truth (drawio-only baselines liberated into queryable data)
- Excalidraw swimlane rendered from the process note — derived view, not the source of truth; prior version archived to diagrams/_archive/. Horizontal and vertical are separate files that can coexist for the same process.
- Human-readable interview notes, insights, decisions and quotes written by the progressive interview
- One A4 page — 3 broken / 3 fixes / 1 highest-leverage move, in the owner's own vocabulary. Saved in the prospect's existing lead folder; when no lead folder exists the page is returned in the conversation and no folder is created
- Optional swimlane render of the process note
- Optional visual export rendered from the process notes — not the source of truth
- Per-stage verdict table with the evidence each verdict rests on, plus the vault-visible-only caveat
- Registry with domain tables + Value-Chain Mapping section, same contract as the company registry (parsed by list_value_chains.py and consumed by owner-priority-system kpi_refresh.py/kpi_verify.py)
- Source-of-truth process note with steps[], owners, state, and opportunity flags
- Structured `type: process` note(s) — the source of truth (steps, owners, state, flags)
- continued_baseline (drawio)
- roadmap_page (drawio-page)
- scan_summary (markdown)
- session_state (yaml)
- {client.business-baseline.processes}/{process-id}.md
- {client.business-baseline}/business_baseline_summary.md
- {client.business-baseline}/diagrams/{client-id}-business-baseline.drawio
- {client.business-baseline}/diagrams/{client-id}-business-baseline.drawio (Action Roadmap page)
- {client.business-baseline}/diagrams/{client-id}-business-baseline.drawio (new page)
- {client.business-baseline}/diagrams/{process-id}-swimlane.excalidraw.md (client scope, horizontal) or {company.processes}/diagrams/{process-id}-swimlane.excalidraw.md (company scope, horizontal); vertical orientation appends -vertical before the extension ({process-id}-swimlane-vertical.excalidraw.md)
- {client.business-baseline}/session-notes.md
- {client.business-baseline}/session-state.yaml
- {company.management}/KPI-REGISTRY.md (company scope) or {client.business-baseline}/kpi-registry.md (client scope)
- {company.reports}/capability-rag/axis2_{YYYY-MM-DD}.md
- {lead.root}/instant-audit-{YYYY-MM-DD}.md

## Seen in these workflows

- [Map Your Business in 30 Minutes](../../workflows/strategy/business-baseline.md)

