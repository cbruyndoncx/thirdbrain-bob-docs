---
type: reference
title: ThirdBrain Onboarding Wizard
status: draft
created: 2026-04-11
modified: 2026-08-31
tags:
  - onboarding
  - thirdbrain
  - wizard
related:
  - "[[vault-intro/SKILL.md|vault-intro]]"
---

# ThirdBrain Onboarding Wizard

> Click any button below to open a guided conversation with your AI agent. Each step builds on the last — work through them in order, or jump to what you need.

---

## Before You Start

Make sure the **Agent Client** panel is visible in your sidebar (click the robot icon or run `Agent Client: Open chat view` from the command palette).

---

## Phase 1: Know Yourself (L1 → L2)

> *Get your knowledge out of your head and into the vault.*

### Step 1: Vault Tour

Get oriented — learn how the vault works, where things go, and see files appear in real-time.

```dataviewjs
const btn = dv.el("button", "▶ Take the Vault Tour");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#7c3aed; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `/vault-intro start`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

### Step 2: Build Your Personal Context

Tell the AI about yourself — your role, values, working style, and constraints. This shapes how every skill responds to you.

```dataviewjs
const btn = dv.el("button", "▶ Build My Profile");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#7c3aed; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Run /personal-context-builder — I want to build my personal context. Start with the guided interview.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

### Step 3: Map Your Business

Walk through a structured interview that maps your business model, revenue, operations, and team into a visual baseline.

```dataviewjs
const btn = dv.el("button", "▶ Map My Business");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#7c3aed; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Run /business-baseline — I want to map my business operations. Start with the Progressive Interview to understand my business before creating any diagrams.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

---

## Phase 2: Get Structured (L2 → L3)

> *Turn files into connected, queryable data.*

### Step 4: Create Your First Client

Set up a properly structured client workspace with profile, contacts, and project folders.

```dataviewjs
const btn = dv.el("button", "▶ Create a Client");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#2563eb; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Help me create my first client workspace. Ask me for:
1. Client company name
2. A short kebab-case ID (e.g. "acme-corp")
3. Industry and location
Then run the create-client script to set up their folder structure.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

### Step 5: Add People & Meetings

Learn the pattern: create a person, log a meeting, link them together.

```dataviewjs
const btn = dv.el("button", "▶ Add People & Meetings");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#2563eb; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Walk me through adding contacts and meeting notes to my vault:
1. Create a person note for a key contact (ask me for their details)
2. Create a meeting note linked to that person
3. Show me how Dataview queries let me find all meetings with this person later

Use the vault's data model and templates.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

### Step 6: Check Your Vault Health

Run a quick audit to see how well your vault is structured so far.

```dataviewjs
const btn = dv.el("button", "▶ Audit My Vault");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#2563eb; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Run /obsidian-ops assessment — audit my vault for orphaned notes, missing metadata, broken links, and tag inconsistencies. Give me a health score and the top 5 things to fix.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

---

## Phase 3: Put Skills to Work (L3 → L4)

> *Let AI handle the first pass. You review and refine.*

### Step 7: Run a Website Audit

See a full skill in action — audit any website for SEO, performance, and content quality.

```dataviewjs
const btn = dv.el("button", "▶ Audit a Website");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#059669; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Run /website-audit — ask me for the URL of a website I want to audit. Then run a comprehensive audit covering SEO, content, performance, and UX.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

### Step 8: Research a Prospect

Run a full prospect audit — company research, decision maker mapping, and lead scoring.

```dataviewjs
const btn = dv.el("button", "▶ Research a Prospect");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#059669; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Run /prospect-audit — ask me for a company name and URL. Research them thoroughly and produce a prospect profile with lead score, key contacts, and recommended approach.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

### Step 9: Write a Proposal

Draft a client proposal using your vault context — client profile, meeting notes, and business baseline feed into the output.

```dataviewjs
const btn = dv.el("button", "▶ Draft a Proposal");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#059669; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Run /proposal-writer — I want to draft a proposal for a client. Ask me which client (or help me pick from existing clients in the vault), what the engagement is about, and any meeting transcripts or notes to reference.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

---

## Phase 4: Chain & Govern (L4 → L6)

> *Skills feeding skills. Quality you can measure.*

### Step 10: Run Your First Playbook

Execute a multi-step workflow where skills chain together automatically.

```dataviewjs
const btn = dv.el("button", "▶ Run a Playbook");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#dc2626; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Show me the available playbooks in the vault and help me run one. I want to see how multiple skills chain together into an end-to-end workflow. Recommend a playbook based on what I've set up so far.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

### Step 11: Quality Check Your Work

Run the QMS quality loop on any deliverable you've created.

```dataviewjs
const btn = dv.el("button", "▶ Quality Check");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#dc2626; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Run /qms-qa-loop on the most recent deliverable I created. Score it against the appropriate rubric, generate a revision checklist if it needs work, and explain the quality system.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

---

## What's My Level?

Take the ThirdBrain Maturity Model self-assessment — seven levels, from knowledge living in your head (L1) to a system that compounds across engagements (L7):

```dataviewjs
const btn = dv.el("button", "▶ Assess My Maturity Level");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#f59e0b; color:black; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `Help me assess my ThirdBrain maturity level. Walk me through these 6 statements one at a time, ask me to honestly evaluate each, and tell me what level I'm at:

1. I can explain my full business model in a document someone else can read (L2+)
2. My client data follows a consistent structure with standard fields (L3+)
3. I use AI to produce first drafts of proposals, reports, or audits (L4+)
4. Multiple AI skills chain together in my workflows without manual handoff (L5+)
5. Every client deliverable passes through a quality rubric before delivery (L6+)
6. My system references prior engagements and research when starting new work (L7)

After the assessment, recommend which steps in the onboarding wizard I should focus on next.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```

---

## Need Help?

```dataviewjs
const btn = dv.el("button", "💬 Ask a Question");
btn.style.cssText = "padding:10px 20px; cursor:pointer; background:#6b7280; color:white; border:none; border-radius:8px; font-size:14px; font-weight:600;";
btn.addEventListener("click", async () => {
  const prompt = `I'm working through the ThirdBrain onboarding wizard and I have a question. Let me describe what I'm stuck on.`;
  const plugin = app.plugins.plugins['agent-client'];
  await plugin.openNewChatViewWithAgent(plugin.settings.defaultAgentId);
  await new Promise(r => setTimeout(r, 1200));
  const views = plugin.viewRegistry.getAll();
  const latest = views[views.length - 1];
  latest.setInputState({ text: prompt, files: [] });
});
```
