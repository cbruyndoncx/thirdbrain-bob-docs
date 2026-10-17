"""MkDocs hook: build the site menu from nav.yml and the library catalogue.

nav.yml holds the curated menu with readable labels. This hook, run by `mkdocs build` and
`mkdocs serve` (mkdocs.yml `hooks:`), turns it into the `nav` setting:

  - `Library: generated` becomes Skills and Workflows, each grouped by business area in the
    order and with the labels of data/catalogue.json;
  - an entry whose page is gone (a renamed or removed Wiki page) is left out and logged;
  - `hidden` pages stay out of the menu (MkDocs still builds them);
  - every other page in neither list goes under "More" and is logged, so a new Wiki page is
    visible straight away and the log says where to place it;
  - an entry `page.md#anchor` is a shortcut to a section of a page listed elsewhere in the menu
    (one source, two ways in); it links to that page's clean address plus the anchor.

It also gives every menu page a clean address taken from its place in the menu, so readers see
/get-started/quickstart/ instead of the vault folder /02-Setup/quickstart/: the section labels
and the page label, slugified; a section's "Overview" or "Contents" page gets the section's own
address. The vault folder address keeps working as a redirect, because release pointers
(vault-release `docs_page_url`) and older links are built from the vault path. Nothing moves in
docs/: only where MkDocs writes the page changes, so links and images keep resolving. Renaming a
menu label changes that page's clean address.
"""
from __future__ import annotations

import fnmatch
import html
import json
import logging
import os
import re
from pathlib import Path

import yaml

log = logging.getLogger("mkdocs.hooks.nav")
ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ("skills", "workflows")
SECTION_PAGE = ("Overview", "Contents")   # the label that gives a page its section's address
_clean: dict[str, str] = {}              # docs-relative source path -> clean address ("a/b")
_SHORTCUT = "shortcut:"                  # placeholder for `page.md#anchor` until addresses are known


def _slug(label: str) -> str:
    s = label.lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def _title(page: Path) -> str:
    text = page.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        meta = yaml.safe_load(text[4:end]) or {} if end != -1 else {}
        if isinstance(meta, dict) and meta.get("title"):
            return str(meta["title"])
    return page.stem


def _library(docs: Path) -> list:
    """Skills and Workflows sections, one subsection per business area."""
    cat = json.loads((ROOT / "data" / "catalogue.json").read_text(encoding="utf-8"))
    areas = [(a["key"], a["label"]) for a in cat["areas"]]
    areas.append((cat["foundational"]["key"], cat["foundational"]["label"]))
    sections = []
    for kind in LIBRARY:
        items: list = [f"{kind}/index.md"]
        for key, label in areas:
            folder = docs / kind / key
            pages = sorted(folder.glob("*.md")) if folder.is_dir() else []
            if pages:
                items.append({label: [{_title(p): p.relative_to(docs).as_posix()} for p in pages]})
        sections.append({kind.capitalize(): items})
    return sections


def _resolve(entries: list, pages: set[str], listed: set[str], docs: Path, prefix: tuple = ()) -> list:
    out = []
    for entry in entries:
        if isinstance(entry, str):
            entry = {None: entry}
        (label, value), = entry.items()
        if value == "generated":
            out.append({label: _library(docs)})
        elif isinstance(value, list):
            children = _resolve(value, pages, listed, docs, prefix + (_slug(label),))
            if children:
                out.append({label: children})
        elif isinstance(value, str) and "#" in value:
            page = value.split("#", 1)[0]
            if page in pages:
                out.append({label: _SHORTCUT + value})
            else:
                log.info("nav.yml: %s is not in the docs (renamed or removed?), left out of the menu", value)
        elif value in pages:
            listed.add(value)
            if value != "index.md" and label:
                parts = prefix if label in SECTION_PAGE else prefix + (_slug(label),)
                _clean[value] = "/".join(parts)
            out.append(value if label is None else {label: value})
        else:
            log.info("nav.yml: %s is not in the docs (renamed or removed?), left out of the menu", value)
    return out


def on_config(config):
    _clean.clear()
    spec = yaml.safe_load((ROOT / "nav.yml").read_text(encoding="utf-8"))
    docs = Path(config["docs_dir"])
    pages = {p.relative_to(docs).as_posix() for p in docs.rglob("*.md")}
    listed: set[str] = set()
    nav = _resolve(spec["nav"], pages, listed, docs)

    hidden = spec.get("hidden") or []
    library = {p for p in pages if p.split("/", 1)[0] in LIBRARY}
    more = sorted(p for p in pages - listed - library
                  if not any(fnmatch.fnmatch(p, pat) for pat in hidden))
    if more:
        log.info("nav.yml: %d page(s) not placed, shown under More: %s", len(more), ", ".join(more))
        nav.append({"More": more})
    config["nav"] = _shortcuts(nav)
    return config


def _shortcuts(entries: list) -> list:
    """Replace `page.md#anchor` placeholders with the page's clean address and the anchor. The
    result is a site-relative link, which the theme makes relative to each page."""
    out = []
    for entry in entries:
        if isinstance(entry, dict):
            (label, value), = entry.items()
            if isinstance(value, list):
                value = _shortcuts(value)
            elif isinstance(value, str) and value.startswith(_SHORTCUT):
                page, anchor = value[len(_SHORTCUT):].split("#", 1)
                base = _clean.get(page) or page[:-3]
                value = f"{base}/#{anchor}"
            entry = {label: value}
        out.append(entry)
    return out


def on_files(files, config):
    """Write each menu page to its clean address."""
    taken: dict[str, str] = {}
    for f in files.documentation_pages():
        clean = _clean.get(f.src_uri)
        if clean is None:
            continue
        if clean in taken:
            raise ValueError(f"nav.yml: {f.src_uri} and {taken[clean]} both map to /{clean}/; "
                             "rename one of the labels")
        taken[clean] = f.src_uri
        f.dest_uri = f"{clean}/index.html"
        f.url = f"{clean}/"
        f.abs_dest_path = os.path.normpath(os.path.join(config["site_dir"], f.dest_uri))
    return files


def _redirect(site: Path, base: str, at: str, to: str, text: str) -> None:
    """Write site/<at>/index.html sending the reader to /<to>/, unless a page lives there."""
    target = site / at / "index.html"
    if target.exists():
        return
    url = base.rstrip("/") + "/" + to + "/"
    rel = os.path.relpath(site / to, site / at).replace(os.sep, "/") + "/"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(text)}</title><link rel=\"canonical\" href=\"{html.escape(url)}\">"
        f"<meta http-equiv=\"refresh\" content=\"0; url={html.escape(rel)}\">"
        f"</head><body><p>{html.escape(text)}: <a href=\"{html.escape(rel)}\">{html.escape(url)}</a>.</p>"
        "</body></html>\n", encoding="utf-8")


def on_post_build(config):
    """Redirects: each page's vault-folder address to its clean address, and each menu section's
    address (/get-started/, /get-started/install/) to the first page of that section, so no
    address in the menu's tree is an empty folder."""
    site = Path(config["site_dir"])
    base = config["site_url"] or "/"
    for src, clean in _clean.items():
        old = src[:-3]
        if old.endswith("/index") or old.endswith("/README"):
            old = old.rsplit("/", 1)[0]
        _redirect(site, base, old, clean, "This page is now at")
    first: dict[str, str] = {}
    for clean in _clean.values():          # menu order, so the first match is the first page
        parts = clean.split("/")
        for i in range(1, len(parts)):
            first.setdefault("/".join(parts[:i]), clean)
    for section, page in first.items():
        _redirect(site, base, section, page, "This section starts at")
