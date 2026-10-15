#!/usr/bin/env python3
"""Export the BOB vault wiki to a MkDocs site tree.

Usage: export_wiki.py SRC_WIKI DOCS_DIR [--exclude-drafts] [--linkmap build/linkmap.json]

Writes into DOCS_DIR without clearing it (build.py owns cleaning), so it can
sit beside the generated skills/ and workflows/ sections. Wikilinks that point
outside the wiki fall back to the link map written by build_library.py.

Converts Obsidian syntax (wikilinks, embeds, callouts) to plain markdown,
drops Obsidian-only blocks, copies referenced images, and writes a report.
"""
import argparse, json, os, re, shutil, sys
from collections import defaultdict
from pathlib import Path
import yaml

EXCLUDE_PATHS = [          # relative to wiki root; prefix match
    "01-BOB/Internship",
    "01-BOB/Development",
    "cc-prototype-dashboard.md",
    "CLAUDE.md",
    "AGENTS.md",
]
HOME_SRC = "start_here.md"   # becomes index.md
IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
DROP_FENCES = ("dataview", "dataviewjs", "base")

FENCE_RE = re.compile(r"^(```|~~~)")
WIKI_RE = re.compile(r"(!?)\[\[([^\]]+?)\]\]")
CALLOUT_RE = re.compile(r"^>\s*\[!(\w+)\][+-]?\s*(.*)$")


