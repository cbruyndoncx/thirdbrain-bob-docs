---
title: "Playbooks Demo — See It in Action"
type: knowledge-base
status: final
created: 2026-03-18
modified: 2026-03-18
tags:
  - playbooks
  - demo
  - onboarding
---

# Playbooks Demo

> This walkthrough shows exactly what happens when you run a playbook — from first command to finished output. We'll use the **Lead Generation Activation** playbook as our example.

## Prerequisites

Before starting, you should have:

- A client workspace created (via `create-client` or manually)
- The client's website URL
- Basic knowledge of who the client sells to

If you're brand new to the vault, read [[playbooks]] first for the concepts.

---

## Step 1 — Start the Playbook

You say:

```
start playbook: Lead generation activation
```

The agent reads the playbook, loads all Required Context files, and creates a TaskNote:

```yaml
---
type: task
title: "Lead generation activation: Acme Corp"
status: in-progress
playbook: "[[Lead generation activation]]"
remaining-steps: 8
awaiting: ""
priority: high
assignee: [Agent]
---
```

---

## Step 2 — Agent Runs ICP Discovery (AGENT)

The agent invokes `icp-discovery` autonomously. It asks you a few targeted questions about the client's customers, then generates an ICP profile.

**What you see:**

> Step 1/8 complete — ICP Discovery
> - Created: `{company.clients}/acme/icp_profile.md`
> - Remaining: 7 steps
> - Next: social-media-audit (AGENT)

---

## Step 3 — Agent Runs Social Media Audit (AGENT)

The agent checks the client's social profiles, scores presence, and identifies gaps.

**What you see:**

> Step 2/8 complete — Social Media Audit
> - Created: `{company.clients}/acme/research/social_media_audit.md`
> - Remaining: 6 steps
> - Next: brand-voice-generator (AGENT)

---

## Step 4 — Agent Generates Brand Voice (AGENT)

The agent analyzes existing client content and extracts voice guidelines.

**What you see:**

> Step 3/8 complete — Brand Voice Generator
> - Created: `{company.clients}/acme/brand_voice_guide.md`
> - Remaining: 5 steps
> - Next: Review ICP, audit, voice (HUMAN)

---

## Step 5 — You Review and Adjust (HUMAN)

The agent **pauses** and presents everything so far:

> **Awaiting your input**
>
> I've completed 3 steps. Here's what I found:
>
> **ICP Profile:** B2B SaaS founders, 10-50 employees, €500K-€5M revenue, struggling with manual operations...
>
> **Social Audit:** LinkedIn is active but inconsistent. Instagram dormant. No YouTube presence. Facebook page exists but unused...
>
> **Brand Voice:** Authoritative but approachable. Avoids jargon. Emphasis on practical outcomes...
>
> **What I need from you:**
> 1. Does the ICP look right, or should I adjust the target?
> 2. Which channels should we prioritize?
> 3. Any voice adjustments?

The TaskNote updates:

```yaml
status: awaiting-input
awaiting: "Review ICP, social audit findings, and brand voice — confirm direction"
remaining-steps: 5
```

**You respond:**

> ICP is good. Focus on LinkedIn and email — skip Instagram for now. Voice is spot on.

---

## Step 6 — Agent Builds Content Strategy (AGENT)

With your confirmed direction, the agent runs `content-strategy` — builds topic clusters, maps content to the buyer journey, and creates a 4-week calendar.

**What you see:**

> Step 5/8 complete — Content Strategy
> - Created: `{company.clients}/acme/content_strategy.md`
> - Remaining: 3 steps
> - Next: social-content (AGENT)

---

## Step 7 — Agent Writes Social Posts (AGENT)

The agent writes LinkedIn posts from the content strategy, using the confirmed brand voice.

> Step 6/8 complete — Social Content
> - Created: `{company.clients}/acme/deliverables/social_posts.md`
> - Remaining: 2 steps
> - Next: email-sequence (AGENT)

---

## Step 8 — Agent Creates Email Sequences (AGENT)

Nurture sequence, welcome sequence, and lead capture emails — all segmented by ICP.

> Step 7/8 complete — Email Sequence
> - Created: `{company.clients}/acme/deliverables/email_sequences.md`
> - Remaining: 1 step
> - Next: cro (AGENT)

---

## Step 9 — Agent Optimizes Conversion Paths (AGENT)

