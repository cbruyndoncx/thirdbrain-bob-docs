---
type: reference
title: Skill Packs
---

# Skill Packs

**Skill Packs** are themed collections of skills: one **Core Pack** of general skills and one pack per department (marketing, business, enterprise, sales, media, operations, PMBOK, process, engineering). The full vault already contains every pack. The starter vault is the minimal workspace: it holds only the skills that operate the vault and reaches every other skill over the skills MCP server, or offline by unpacking a pack's ZIP into it.

Each pack ZIP is self-contained: it carries the skills its members depend on, so one pack works on its own in a starter vault. A skill's **Free** or **Pro** label is its catalogue edition — Pro means specialised, harder to install, enterprise-grade — and both editions of a department ship in the same pack.

**How to activate a pack:** Open **Settings > Skills Manager**, search or browse by category, and use **bulk enable** on the skills you want. Each pack below lists its skills for easy filtering.

**How to deactivate:** Same process — bulk disable skills you're not using. Disabled skills stay installed but invisible to AI agents and the `/` menu.

---

<!-- The GENERATED regions below are rewritten by vault-release/scripts/generate_skill_packs.py from each skill's `pricing-tier`. Edit the prose outside them; a pack's description is the `descriptor` in its product note. A pack's own tips go directly under its `PACK` region, as a bold label and bullets (never a `##` heading); they appear in that pack's section on the docs site. Keep counts and versions out of them. -->

## Core Pack

<!-- BEGIN GENERATED: STARTER SET -->
The **Core Pack** (`pack-core`, 202 skills, `pricing-tier: starter`) holds the general skills. The full vault installs them; the minimal starter vault does not, and reaches them through this pack or the skills MCP server. It covers:

| Category | Skills |
|----------|--------|
| utilities | 29 |
| product-management | 28 |
| documents | 21 |
| obsidian | 21 |
| productivity | 20 |
| sales | 19 |
| content | 11 |
| human-resources | 10 |
| diagramming | 9 |
| research | 7 |
| operations | 5 |
| qms | 4 |
| business | 3 |
| integrations | 3 |
| video | 3 |
| development | 2 |
| marketing-analytics | 2 |
| marketing-content | 2 |
| finance | 1 |
| images | 1 |
| marketing-seo | 1 |
<!-- END GENERATED: STARTER SET -->

<!-- BEGIN GENERATED: PACKS -->
---

## Department Packs
<!-- END GENERATED: PACKS -->

Each department pack below is one self-contained ZIP: its Free and Pro skills together, plus the
skills they depend on.

<!-- BEGIN GENERATED: PACK pack-business -->
### Business Pack

Business operations, reporting and advisory skills, plus executive coaching and owner productivity

`pack-business` — 31 skills: 27 Free (`pricing-tier: pack-business-free`), 4 Pro (`pricing-tier: pack-business-pro`)

- `ai-budget-review` — Free
- `ai-session-ledger` — Free
- `ai-transformation` — Free
- `ai-work-audit` — Free
- `ask-boardroom` — Free
- `ask-zeus` — Free
- `bob-ai-audit` — Free
- `business-baseline` — Free
- `business-pulse` — Free
- `business-reporting` — Free
- `buyback-rate` — Pro
- `catalog-csv-ingest` — Free
- `catalog-reply` — Free
- `client-health-tracker` — Free
- `client-offboarding` — Free
- `coaching-discovery` — Pro
- `customer-pulse` — Free
- `drafting-data-privacy-docs` — Free
- `executive-advisory` — Pro
- `idea-validator` — Free
- `operating-dashboard` — Free
- `order-to-pay` — Free
- `owner-priority-system` — Pro
- `process-kaizen` — Free
- `purchase-order` — Free
- `purchase-requisition` — Free
- `roi-calculator` — Free
- `supplier-feedback` — Free
- `survey-feedback-pipeline` — Free
- `testimonial-collector` — Free
- `time-tracking-reporter` — Free

Bundled runtime dependencies (13): `bob-workspace-compose`, `branded-pdf`, `coa-account`, `context-pack`, `fetch-google-sheet`, `journal-entry-poster`, `json-canvas`, `model-cost-benchmark`, `pdf-report`, `personal-backlog`, `tasknotes`, `user-feedback-system`, `vault-preflight`
<!-- END GENERATED: PACK pack-business -->

**Tips & gotchas**

