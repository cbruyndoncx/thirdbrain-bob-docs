---
description: 'Target Audience: Vault owners and operators deciding whether a task, prompt, or skill can run on a cheaper model without losing acceptable output quality.'
title: model-cost-benchmark
---

# model-cost-benchmark

Target Audience: Vault owners and operators deciding whether a task, prompt, or skill can run on a cheaper model without losing acceptable output quality.

- **Area:** Foundational
- **Category:** utilities
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Product Manager, Operations Manager

Runs the same task across several models and reports measured cost, tokens, and latency so a cheaper model can be adopted with evidence.

## How you ask

- “Can this skill run on Haiku instead of Opus?”
- “Compare Haiku, Sonnet and Opus on this prompt and tell me what it costs”
- “Benchmark this task across Claude and Gemini”
- “Is Opus actually worth it for this job?”

## Inputs

- task — The prompt to benchmark, inline or as a file
- models — Comma-separated provider:model specs (default claude:haiku,claude:sonnet,claude:opus)
- results_dir — Directory produced by the run route
- instructions — Cacheable prefix tokens per run (system prompt + auto-loaded context + skill)
- output_tokens — Output tokens per run, measured from a benchmark run
- batch_size — Runs sharing one cache window; 1 (default) means isolated scheduled runs where the cache never hits
- skill — Skill whose behaviour is being baselined
- results_dir — Benchmark run directory to promote, or the new run to check; omit on check for a staleness-only pass
- baseline — Existing baseline JSON to check against
- results_dir — Directory to clean, passed via --cleanup

## Outputs

- baseline (json)
- benchmark-results (json)
- lever-comparison (text)
- metrics-summary (markdown)
- prefer a permanent directory)
- pruned-dir (directory)
- recommendation (markdown)
- regression-delta (text)
- stdout
- {skills.root}/{skill}/baselines/{name}.json

