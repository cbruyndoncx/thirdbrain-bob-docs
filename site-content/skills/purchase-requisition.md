---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: purchase-requisition — ThirdBrain BOB skill
  description: 'Create, review, and track purchase requisitions — the first step in the procure-to-pay lifecycle. A PR captures what is needed, why, how much it costs, and who '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: purchase-requisition
catLabel: operations
area: operations
desc: Creates and manages purchase requisitions — the formal request to buy goods or services.
summary: Create, review, and track purchase requisitions — the first step in the procure-to-pay lifecycle. A PR captures what is needed, why, how much it costs, and who needs to approve it before a purchase order is created.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- source (create) — Purchase need description and estimated cost
- source (review) — PR ID and approval decision
- source (dashboard) — Dashboard request with optional filters
- all — loaded from your vault context
- profile — loaded from your vault context
outputs:
- pr-dashboard (markdown)
- purchase-requisition (markdown)
- reviewed-pr (markdown)
- '{scope.finance.ap-requisitions}/PR-{YYYY}-{NNN}.md'
- '{scope.finance.ap-requisitions}/{pr-id}.md'
- '{scope.finance.ap}/pr_dashboard_{YYYY-MM-DD}.md'
prompts:
- I need to purchase a project management tool for the team, about $500 per year
- Review and approve PR-2026-014 for the new office supplies order
- Show me a dashboard of all open purchase requisitions and flag anything older than a week
- Create a purchase request for consulting services from Acme Corp, estimated at $12,000
---
