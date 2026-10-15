---
description: Brand foundations, content production and repurposing, publishing channels,
  campaigns, audits, and the draft-to-published content lifecycle
title: BOB User Manual — 9. Marketing & Content
---

# 9. Marketing & Content

The Marketing & Content module covers the **create-to-publish value chain** — every step from brand foundation through content creation, review, channel publishing, and performance measurement. It also feeds the lead-to-cash chain: outreach drafts, campaign sequences, and SEO content all flow through here before reaching prospects.

BOB does not publish anything without your review. The module is built around a draft → review → scheduled → published lifecycle, with a clear gate before anything goes out.

## 9.1 Brand foundations

Before BOB can write content that sounds like you, it needs to know your voice. This is a one-time setup step, not an ongoing workflow.

### Brand voice

Run `brand-voice-generator` once, early on. BOB interviews you — or analyzes samples of your existing writing — and produces a brand voice document: tone descriptors, vocabulary preferences, sentence rhythm, things to avoid, and example passages. This document is stored at `{company.brand}` and is read automatically by every content-drafting skill.

If your voice shifts or you add a new writer to the team, re-run `brand-voice-generator` and replace the file.

### Brand system

`brand-system` handles the visual and messaging layer: colour palette, typefaces, taglines, positioning statement, and messaging hierarchy. It writes a `DESIGN.md` design spec in `{company.brand}`, with companion UI and media standards files; a product or a client can have its own spec in `{product.brand}` or `{client.brand}`. Skills that produce designed deliverables — `branded-pdf`, `corporate-pdf`, presentation tools — read from this spec.

You do not need to update these files frequently. Treat them as your single source of truth for brand rules and update them only when your brand changes.

## 9.2 Content production

### Social and editorial content

`social-content` is the workhorse for regular publishing. Give it source material — a meeting note, a report excerpt, a client insight, a link — and it drafts posts calibrated to your chosen channel (LinkedIn, X, Substack, or others). It applies your brand voice automatically.

Typical workflow:

1. Point BOB at your source: "Write a LinkedIn post from the notes in last week's client call."
2. `social-content` reads the source and drafts two or three options in your voice.
3. Drafts land in `{company.marketing}/{channel}/drafts/` with `status: draft`.
4. You review in Obsidian, edit inline if needed, and change `status: scheduled` or `status: approved`.
5. Only then does publishing happen — either manually or via a publisher skill.

### Repurposing

Good content is expensive to produce. `content-repurposer` multiplies its value. Give it one strong piece — a long article, a recorded talk transcript, a case study — and specify which formats you need. BOB produces a set of derivative pieces: a short-form post, a newsletter excerpt, a pull-quote set, a thread structure.

The output is a set of draft notes, one per format, saved alongside the source. They are not identical rehashes — BOB rewrites for each context, applying channel-appropriate length and framing.

### Copywriting

`copywriting` handles persuasive writing with a defined commercial goal: landing pages, product descriptions, call-to-action blocks, email subject lines. Unlike `social-content`, which works from your existing material, `copywriting` starts from a brief. Tell BOB the offer, the audience, the desired action, and any constraints. BOB drafts; you approve.

## 9.3 Channels and publishing

### The review gate

Every content workflow produces a draft, never a live post. The status field in the note frontmatter controls progression:

| Status | Meaning |
|--------|---------|
| `draft` | Created by BOB; not reviewed |
| `in-review` | Under your review or a collaborator's |
| `approved` | Cleared for scheduling or publication |
| `scheduled` | Queued for a specific publish date |
| `published` | Live; publisher confirmed |

No publisher skill will act on a note with `status: draft`. This is intentional and cannot be bypassed.

### Publisher skills

| Skill | Channel | Notes |
|-------|---------|-------|
| `social-publisher` | LinkedIn, X, and others | Uses configured channel credentials; posts at scheduled time |
| `wordpress-publisher` | WordPress sites | Posts as draft in WordPress; you publish from the CMS |
| `metalsmith-publisher` | Static sites (brn.cx and similar) | Generates the file and writes to the site source; build runs separately |

`wordpress-publisher` and `metalsmith-publisher` never push a live page directly. WordPress receives a draft; Metalsmith writes source files that a build step then compiles. The final live state is always the result of a separate deliberate action.

### Where content is saved

| Content type | Vault path |
|-------------|------------|
| LinkedIn drafts | `{company.marketing}/linkedin/` |
| Newsletter / Substack | `{company.marketing}/newsletter/` |
| Blog and long-form | `{company.marketing}/content/` |
| Outreach (cold/warm) | `{company.marketing}/{channel}/` |
| Campaign assets | `{company.marketing}/{channel}/` |
| Brand files | `{company.brand}` |

## 9.4 Campaigns and sequences

A campaign is a coordinated set of content pieces aimed at a defined audience over a defined period. BOB can plan and draft the full campaign, but you control sequencing and timing.

