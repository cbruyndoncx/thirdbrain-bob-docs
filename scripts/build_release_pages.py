#!/usr/bin/env python3
"""Build the release pages of the docs site from vault files synced into data/release/.

Usage: build_release_pages.py SRC_DIR DOCS_DIR [--linkmap build/linkmap.json]

SRC_DIR is data/release/, filled by scripts/sync_release_pages.sh with files the vault
generates at release time. This script only copies and converts; the content is generated
in the vault (vault-release), never edited here.

  SKILL-PACKS.md  -> skill-packs.md  one section per pack, each with a stable anchor named
                                     after the pack id without `pack-` (#core, #sales, #pmbok)

Conversions: front matter and HTML comments (the vault's GENERATED markers) are dropped,
wikilinks become plain text or site links, and a skill name that starts a list item or a
table row links to its Library page when the Library has one.
"""
import argparse, json, re, sys
from pathlib import Path

PAGES = [
    # src file in SRC_DIR, page in DOCS_DIR, page title, add pack anchors
    ("SKILL-PACKS.md", "skill-packs.md", "Skill packs", True),
]

COMMENT_RE = re.compile(r"<!--.*?-->\n?", re.S)
WIKI_RE = re.compile(r"!?\[\[([^\]]+?)\]\]")
FENCE_RE = re.compile(r"^(```|~~~)")
HEADING_RE = re.compile(r"^(#{2,3}) (.+?)\s*$")
# The pack id as the generated text writes it: "`pack-sales` — 16 skills" or "(`pack-core`, 202 skills".
PACK_ID_RE = re.compile(r"`pack-([a-z0-9-]+)`(?= —|,)")
LIST_SKILL_RE = re.compile(r"^(\s*- )`([a-z0-9][a-z0-9-]*)`")
ROW_SKILL_RE = re.compile(r"^\| (`?)([a-z0-9][a-z0-9-]*)\1 \|")


def norm(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def split_fm(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def convert(text, linkmap, pack_anchors, name):
    text = COMMENT_RE.sub("", split_fm(text))
    lines = text.split("\n")
    out, in_fence, anchors = [], None, []

    def skill_link(skill):
        target = linkmap.get(norm(skill))
        return target if target and target.startswith("skills/") else None

    def wikilink(m):
        target, _, alias = m.group(1).replace("\\|", "|").partition("|")
        target = target.partition("#")[0]
        label = alias or Path(target).stem
        link = linkmap.get(norm(Path(target).parent.name if Path(target).name.lower() == "skill.md"
                                else Path(target).stem))
        return f"[{label}]({link})" if link else label

    for i, ln in enumerate(lines):
        fence = FENCE_RE.match(ln.strip())
        if fence:
            in_fence = None if in_fence and ln.strip().startswith(in_fence) else (in_fence or fence.group(1))
            out.append(ln)
            continue
        if in_fence:
            out.append(ln)
            continue
        parts = re.split(r"(`[^`]*`)", ln)
        ln = "".join(p if p.startswith("`") else WIKI_RE.sub(wikilink, p) for p in parts)
        h = HEADING_RE.match(ln)
        if h and pack_anchors:
            # the pack id is the first one written in this heading's section
            section = []
            for nxt in lines[i + 1:]:
                if HEADING_RE.match(nxt) or nxt.startswith("# "):
                    break
                section.append(nxt)
            m = PACK_ID_RE.search("\n".join(section))
            if m:
                anchor = m.group(1)
                if anchor in anchors:
                    sys.exit(f"{name}: two sections for pack-{anchor}")
                if "{" in h.group(2):
                    sys.exit(f"{name}: heading already has attributes: {ln}")
                anchors.append(anchor)
                ln = f"{h.group(1)} {h.group(2)} {{ #{anchor} }}"
        m = LIST_SKILL_RE.match(ln) or ROW_SKILL_RE.match(ln)
        if m:
            skill = m.group(2)
            link = skill_link(skill)
            if link:
                shown = m.group(0).rstrip(" |")[len(m.group(1) if m.re is LIST_SKILL_RE else "| "):]
                ln = ln.replace(shown, f"[{shown}]({link})", 1)
        out.append(ln)
    return "\n".join(out).rstrip() + "\n", anchors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("docs")
    ap.add_argument("--linkmap", default=None)
    a = ap.parse_args()
    src, docs = Path(a.src), Path(a.docs)
    linkmap = json.loads(Path(a.linkmap).read_text()) if a.linkmap and Path(a.linkmap).exists() else {}
    for src_name, dest_name, title, pack_anchors in PAGES:
        path = src / src_name
        if not path.is_file():
            sys.exit(f"missing {path}: run scripts/sync_release_pages.sh")
        body, anchors = convert(path.read_text(encoding="utf-8"), linkmap, pack_anchors, src_name)
        if pack_anchors and not anchors:
            sys.exit(f"{src_name}: no pack sections found")
        (docs / dest_name).write_text(f"---\ntitle: {title}\n---\n\n{body}", encoding="utf-8")
        extra = f" anchors={','.join(anchors)}" if anchors else ""
        print(f"{dest_name}: from {src_name}{extra}")


if __name__ == "__main__":
    main()