- **Bring real context to `ask-boardroom` and `ask-zeus`.** Both skills run strategic sessions against your vault. A live decision — with actual numbers, actual constraints — produces sharp output. A vague hypothetical produces generic advice.
- **Don't run `business-reporting` on a thin data set.** If you have few invoices and no time logs, the reports reflect that. Run `time-tracking-reporter` for at least two weeks before generating a cohort analysis or QBR — the report is only as good as what's behind it.
- **Brief coaching clients before using `coaching-discovery`.** It is built around ICF methodology; if your clients aren't expecting a coaching frame, using it in a consulting context without that setup can feel abrupt.
- **Give the advisory skills specifics.** They produce sharper output when you give them actual numbers, real constraints and named decisions. Generic inputs produce generic output — the skill can only work with what you bring.

<!-- BEGIN GENERATED: PACK pack-engineering -->
### Engineering Pack

Engineering consultancy — FIDIC contract analysis, EOT claims, variation orders, delay analysis

`pack-engineering` — 6 skills: 6 Pro (`pricing-tier: pack-engineering-pro`)

- `boq-audit` — Pro
- `contract-clause-analyzer` — Pro
- `contractor-claims-response` — Pro
- `delay-analysis-tool` — Pro
- `eot-claims-preparer` — Pro
- `variation-order-analyzer` — Pro

Bundled runtime dependencies (3): `context-pack`, `personal-backlog`, `tasknotes`
<!-- END GENERATED: PACK pack-engineering -->

**Tips & gotchas**

- **Gather the baseline before `delay-analysis-tool`.** It uses Critical Path Method and requires a baseline programme and a delay event log as input. The more structured your input, the more defensible the Time Impact Analysis output.
- **Run `contract-clause-analyzer` before `eot-claims-preparer`.** Don't generate a claim without first analysing the relevant clauses: the claim structure depends on the specific FIDIC edition and any bespoke amendments in the contract.

<!-- BEGIN GENERATED: PACK pack-enterprise -->
### Enterprise Pack

HR, finance, compliance, accounts review and enterprise operations skills

`pack-enterprise` — 37 skills: 28 Free (`pricing-tier: pack-enterprise-free`), 9 Pro (`pricing-tier: pack-enterprise-pro`)

- `ar-followup` — Free
- `audit-findings-tracker` — Free
- `bank-reconciliation` — Free
- `be-accounts-review` — Pro
- `coa-account` — Free
- `collections-escalation` — Pro
- `ct-return-preparer` — Free
- `ecl-calculator` — Free
- `employee-onboarding` — Free
- `employment-contract-templates` — Free
- `eu-accounts-review` — Pro
- `financial-decision-cadence` — Pro
- `financial-reporting` — Pro
- `financial-statement-generator` — Free
- `fixed-asset-register` — Free
- `food-label-compliance` — Pro
- `fs-notes-generator` — Free
- `fx-revaluation` — Free
- `gratuity-calculator` — Free
- `hiring` — Free
- `hr-ops` — Free
- `ifs-internal-audit` — Pro
- `invoice-collector` — Pro
- `invoice-description` — Free
- `lease-register` — Free
- `nl-accounts-review` — Pro
- `one-on-ones` — Free
- `owner-value-view` — Free
- `period-close-orchestrator` — Free
- `prepare-application` — Free
- `revenue-recognition-tracker` — Free
- `review-job` — Free
- `skill-gap-learning-path` — Free
- `tax-season-organizer` — Free
- `trial-balance-generator` — Free
- `vat-return-preparer` — Free
- `wps-sif-generator` — Free

Bundled runtime dependencies (9): `branded-pdf`, `context-pack`, `corporate-pdf`, `journal-entry-poster`, `pdf-report`, `performance-framework`, `performance-review`, `personal-backlog`, `tasknotes`
<!-- END GENERATED: PACK pack-enterprise -->

**Tips & gotchas**

- **Run `period-close-orchestrator` before individual close sub-skills.** It sequences everything in the right order and gates the hard close on completion. Running `trial-balance-generator` or `financial-statement-generator` before the period is properly closed produces numbers that don't hold up.
- **`employment-contract-templates` output is a first draft, not a signed document.** It produces a solid starting point — have your legal advisor or HR partner review before issuing any contract to an employee. Jurisdiction-specific clauses in particular need a human check.
- **Pair `invoice-collector` with `collections-escalation` as a monthly routine.** Collect first, then immediately run escalation on anything overdue. Run in sequence, they replace a full AR admin cycle.
- **Give `eu-accounts-review` every entity in a group.** Running it on a group structure without the subsidiary accounts for all entities listed produces a partial analysis; missing one entity skews the consolidation picture.

