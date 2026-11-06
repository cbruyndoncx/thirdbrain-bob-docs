# Learning Path: From Setup to Showstopper

Your self-paced guide to building an AI-powered business operating system. Pick your track based on your vault edition, then follow the stages in order.

**Prerequisites:** Complete guides [[01_obsidian_quick_start]], [[02_your_first_skill]], and [[03_skills_by_use_case]] first.

---

## Choose Your Track

| Track | For | Stages | Time |
|-------|-----|--------|------|
| **Starter** | Starter vault + free skill packs | 8 stages | ~3 hours |
| **Pro** | Full vault (all skills) | 10 stages | ~5 hours |

Both tracks start the same way — teaching the AI who you are. The Starter track uses only skills included in the starter vault and free packs. Pro stages are marked with a ⭐ badge.

> [!tip] You don't need to finish everything in one session. Pick up where you left off — the vault remembers your progress through the files it creates.

---

## Phase 1: Build Your AI Brain

*First, teach the vault who you are. Every skill you run after this will be smarter because of what you set up here.*

---

### Stage 1: Your Personal Profile

**Time:** 30 min | **Track:** Starter + Pro

Build the foundation: your values, decision-making principles, daily rhythms, and working preferences. This is what makes AI advice actually fit your life.

**Say this:**
> Help me build my personal context using personal-context-builder

Claude will interview you — one question at a time, 5-8 exchanges per file. Answer honestly. The quirks are the whole point.

**What you'll get:**
- `{me.constitution}` — your values, non-negotiables, and trade-off preferences
- `{me.profile-root}/personal_life.md` — daily rhythms, energy patterns, what fills vs depletes you

> [!tip] Already have these files populated? Tell Claude "Check if my profile files exist first" — the skill will detect them and skip what's done.

**Checkpoint:** Open both files in Obsidian. Read through them. If something feels off, tell Claude "That's not quite right, here's what I actually mean..." — the skill is conversational.

> [!info] What just happened
> You just gave your vault a personality. These two files are referenced by `brand-voice-generator` (authentic voice), `copywriting` (messaging tone), and every content skill. Every skill that touches "you" reads these files.

---

### Stage 2: Your Personal Voice

**Time:** 30 min | **Track:** Starter + Pro | **Prerequisites:** Stage 1

Define how you write and communicate. Claude will either analyze your existing writing samples or interview you about your style preferences.

**Say this:**
> Run brand-voice-generator for my personal brand. I'd like to provide some writing samples for analysis.

Prepare 5-10 samples of your writing: emails, LinkedIn posts, proposals, Slack messages — anything that sounds like "you." Paste them when asked.

**What you'll get:**
- `{me.profile-root}/brand/brand.json` — colors, fonts, visual identity
- `{me.profile-root}/brand/brand_system.md` — design philosophy
- `{me.profile-root}/brand/config.json` — output settings
- `{me.profile-root}/tone_of_voice.md` — your voice mapped across 6 dimensions: personality, vocabulary, sentence structure, formatting, teaching style, emotional register

> [!tip] No writing samples handy? Say "Let's do the interview path instead" — Claude will ask 6 structured questions about your communication style.

**Checkpoint:** Open `tone_of_voice.md`. Every field should have your actual words and patterns — no more `[placeholder]` brackets. If a section feels generic, tell Claude to push deeper.

> [!info] What just happened
> Your tone of voice file is now loaded by every content-generating skill: `copywriting`, `social-content`, `email-sequence`, and more. From now on, when Claude writes for you, it writes *like* you.

> [!example] ⭐ PRO: Business Baseline
> With the Pro vault, your next step would be mapping your entire business visually — revenue model, customer journey, internal processes — all generated as interactive Draw.io diagrams. The `business-baseline` skill interviews you for 60 minutes and produces a complete operating model with a 90-day improvement roadmap.

---

### ⭐ Stage 3: Your Business Map (Pro only)

**Time:** 60 min | **Track:** Pro | **Prerequisites:** Stages 1-2 recommended

Map your entire business operations visually. Claude interviews you about your business model, customer journey, and internal processes — then generates diagrams.

**Say this:**
> I want to run a business x-ray on my own company. Let's map my business operations.

Claude will ask about your business type, revenue model, customer journey, and key processes. It infers first, then asks you to confirm or correct — less typing for you.

**What you'll get:**
- Business Map diagram (Draw.io) — your whole business at a glance
- Bow-Tie Funnel — acquisition through expansion
- Process Swimlanes — drill into specific operations
- 90-Day Roadmap — prioritized improvements based on pain points discovered

**Checkpoint:** Open the Draw.io diagrams in Obsidian. Your business should be recognizable. Key processes should be mapped with owners and pain points annotated.

> [!info] What just happened
> You now have a visual operating model of your business. The `business-baseline` skill supports 14 business archetypes (Coach, Agency, SaaS, Service Provider, etc.) and adapts its questions accordingly. These diagrams become reference material for strategy sessions and the skills in Phase 3.

---

