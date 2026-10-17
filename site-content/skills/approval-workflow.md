---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: approval-workflow — ThirdBrain BOB skill
  description: USE WHEN user says "approval workflow", "run approval-workflow", or requests similar functionality. Define quality gates and sign-off requirements for AI-assist
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: approval-workflow
catLabel: qms
area: operations
desc: Defines approval checklists in Obsidian, sets review stages, and configures sign-off gates before work is delivered.
summary: USE WHEN user says "approval workflow", "run approval-workflow", or requests similar functionality. Define quality gates and sign-off requirements for AI-assisted work before external delivery.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- artifact_type — What the deliverable is — proposal, blog post, client email, contract. Drives the tier lookup in the approval matrix.
- artifact_link — Wikilink, path, or URL the approver opens to review the item. The approval request is not sendable without it.
- audience — Who the artifact reaches once released. Widening the audience raises the tier and hardens the release gate. (internal | external | public)
- due_date — Date the approval is needed by. Compared against the tier SLA to decide whether the request is already at risk of escalation.
- approver — Named person who gives the go/no-go. A role title is not sufficient — the approval record has to name a person.
- request — The sign-off being asked for and any constraints already known, such as a fixed send date.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- work_type — The recurring category the policy governs — blog posts, client proposals, routine client emails. One policy, one category.
- risk_profile — Standing risk assessment for the category across audience, reversibility, stakes, and frequency. Sets the default tier band. (low | medium | high)
- standard_approvers — Primary and backup approvers who hold sign-off for this category by default, so each instance does not need a fresh decision.
- escalation_owner — Who the request moves to when the standard approver is unavailable or the SLA is breached.
- request — The policy being asked for, including any existing practice it has to replace or formalise.
- work_type — The release under multi-party review — contract, public statement, cross-functional campaign. Determines which groups have standing.
- required_approver_groups — The groups that must each sign off — legal, finance, leadership, client. Release is blocked until every listed group has an explicit decision.
- approval_mode — Whether each group reviews in turn or all at once. Sequential protects a dependency between reviews; parallel trades that for elapsed time. (sequential | parallel)
- blocking_conditions — The conditions that make the release a no-go regardless of who else approved, so a blocker cannot be overridden by a later approval.
- request — The release to be approved and any fixed deadline the approval order has to fit inside.
outputs:
- Approval package for the one artifact — selected tier with its risk justification, approver and backup, the request and response formats, the frontmatter fields to record, and the release gate.
- Multi-party approval plan — approval order, per-group decision checkpoints and review focus, no-go conditions, the combined release gate, and the escalation path for each group.
- Standing policy for the work type — default tier, standard and backup approvers, SLA, the approved/rejected/pending definitions, the reusable checklist, the `approval_status` frontmatter fields, and the escalation path.
- '{scope.qms.root}/approval-workflow-{YYYY-MM-DD}.md'
prompts:
- Set up quality gates for our deliverable review process
- Create an approval checklist for client deliverables
- Configure review stages and sign-off requirements
- Define escalation criteria for our QA workflow
---
