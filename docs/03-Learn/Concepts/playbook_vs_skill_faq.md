---
title: 'FAQ — Playbook vs Skill: How to Decide'
---

# Playbook vs Skill — How to Decide

Skills and playbooks both live in the vault. They look similar at a glance — both are reusable, both can be triggered by name, both produce work. But they solve different problems. This FAQ helps you pick the right one when you build something new, and explains why playbooks exist at all.

> Background reading: [playbooks](playbooks.md) for the full mechanics, [what_is_jtbd](what_is_jtbd.md) for the thinking behind playbooks.

---

## The One-Line Difference

- **Skill** = *how* to do **one thing** well (write a cold email, score content, run an SEO audit).
- **Playbook** = *what* needs to happen **end-to-end** to finish a real job (sequences skills, adds human checkpoints, defines "done").

Skills are verbs. Playbooks are sentences. If you find yourself writing "first do A, then B, then check with the human, then C" — that's a playbook, not a skill.

---

## The Decision Test

Ask these questions in order. Stop at the first "yes."

| # | Question | If yes → |
|---|----------|----------|
| 1 | Does the work involve **more than one skill** in a defined order? | **Playbook** |
| 2 | Are there **human decision points** between steps (review, approve, pick option)? | **Playbook** |
| 3 | Is there a **quality gate** the final output must pass before it's "done"? | **Playbook** |
| 4 | Does it need **multiple context files** loaded up front (brand voice + ICP + template)? | **Playbook** |
| 5 | Is it a **single, self-contained capability** with one clear output? | **Skill** |
| 6 | Could it be **reused as a building block** inside a larger job? | **Skill** |

Rule of thumb: if a competent operator could do the whole job in one sitting using one tool, it's a skill. If they'd need a checklist taped to the wall, it's a playbook.

---

## Quick Examples

| Job | Skill or Playbook? | Why |
|-----|--------------------|-----|
| Write a LinkedIn post from a topic | Skill (`social-content`) | One input, one output, no human checkpoints |
| Score content against the rubric | Skill (`content-scorer`) | Single capability, reusable inside larger flows |
| Publish a YouTube video end-to-end | Playbook | Strategy → script → thumbnail → description → social — multiple skills, human review points, quality gate |
| Onboard a new client | Playbook | Profile setup, kickoff meeting, deal record, intro email, project folder — sequenced steps with handoffs |
| Run a monthly close | Playbook | Capture → reconcile → review → report — recurring, multi-step, gated by approval |
| Generate a thumbnail image | Skill (`ai-image-gen`) | One ask, one render, used inside many playbooks |

If a "skill" you're sketching has more than ~3 steps with branches and waits, it's a playbook in disguise. Split it.

---

## Why Playbooks Exist — The Advantages Over Skills Alone

Skills alone leave the human as the orchestrator. Playbooks shift that load into the vault.

### 1. The vault remembers the sequence — you don't

With skills only, you have to remember which to call, in what order, with what inputs. Forget a step (e.g. score the content before publishing) and quality drops silently. Playbooks encode the order once, so it's right every time.

### 2. Context is pre-loaded, not hunted

Every playbook lists `Required Context` — brand voice, ICP, templates, prior decisions. The agent loads them up front. With skills alone, you re-explain context every run, and details drift.

### 3. Human checkpoints are explicit, not improvised

Playbooks mark each step `(HUMAN)` or `(AGENT)`. The agent runs the agent steps autonomously and **stops** at human steps with a clear `awaiting:` prompt. You're never surprised by an autonomous decision, and you're never blocking on a step the agent could have done.

### 4. Quality gates make "done" objective

A skill produces an output. A playbook produces an output **that has passed a defined standard** — e.g. content-scorer must return 75+, all human reviews complete. No more "I think it's done" — the gate decides.

### 5. Progress is visible

Running playbooks become TaskNotes with `remaining-steps` and `awaiting`. The `playbooks-in-flight` Base view shows what's running, what's blocked on you, what's almost done. With skills alone, in-flight work lives in your head.

### 6. They scale knowledge across people

A playbook is the documented way the business does something. A new team member runs the playbook and produces work to standard on day one. Skills give them tools; playbooks give them the process.

### 7. They can be customized per scope without losing the recipe

A library playbook (`Publish YouTube content piece`) can be overridden at company, personal, or client scope — different context files, different quality gate, same backbone. Skills don't have this hierarchy; they're the same everywhere.

### 8. They turn ad-hoc work into a repeatable process

The first time you run a job, you're inventing the sequence. The second time, you should be running a playbook. Codifying the sequence is the moment work stops being craft and starts being operations.

---

## Why Skills Still Matter — Don't Over-Playbook

Playbooks are not better than skills. They depend on skills. A common mistake is wrapping a single skill in a playbook just to feel organized — that adds ceremony without value.

Build a skill when:

- The capability is genuinely **one thing** (one clear output, no branches).
- It will be **reused inside multiple playbooks** (a good skill earns its keep across jobs).
- The user wants to call it directly without the overhead of starting a playbook run.

Build a playbook when:

- The job needs **multiple skills**, or skills + human steps, in a specific order.
- The job recurs and you want it done **the same way every time**.
- "Done" requires a **quality bar**, not just step completion.

---

## Common Mis-shapes to Avoid

| Mis-shape | Symptom | Fix |
|-----------|---------|-----|
| Mega-skill | A "skill" with 8 internal steps, branches, and human review points | Split into 3-5 skills + a playbook that sequences them |
| Mini-playbook | A playbook with one step that just calls one skill | Delete the playbook — call the skill directly |
| Skill that needs context | A skill that requires brand voice + ICP + product context loaded every run | Wrap it in a playbook that loads context once |
| Hidden quality gate | A playbook with no `Quality gate` section | Add one — otherwise "done" is fuzzy and rework leaks downstream |

---

## Where to Look

- All skills: [SKILLS](../../skills/index.md)
- All playbooks: [PLAYBOOKS](playbooks.md)
- Where each fits in the business: VALUE-CHAINS
- Mechanics of how playbooks run: [playbooks](playbooks.md)
- The thinking behind jobs and recipes: [what_is_jtbd](what_is_jtbd.md)

Routing rule: *"How does the business choose?"* → operating-controls. *"How does work flow?"* → value chain. *"What do I do now?"* → skill or playbook.