## Phase 2: Create Real Content

*Your context files are populated. Now watch what happens when AI skills can actually read your voice and your values.*

---

### Stage 3 / ⭐ 4: Write Landing Page Copy

**Time:** 15 min | **Track:** Starter + Pro | **Prerequisites:** Stage 2

This is the moment it clicks. Ask Claude to write copy and watch it use your actual voice, not generic marketing speak.

**Say this:**
> Use copywriting to write a homepage hero section for my business. Target [describe your ideal customer briefly].

**What you'll get:**
- 3 headline variants with different angles (pain, aspiration, proof)
- Supporting subheadline and body copy
- CTA button text options
- All written in your tone of voice

**Checkpoint:** Read the output aloud. Does it sound like you? Compare it to your writing samples from Stage 2. The voice should be recognizably yours, not generic AI copy.

> [!info] What just happened
> The `copywriting` skill loaded your `tone_of_voice.md` and `constitution.md` before writing a single word. That's why the output matches your style. Without those files, you'd get competent but generic copy. With them, you get *your* copy.

---

### Stage 4 / ⭐ 5: Define Your Ideal Customer

**Time:** 20 min | **Track:** Starter + Pro | **Prerequisites:** Stage 1

Build a detailed profile of who you're selling to. This feeds every marketing skill that comes after.

**Say this:**
> Help me define my ideal customer profile using icp-discovery

Claude will interview you about your best customers, their pain points, buying triggers, and objections. If you have real customer data, even better — bring examples.

**What you'll get:**
- `{company.icp}` — demographics, psychographics, buying behavior, key pain points
- Persona template with quotes, objections, and decision criteria

**Checkpoint:** Read the ICP. Does it describe a real person you've actually sold to? If it feels too broad ("small business owners"), push Claude to narrow it: "My best clients are specifically..."

> [!info] What just happened
> Your ICP file is now loaded by `marketing-ideas`, `social-content`, `email-sequence`, `competitor-alternatives`, and more. Every marketing skill now knows who you're talking to — not just what you sound like.

---

### Stage 5 / ⭐ 6: Your First LinkedIn Post

**Time:** 15 min | **Track:** Starter + Pro | **Prerequisites:** Stages 2, 4

Generate a ready-to-publish LinkedIn post. This is the fastest way to see your voice + ICP working together.

**Say this:**
> Use social-content to write a LinkedIn post about [a topic you know well]. Target my ICP.

Pick something you have a genuine opinion on — a lesson learned, a contrarian take, a client win (anonymized).

**What you'll get:**
- A LinkedIn post with hook, body, and CTA
- 3 variant hooks to A/B test
- Hashtag suggestions based on your niche

**Checkpoint:** Would you actually post this? If yes, do it. If it feels off, tell Claude what to adjust — the skill iterates well.

