---
description: Import a supplier or client catalogue into validated Product records. The canonical record is one Product per SKU; repeated imports update the matching SKU and preserve the source catalogue and import date.
title: catalog-csv-ingest
---

# catalog-csv-ingest

Import a supplier or client catalogue into validated Product records. The canonical record is one Product per SKU; repeated imports update the matching SKU and preserve the source catalogue and import date.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Import supplier or client product catalogues from CSV or spreadsheet exports into validated Product records.

## Inputs

- catalogue — CSV with sku, product_name, unit_price, price_currency; optional brand, category (kept as catalogue_category), supplier_id, current_stock, unit_of_measure, variants
- client_id — Client scope for the imported catalogue
- source_catalog — Human-readable catalogue/source name

## Outputs

- import_manifest (json)
- product_records (markdown)
- {client.catalogue.products}/{sku}.md
- {client.catalogue}/catalogue-index.json

