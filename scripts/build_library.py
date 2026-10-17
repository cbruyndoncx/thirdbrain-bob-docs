#!/usr/bin/env python3
"""Build the skills/ and workflows/ sections of the docs site.

Usage: build_library.py CATALOGUE_JSON DOCS_DIR [--linkmap build/linkmap.json]

CATALOGUE_JSON is data/catalogue.json, written by the website's
scripts/emit_catalogue.py (through scripts/sync_catalogue.sh). It carries the same
skills, workflows and business areas the website publishes, as data.

Writes docs/skills/*.md, docs/workflows/*.md, an index per section grouped by
business area, and a link map so wiki pages can link to skills and workflows.
"""
import argparse, json, os, re
from collections import defaultdict
from pathlib import Path
import yaml

AREA_ORDER = ["marketing", "sales", "finance", "operations", "project-delivery",
              "people", "strategy", "research", "foundational"]




def _walk(v):
    if isinstance(v, str):
        return plain(v)
    if isinstance(v, list):
        return [_walk(x) for x in v]
    if isinstance(v, dict):
        return {k: _walk(x) for k, x in v.items()}
    return v


def uniq(xs):
    seen, out = set(), []
    for x in xs or []:
        k = x if isinstance(x, str) else (x.get("label") if isinstance(x, dict) else str(x))
        if k not in seen:
            seen.add(k); out.append(k)
    return out


MDLINK = re.compile(r"\[([^\]]+)\]\((?!https?://)[^)]*\)")


def plain(s):
    """Flatten relative markdown links (they point at unpublished skill files)."""
    return MDLINK.sub(r"\1", s) if isinstance(s, str) else s


def cell(s):
    return plain(str(s)).replace("|", "\\|").replace("\n", " ").strip()


def unbracket(v):
    v = str(v).strip()
    return v[1:-1] if v.startswith("[") and v.endswith("]") else v


def meta_list(rows):
    return "".join(f"- **{k}:** {cell(unbracket(v))}\n" for k, v in rows if v) + "\n" if any(v for _, v in rows) else ""


def bullets(items):
    return "\n".join(f"- {i}" for i in items) + "\n" if items else ""


def title_of(slug):
    return slug.replace("-", " ").replace("_", " ")


