# Obsidian Quick Start

Learn to navigate your vault in 10 minutes.



---

## 1. What is Obsidian?

**Obsidian is your local knowledge base.**

- All files are plain text (Markdown) stored on YOUR computer
- No cloud lock-in - you own your data
- AI agents (Claude Code) can read and write directly to these files

**Think of it as**: A smart folder system where everything links together.

---

## 2. The Vault Structure

Your vault is organized into numbered zones:

| Folder         | Purpose            | You'll Use For                    |
| -------------- | ------------------ | --------------------------------- |
| `{vault.core}`      | System files       | Templates, settings (don't edit)  |
| `{me.root}`        | Personal workspace | Your profile, contacts, ideas     |
| `{company.root}`   | Your business      | Services, pricing, knowledge base |
| `{company.clients}`   | Client work        | Projects, meetings, deliverables  |
| `{resource.root}` | Research           | Market data, references           |
<!-- SCREENSHOT: File explorer showing the main folders -->

---

## 3. The Left Sidebar

The left sidebar is your navigation hub.

**Top icons:**
- 📁 File explorer (folder view)
- 🔍 Search (find anything)
- ⭐ Bookmarks (quick access)

**Tip**: Click the folder icon to see all your files organized by folder.

<!-- SCREENSHOT: Left sidebar with icons highlighted -->

---

## 4. Opening Files

**Three ways to open a file:**

1. **Click** in the file explorer (left sidebar)
2. **Search** with `Ctrl+O` (or `Cmd+O` on Mac)
3. **Click a link** like [README](README.md) in any note

**Pro tip**: `Ctrl+O` is the fastest way. Just start typing the file name.

<!-- SCREENSHOT: Quick switcher dialog (Ctrl+O) -->

---

## 5. Understanding Links

Links connect your notes together.

| Syntax | What It Does |
|--------|--------------|
| `[[Note Name]]` | Links to another note |
| `[[Note Name\|Display Text]]` | Link with custom text |
| `#tag` | Adds a tag for organization |

**Example**: [02_your_first_skill](02_your_first_skill.md) links to the next guide.

When you click a link, Obsidian opens that note.

---

## 6. The Right Sidebar

The right sidebar shows context about the current note.

**Useful panels:**
- **Backlinks**: What links TO this note
- **Outgoing links**: What this note links TO
- **Table of contents**: Jump to headings

**Tip**: You can collapse it with the arrow if you need more space.

<!-- SCREENSHOT: Right sidebar showing backlinks -->

---

## 7. Where AI Outputs Go

Some workflows save files to your vault during the run; others just return the answer in the chat. When a file is saved, Claude shows the path in the run output. Typical destinations:

| Output Type | Typical Save Location |
|-------------|-----------------------|
| Mind maps, diagrams | Where you specify (or current folder) |
| Client work | `{company.clients}[client-name]/` |
| Documents | Relevant folder based on content |
| Meeting notes | `{me.meetings}` or client folder |

Some skills auto-open the file in Obsidian; others don't. If a file doesn't open automatically, copy the path from the run output and open it via `Ctrl+O`.

---

## 8. Essential Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+O` | Quick open (find any file) |
| `Ctrl+P` | Command palette (all commands) |
| `Ctrl+E` | Toggle edit/preview mode |
| `Ctrl+N` | New note |
| `Ctrl+F` | Find in current note |
| `Ctrl+Shift+F` | Search entire vault |

**Just remember `Ctrl+O`** - it's the most useful one.

<!-- SCREENSHOT: Command palette (Ctrl+P) showing options -->

---

## What's Next?

You now know enough to navigate. Time to run your first AI skill.

→ Continue to [02_your_first_skill](02_your_first_skill.md)
