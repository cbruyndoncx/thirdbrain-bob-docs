---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: catalog-csv-ingest — ThirdBrain BOB skill
  description: 'Import a supplier or client catalogue into validated Product records. The canonical record is one Product per SKU; repeated imports update the matching SKU and '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: catalog-csv-ingest
catLabel: operations
area: operations
desc: Import supplier or client product catalogues from CSV or spreadsheet exports into validated Product records.
summary: Import a supplier or client catalogue into validated Product records. The canonical record is one Product per SKU; repeated imports update the matching SKU and preserve the source catalogue and import date.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- catalogue — CSV with sku, product_name, unit_price, price_currency; optional brand, category (kept as catalogue_category), supplier_id, current_stock, unit_of_measure, variants
- client_id — Client scope for the imported catalogue
- source_catalog — Human-readable catalogue/source name
outputs:
- import_manifest (json)
- product_records (markdown)
- '{client.catalogue.products}/{sku}.md'
- '{client.catalogue}/catalogue-index.json'
prompts: []
---
