# BOB Docs

Public documentation for BOB: the vault wiki, plus the skills and workflows library.
Built with MkDocs Material and deployed to GitHub Pages (`.github/workflows/pages.yml`).

`docs/` is **generated and committed** (CI has no access to the private vault). Do not edit it by hand.

## Rebuild

    scripts/build.sh [VAULT_WIKI] [SITE_CONTENT_EN]
    mkdocs build --strict      # or: mkdocs serve

- `scripts/export_wiki.py` converts `00-CORE/Wiki` (wikilinks, embeds, callouts) and drops internal folders; see `EXCLUDE_PATHS`.
- `scripts/build_library.py` builds `docs/skills` and `docs/workflows`. It currently reads the website's `src/content/en` pages (copy phase). Next step: read the vault via the website's `catalogue.py` and remove those pages from the website.
- `reports/wiki-export.md` lists unresolved links, dropped blocks, draft pages and assets that were not exported (diagrams).
