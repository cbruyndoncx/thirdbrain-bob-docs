# Marketing Skills User Guide

> **Complete Reference for Marketing, Paid Ads, Analytics, and Growth Skills**
>
> Version 1.0 | Last Updated: 2026-02-09

---

## Table of Contents

1. [Overview](#overview)
2. [Skill Categories](#skill-categories)
3. [Quick Start Prompts](#quick-start-prompts)
4. [Skill Reference](#skill-reference)
5. [Compound Workflows](#compound-workflows)
6. [Input Files & Dependencies](#input-files--dependencies)
7. [Sample Workflows](#sample-workflows)

---

## Overview

This vault contains **30+ marketing skills** that work together as an integrated marketing operating system. Skills can be used individually or combined for powerful compound workflows.

### How Skills Work

1. **Activation**: Describe what you need; Claude matches to the right skill
2. **Context Loading**: Skill reads `{company.marketing-context}` if available
3. **Interview**: Skill gathers missing context through questions
4. **Execution**: Skill produces frameworks, copy, analysis, or strategy
5. **Compound Use**: Output from one skill becomes input for another

### Key Files

| File | Purpose | Create This First |
|------|---------|-------------------|
| `{company.marketing-context}` | Shared context for all marketing skills | Yes - reduces repetitive questions |
| `{company.icp}` | ICP document | Use icp-discovery skill |
| `{company.offerings}` | What you sell | Manual or skill-generated |

---

## Skill Categories

### Paid Advertising & Campaigns
| Skill | Trigger Phrases | What It Does |
|-------|-----------------|--------------|
| **paid-ads** | "PPC", "ad campaign", "Meta ads", "Google Ads", "ROAS" | Campaign strategy, ad copy, audience targeting, optimization |
| **google-ads-scripts** | "automate Google Ads", "bid optimization", "keyword management" | JavaScript automation for Google Ads |
| **ab-test-setup** | "A/B test", "split test", "experiment" | Experiment design, sample size, statistical analysis |

### Analytics & Tracking
| Skill | Trigger Phrases | What It Does |
|-------|-----------------|--------------|
| **analytics-tracking** | "set up tracking", "event tracking", "UTM parameters" | Tracking plans, event architecture, implementation |
| **ga4** | "Google Analytics", "GA4 setup", "custom dimensions" | Complete GA4 implementation guide |
| **gtm** | "Tag Manager", "GTM", "data layer" | GTM container setup, tags, triggers, variables |

### Conversion Rate Optimization (CRO)
| Skill | Trigger Phrases | What It Does |
|-------|-----------------|--------------|
| **page-cro** | "improve conversions", "CRO audit", "landing page optimization" | Page analysis, conversion improvements |
| **form-cro** | "form optimization", "form friction", "lead form" | Form field optimization, multi-step forms |
| **signup-flow-cro** | "signup conversions", "registration flow" | Account creation flow optimization |
| **onboarding-cro** | "user activation", "onboarding flow", "time-to-value" | Post-signup activation optimization |
| **popup-cro** | "exit intent", "popup conversions", "email popup" | Modal/popup design and optimization |

### Content & Copywriting
| Skill | Trigger Phrases | What It Does |
|-------|-----------------|--------------|
| **copywriting** | "write copy", "headline help", "CTA copy" | Marketing copy for pages |
| **copy-editing** | "edit copy", "polish this", "review my copy" | Multi-pass copy improvement |
| **content-strategy** | "what should I write about", "content planning" | Topic clusters, content pillars |
| **email-sequence** | "drip campaign", "welcome sequence", "nurture emails" | Email automation design |
| **social-content** | "LinkedIn post", "Twitter thread", "content calendar" | Social media strategy and content |

### SEO & Search
| Skill | Trigger Phrases | What It Does |
|-------|-----------------|--------------|
| **seo-audit** | "SEO audit", "check my SEO", "technical SEO" | 7-domain SEO analysis with scoring |
| **programmatic-seo** | "pages at scale", "location pages", "template pages" | Scalable SEO page strategies |
| **schema-markup** | "structured data", "JSON-LD", "rich snippets" | Schema.org implementation |

### Business Strategy
| Skill | Trigger Phrases | What It Does |
|-------|-----------------|--------------|
| **icp-discovery** | "ideal customer", "ICP", "buyer persona" | Guided interview to build ICP document |
| **pricing-strategy** | "pricing tiers", "freemium", "value metric" | Pricing and packaging design |
| **launch-strategy** | "product launch", "Product Hunt", "go-to-market" | Phased launch planning |
| **competitor-alternatives** | "vs page", "alternative page", "competitor comparison" | Competitive content pages |

### Growth & Retention
| Skill | Trigger Phrases | What It Does |
|-------|-----------------|--------------|
| **referral-program** | "refer a friend", "affiliate program", "viral loop" | Referral/affiliate program design |
| **paywall-upgrade-cro** | "upgrade flow", "conversion to paid" | Free-to-paid conversion optimization |
| **free-tool-strategy** | "engineering as marketing", "free calculator" | Free tool lead generation |

---

## Quick Start Prompts

Copy these prompts to immediately activate skills:

### Foundation Setup
```
Let's build my product marketing context. I want to create a shared context
file that all marketing skills can reference.
```

```
Let's define my ICP. I sell [product/service] to [audience].
```

### Paid Advertising
```
Help me plan a Google Ads campaign for [product]. My budget is $X/month,
and my target CPA is $Y.
```

```
I need Meta ad copy for [product]. The goal is [leads/sales/signups].
My audience is [description].
```

```
Write a Google Ads script to pause keywords with Quality Score below 4
and spend over $100.
```

### Conversion Optimization
```
Audit this page for conversion issues: [URL]
```

```
Optimize my signup flow. Currently we ask for [fields] and have [X]% completion.
```

```
Design an exit-intent popup for [goal]. Current traffic is [X] visitors/month.
```

### Content & SEO
```
Create a content strategy for [business]. Our ICP is [description]
and we want to rank for [topics].
```

```
Run an SEO audit on [URL]. Focus on technical issues and AI visibility.
```

```
Write homepage copy for [product]. Primary CTA is [action].
```

### Email & Nurture
```
Create a welcome email sequence for new trial users. Our activation
action is [specific action].
```

```
Design a re-engagement sequence for users inactive for 30+ days.
```

### Strategy
```
Help me design pricing tiers for [product]. We currently charge [price]
and our main competitor charges [competitor price].
```

```
Plan a Product Hunt launch for [product]. Launch date is [date].
```

---

## Skill Reference

### paid-ads

**Purpose**: Complete paid advertising strategy across Google, Meta, LinkedIn, Twitter/X, and TikTok.

**Inputs Required**:
- Campaign goals (awareness, traffic, leads, sales)
- Target CPA or ROAS
- Monthly/weekly budget
- Landing page URL
- Audience description
- Existing pixel/conversion data

**Outputs**:
- Campaign structure with naming conventions
- Ad copy variations (PAS, BAB, Social Proof formulas)
- Audience targeting recommendations
- Budget allocation strategy
- Optimization playbook

**Key Frameworks**:
- Platform Selection Matrix (Google vs Meta vs LinkedIn)
- Retargeting Funnel Strategy (TOF/MOF/BOF)
- Creative Testing Hierarchy

**Related Skills**: analytics-tracking, ab-test-setup, page-cro, copywriting

---

### google-ads-scripts

**Purpose**: JavaScript automation for Google Ads campaign management.

**Inputs Required**:
- Google Ads account access
- Specific automation goal
- Thresholds (ROAS targets, quality score minimums, budget limits)

**Outputs**:
- Working JavaScript code for Google Ads Scripts
- Audit log configuration
- Google Sheets integration for reporting

**Key Capabilities**:
- Pause low-quality keywords
- Optimize bids based on ROAS
- Export performance to Google Sheets
- Budget management automation
- Day-of-week bid adjustments
- Quality score monitoring

**External Dependencies**:
- Google Ads account
- Google Sheets (for reporting)
- Google Apps Script (optional)

**Files**: `references/ads-api-reference.md`, `scripts/validators.py`

---

### ab-test-setup

**Purpose**: Statistically valid experiment design and analysis.

**Inputs Required**:
- Baseline conversion rate
- Traffic volume
- Minimum detectable effect (MDE)
- Testing tool available

**Outputs**:
- Hypothesis document
- Sample size calculation
- Test design (A/B, A/B/n, MVT)
- Metrics framework (primary, secondary, guardrail)
- Analysis checklist

**Key Frameworks**:
- Hypothesis Template: "Because [observation], we believe [change] will cause [outcome]"
- Sample Size Quick Reference Table
- Statistical Significance Interpretation

**Files**: `references/sample-size-guide.md`, `references/test-templates.md`

**Related Skills**: page-cro, analytics-tracking, copywriting

---

### analytics-tracking

**Purpose**: Analytics implementation and measurement strategy.

**Inputs Required**:
- Business goals and key conversions
- Current tools (GA4, Mixpanel, etc.)
- Tech stack
- Privacy/compliance requirements

**Outputs**:
- Tracking plan document
- Event naming conventions
- UTM parameter strategy
- Implementation guide

**Key Frameworks**:
- Object-Action Event Naming (`signup_completed`, `cta_clicked`)
- Event Types: Pageviews, User Actions, System Events, Conversions
- Debugging Checklist

**Files**: `references/event-library.md`, `references/ga4-implementation.md`, `references/gtm-implementation.md`

**Related Skills**: ga4, gtm, ab-test-setup

---

### ga4

**Purpose**: Complete Google Analytics 4 implementation guide.

**Inputs Required**:
- GA4 Measurement ID (G-XXXXXXXXXX)
- Implementation method (gtag.js, GTM, or CMS plugin)
- Events to track

**Outputs**:
- Setup instructions
- Custom event implementation
- Custom dimensions configuration
- Ecommerce tracking
- Privacy/consent mode setup

**Key Frameworks**:
- Event Categories: Automatic, Enhanced Measurement, Recommended, Custom
- Parameter Limits: 25 per event, 40 char names, 100 char values
- Reporting Identity: User ID, Device ID, Modeling

**Files**: 15 reference files covering setup, events, dimensions, reporting, BigQuery, privacy

**External Dependencies**: GA4 property, gtag.js or GTM

**Related Skills**: gtm, analytics-tracking

---

### gtm

**Purpose**: Google Tag Manager implementation and management.

**Inputs Required**:
- GTM Container ID
- Tags to implement (GA4, Google Ads, Facebook Pixel, etc.)
- Trigger conditions
- Data layer requirements

**Outputs**:
- Container configuration
- Tag/Trigger/Variable setup
- Data layer implementation code
- Debugging workflow

**Key Frameworks**:
- Tag Naming: `[Platform] - [Type] - [Description]`
- ES5 JavaScript requirement (var, function, string concat)
- RE2 Regex syntax

**Files**: 9 reference files covering setup, tags, triggers, variables, data layer, debugging, API

**External Dependencies**: GTM account, website access

**Related Skills**: ga4, analytics-tracking

---

### page-cro

**Purpose**: Conversion rate optimization for marketing pages.

**Inputs Required**:
- Page URL or content
- Page type (homepage, landing, pricing, feature, blog)
- Primary conversion goal
- Traffic source
- Current metrics

**Outputs**:
- Quick wins (immediate fixes)
- High-impact changes (prioritized)
- A/B test ideas
- Copy alternatives with rationale

**Analysis Framework** (in order of impact):
1. Value Proposition Clarity
2. Headline Effectiveness
3. CTA Placement, Copy, and Hierarchy
4. Visual Hierarchy and Scannability
5. Trust Signals and Social Proof
6. Objection Handling
7. Friction Points

**Files**: `references/experiments.md`

**Related Skills**: copywriting, ab-test-setup, signup-flow-cro, form-cro, popup-cro

---

### form-cro

**Purpose**: Optimize forms that are NOT signup/registration.

**Inputs Required**:
- Form type (lead capture, contact, demo request, quote, survey)
- Current field count and completion rate
- Mobile vs desktop split
- What happens after submission

**Outputs**:
- Field-by-field optimization
- Layout recommendations
- Error handling improvements
- Multi-step form design (if applicable)
- Test hypotheses

**Key Frameworks**:
- Field Cost: 3 fields baseline; 7+ = 25-50% reduction
- Field Order: Easy first, sensitive last
- Single column > multi-column

**Files**: Extensive experiment ideas for form structure, copy, and mobile

**Related Skills**: signup-flow-cro, popup-cro, page-cro, ab-test-setup

---

### signup-flow-cro

**Purpose**: Optimize signup, registration, and trial activation flows.

**Inputs Required**:
- Flow type (free trial, freemium, paid, waitlist)
- Current steps and fields
- Completion rate and drop-off points
- Compliance requirements

**Outputs**:
- Field reduction recommendations
- Single-step vs multi-step decision
- Social auth strategy
- Mobile optimization
- Post-submit experience design

**Key Frameworks**:
- Essential fields: Email, Password
- Often needed: Name
- Usually deferrable: Company, Role, Team size, Phone

**Related Skills**: onboarding-cro, form-cro, page-cro, ab-test-setup

---

### onboarding-cro

**Purpose**: Post-signup user activation and time-to-value optimization.

**Inputs Required**:
- Product type and core value proposition
- Activation definition ("aha moment")
- Current flow and drop-off points
- Activation rate

**Outputs**:
- Activation goal definition
- Onboarding flow design
- Checklist items
- Empty state copy
- Email sequence triggers
- Metrics plan

**Key Frameworks**:
- Time-to-Value First
- One Goal Per Session
- Do, Don't Show
- Progress Creates Motivation

**Related Skills**: signup-flow-cro, email-sequence, paywall-upgrade-cro

---

### popup-cro

**Purpose**: Popup, modal, and overlay optimization.

**Inputs Required**:
- Popup purpose (email capture, lead magnet, discount, exit intent)
- Trigger type (time, scroll, exit intent, click)
- Current performance
- Mobile vs desktop split

**Outputs**:
- Popup type recommendation
- Trigger strategy
- Copy (headline, subhead, CTA, decline)
- Design specifications
- Frequency and targeting rules
- Multiple popup strategy (if needed)

**Key Frameworks**:
- Timing: Too early = annoying; Too late = missed opportunity
- Trigger Types: Time, Scroll, Exit Intent, Click, Page Count, Behavior
- Benchmarks: Email 2-5%, Exit Intent 3-10%, Click-triggered 10%+

**Related Skills**: form-cro, page-cro, email-sequence

---

### copywriting

**Purpose**: Marketing copy for pages (homepage, landing, pricing, feature, about).

**Inputs Required**:
- Page type and primary action
- Target audience
- Product/offer differentiation
- Proof points (numbers, testimonials)
- Traffic source

**Outputs**:
- Full page copy organized by section
- Headline alternatives (2-3 with rationale)
- CTA alternatives
- Meta content (title, description)

**Key Principles**:
- Clarity over Cleverness
- Benefits over Features
- Specificity over Vagueness
- Customer Language over Company Language

**Files**: `references/copy-frameworks.md`, `references/natural-transitions.md`

**Related Skills**: copy-editing, page-cro, email-sequence, popup-cro

---

### content-strategy

**Purpose**: Plan content that drives traffic, builds authority, and generates leads.

**Inputs Required**:
- Business and ICP description
- Primary goal (traffic, leads, brand awareness)
- Customer questions and objections
- Existing content and resources

**Outputs**:
- 3-5 Content Pillars with rationale
- Priority Topics with keyword targets
- Topic Cluster Map
- Prioritization scoring

**Key Frameworks**:
- Searchable vs Shareable Content
- Hub and Spoke Architecture
- Keyword Research by Buyer Stage (Awareness → Consideration → Decision → Implementation)
- Content Ideation Sources: Keywords, Call Transcripts, Surveys, Forums, Competitors

**Related Skills**: copywriting, seo-audit, programmatic-seo, social-content

---

### email-sequence

**Purpose**: Email sequences, drip campaigns, and lifecycle automation.

**Inputs Required**:
- Sequence type (welcome, nurture, re-engagement, onboarding, sales)
- Trigger event
- Audience context
- Primary conversion goal

**Outputs**:
- Sequence overview (trigger, timing, exit conditions)
- Email-by-email copy (subject, preview, body, CTA)
- Metrics plan

**Key Frameworks**:
- One Email, One Job
- Value Before Ask
- Timing: Welcome immediate, early 1-2 days, nurture 2-4 days

**Files**: `references/sequence-templates.md`, `references/email-types.md`, `references/copy-guidelines.md`

**External Dependencies**: Email platform (Customer.io, Mailchimp, Resend, SendGrid)

**Related Skills**: onboarding-cro, copywriting, popup-cro

---

### seo-audit

**Purpose**: Comprehensive SEO analysis across 7 domains with scoring.

**Inputs Required**:
- URL to audit
- Audit type (quick, full site, competitor, AI visibility)

**Outputs**:
- Scored report (0-100 per domain, weighted overall)
- Critical issues, warnings, info items
- Prioritized action plan
- Score projection

**7 Audit Domains**:
1. Technical SEO (20%)
2. On-Page SEO (20%)
3. Content Quality (15%)
4. Performance (15%)
5. Structured Data (10%)
6. Mobile Usability (10%)
7. AI Visibility (10%)

**Data Collection** (no API keys required):
- HTML via WebFetch
- robots.txt, sitemap.xml, llms.txt
- HTTP headers via curl
- PageSpeed Insights API (free)

**Files**: 7 reference files, 2 templates, scoring rubric

**Related Skills**: content-strategy, programmatic-seo, schema-markup

---

### icp-discovery

**Purpose**: Build Ideal Customer Profiles through guided discovery interview.

**Inputs Required**:
- Company context (from `22-COMPANY/about/`)
- Buyer model determination (B2B, Owner-Operator, B2C)
- Interview responses

**Outputs**:
- `ideal_customer_profile.md` with full profile
- Optional: ICP scoring card
- Per-service-line ICPs if applicable

**Buyer Models**:
- **B2B**: Companies with teams, buying committees
- **Owner-Operator**: Solopreneurs, freelancers, small business owners
- **B2C**: Individual consumers

**Files**: `references/icp_framework.md`, `references/scoring_rubric.md`

**Related Skills**: pricing-strategy, content-strategy, paid-ads

---

### pricing-strategy

**Purpose**: Pricing, packaging, and monetization strategy.

**Inputs Required**:
- Product type (SaaS, marketplace, e-commerce, service)
- Current pricing and target market
- Competitor pricing
- Go-to-market motion (self-serve, sales-led, hybrid)

**Outputs**:
- Pricing tier structure
- Value metric recommendation
- Pricing page best practices
- Price increase strategy (if applicable)

**Key Frameworks**:
- Three Pricing Axes: Packaging, Pricing Metric, Price Point
- Good-Better-Best Tier Framework
- Van Westendorp Method
- Pricing Psychology: Anchoring, Decoy Effect, Charm Pricing

**Files**: `references/tier-structure.md`, `references/research-methods.md`

**Related Skills**: page-cro, copywriting, ab-test-setup

---

### launch-strategy

**Purpose**: Product launches, feature announcements, and release strategy.

**Inputs Required**:
- What's launching (new product, major feature, minor update)
- Audience size and engagement
- Owned channels (email list, blog, community)
- Timeline

**Outputs**:
- Phase-by-phase launch plan
- Channel strategy (ORB Framework)
- Product Hunt strategy (if applicable)
- Post-launch marketing plan
- Launch checklist

**Five-Phase Approach**:
1. Internal Launch
2. Alpha Launch
3. Beta Launch
4. Early Access Launch
5. Full Launch

**ORB Framework**:
- **Owned**: Email, blog, community (build these first)
- **Rented**: Social media, app stores (drive to owned)
- **Borrowed**: Guest content, collaborations, influencers

**Related Skills**: email-sequence, page-cro, social-content

---

### programmatic-seo

**Purpose**: SEO-optimized pages at scale using templates and data.

**Inputs Required**:
- Keyword patterns to target
- Available data (proprietary, product-derived, public)
- Number of pages planned
- Technical stack

**Outputs**:
- Playbook recommendation
- Page template design
- Internal linking architecture
- Quality checklist

**12 Playbooks**:
Templates, Curation, Conversions, Comparisons, Examples, Locations, Personas, Integrations, Glossary, Translations, Directory, Profiles

**Key Principles**:
- Unique value per page (not just variable swapping)
- Proprietary data wins
- Subfolders over subdomains
- Quality over quantity

**Files**: `references/playbooks.md`

**Related Skills**: seo-audit, schema-markup, competitor-alternatives

---

### social-content

**Purpose**: Social media content strategy and creation.

**Inputs Required**:
- Platform focus (LinkedIn, Twitter/X, Instagram, TikTok, Facebook)
- Goals (brand awareness, leads, traffic, community)
- Audience and brand voice
- Time available

**Outputs**:
- Content pillars (3-5 with % allocation)
- Hook formulas
- Content calendar
- Repurposing system
- Engagement strategy

**Key Frameworks**:
- Platform Quick Reference (best for, frequency, key format)
- Hook Types: Curiosity, Story, Value, Contrarian
- Reverse Engineering Viral Content (6-step process)

**Files**: `references/platforms.md`, `references/post-templates.md`, `references/reverse-engineering.md`

**Related Skills**: copywriting, launch-strategy, email-sequence

---

### referral-program

**Purpose**: Referral and affiliate program design.

**Inputs Required**:
- Program type (customer referral vs affiliate)
- Customer LTV and current CAC
- Product shareability
- Budget for rewards

**Outputs**:
- Program design (referral loop, trigger moments)
- Incentive structure
- Launch checklist
- Email sequences
- Optimization playbook

**Key Frameworks**:
- Referral Loop: Trigger → Share → Convert → Reward → Loop
- Single-sided vs Double-sided Rewards
- Referral vs Affiliate Decision Matrix

**Files**: `references/program-examples.md`, `references/affiliate-programs.md`

**External Dependencies**: Referral platform (Rewardful, Tolt, Mention Me)

**Related Skills**: launch-strategy, email-sequence, analytics-tracking

---

## Compound Workflows

Skills are most powerful when combined. Here are proven multi-skill workflows:

### Workflow 1: Complete Campaign Launch

**Skills**: icp-discovery → content-strategy → copywriting → page-cro → paid-ads → analytics-tracking → ab-test-setup

```
Week 1: Foundation
├── icp-discovery: Define your ideal customer
├── content-strategy: Identify pain points and keywords
└── Save output to {company.marketing-context}

Week 2: Assets
├── copywriting: Create landing page copy
├── page-cro: Optimize for conversions
└── analytics-tracking: Set up conversion tracking

Week 3: Launch
├── paid-ads: Design campaign structure and ad copy
├── ga4 + gtm: Implement tracking
└── ab-test-setup: Plan landing page tests
```

### Workflow 2: SEO Content Machine

**Skills**: content-strategy → seo-audit → programmatic-seo → copywriting → schema-markup

```
Phase 1: Strategy
├── seo-audit: Baseline current SEO health
├── content-strategy: Define pillars and clusters
└── Identify programmatic opportunities

Phase 2: Build
├── programmatic-seo: Design template pages
├── copywriting: Create pillar content
├── schema-markup: Add structured data
└── seo-audit: Validate implementation
```

### Workflow 3: Conversion Funnel Optimization

**Skills**: page-cro → form-cro → signup-flow-cro → onboarding-cro → email-sequence

```
Start at the bottom of funnel (highest impact):
├── onboarding-cro: Optimize activation rate
├── signup-flow-cro: Reduce signup friction
├── form-cro: Optimize lead capture
├── page-cro: Improve landing pages
└── email-sequence: Create nurture flows
```

### Workflow 4: Product Launch

**Skills**: launch-strategy → copywriting → email-sequence → social-content → paid-ads → popup-cro

```
Pre-Launch:
├── launch-strategy: Plan phases and channels
├── copywriting: Create launch landing page
├── email-sequence: Design announcement sequence
└── popup-cro: Create early access capture

Launch:
├── social-content: Content calendar for launch week
├── paid-ads: Paid promotion strategy
└── email-sequence: Nurture new signups
```

### Workflow 5: Paid Ads Optimization Loop

**Skills**: paid-ads → analytics-tracking → ab-test-setup → page-cro → google-ads-scripts

```
Continuous Optimization:
├── paid-ads: Initial campaign setup
├── analytics-tracking: Attribution setup
├── ab-test-setup: Landing page tests
├── page-cro: Apply learnings
├── google-ads-scripts: Automate bid optimization
└── Repeat with learnings
```

### Workflow 6: Full-Funnel Growth System

**Skills**: icp-discovery → content-strategy → seo-audit → paid-ads → page-cro → signup-flow-cro → onboarding-cro → email-sequence → referral-program

```
Foundation Layer:
├── icp-discovery: Know your customer
├── content-strategy: Organic acquisition strategy
└── pricing-strategy: Monetization design

Acquisition Layer:
├── seo-audit + programmatic-seo: Organic traffic
├── paid-ads: Paid traffic
├── social-content: Social distribution
└── page-cro: Convert traffic

Activation Layer:
├── signup-flow-cro: Reduce friction
├── onboarding-cro: Drive to aha moment
└── email-sequence: Nurture to activation

Retention & Growth Layer:
├── referral-program: Viral growth
├── email-sequence: Retention campaigns
└── paywall-upgrade-cro: Monetization
```

---

## Input Files & Dependencies

### Shared Context Files

| File | Purpose | Skills That Use It |
|------|---------|-------------------|
| `{company.marketing-context}` | Company, product, audience context | ALL marketing skills |
| `{company.profile}` | Company identity | icp-discovery |
| `{company.offerings}` | What you sell | icp-discovery |
| `{company.icp}` | ICP document | content-strategy, copywriting, paid-ads |

### Per-Skill Reference Files

Most skills include `references/` folders with:
- Frameworks and templates
- Checklists and rubrics
- Example documents
- Implementation guides

### External Dependencies by Skill

| Skill | External Dependencies |
|-------|----------------------|
| **paid-ads** | Ad platform accounts (Google, Meta, LinkedIn), Conversion pixels |
| **google-ads-scripts** | Google Ads account, Google Sheets |
| **ga4** | GA4 property, gtag.js or GTM |
| **gtm** | GTM account, website access |
| **seo-audit** | None (uses free PageSpeed API) |
| **email-sequence** | Email platform (Customer.io, Mailchimp, Resend, etc.) |
| **referral-program** | Referral platform (Rewardful, Tolt, etc.) |
| **ab-test-setup** | Testing tool (Optimizely, VWO, PostHog) |

### Tool Integrations

Many skills reference a tools registry at `tools/REGISTRY.md` with integration guides for:

**Analytics**: GA4, Mixpanel, Amplitude, PostHog, Segment

**Advertising**: Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads

**Email**: Customer.io, Mailchimp, Resend, SendGrid, Kit

**Referrals**: Rewardful, Tolt, Mention Me, Dub.co

---

## Sample Workflows

### Example 1: "I need to launch a new feature"

**Prompt sequence**:

```
1. "Help me plan the launch for our new [feature]. Launch date is [date]."
   → Activates: launch-strategy
   → Output: Phase-by-phase plan, channel strategy

2. "Write the announcement email sequence"
   → Activates: email-sequence
   → Output: 3-5 email sequence with full copy

3. "Create the landing page copy for this feature"
   → Activates: copywriting
   → Output: Full page copy with alternatives

4. "Set up the tracking for this launch"
   → Activates: analytics-tracking
   → Output: Event tracking plan, UTM strategy

5. "Create social content for launch week"
   → Activates: social-content
   → Output: Content calendar with posts
```

### Example 2: "My ads aren't converting"

**Prompt sequence**:

```
1. "Audit my landing page for conversion issues: [URL]"
   → Activates: page-cro
   → Output: Issues, fixes, test ideas

2. "The form might be the problem - it has 8 fields"
   → Activates: form-cro
   → Output: Field reduction strategy, layout fixes

3. "Design an A/B test for the new form vs current"
   → Activates: ab-test-setup
   → Output: Hypothesis, sample size, metrics

4. "Rewrite the headline and CTA copy"
   → Activates: copywriting
   → Output: 3 headline alternatives, 3 CTA alternatives

5. "Set up proper conversion tracking"
   → Activates: analytics-tracking + ga4
   → Output: Event setup, attribution configuration
```

### Example 3: "Build my content strategy from scratch"

**Prompt sequence**:

```
1. "Let's define my ICP first"
   → Activates: icp-discovery
   → Output: Comprehensive ICP document

2. "Create a content strategy based on this ICP"
   → Activates: content-strategy
   → Output: Pillars, clusters, priority topics

3. "Run an SEO audit on my current site"
   → Activates: seo-audit
   → Output: Scored report, opportunities

4. "Design a programmatic SEO approach for [pattern]"
   → Activates: programmatic-seo
   → Output: Template, data requirements, architecture

5. "Write the pillar page for [topic]"
   → Activates: copywriting
   → Output: Full page copy
```

### Example 4: "Improve my signup conversion rate"

**Prompt sequence**:

```
1. "Audit my signup flow - here's the current process: [description]"
   → Activates: signup-flow-cro
   → Output: Field reduction, UX improvements

2. "Now optimize what happens after signup"
   → Activates: onboarding-cro
   → Output: Activation definition, checklist design

3. "Create the onboarding email sequence"
   → Activates: email-sequence
   → Output: 5-7 email sequence

4. "Design re-engagement for users who don't activate"
   → Activates: email-sequence
   → Output: Recovery sequence

5. "Set up the tracking for this funnel"
   → Activates: analytics-tracking
   → Output: Funnel events, drop-off tracking
```

---

## Best Practices

### 1. Create Product Marketing Context First

Before using any skill extensively, create `{company.marketing-context}`:

```markdown
# Product Marketing Context

## Company
- Name: [Company Name]
- What we do: [One sentence]
- Category: [Market category]

## Product
- Core value proposition: [Primary benefit]
- Key differentiators: [1-3 unique aspects]
- Primary use cases: [Top 3]

## Audience
- ICP: [Description]
- Key pain points: [Top 3]
- Buying triggers: [What makes them buy now]

## Voice & Tone
- Brand personality: [3-5 adjectives]
- Formality level: [Casual/Professional/Formal]
- What to avoid: [Topics, phrases, approaches]
```

### 2. Follow Skill Relationships

Each skill documents related skills. Use them:
- `page-cro` recommends `ab-test-setup` for testing changes
- `copywriting` recommends `copy-editing` for polish
- `signup-flow-cro` connects to `onboarding-cro`

### 3. Work Bottom-Up on Funnels

Start optimizing at the bottom of funnel (highest impact):
1. Onboarding/activation first
2. Then signup
3. Then landing pages
4. Then traffic sources

### 4. Use Sub-Agents for Heavy Lifting

Several skills are designed to spawn sub-agents:
- `seo-audit`: Parallel analysis of 7 domains
- `business-baseline`: Diagram generation
- Complex skills with multiple outputs

### 5. Track What You Build

After implementing any skill output:
1. Use `analytics-tracking` to measure
2. Use `ab-test-setup` to validate
3. Document learnings in your vault

---

## Troubleshooting

### "Skill isn't activating"

- Use exact trigger phrases from the skill description
- Be specific about what you want
- Try: "I want to [exact skill name]..."

### "Missing context"

- Create `{company.marketing-context}`
- Answer the skill's initial questions fully
- Provide URLs, metrics, and examples

### "Output isn't actionable"

- Provide more specific inputs
- Ask follow-up questions
- Request specific formats ("give me the email copy" vs "help with email")

### "Skill asks too many questions"

- Front-load context in your prompt
- Use {company.marketing-context}
- Provide: audience, goal, constraints, current state

---

## Appendix: Skill Quick Reference

| Skill | Primary Use Case | Key Output |
|-------|-----------------|------------|
| paid-ads | Ad campaigns | Campaign structure, ad copy |
| google-ads-scripts | Google Ads automation | JavaScript code |
| ab-test-setup | Experiment design | Hypothesis, sample size |
| analytics-tracking | Tracking implementation | Event plan, UTM strategy |
| ga4 | GA4 setup | Implementation guide |
| gtm | Tag Manager | Container config |
| page-cro | Page conversion | Audit, fixes, tests |
| form-cro | Form optimization | Field optimization |
| signup-flow-cro | Signup optimization | Flow redesign |
| onboarding-cro | User activation | Onboarding design |
| popup-cro | Modal optimization | Popup design |
| copywriting | Marketing copy | Page copy |
| copy-editing | Copy improvement | Edited copy |
| content-strategy | Content planning | Pillars, topics |
| email-sequence | Email automation | Email sequence |
| social-content | Social media | Content calendar |
| seo-audit | SEO analysis | Scored report |
| programmatic-seo | Pages at scale | Template design |
| schema-markup | Structured data | JSON-LD code |
| icp-discovery | Customer profile | ICP document |
| pricing-strategy | Pricing design | Tier structure |
| launch-strategy | Product launch | Launch plan |
| competitor-alternatives | Comparison content | Page framework |
| referral-program | Viral growth | Program design |
| paywall-upgrade-cro | Monetization | Upgrade flow |
| free-tool-strategy | Lead generation | Tool strategy |

---

*This guide is a living document. As skills evolve, update this reference.*
