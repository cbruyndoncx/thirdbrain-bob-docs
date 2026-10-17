---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ab-test-setup — ThirdBrain BOB skill
  description: Design A/B tests that produce statistically valid, actionable results.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ab-test-setup
catLabel: marketing-funnel
area: marketing
desc: Marketing-focused A/B testing — calculates sample sizes, structures hypotheses, designs variant copy, and analyzes test results.
summary: Design A/B tests that produce statistically valid, actionable results.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- request — The change under consideration and the outcome it is meant to move — the raw material for the hypothesis statement.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Business model and target market used to decide which surface and audience the test runs on.
- marketing-context — Positioning and current funnel metrics that ground the observation clause of the hypothesis.
- baseline-metrics — Current conversion rate and traffic volume on the tested surface. Absent, the route asks for them before it can size the test.
- request — The test being prepared and the part of the setup that is in doubt — variant logic, instrumentation, or QA.
- ab-test-plan — Plan from the `planning` route, read back so the readiness check is made against the hypothesis, metrics, and sample size that were actually committed to.
- marketing-context — Existing measurement setup and funnel definitions the variant tracking has to line up with.
- request — The test being read out and the decision the readout has to support.
- results-data — Observed exposures and conversions per variant. Without them the route cannot check sample sufficiency or significance and must not call the test.
- ab-test-plan — Plan from the `planning` route, read back so the result is judged against the pre-committed sample size and primary metric rather than a metric chosen after the fact.
- request — The change the user wanted to test and the surface it sits on.
- baseline-metrics — Traffic volume and baseline conversion rate — the numbers that establish the test cannot reach significance and bound what a directional read can claim.
- profile — Business model and target market used to judge which bolder change is worth making without a statistical read.
outputs:
- Hypothesis, variant definitions, primary/secondary/guardrail metrics, sample size and duration, traffic allocation, owners, and launch dependencies.
- Per-item verdict on the pre-launch checklist, the blocking gaps in variant logic or tracking, and the go/no-go call.
- Running log of every experiment run, appended with this test's hypothesis, decision, and learning.
- Sample and significance check, effect size against the MDE, secondary and guardrail readings, segment differences, the decision, and the learnings.
- The stated statistical limitation, the directional test or bolder change proposed instead, the metric that would call it, and the next concrete action.
- '{scope.marketing}/experiments/ab-test-log.md'
- '{scope.marketing}/experiments/ab-test-plan-{test-name}.md'
- '{scope.marketing}/experiments/ab-test-results-{test-name}.md'
prompts:
- Design an A/B test for our pricing page layout
- Calculate the sample size needed for testing our new checkout flow
- Structure a hypothesis for testing shorter signup forms
- Analyze my A/B test results — variant B had 4.2% vs control 3.8%
---