The agent analyzes the client's landing pages and recommends conversion improvements.

> Step 8/8 complete — CRO Analysis
> - Created: `{company.clients}/acme/deliverables/cro_recommendations.md`
> - Remaining: 0 steps
> - Running quality gate...

---

## Step 10 — Quality Gate

The agent evaluates every condition:

> **Quality Gate Results:**
> - ✅ ICP profile has no empty required fields
> - ✅ Content calendar covers 4 weeks (28 posts planned)
> - ✅ Email sequence has 6 emails with segmentation logic
> - ✅ CRO recommendations tied to specific page elements
>
> **All conditions passed** — TaskNote status set to `done`

---

## The Final TaskNote

```yaml
---
type: task
title: "Lead generation activation: Acme Corp"
status: done
playbook: "[[Lead generation activation]]"
remaining-steps: 0
awaiting: ""
priority: high
assignee: [Agent]
---
```

The body contains the full step log:

```markdown
### Step 1 — icp-discovery (AGENT)
- **Status:** done
- **Completed:** 2026-03-18 10:15
- **Output:** ICP profile for B2B SaaS founders
- **Files:** [[icp_profile]]

### Step 2 — social-media-audit (AGENT)
- **Status:** done
- **Completed:** 2026-03-18 10:22
- **Output:** Social presence scored across 4 platforms
- **Files:** [[social_media_audit]]

### Step 3 — brand-voice-generator (AGENT)
- **Status:** done
- **Completed:** 2026-03-18 10:28
- **Output:** Brand voice guidelines extracted
- **Files:** [[brand_voice_guide]]

### Step 4 — Review (HUMAN)
- **Status:** done
- **Completed:** 2026-03-18 10:35
- **Decision:** ICP confirmed. Focus LinkedIn + email. Skip Instagram.

### Step 5 — content-strategy (AGENT)
- **Status:** done
- **Completed:** 2026-03-18 10:48
- **Output:** 4-week content calendar with topic clusters
- **Files:** [[content_strategy]]

### Step 6 — social-content (AGENT)
- **Status:** done
- **Completed:** 2026-03-18 10:55
- **Output:** 12 LinkedIn posts
- **Files:** [[social_posts]]

### Step 7 — email-sequence (AGENT)
- **Status:** done
- **Completed:** 2026-03-18 11:05
- **Output:** 6-email nurture sequence
- **Files:** [[email_sequences]]

### Step 8 — cro (AGENT)
- **Status:** done
- **Completed:** 2026-03-18 11:15
- **Output:** 8 conversion recommendations
- **Files:** [[cro_recommendations]]
```

---

## What Just Happened

In about **1 hour**, you got:

| Deliverable | What It Is |
|-------------|------------|
| ICP Profile | Who to target and why |
| Social Audit | Where the client stands today |
| Brand Voice | How to sound like them |
| Content Strategy | What to publish and when |
| 12 LinkedIn Posts | Ready-to-schedule content |
| Email Sequence | 6-email nurture campaign |
| CRO Recommendations | How to convert more visitors |

**Your total input:** One review step where you confirmed direction and picked channels. The agent handled everything else.

---

## Try It Yourself

Pick any playbook and say `start playbook: [name]`. Here are good starting points:

| If you want to... | Run this playbook |
|-------------------|-------------------|
| Audit a client's online presence | [[Digital authority baseline]] |
| Help a client price better | [[Margin improvement]] |
| Reduce founder dependency | [[Founder independence]] |
| Make a big strategic decision | [[Strategic decision framework]] |
| Improve a client's sales process | [[Sales conversion improvement]] |

See all available playbooks: browse `{company.playbooks}` or check the [[playbooks-in-flight]] dashboard for active runs.

---

## Common Questions

**Q: Can I skip a step?**
No. HUMAN steps require your explicit input. AGENT steps run automatically. The playbook ensures nothing is missed.

**Q: Can I pause and resume later?**
Yes. The TaskNote tracks exactly where you stopped. Say "resume playbook" and the agent reads the step log to pick up where it left off.

**Q: Can I customize a playbook for a specific client?**
Yes. Copy the playbook to `{client.root}/Playbooks/` and adjust steps, context files, or quality gates. The client version overrides the library version.

**Q: What if a step fails?**
The agent stops, reports the error, and keeps the TaskNote open. You decide whether to retry, skip, or troubleshoot.