> [!info] What just happened
> The `social-content` skill combined your `tone_of_voice.md` (how you write), `icp.md` (who you're writing for), and your topic expertise into platform-native content. Three context files, one post, zero "sounds like AI."

> [!example] ⭐ PRO: Deep Research
> Want Claude to spend 10 minutes autonomously searching the web, evaluating sources, and synthesizing findings into a cited research report? The `deep-research` skill uses advanced reasoning models (DeepSeek R1 or OpenAI o4-mini) for questions you'd normally spend an afternoon Googling.

---

## Phase 3: Plan Your Growth

*You've built context and created content. Now use it for strategic planning.*

---

### Stage 6 / ⭐ 7: Marketing Ideas

**Time:** 15 min | **Track:** Starter + Pro | **Prerequisites:** Stage 4

Get a tailored list of marketing tactics for your specific business and ICP — not generic advice, but specific plays from a library of 139 proven strategies.

**Say this:**
> Use marketing-ideas to brainstorm marketing tactics for my business. Focus on [low-budget / content-led / referral-based / whatever fits].

**What you'll get:**
- 10-15 prioritized marketing tactics matched to your business type
- For each: what it is, why it works for you, effort level, expected timeline
- Quick-win recommendations vs long-term plays

**Checkpoint:** At least 3 ideas should make you think "I should actually try that." If they're too generic, give Claude more specifics about your constraints (budget, team size, channels you prefer).

> [!info] What just happened
> The `marketing-ideas` skill read your ICP and profile to filter its strategy library. A coaching business gets different tactics than a SaaS company. Your constraints (solo founder vs team, bootstrapped vs funded) further narrow the recommendations.

> [!example] ⭐ PRO: Board of Advisors
> The showstopper: ask a strategic question and get a full board of advisors debating it — each one a named thought leader with a distinct perspective. Position papers, rebuttals, a vote tracker, and an interactive HTML with assumption sliders that dynamically recalculate projections. The `ask-boardroom` skill spawns parallel agents that read your company profile to ground every recommendation.

---

### Stage 7 / ⭐ 8: Email Sequence

**Time:** 20 min | **Track:** Starter + Pro | **Prerequisites:** Stages 2, 4

Create a multi-email sequence — welcome, nurture, or outreach — written in your voice and targeted at your ICP.

**Say this:**
> Use email-sequence to create a 5-email welcome sequence for new subscribers. Target my ICP.

Or pick what fits: cold outreach, re-engagement, onboarding, post-purchase nurture.

**What you'll get:**
- 5 emails with subject lines, preview text, and body copy
- Send timing recommendations (day 1, day 3, day 7, etc.)
- Segmentation logic (if applicable)
- Each email written in your voice with ICP-appropriate messaging

**Checkpoint:** Read email #1 aloud. Would you send this to a real prospect or subscriber? The subject line should make you want to open it, and the body should sound like you wrote it.

> [!info] What just happened
> The `email-sequence` skill combined your voice, ICP, and business context into a complete campaign. The timing recommendations are based on engagement research for your business type. One prompt, five ready-to-load emails.

> [!example] ⭐ PRO: Client Proposal
> Turn meeting notes or a transcript into a professional Word document — formatted, branded, and written in your voice. The `proposal-writer` skill reads your company profile, offerings, tone of voice, and the client conversation to produce a six-section proposal ready to send. One prompt, five context files, one polished deliverable.

---

### Stage 8 / ⭐ 9: Vault Health Check

**Time:** 10 min | **Track:** Starter + Pro | **Prerequisites:** All previous stages

Now that your vault is populated, see how far you've come. This produces a visual dashboard with scores — your "after" snapshot.

**Say this:**
> Run a vault checkup using obsidian-ops

**What you'll get:**
- A markdown report with embedded SVG charts: health gauge, radar chart, tag treemap
- A vault score (0-100) with letter grade
- Top 3 fixes to improve vault quality

**Checkpoint:** Compare this to a fresh vault. Your score reflects real content — profile files, brand assets, ICP, business context. The radar chart should show strength in areas you've built out.

> [!info] What just happened
> The `obsidian-ops` skill scanned every file in your vault — notes, tags, links, metadata. Unlike running this on an empty vault, you now have meaningful data. This is your "before" snapshot for ongoing vault maintenance.

---

### ⭐ Stage 10: Strategy Document (Pro only)

**Time:** 30 min | **Track:** Pro | **Prerequisites:** Phase 1

Create a formal product or business strategy using proven frameworks (Playing to Win, Porter's Five Forces, Blue Ocean, etc.).

**Say this:**
> Help me create a product strategy using strategy-frameworks. My strategic question is: [your question]

Examples:
- "Where should we play in the AI consulting market and how do we win?"
- "How do we position against [competitor] in [market segment]?"

**What you'll get:**
- Framework selection guide (Claude recommends which framework fits your question)
- A complete Strategy Document: winning aspiration, where to play / not to play, how to win, capabilities gap analysis, Now/Next/Later roadmap, kill signals

**Checkpoint:** The document should have specific choices — not just analysis. "Where to play" should name segments you're targeting AND segments you're deliberately ignoring.

> [!info] What just happened
> The `strategy-frameworks` skill applied a structured strategic framework to your question. If your business-baseline diagrams exist (Stage 3), Claude references your actual business operations. If your ICP is defined, it informs the "where to play" choices. Context compounds.

---

## What's Next?

You've completed the learning path. Here's what to explore:

### Daily Habits
- Set up `daily-briefing` for a personalized morning digest (configure VIP senders, tracked companies)
- Use `ask-zeus` for quick strategic decisions (Pro)
- Run `obsidian-ops` weekly to keep your vault healthy

### Content & Marketing
- `social-content` — write platform-specific posts
- `seo-content-machine` — end-to-end SEO content pipeline
- `content-repurposer` — turn one piece into seven formats (Pro)

### Client Work
- `create-client` — set up a new client workspace
- `competitor-alternatives` — research and compare competitors
- `consultative-selling` — build discovery questions and ROI calculators (Pro)

### Advanced (Pro)
- `ask-boardroom` — run it for every major decision
- `pptx-tools` — generate branded slide decks
- `operating-dashboard` — create a visual business dashboard

---

## Appendix: Context File Map

This shows which files feed which skills — and why the order matters.

```
Phase 1 creates:
├── {me.profile-root}
│   ├── constitution.md        → copywriting, social-content, email-sequence
│   ├── personal_life.md       → daily-briefing
│   ├── tone_of_voice.md       → ALL content skills
│   └── brand/                 → pptx-tools, corporate-pdf
│       ├── brand.json
│       ├── brand_system.md
│       └── config.json
├── {company.profile-root}
│   └── icp.md                 → marketing-ideas, social-content, email-sequence
└── {company.processes}   (Pro only)
    └── X-RAY/                 → strategy-frameworks, operating-dashboard

Phase 2 uses:
├── tone_of_voice.md           → copywriting, social-content
└── icp.md                     → social-content, marketing-ideas

Phase 3 uses:
├── Everything from Phase 1 + 2
└── {company.profile-root}
    └── offerings.md           → proposal-writer (Pro), consultative-selling (Pro)
```