def front(title, desc=None):
    h = {"title": title}
    if desc:
        h["description"] = desc
    return "---\n" + yaml.safe_dump(h, allow_unicode=True, width=1000) + "---\n\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("catalogue"); ap.add_argument("docs")
    ap.add_argument("--linkmap", default=None)
    a = ap.parse_args()
    docs = Path(a.docs)
    cat = json.loads(Path(a.catalogue).read_text(encoding="utf-8"))

    areas = {x["key"]: x for x in cat["areas"]}
    areas["foundational"] = cat["foundational"]
    skills = {s["skillName"]: _walk(s) for s in sorted(cat["skills"], key=lambda s: s["skillName"])}
    workflows = {}
    for w in sorted(cat["workflows"], key=lambda w: w["slug"]):
        fm = {k: v for k, v in w.items() if k not in ("slug", "body")}
        workflows[w["slug"]] = (_walk(fm), w["body"].strip())

    sk_dir, wf_dir = docs / "skills", docs / "workflows"
    sk_dir.mkdir(parents=True, exist_ok=True); wf_dir.mkdir(parents=True, exist_ok=True)

    def area_of(fm):
        return fm.get("area") or "foundational"

    def sk_rel(n):           # path under docs/
        return f"skills/{area_of(skills[n])}/{n}.md"

    def wf_rel(s):
        return f"workflows/{area_of(workflows[s][0])}/{s}.md"

    def rel(frm, to):
        return os.path.relpath(to, os.path.dirname(frm)).replace("\\", "/")

    by_skill = defaultdict(list)
    for slug, (fm, _) in workflows.items():
        by_skill[fm.get("skillName")].append(slug)

    # ---- skill pages
    for name, fm in skills.items():
        out = [front(name, fm.get("summary") or fm.get("desc")), f"# {name}\n\n"]
        if fm.get("summary") or fm.get("desc"):
            out.append(f"{fm.get('summary') or fm.get('desc')}\n\n")
        meta = [("Area", areas.get(fm.get("area"), {}).get("label", fm.get("area"))),
                ("Category", (fm.get("catLabel") or "").replace("-", " ")),
                ("Level", fm.get("difficulty")), ("Input", fm.get("inputType")),
                ("Output", fm.get("outputType")), ("Setup", fm.get("requires")),
                ("Roles", fm.get("roles"))]
        out.append(meta_list(meta))
        if fm.get("desc") and fm.get("desc") != fm.get("summary"):
            out.append(f"{fm['desc']}\n\n")
        if fm.get("prompts"):
            out.append("## How you ask\n\n" + "".join(f"- “{p}”\n" for p in fm["prompts"]) + "\n")
        if fm.get("inputs"):
            out.append("## Inputs\n\n" + bullets(uniq(fm["inputs"])) + "\n")
        if fm.get("outputs"):
            out.append("## Outputs\n\n" + bullets(uniq(fm["outputs"])) + "\n")
        wfs = by_skill.get(name, [])
        if wfs:
            out.append("## Seen in these workflows\n\n" + "".join(
                f"- [{workflows[w][0].get('title') or title_of(w)}]({rel(sk_rel(name), wf_rel(w))})\n" for w in wfs) + "\n")
        dest = docs / sk_rel(name); dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("".join(out), encoding="utf-8")

    # ---- workflow pages
    for slug, (fm, body) in workflows.items():
        title = fm.get("title") or title_of(slug)
        out = [front(title, fm.get("outcome")), f"# {title}\n\n"]
        if fm.get("subtitle"):
            out.append(f"*{fm['subtitle']}*\n\n")
        yt = fm.get("youtubeId")
        if yt:
            out.append(f'<div class="video-wrap"><iframe width="100%" height="420" '
                       f'src="https://www.youtube.com/embed/{yt}?rel=0" title="{cell(title)}" '
                       f'frameborder="0" allowfullscreen loading="lazy"></iframe></div>\n\n')
        if fm.get("hook"):
            out.append("> " + str(fm["hook"]).strip().replace("\n", "\n> ") + "\n\n")
        if fm.get("outcome"):
            out.append(f"**Outcome:** {fm['outcome']}\n\n")
        meta = [("Area", areas.get(fm.get("area"), {}).get("label", fm.get("area"))),
                ("Level", fm.get("difficulty")),
                ("Roles", ", ".join(fm.get("primaryRoles") or [])),
                ("Time savings", fm.get("timeSavings")), ("Try it", fm.get("trigger")),
                ("Compounding", fm.get("compounding")), ("Frequency", fm.get("frequency")),
                ("Published", fm.get("published"))]
        out.append(meta_list(meta))
        for head, key in (("Inputs", "inputs"), ("What BOB does", "steps"), ("Outputs", "outputs")):
            items = fm.get(key)
            if not items:
                continue
            lines = []
            for n, it in enumerate(items, 1):
                if isinstance(it, dict):
                    lab = f"{it.get('icon', '')} {it.get('label', '')}".strip()
                else:
                    lab = str(it)
                lines.append(f"{n}. {lab}" if key == "steps" else f"- {lab}")
            out.append(f"## {head}\n\n" + "\n".join(lines) + "\n\n")
        if fm.get("benefits"):
            out.append("## Benefits\n\n" + bullets(fm["benefits"]) + "\n")
        sk = fm.get("skillName")
        if sk in skills:
            out.append(f"Built on the [{sk}]({rel(wf_rel(slug), sk_rel(sk))}) skill.\n")
        dest = docs / wf_rel(slug); dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("".join(out), encoding="utf-8")

    # ---- indexes
    def group(rows):
        g = defaultdict(list)
        for r in rows:
            g[r[0] or "foundational"].append(r[1:])
        return g

    def index(path, title, intro, rows, linkdir):
        g = group(rows)
        txt = [front(title), f"# {title}\n\n{intro}\n\n"]
        for key in AREA_ORDER + sorted(k for k in g if k not in AREA_ORDER):
            if key not in g:
                continue
            ar = areas.get(key, {"label": key})
            txt.append(f"## {ar.get('label', key)}\n\n")
            if ar.get("blurb"):
                txt.append(f"{ar['blurb']}\n\n")
            txt.append("| Name | What it does |\n|---|---|\n")
            for slug, label, d in sorted(g[key], key=lambda x: x[1].lower()):
                txt.append(f"| [{cell(label)}]({slug}) | {cell(d)} |\n")
            txt.append("\n")
        path.write_text("".join(txt), encoding="utf-8")

    index(sk_dir / "index.md", "Skills",
          f"{len(skills)} skills across every part of the business. Each page lists how to ask, what it needs and what it produces.",
          [(f.get("area"), sk_rel(n)[len("skills/"):], n, f.get("summary") or f.get("desc") or "") for n, f in skills.items()], "")
    index(wf_dir / "index.md", "Workflows",
          f"{len(workflows)} end-to-end workflows, built from the skills. Many have a video walkthrough.",
          [(f.get("area"), wf_rel(s)[len("workflows/"):], f.get("title") or title_of(s), f.get("outcome") or f.get("subtitle") or "")
           for s, (f, _) in workflows.items()], "")

    # ---- link map for the wiki export (keys = normalised names)
    def norm(s):
        return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    lm = {}
    lm["skills"] = "skills/index.md"
    lm["workflows"] = "workflows/index.md"
    for s in skills:
        lm[norm(s)] = sk_rel(s)
    for s, (f, _) in workflows.items():
        lm[norm(s)] = wf_rel(s)
        lm.setdefault(norm(s.removeprefix("pb-")), wf_rel(s))
        if f.get("title"):
            lm.setdefault(norm(f["title"]), wf_rel(s))
    if a.linkmap:
        Path(a.linkmap).parent.mkdir(parents=True, exist_ok=True)
        Path(a.linkmap).write_text(json.dumps(lm, indent=1))
    print(f"skills={len(skills)} workflows={len(workflows)} linkmap={len(lm)}")


if __name__ == "__main__":
    main()
