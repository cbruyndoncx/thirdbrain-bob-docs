# Prompt Showcase

**You don't have to learn this system. You just talk to it.**

This is a map of everything you can ask your vault to do, organized by area of the business. You don't have to learn commands — you describe what you want, and the system picks the right **skill** (one task) or **playbook** (a whole guided workflow).

Pick the area you're working in below. Each area page explains how that part of the business flows, the **playbooks** and **skills** available, and example prompts you can copy.

> [!tip] How to read the graph
> Open the **graph view** filtered to `path:"06-Prompt-Showcase" OR path:"Playbooks" OR path:"skill-docs"`. The center hub branches into the 12 business **areas**; each area links out to the **playbooks** and **skill docs** behind it — and those link onward to the underlying skills. Color by path: green for `Playbooks/`, blue for `skill-docs/`.

> [!example] One-click graph
> [Open the Prompt Showcase graph](obsidian://adv-uri?vault=brncx-skills&workspace=Prompt-Showcase)
> *(works once the `Prompt-Showcase` workspace has been saved — see **[[#Setup — save the graph workspace|Setup]]** at the bottom of this page)*

---

## Business Areas

- [[Grow Revenue]] — win customers and get paid
- [[Deliver & Delight]] — deliver work and keep clients happy
- [[Know Your Numbers]] — bookkeeping, close, reporting
- [[Buy Smart]] — purchasing and suppliers
- [[Build the Team]] — hiring and people
- [[Set Direction]] — strategy and planning
- [[Ship & Confirm]] — order fulfilment
- [[Make It Right]] — production and quality
- [[Turn Demand into Orders]] — pricing and demand
- [[Idea to Market]] — new product launch
- [[Serve & Grow Clients]] — onboarding and retention
- [[Create & Publish Content]] — content and marketing

---

**New here?** The two master indexes show the full library: [[PLAYBOOKS]] (guided workflows) and [[SKILLS]] (single capabilities).

**Want the firehose?** [[All Example Prompts]] lists every advertised trigger across all skills — the exhaustive companion to these curated guides.

---

## Setup — save the graph workspace

The one-click graph button above restores a saved layout named `Prompt-Showcase`. Obsidian
cannot create that layout for you, so it has to be saved once per vault. It takes about a
minute, and only has to be done on this machine one time.

Both core plugins this needs — **Graph view** and **Workspaces** — are already enabled here,
as is **Advanced URI**, so you can go straight to the steps.

### 1. Open a graph and filter it

Open the graph view (`Ctrl+G`, or the graph icon in the left ribbon). In the graph's
**Filters** panel, replace whatever is in the search box with:

```
path:"06-Prompt-Showcase" OR path:"Playbooks" OR path:"skill-docs"
```

The `path:` prefix matters. Without it Obsidian searches note *content* rather than
location, which pulls in a few thousand unrelated notes and buries the structure you
actually want to see.

### 2. Set the display options

In the same panel:

| Setting | Value | Why |
|---|---|---|
| Tags | off | tag nodes crowd out the area-to-skill structure |
| Attachments | off | same |
| Orphans | off | every node here should be reachable from the hub |
| Existing files only | on | hides not-yet-written notes |

Then under **Groups**, add two color groups:

| Query | Color |
|---|---|
| `path:"Playbooks"` | green |
| `path:"skill-docs"` | blue |

That gives you the reading the tip at the top of this page describes: this hub at the
centre, branching into the 12 business areas, each fanning out into the green playbooks
and blue skill docs behind it.

### 3. Save it under the exact name

Open the command palette (`Ctrl+P`) → **Workspaces: Manage workspace layouts** → type the
name and click **Save**:

```
Prompt-Showcase
```

The name must match exactly, hyphen included — the button at the top of this page looks it
up by that string, and a mismatch fails silently rather than telling you it missed.

### Checking it worked

Click **[Open the Prompt Showcase graph](obsidian://adv-uri?vault=brncx-skills&workspace=Prompt-Showcase)**
again. A filtered graph should open.

If nothing happens, the layout did not save under that name — reopen **Manage workspace
layouts** and confirm `Prompt-Showcase` is listed. If the graph opens but is empty, the
filter is the problem rather than the workspace: check the `path:` prefixes survived, since
pasting into the box occasionally drops the quotes.

> [!warning] Saving a workspace captures whatever is open
> Obsidian saves the *entire* window layout under that name, not just the graph. Close
> unrelated tabs and side panels before step 3, or they come back every time you click the
> button.
