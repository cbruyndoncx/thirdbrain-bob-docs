---
type: knowledge-base
title: "Quickstart — Your First 5 Minutes with BOB"
status: final
created: 2026-04-28
modified: 2026-04-28
tags: [bob, quickstart, userguide]
---

# Quickstart — Your First 5 Minutes with BOB

For users who already have BOB installed (done-for-you setup, or after completing [[getting_started]]). This page verifies the install works and shows your first real query.

> If you don't have BOB installed yet → start with [[getting_started]] (vault root) instead.

---

## Step 1 — Open the vault in Obsidian (30 sec)

1. Open Obsidian
2. Choose this vault from the vault picker
3. The sidebar shows the vault's top-level folders — on the default layout `00-CORE/`, `10-ME/`, `20-COMPANY/`, etc.

✅ If you see those folders, the vault loaded correctly.

---

## Step 2 — Open the Agent Client panel (30 sec)

1. In Obsidian, open the **Command Palette** (`Ctrl+P` / `Cmd+P`)
2. Type `Agent Client` and select **Agent Client: Open**
3. A side panel opens with a chat-style interface

✅ If the panel opens and shows a model selector, the ACP plugin is working.

If the panel doesn't open: see [[02-Setup/AI-Tools/agent-client-installation]].

---

## Step 3 — Ask BOB a sanity-check question (1 min)

Type this exactly into the Agent Client panel:

```
List the top-level folders in this vault and tell me what each is for.
```

Press Enter. Within ~10 seconds you should see BOB:
- Read the vault structure
- Return a short description of each top-level folder (`{vault.core}`, `{me.root}`, `{company.root}`, `{company.clients}`, `{resource.root}`)

✅ If you got a sensible answer, all 4 layers are working: Obsidian → ACP → Claude Code → AI model.

If BOB errors out or hangs: see **Troubleshooting** below.

---

## Step 4 — Ask BOB something useful (2 min)

Now try a real business question. Pick one:

| Try this | What happens |
|----------|--------------|
| `Help me draft a 3-line cold email for a B2B SaaS prospect` | BOB picks the `cold-email` skill, asks 1–2 clarifying questions, drafts copy |
| `What skills do you have for sales?` | BOB lists relevant skills from the library (~100+ for starter vault) |
| `Summarize what's in 40-RESOURCES/` | BOB reads the folder and returns a topic map |
| `Walk me through setting up my company profile` | BOB invokes onboarding flow |

✅ You're now using BOB.

---

## Step 5 — Where to go next (1 min)

| Goal | Read |
|------|------|
| Understand what BOB is and how it works | [[01-BOB/Onboarding/bob_overview]] |
| Learn day-to-day usage patterns | [[using_bob]] |
| Browse all available skills | [[SKILLS]] (vault root — auto-generated index) |
| Customize for your business | Add company info to `{company.profile-root}` |
| Add your first client | Use the `create-client` skill |
| Have agents check every note they write | [[install-agent-hooks]] (once per machine) |

---

## Troubleshooting

| Symptom | Guide |
|---------|-------|
| Agent Client panel won't open, API key errors | [[ts_agent_client]] |
| Skills not found, symlink broken | [[ts_skills]] |
| Vault folders missing, trust prompt skipped | [[ts_vault]] |
| "command not found", plugins not loading | [[ts_install]] |

For environment verification, see [[01-BOB/Onboarding/environment_checklist]].

---

## Related

- [[start_here]] — Pick a longer learning path
- [[01-BOB/Onboarding/MOC-bob_onboarding]] — Conceptual onboarding
- [[using_bob]] — Day-to-day patterns