def split_fm(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            try:
                fm = yaml.safe_load(text[4:end]) or {}
            except yaml.YAMLError:
                fm = {}
            return fm if isinstance(fm, dict) else {}, text[end + 4:].lstrip("\n")
    return {}, text


def excluded(rel):
    return any(rel == p or rel.startswith(p + "/") for p in EXCLUDE_PATHS)


def slug(h):
    s = re.sub(r"[^\w\s-]", "", h.lower()).strip()
    return re.sub(r"[\s]+", "-", s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("docs")
    ap.add_argument("--exclude-drafts", action="store_true")
    ap.add_argument("--linkmap", default=None)
    a = ap.parse_args()
    src, docs = Path(a.src), Path(a.docs)
    docs.mkdir(parents=True, exist_ok=True)
    linkmap = {}
    if a.linkmap and Path(a.linkmap).exists():
        linkmap = json.loads(Path(a.linkmap).read_text())

    report = defaultdict(list)
    all_files = [p for p in src.rglob("*") if p.is_file()]
    by_name = defaultdict(list)           # basename (no ext, lower) -> rel paths of md
    by_file = defaultdict(list)           # filename lower -> rel paths (assets)
    pages = {}                            # rel -> (fm, body)

    for p in all_files:
        rel = p.relative_to(src).as_posix()
        if excluded(rel):
            report["excluded"].append(rel); continue
        by_file[p.name.lower()].append(rel)
        if p.suffix == ".md":
            fm, body = split_fm(p.read_text(encoding="utf-8", errors="replace"))
            if a.exclude_drafts and fm.get("status") == "draft":
                report["excluded-draft"].append(rel); continue
            if fm.get("publish") is False:
                report["excluded-publish-false"].append(rel); continue
            pages[rel] = (fm, body)
            by_name[p.stem.lower()].append(rel)
            if p.name.endswith(".pdf.md"):
                by_name[p.name[:-3].lower()].append(rel)

    def out_path(rel):
        return "index.md" if rel == HOME_SRC else rel

    def resolve_page(target, frm):
        t = target.strip().rstrip("/")
        if t.endswith(".md"): t = t[:-3]
        cands = [r for r in pages if r[:-3].lower() == t.lower()]
        if not cands:
            cands = by_name.get(Path(t).name.lower(), [])
        if len(cands) > 1:   # prefer same folder, then shortest
            same = [c for c in cands if str(Path(c).parent) == str(Path(frm).parent)]
            cands = same or sorted(cands, key=len)
        return cands[0] if cands else None

    def resolve_asset(target):
        cands = by_file.get(Path(target).name.lower(), [])
        exact = [c for c in cands if c.lower().endswith(target.lower())]
        c = exact or cands
        return c[0] if c else None

    def relurl(frm, to):
        r = os.path.relpath(out_path(to), os.path.dirname(out_path(frm)) or ".")
        return "<" + r.replace("\\", "/") + ">" if " " in r else r

    copied = set()

    def norm(s):
        return re.sub(r"[^a-z0-9]+", "-", Path(s).name.lower().removesuffix(".md")).strip("-")

    def relurl_docs(frm, docs_rel):
        return os.path.relpath(docs_rel, os.path.dirname(out_path(frm)) or ".").replace("\\", "/")

    def convert_inline(line, rel):
        def sub(m):
            bang, inner = m.group(1), m.group(2)
            inner = inner.replace("\\|", "|")
            target, _, alias = inner.partition("|")
            target, _, anchor = target.partition("#")
            if bang:
                ext = Path(target).suffix.lower()
                if ext in IMG_EXT:
                    ar = resolve_asset(target)
                    if not ar:
                        report["missing-image"].append(f"{rel}: {target}"); return ""
                    copied.add(ar)
                    return f"![{Path(target).stem}]({relurl(rel, ar)})"
                if ext in (".canvas", ".excalidraw", ".drawio", ".mp3", ".json"):
                    report["skipped-embed"].append(f"{rel}: {target}"); return ""
                pr = resolve_page(target, rel)   # note transclusion -> link
                if pr:
                    return f"[{alias or Path(target).stem}]({relurl(rel, pr)})"
                report["unresolved-embed"].append(f"{rel}: {target}"); return ""
            if not target:                       # [[#heading]]
                return f"[{alias or anchor}](#{slug(anchor)})"
            pr = resolve_page(target, rel)
            text = alias or Path(target).stem
            if pr:
                url = relurl(rel, pr)
                if anchor:
                    url = url.rstrip(">") + "#" + slug(anchor) + (">" if url.endswith(">") else "")
                return f"[{text}]({url})"
            ar = resolve_asset(target) if Path(target).suffix.lower() in IMG_EXT else None
            if ar:
                copied.add(ar); return f"[{text}]({relurl(rel, ar)})"
            lm = linkmap.get(norm(target))
            if lm:
                return f"[{text}]({relurl_docs(rel, lm)})"
            report["unresolved-link"].append(f"{rel}: [[{target}]]")
            return text
        # protect inline code
        parts = re.split(r"(`[^`]*`)", line)
        return "".join(p if p.startswith("`") else WIKI_RE.sub(sub, p) for p in parts)

    def convert_body(body, rel):
        lines, res, i = body.split("\n"), [], 0
        in_fence, drop = None, False
        while i < len(lines):
            ln = lines[i]
            fm_ = FENCE_RE.match(ln.strip())
            if fm_:
                if in_fence is None:
                    in_fence = fm_.group(1)
                    lang = ln.strip()[3:].strip().lower()
                    drop = lang in DROP_FENCES
                    if drop: report["dropped-block"].append(f"{rel}: ```{lang}")
                elif ln.strip().startswith(in_fence):
                    in_fence = None
                    if drop: drop = False; i += 1; continue
            if in_fence is not None or fm_:
                if not drop: res.append(ln)
                i += 1; continue
            m = CALLOUT_RE.match(ln)
            if m:
                kind, title = m.group(1).lower(), m.group(2).strip()
                kind = {"example": "example", "important": "danger", "info": "info",
                        "tip": "tip", "warning": "warning"}.get(kind, "note")
                res.append(f'!!! {kind} "{title}"' if title else f"!!! {kind}")
                i += 1
                while i < len(lines) and lines[i].startswith(">"):
                    body_ln = re.sub(r"^>\s?", "", lines[i])
                    res.append("    " + convert_inline(body_ln, rel) if body_ln.strip() else "")
                    i += 1
                res.append("")
                continue
            res.append(convert_inline(ln, rel))
            i += 1
        return "\n".join(res)

    for rel, (fm, body) in sorted(pages.items()):
        text = convert_body(body, rel)
        head = {}
        if fm.get("title"): head["title"] = str(fm["title"])
        if fm.get("description"): head["description"] = str(fm["description"])
        pre = "---\n" + yaml.safe_dump(head, allow_unicode=True) + "---\n\n" if head else ""
        dest = docs / out_path(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(pre + text, encoding="utf-8")
        if fm.get("status") == "draft":
            report["published-but-draft"].append(rel)

    for ar in sorted(copied):
        d = docs / ar
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src / ar, d)
    for rel in by_file.values():
        for r in rel:
            if not r.endswith(".md") and Path(r).suffix.lower() not in IMG_EXT:
                report["not-exported-asset"].append(r)

    rep_dir = docs.parent / "reports"
    rep_dir.mkdir(exist_ok=True)
    with open(rep_dir / "wiki-export.md", "w") as f:
        f.write(f"# Export report\n\nPages: {len(pages)}  Images copied: {len(copied)}\n\n")
        for k in sorted(report):
            f.write(f"## {k} ({len(report[k])})\n")
            for x in sorted(set(report[k])): f.write(f"- {x}\n")
            f.write("\n")
    print(f"pages={len(pages)} images={len(copied)}")
    for k in sorted(report): print(f"  {k}: {len(report[k])}")


if __name__ == "__main__":
    main()