<!-- BEGIN GENERATED: PACK pack-marketing -->
### Marketing Pack

Full marketing toolkit — strategy, content, SEO audits, ads, analytics, conversion, plus advanced SEO publishing and automation

`pack-marketing` — 58 skills: 50 Free (`pricing-tier: pack-marketing-free`), 8 Pro (`pricing-tier: pack-marketing-seo-pro`)

- `ab-test-setup` — Free
- `ad-creative` — Free
- `analytics-tracking` — Free
- `app-store-optimization` — Free
- `blotato` — Free
- `blotato-publisher` — Pro
- `cold-outreach` — Free
- `commentary-video` — Free
- `competitor-alternatives` — Free
- `content-destinations` — Free
- `content-repurposer` — Free
- `content-scorer` — Pro
- `content-strategy` — Free
- `copy-editing` — Free
- `copywriting` — Free
- `course-builder` — Free
- `cro` — Free
- `customer-persona-panels` — Free
- `email-sequence` — Free
- `free-tool-strategy` — Free
- `ga4-analytics` — Free
- `geo-audit` — Free
- `google-ads-scripts` — Free
- `gtm-tagging` — Free
- `icp-discovery` — Free
- `influencer-outreach` — Free
- `launch-execution` — Free
- `launch-strategy` — Free
- `lead-magnet-generator` — Free
- `local-outreach` — Free
- `market-sizing-analysis` — Free
- `marketing-ideas` — Free
- `marketing-psychology` — Free
- `marketing-report` — Free
- `messaging-coherence` — Free
- `meta-ads` — Free
- `metalsmith-publisher` — Pro
- `onboarding-cro` — Free
- `paid-ads` — Free
- `paywall-upgrade-cro` — Free
- `positioning-craft` — Free
- `premium-design` — Free
- `pricing-strategy` — Free
- `product-marketing-context` — Free
- `product-page-audit` — Free
- `profile-cms` — Free
- `programmatic-seo` — Pro
- `referral-program` — Free
- `schema-markup` — Pro
- `seo-audit` — Free
- `seo-content-machine` — Pro
- `social-content` — Free
- `social-listening` — Free
- `social-media-audit` — Free
- `webinar-strategy` — Free
- `website-audit` — Free
- `wordpress-publisher` — Pro
- `wordpress-theme-builder` — Pro

Bundled runtime dependencies (10): `brand-system`, `branded-pdf`, `context-pack`, `corporate-pdf`, `linkedin-engager-leads`, `pdf-report`, `personal-backlog`, `social-notes`, `social-publisher`, `tasknotes`
<!-- END GENERATED: PACK pack-marketing -->

**Tips & gotchas**

- **Start with `icp-discovery` before any campaign work.** The other skills produce sharper outputs when they know exactly who you're targeting. Vague personas produce vague copy.
- **Don't run `geo-audit` on a brand-new domain.** It checks how AI engines cite your client — a site with no content or backlinks will score zero and mislead you. Run it after at least three months of published content.
- **Run `seo-content-machine` with a clear target keyword and competitor URL.** The pipeline uses that input to shape structure, headings, and internal links. Vague inputs produce generic output that won't rank.
- **Add `schema-markup` as the last step, not the first.** Schema applied before the page content is finalized often mismatches the actual page structure. Run it after the post is live and the content is settled.

<!-- BEGIN GENERATED: PACK pack-media -->
### Media Pack

Video generation, image creation, and media processing

`pack-media` — 9 skills: 9 Free (`pricing-tier: pack-media-free`)

- `ai-image-gen` — Free
- `ai-video-gen` — Free
- `avatar-video` — Free
- `explainer-video-guide` — Free
- `hyperframes-studio` — Free
- `marketing-video-guide` — Free
- `process-video` — Free
- `remotion-reference-pack` — Free
- `veo-video-gen` — Free

Bundled runtime dependencies (4): `context-pack`, `personal-backlog`, `social-notes`, `tasknotes`
<!-- END GENERATED: PACK pack-media -->

**Tips & gotchas**

- **`ai-video-gen` needs an active inference.sh account.** Set your API key in vault config before your first run, or use `veo-video-gen` (Gemini API) as a dependency-free alternative.
- **Don't skip the scripting step.** Generating a video without a clear brief produces generic output. Use `marketing-video-guide` first to structure your concept, then pass its output to the generation skill.

<!-- BEGIN GENERATED: PACK pack-operations -->
### Operations Pack

