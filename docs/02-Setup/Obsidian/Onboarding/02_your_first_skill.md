# Your First Skill

Run an AI skill hands-on in 10 minutes.

---

## 1. What is a Skill?

**A skill is a guided workflow for Claude.**

Instead of giving Claude vague instructions, skills provide:
- Step-by-step procedures
- Output templates
- File format knowledge
- Best practices

**Result**: Consistent, high-quality outputs every time.

---

## 2. How to Activate a Skill

**You don't need to know skill names.** Just describe what you want.

| You Say | Claude Activates |
|---------|------------------|
| "Create a mind map of..." | `excalidraw-easy` |
| "Help me define my ideal customer" | `icp-discovery` |
| "Map out my business operations" | `business-baseline` |
| "Generate a Word document for..." | `docx` |

Claude matches your intent to the right skill automatically.

---

## 3. Let's Try It - Mind Map

**Step 1**: Open your terminal where Claude Code runs

**Step 2**: Navigate to your vault folder:
```bash
cd /path/to/your/vault
```

**Step 3**: Start Claude Code:
```bash
claude
```

**Step 4**: Type this prompt:
```
Create a mind map of the benefits of AI for small business
```

<!-- SCREENSHOT: Terminal with the prompt typed -->

---

## 4. Watch Claude Work

Claude will:

1. **Recognize** you want a diagram → activates `excalidraw-easy`
2. **Ask permission** to use the skill (say yes)
3. **Plan** the mind map structure
4. **Generate** the `.excalidraw` file
5. **Save** it to your vault

You'll see the thinking process in real-time.

<!-- SCREENSHOT: Claude processing the request -->

---

## 5. Find Your Output

After Claude finishes:

1. **Check the terminal** - it shows the path where the file was saved
2. **Open Obsidian** - some skills auto-open the file; the Excalidraw skill usually does
3. **If it didn't open**: Use `Ctrl+O` and search for "mind map", or paste the path from the run output

The diagram opens in Obsidian's Excalidraw plugin.

<!-- SCREENSHOT: Excalidraw diagram open in Obsidian -->

---

## 6. Try Another - Capture a Note

Skills aren't just for diagrams. Try capturing an idea:

```
Create a new note: I had an idea for a referral program
where existing clients get 10% off their next project
for every new client they bring in
```

Claude uses the `new` skill to:
- Classify this as an "idea"
- Create a properly formatted note
- Save it to `{me.ideas}`
- Open it in Obsidian

---

## 7. The Pattern

Most skills follow this pattern:

```
1. You describe what you want (natural language)
2. Claude picks the skill (automatic)
3. Claude may ask clarifying questions
4. Claude generates the output
5. Some skills save a file to the vault; the run output shows the path
```

**You focus on WHAT. Claude handles HOW.**

---

## 8. What If It Doesn't Work?

| Problem | Solution |
|---------|----------|
| "Skill not found" | Rephrase your request more specifically |
| Wrong output location | Tell Claude where to save: "Save it to {company.clients}/acme/" |
| Skill asks too many questions | Answer them, or say "Use defaults" |
| Output isn't right | Say "Revise this to..." and explain |

**Claude learns from your feedback within the conversation.**

---

## You Did It!

You've run your first skill. Here's what to explore next:

- [03_skills_by_use_case](03_skills_by_use_case.md) - Find the right skill for any task
- [04_learning_path](04_learning_path.md) - A staged path through the skills, week by week

---

## Quick Reference

**Start Claude Code:**
```bash
cd /path/to/vault && claude
```

**Best starter prompts:**
- "Create a mind map of [topic]"
- "Help me define my ideal customer"
- "Generate a proposal for [client]"
- "Map out my [process] as a flowchart"

→ Continue to [03_skills_by_use_case](03_skills_by_use_case.md)
