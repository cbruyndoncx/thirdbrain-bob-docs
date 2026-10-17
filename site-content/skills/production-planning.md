---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: production-planning — ThirdBrain BOB skill
  description: Analyze manufacturing operations data from Odoo MRP or ERPNext Manufacturing. Generates reports on production order status, work center capacity and OEE, BOM st
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: production-planning
catLabel: operations
area: operations
desc: Analyze manufacturing orders, BOM structures, work center capacity, OEE metrics, and scrap rates.
summary: Analyze manufacturing operations data from Odoo MRP or ERPNext Manufacturing. Generates reports on production order status, work center capacity and OEE, BOM structure and cost, production scheduling, and scrap/waste trends.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- data_source — CSV path, inline data, or 'mcp' for live query
- 'date_range — Reporting period (default: last 30 days)'
- offerings — Offerings catalogue — what we produce; anchors product-level commentary.
- bom_reference — Specific BOM reference to analyze (omit for all active BOMs)
- 'horizon — Scheduling horizon (default: 2 weeks)'
- 'date_range — Reporting period (default: last 90 days)'
outputs:
- BOM tree, cost rollup, single-source flags
- Gantt-style schedule with critical path
- MO pipeline report with state breakdown and completion rates
- Scrap rates with trends by product, work center, and period
- Utilization and OEE per work center with bottleneck flags
- '{client.deliverables.production}/bom_analysis.md'
- '{client.deliverables.production}/capacity_report.md'
- '{client.deliverables.production}/mo_status_report.md'
- '{client.deliverables.production}/production_schedule.md'
- '{client.deliverables.production}/scrap_analysis.md'
prompts:
- Show me the status of all manufacturing orders for Bobbolt over the last 30 days
- Which work centers are bottlenecks right now? Give me the capacity and OEE breakdown
- Explode the BOM for product SKU-4200 and flag any single-source components
- Build a two-week production schedule from the open manufacturing orders
- What are our scrap rates by work center for the last quarter, and where is waste trending up?
---