To run a campaign:

1. Brief BOB: audience, goal, duration, channels, key messages.
2. BOB proposes a content calendar — posts, emails, landing page copy, and the sequence logic.
3. You approve the plan. BOB then drafts each piece as a separate note.
4. Each note goes through the normal draft → review → approved → scheduled flow.

For email-based nurture or outbound sequences, `outbound-sequence` (see [chapter 8](08-sales-crm.md)) produces the sequence structure, and `social-publisher` or your email tool handles sending. BOB links the sequence notes so you can review the full arc before any piece goes out.

Relevant playbooks: [Content strategy to publish](../../workflows/pb-content-strategy-to-publish.md), [Content campaign launch](../../workflows/pb-content-launch.md), [Daily Content Machine](../../workflows/pb-daily-content-machine.md), [Blog creation quality loop](../../workflows/pb-blog-creation-quality-loop.md).

## 9.5 Audits

Run audits quarterly, or before a major relaunch, or when something is clearly underperforming. Each audit skill returns a scored report and a prioritised list of concrete actions — not a summary of what's already there.

| Skill | What it audits | Primary output |
|-------|---------------|----------------|
| `seo-audit` | On-page SEO: title tags, meta descriptions, heading structure, internal linking, keyword gaps | Scored report with fixes ranked by impact |
| `geo-audit` | Generative engine optimisation: how your content appears in AI-generated answers | Visibility score and content recommendations |
| `website-audit` | Overall site health: performance, UX, conversion friction, messaging clarity | Prioritised improvement list |
| `social-media-audit` | Channel performance: posting frequency, engagement rates, content mix, audience trends | Channel-by-channel score with actions |

Audit reports land in `{company.reports}` with the date and audit type in the filename. They are inputs, not conclusions — the action items are what matter.

## 9.6 Deliverable rendering

Some marketing work needs to be sent to clients or prospects as a finished document, not a vault note.

- `branded-pdf` renders any approved note as an on-brand PDF, applying your brand-system colours, typeface, and logo.
- `lead-magnet-generator` builds a multi-page downloadable guide, checklist, or toolkit from a topic, plus the promotion posts to distribute it.
- Visual skills (`visual-designer`, `excalidraw-diagrams`, `d2-diagram`) produce charts, diagrams, and visual assets that can be embedded in documents or posts.
- Video and motion graphics skills exist for producing short explainer videos, testimonial clips, and social video content — the [Daily Content Machine](../../workflows/pb-daily-content-machine.md) and AI News Daily Video Pipeline playbooks orchestrate these.

Rendered files are saved to `{client.deliverables}` if client-facing, or to the relevant `{company.marketing}` subfolder for owned channels.

## 9.7 Skills in this module

| Skill | Primary use |
|-------|-------------|
| `brand-voice-generator` | Capture and codify your tone and style |
| `brand-system` | Visual identity and messaging hierarchy |
| `social-content` | Social and editorial post drafting |
| `content-repurposer` | One piece → many formats |
| `copywriting` | Persuasive copy with a commercial goal |
| `social-publisher` | Post to social channels on schedule |
| `wordpress-publisher` | Push content to WordPress as a draft |
| `metalsmith-publisher` | Write to static-site source |
| `seo-audit` | On-page SEO scoring and fixes |
| `geo-audit` | Generative engine visibility |
| `website-audit` | Full site health and conversion review |
| `social-media-audit` | Channel performance review |
| `branded-pdf` | On-brand PDF rendering |
| `content-scorer` | Quality and readability scoring |
| `copy-editing` | Grammar, clarity, and consistency pass |
| `humanize-content` | Remove AI cadence from drafts |
| `messaging-coherence` | Check that all content tells the same story |

## 9.8 The content lifecycle in practice

The draft → review → scheduled → published progression is not bureaucracy. It exists because published content is hard to retract, and inconsistent brand voice compounds over time.

A practical routine:

- **Monday:** review all notes with `status: draft` created last week. Approve, request revisions, or delete.
- **Wednesday:** check `status: scheduled` queue. Confirm timing still makes sense.
- **Friday:** review anything that went `status: published` that week. Note what to repurpose.

BOB can generate this weekly content review as a dashboard if you run `weekly-review` with the marketing context specified.

## 9.9 Good practices

- **Run `brand-voice-generator` before any bulk drafting.** Content produced without a voice file will require heavier editing.
- **Always check `messaging-coherence` before a campaign launch.** It is easy for individual posts to drift from the core message when drafted at different times.
- **Use `content-repurposer` before reaching for `social-content`.** If you have a strong existing piece, repurposing is faster and more consistent than drafting from scratch.
- **Treat audit actions as a backlog, not a to-do list.** A `seo-audit` can return fifty items. Add them to your task notes and work through them by impact, not by order.
- **Never change `status: published` back to `draft` in place.** If a published piece needs revision, create a new note as the corrected version and link the old one.