Manufacturing, supply chain, procurement, and logistics

`pack-operations` — 12 skills: 12 Pro (`pricing-tier: pack-operations-pro`)

- `bill-of-materials` — Pro
- `delivery-confirmation` — Pro
- `demand-forecasting` — Pro
- `demand-signal-analysis` — Pro
- `erp-reference` — Pro
- `integration-reference` — Pro
- `order-management` — Pro
- `packaging-logistics` — Pro
- `production-planning` — Pro
- `production-scheduling` — Pro
- `quality-control` — Pro
- `strategic-sourcing` — Pro

Bundled runtime dependencies (3): `context-pack`, `personal-backlog`, `tasknotes`
<!-- END GENERATED: PACK pack-operations -->

**Tips & gotchas**

- **`erp-reference` is a lookup skill, not a workflow.** Use it to pull field mappings and CSV formats when connecting client data to Odoo or ERPNext, not as a starting point for a client session.
- **Use real client data.** These skills need it to produce useful output. Don't demo them with made-up numbers — results that look precise but aren't grounded will erode trust fast.

<!-- BEGIN GENERATED: PACK pack-pmbok -->
### PMBOK Pack

Full PMBOK 7/8 project management framework

`pack-pmbok` — 14 skills: 14 Pro (`pricing-tier: pack-pmbok-pro`)

- `project-change-control` — Pro
- `project-charter` — Pro
- `project-closure` — Pro
- `project-context` — Pro
- `project-evm` — Pro
- `project-procurement` — Pro
- `project-quality` — Pro
- `project-raci` — Pro
- `project-resource` — Pro
- `project-risk` — Pro
- `project-schedule` — Pro
- `project-stakeholder` — Pro
- `project-status` — Pro
- `project-wbs` — Pro

Bundled runtime dependencies (3): `context-pack`, `personal-backlog`, `tasknotes`
<!-- END GENERATED: PACK pack-pmbok -->

**Tips & gotchas**

- **Start each engagement with `project-context`** to set PMBOK 7 tailoring decisions. It shapes how every downstream skill behaves — skipping it means generic output instead of delivery-approach-specific artefacts.
- **Don't run `project-status` before the charter, WBS and risk register exist.** The skill aggregates from those artefacts; run it on an empty project and you get a skeleton, not a report.

<!-- BEGIN GENERATED: PACK pack-process -->
### Process Pack

Governed business-process orchestration — Process Harness runner, policy gates, and the order-to-cash / procure-to-pay case skills

`pack-process` — 8 skills: 8 Pro (`pricing-tier: pack-process-pro`)

- `process-harness` — Pro
- `process-harness-capture-order` — Pro
- `process-harness-credit-check` — Pro
- `process-harness-invoice-issue` — Pro
- `process-harness-invoice-match` — Pro
- `process-harness-invoice-status` — Pro
- `process-harness-payment-prep` — Pro
- `process-harness-supplier-invoice` — Pro

Bundled runtime dependencies (3): `context-pack`, `personal-backlog`, `tasknotes`
<!-- END GENERATED: PACK pack-process -->

**Tips & gotchas**

- **These skills are driven by the Process Harness runner (CLI or cron), not by conversation.** Saying "start a case" in chat does not begin one — the harness starts it, hands each activity a contained context pack, and records the result. That constraint is the product: steps cannot be reordered or skipped by asking nicely.
- **Gates need real approvers.** A gate that nobody is accountable for is a gate that always opens, and the event log will faithfully record that it did.
- **Do not demo this on invented data.** The value is that the trail is true; a fabricated trail teaches the opposite lesson.

<!-- BEGIN GENERATED: PACK pack-sales -->
### Sales Pack

Pipeline management, prospect research, qualification, and outbound

`pack-sales` — 16 skills: 16 Free (`pricing-tier: pack-sales-free`)

- `client-ascension` — Free
- `consultative-selling` — Free
- `decision-maker-mapper` — Free
- `demo-script` — Free
- `guarantee-designer` — Free
- `lead-qualifier` — Free
- `money-model-builder` — Free
- `objection-playbook` — Free
- `offer-builder` — Free
- `prospect-audit` — Free
- `sales-closer` — Free
- `sales-enablement` — Free
- `sales-forecast` — Free
- `sales-metrics-dashboard` — Free
- `sales-pipeline-report` — Free
- `warm-network-activation` — Free

