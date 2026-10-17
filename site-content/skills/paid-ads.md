---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: paid-ads — ThirdBrain BOB skill
  description: Create, optimize, and scale paid advertising campaigns across Google Ads, Meta, LinkedIn, and other platforms. Covers campaign strategy, ad creation, audience t
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: paid-ads
catLabel: marketing-ads
area: marketing
desc: Plans paid advertising campaigns, writes ad copy, defines audience segments, structures tests, analyzes performance metrics, and recommends bidding and optimization…
summary: Create, optimize, and scale paid advertising campaigns across Google Ads, Meta, LinkedIn, and other platforms. Covers campaign strategy, ad creation, audience targeting, and optimization.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing]'
inputs:
- profile — Business model and product type; carries the `regions[]` field that gates the regional-context check.
- icp — Target audience the campaign is built around.
- marketing-context — Positioning and channel mix the platform choice has to stay consistent with.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- objective — Primary campaign goal. It decides which platforms are viable, which bid strategy is offered, and which metric the plan is graded on. (awareness | traffic | leads | sales | app-installs)
- budget — Spend available per month or week, used to size the 70/30 proven-versus-testing split and the number of ad sets.
- target-cpa — Target CPA or ROAS the structure must be buildable against. Absent, the plan names the assumption it used instead.
- request — The planning question to answer, including platforms, offers, or budgets already ruled in or out.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Product and business model the copy is describing.
- icp — Audience whose problem the hook has to name in their own words.
- marketing-context — Positioning and differentiation the copy must not contradict.
- region-context — Regional advertising rules and claim restrictions that constrain what the copy may say.
- platform — Ad platform the copy is written for. It fixes the character limits, asset counts, and native tone — Google RSA output follows `references/rsa-output-spec.md`. (google-ads | meta | linkedin | twitter-x | tiktok)
- offer — What the ad promotes — product, free trial, lead magnet, or demo — and why it is compelling.
- landing-page — Destination URL the copy must stay consistent with, so the ad promise and the post-click page match.
- request — The creative brief — variant count, framework preference, and any angle already ruled out.
- profile — Business model and product type that set which targeting signals are meaningful.
- icp — Ideal customer profile the segment definitions are derived from.
- marketing-context — Channels and competitor set used to size audiences and choose exclusions.
- region-context — Geographic and regulatory limits on targeting in the market being advertised into.
- platform — Ad platform the segments are built in. It fixes which targeting primitives exist — keywords, interests, job titles — and the minimum viable audience size. (google-ads | meta | linkedin | twitter-x | tiktok)
- customer-data — Existing customer export used as the lookalike seed and the suppression list. Absent, the route builds interest or keyword audiences instead and says so.
- request — The targeting problem to solve — new segments, exclusion cleanup, or retargeting window design.
- performance-data — Campaign metrics — impressions, clicks, conversions, spend, CPA, CTR, frequency
- performance-export — Platform reporting export the metrics are quoted from, so every figure carries a named source, attribution window, and date range per the evidence-discipline constraint.
- target-cpa — Target CPA or ROAS goal
- aov — Average order value for profitability check
outputs:
- Headline, description, and CTA variants per platform, each labelled with the framework and angle it tests. `scope` is always required, so this route never falls back to the scratch area (`output.scratch`).
- Per-campaign Red/Yellow/Green grade with its kill, hold, or scale action, the fatigue differential result, funnel diagnosis, and the profitability check. `scope` is always required, so this route never falls back to the scratch area (`output.scratch`).
- Platform selection, account and campaign structure, naming convention, budget allocation, test plan, and the measurement setup the campaign is graded on. `scope` is always required, so this route never falls back to the scratch area (`output.scratch`).
- Segment definitions with their build criteria, lookalike seed and rationale, retargeting windows by funnel stage, and the exclusion list. `scope` is always required, so this route never falls back to the scratch area (`output.scratch`).
prompts:
- Plan a Google Ads campaign for our SaaS product launch
- Write ad copy for our Facebook retargeting campaign
- Analyze our ad performance and recommend optimizations
- Structure an A/B test for our LinkedIn ad creative
- Design audience segments for our Meta ads campaign
---
