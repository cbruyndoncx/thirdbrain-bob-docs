---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: decision-frameworks — ThirdBrain BOB skill
  description: Applies structured analytical frameworks — expected value thinking, regret minimization, and pre-mortems — to difficult decisions. Use when user wants a specifi
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: decision-frameworks
catLabel: product-management
area: strategy
desc: Applies structured analytical frameworks — expected value thinking, regret minimization, and pre-mortems — to difficult decisions.
summary: Applies structured analytical frameworks — expected value thinking, regret minimization, and pre-mortems — to difficult decisions. Use when user wants a specific framework applied, mentions 'decision framework,' 'expected value,' 'pre-mortem,' or 'decision paralysis.' For 1:1 strategic coaching with personal context, see ask-zeus. For multi-perspective board debate, see ask-boardroom.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- request — The decision to structure, its owner, its deadline, and the options already on the table.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- reversibility-triage — Output of the `reversibility-assessment` route, read back so the chosen depth of analysis is justified rather than assumed.
- request — The choice to compare and what is already known to be unknown about it.
- request — The options to price, plus any probability, upside, or cost figures the caller already holds.
- request — The choice and the time horizon the caller wants to be judged against.
- request — The plan or commitment to stress, and the horizon at which failure is imagined.
- preferred-option — The option already favoured — the pre-mortem has nothing to attack without it.
- decision-brief — Brief from the `full-decision` or `lightweight` route, read back so the failure modes attack the recorded assumptions rather than freshly invented ones.
- request — The decision to classify and what undoing it would cost in time, money, and credibility.
outputs:
- Decision statement, options table, per-option assumptions with confidence labels, analysis under each framework, recommendation, success criteria, and review trigger.
- Door type, the cost and latency of reversal, and the recommended analysis depth or bias-to-action call.
- Imagined failure narrative, ranked failure modes with their causes, and a mitigation or early-warning signal for each.
- Options table, the dimensions they differ on, the uncertainty warning, and what evidence would upgrade the comparison to a full brief.
- Per-option expected-value calculation with each probability and value driver labelled by source and confidence.
- Per-option regret assessment at the stated horizon and the asymmetry that decides between them.
- '{scope.knowledge-base.product}/decision-frameworks-reversibility-{YYYY-MM-DD}.md'
- '{scope.knowledge-base.product}/decision-frameworks-{YYYY-MM-DD}.md'
prompts:
- Help me decide using expected value thinking
- Run a pre-mortem on our product launch plan
- Apply regret minimization to this career decision
- I'm stuck between two options — help me think it through
---