Bundled runtime dependencies (6): `branded-pdf`, `context-pack`, `linkedin-engager-leads`, `pdf-report`, `personal-backlog`, `tasknotes`
<!-- END GENERATED: PACK pack-sales -->

**Tips & gotchas**

- **Use `consultative-selling` before a discovery call, not during it.** The skill covers SPIN, Challenger, MEDDIC, MEDDPICC, and others — pick the right methodology for the deal size and buyer type, prep your questions, then run the call. Choosing on the fly means defaulting to habit.
- **Run `lead-qualifier` before writing outreach or demo scripts.** Unqualified contacts waste your sequences and erode sender reputation. Qualify first — BANT and MEDDIC take minutes — then route good-fit accounts to `demo-script` or `sales-closer`.

---

## Quick Reference

<!-- BEGIN GENERATED: QUICK REFERENCE -->
| Pack | Skills | Free | Pro | Bundled | Skills in ZIP |
|------|--------|------|-----|---------|---------------|
| Business Pack | 31 | 27 | 4 | 13 | 44 |
| Engineering Pack | 6 | 0 | 6 | 3 | 9 |
| Enterprise Pack | 37 | 28 | 9 | 9 | 46 |
| Marketing Pack | 58 | 50 | 8 | 10 | 68 |
| Media Pack | 9 | 9 | 0 | 4 | 13 |
| Operations Pack | 12 | 0 | 12 | 3 | 15 |
| PMBOK Pack | 14 | 0 | 14 | 3 | 17 |
| Process Pack | 8 | 0 | 8 | 3 | 11 |
| Sales Pack | 16 | 16 | 0 | 6 | 22 |
| **Total department skills** | **191** | | | | |

Combined with the 202-skill Core Pack, the full library contains **393 skills**.
<!-- END GENERATED: QUICK REFERENCE -->

---

## Release bundles

Hand-authored, and deliberately outside the generated block above: this is a *release*
constraint, not a pack. `generate_skill_packs.py` renders pack membership from each skill's
`pricing-tier`, and no `pricing-tier` value can express "these skills must ship together" —
the bundle below spans three packs.

### Finance cycle (17 skills)

These 17 skills form a single closed cross-reference cycle: each one's `SKILL.md` links to
others in the set, `journal-entry-poster` alone carries 57 inbound wikilinks from within it.
The cycle is documentation, not code — nothing imports anything at runtime, and nothing fails
today because of it — so the cycle is accepted rather than broken (system review 2026-09-06,
decision D5, option A). What follows from accepting it is the rule below.

**Release rule: ship all 17, or none of them.** Releasing a subset produces a package whose
skills reference sibling skills the recipient does not have. Fifteen sit in
`pack-enterprise-free` (the Enterprise Pack), `order-to-pay` sits in `pack-business-free` (the
Business Pack), and `journal-entry-poster` sits in `starter` (re-tiered 2026-09-20; the Core Pack).
The cycle is documentation, not a runtime dependency, so the pack closure does not bundle it:
the Enterprise Pack ZIP carries 16 of the 17 (`journal-entry-poster` is bundled as a runtime
dependency, `order-to-pay` is not), and the Business Pack carries 2. Check this list before
cutting a release that includes any member.

| Skill | pricing-tier |
|---|---|
| `ar-followup` | pack-enterprise-free |
| `bank-reconciliation` | pack-enterprise-free |
| `ct-return-preparer` | pack-enterprise-free |
| `ecl-calculator` | pack-enterprise-free |
| `financial-statement-generator` | pack-enterprise-free |
| `fixed-asset-register` | pack-enterprise-free |
| `fs-notes-generator` | pack-enterprise-free |
| `fx-revaluation` | pack-enterprise-free |
| `gratuity-calculator` | pack-enterprise-free |
| `journal-entry-poster` | starter |
| `lease-register` | pack-enterprise-free |
| `order-to-pay` | pack-business-free |
| `period-close-orchestrator` | pack-enterprise-free |
| `revenue-recognition-tracker` | pack-enterprise-free |
| `trial-balance-generator` | pack-enterprise-free |
| `vat-return-preparer` | pack-enterprise-free |
| `wps-sif-generator` | pack-enterprise-free |


---

## Tips

- **Start small.** Enable one pack at a time. Get comfortable with those skills before adding more.
- **Use search.** The Skills Manager search bar filters by name and description — faster than scrolling.
- **Check the `/` menu.** After enabling a pack, type `/` to see your new slash commands.
- **Disable what you don't use.** Fewer active skills = less noise in conversations and faster agent responses.
