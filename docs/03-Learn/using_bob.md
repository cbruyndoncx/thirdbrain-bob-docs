---
title: Using BOB — Day-to-Day Patterns
---

# Using BOB — Day-to-Day Patterns

How to actually work with BOB once it's installed. Covers the core patterns: asking questions, invoking skills, reviewing output, and saving results back to the vault.

> Prerequisite: completed [quickstart](../02-Setup/quickstart.md) — your install is verified.

---

## The Core Loop

Every interaction with BOB follows the same shape:

```
1. You ask a question or describe a task in Obsidian's Agent Client panel
2. BOB picks a skill (or asks which one to use)
3. BOB asks clarifying questions if needed
4. BOB does the work — reads vault, drafts content, runs analysis
5. BOB returns the output. Depending on the workflow, some files are saved during the run (paths shown in the output); others are returned as a draft for you to save explicitly
6. You review the output, check the paths it wrote to, edit if needed, and save anything still in draft (or send back for revisions)
```

The vault is both BOB's **input** (it reads your context) and **output** (some workflows save artifacts during the run; others return a draft for you to save). When in doubt, check the output paths the run reported — if no path is shown, the draft hasn't been saved yet.

---

## Three Ways to Invoke BOB

### 1. Natural-language request

Just describe what you want:

```
Draft a follow-up email to the prospect we met last Tuesday
```

BOB infers the right skill (`cold-email` or `email-sequence`), reads recent meeting notes, and drafts the email.

**When to use:** Most of the time. BOB is good at picking skills.

---

### 2. Explicit skill name

Reference a skill directly with `/`:

```
/proposal-writer
```

BOB loads that skill and runs its workflow (asking you for inputs).

**When to use:** When you know exactly which skill you want, or BOB picked the wrong one.

**See available skills:** [SKILLS](../skills/index.md) (vault root — auto-generated index of all installed skills).

**See what you bought:** SKILL-CATALOGUE-MAP — a visual catalogue of your package, tier first,
then by category and by value chain.

**See how it fits together:** SKILL-PIPELINE-MAP — one page per business area, showing the
stages in order, which skills run at each, and which of them call each other.

Both are regenerated from the skill library on every release, so they never go stale.

---

### 3. Playbook (multi-step recipe)

For repeatable workflows that chain multiple skills:

```
Run the new-client-onboarding playbook
```

BOB executes the playbook step-by-step, with checkpoints between steps.

**When to use:** Recurring multi-step processes. See [playbooks](Concepts/playbooks.md) to learn the concept.

---

## Where Results Are Saved

BOB respects vault structure. Outputs go to predictable locations:

| Output type | Saved to |
|-------------|----------|
| Client deliverable | `{client.projects}` |
| Marketing content | `{company.marketing}/{channel}/` |
| Internal research | `{resource.root}` |
| Personal note / inbox | `{me.inbox}` |
| Meeting notes | `*/20-MEETINGS/` (under the relevant scope) |
| Tasks | `{output.tasks}` |

BOB always tells you where it's saving before it writes. You can override the path.

---

## Patterns That Work Well

### Bring your own context

BOB is sharper when you point it at relevant files:

```
Using the customer notes in {company.clients}/acme-corp/, draft an upsell proposal
```

vs.

```
Draft an upsell proposal
```

The first version produces a tailored draft; the second produces a generic template.

---

### Iterate, don't restart

If the first answer isn't right, push back in the same conversation:

```
Good draft. Make it shorter and remove the intro paragraph.
```

Don't start a new conversation — BOB loses the thread context.

---

### Save what's good, discard what's not

Some workflows save during execution; others return a draft. Check the output paths the run reports — if a draft you wanted saved isn't there, ask BOB to save it. If the draft is 80% there, save it and edit in Obsidian directly. Don't spend three rounds asking BOB for tiny tweaks — it's faster to edit yourself.

---

### Keep the vault tidy

BOB reads the vault to find context. A messy vault produces noisy answers.

- Routine: review `{me.inbox}` weekly; move or archive
- Routine: tag and link new notes when you create them
- Use the `obsidian-ops` skills for periodic cleanup

---

## Patterns to Avoid

| Don't | Why |
|-------|-----|
| Ask BOB to do something it has no skill for | It will hallucinate. Check [SKILLS](../skills/index.md) first. |
| Paste secrets/API keys into the chat | They'll be sent to the AI provider. Use `.env` for credentials. |
| Treat output as final without reviewing | BOB drafts; **you** approve. Always review business-critical output. |
| Run BOB on a stale vault | If `{company.clients}/acme/` is 6 months out of date, BOB's "current state" advice will be wrong. Update the vault first. |

---

## Switching AI Models

BOB works with Claude (default), OpenAI, Gemini, and others. Switch in the Agent Client panel's model selector.

**When to switch:**
- Cost — Haiku/Mini variants are cheaper for simple drafts
- Latency — local models (via Ollama) for sensitive content
- Capability — Opus/GPT-5/Gemini Ultra for complex reasoning

The vault, skills, and your prompts stay the same. Only Layer 4 (the model) changes.

---

## Getting Better Over Time

BOB improves as your vault matures:

- **Week 1:** generic answers, lots of clarifying questions
- **Month 1:** answers tailored to your domain (after you've added company profile, clients, processes)
- **Month 3+:** BOB references your past decisions, prior client work, and your writing style

The vault is a flywheel. The more you use it, the smarter BOB gets.

---

## Related

- [quickstart](../02-Setup/quickstart.md) — First-run verification
- [bob_overview](../01-BOB/Onboarding/bob_overview.md) — Conceptual foundation
- [playbooks](Concepts/playbooks.md) — Multi-step workflows
- [what_is_jtbd](Concepts/what_is_jtbd.md) — Jobs-to-be-Done framing
- [SKILLS](../skills/index.md) — Auto-generated index of installed skills
- SKILL-CATALOGUE-MAP — Visual catalogue of your package by tier, category and value chain
- SKILL-PIPELINE-MAP — What runs after what, one page per business area
