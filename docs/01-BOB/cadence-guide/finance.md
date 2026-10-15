# Finance

The Finance section covers the full accounting and tax stack: customer invoicing, the general ledger, finance setup, and tax compliance. Each area is a separate nav item with its own tab strip.

---

## Customer Invoices

Lists all `type: invoice` notes. Key fields: invoice ID, client, invoice date, due date, amount, currency, payment status. Status lifecycle: `draft → sent → paid / overdue / cancelled`.

The **Bases dropdown** reflects `{vault.bases}/invoice.base`. Useful views: *Outstanding* (sent, not paid), *Overdue*, *By client*, *This month*.

Use **+ New Invoice** to create an invoice. The currency setting in **Settings → Currency** sets the display default.

![finance_customer-invoices](images/finance_customer-invoices.png)

---

## General Ledger

The General Ledger groups all double-entry accounting screens under one tabbed surface.

### Overview

A dashboard of the current period's GL health: total debits/credits, recent journal entries, accounts with unusual balances, and open reconciliation items.

![finance_general-ledger__overview](images/finance_general-ledger__overview.png)

### Chart of Accounts

Lists all `type: chart-of-accounts` notes for the configured jurisdiction. Each account has a code, name, type (asset/liability/equity/revenue/expense), and normal balance. The Chart of Accounts is the foundation — all journal entries reference account codes defined here.

To add or edit accounts, edit the `.md` files in `{company.finance}/COA/{jurisdiction}/` or use **+ New Account** in the plugin.

![finance_general-ledger__chart-of-accounts](images/finance_general-ledger__chart-of-accounts.png)

### Journal Entries

Lists all `type: journal-entry` notes. Each entry has a JE ID, period, date, type (manual/system/accrual), debit/credit lines, and status (`draft → posted`). Lines reference Chart of Accounts codes.

The **Bases dropdown** reflects `{vault.bases}/journal-entry.base`. Add views for *Unposted*, *By period*, or *By entry type*.

![finance_general-ledger__journal-entries](images/finance_general-ledger__journal-entries.png)

### Bank Reconciliations

Lists all `type: bank-reconciliation` notes. Each reconciliation links a bank account, a period, the bank statement balance, and the GL balance. The reconciled difference should be zero before closing a period.

![finance_general-ledger__bank-reconciliations](images/finance_general-ledger__bank-reconciliations.png)

### Trial Balances

Lists all `type: trial-balance` notes. Each trial balance is generated for a period and shows closing debit and credit totals per account. Total debits must equal total credits before generating financial statements.

![finance_general-ledger__trial-balances](images/finance_general-ledger__trial-balances.png)

### Statements

Lists all `type: financial-statement` notes — P&L, Balance Sheet, Cash Flow, and Changes in Equity. Each statement links to a signed-off trial balance for the period.

![finance_general-ledger__statements](images/finance_general-ledger__statements.png)

### FS Notes

Lists all `type: fs-notes` notes — the narrative notes that accompany financial statements. One notes pack per period covers all four statements. Key sections: significant accounting policies, going concern assessment, and per-line disclosures.

![finance_general-ledger__fs-notes](images/finance_general-ledger__fs-notes.png)

---

## Finance Setup

Finance Setup groups the reference data that underpins the GL and reporting.

### Overview

A summary of setup completeness: accounting periods configured, bank accounts linked, FX rates loaded, inventory items.

![finance_finance-setup__overview](images/finance_finance-setup__overview.png)

### Accounting Periods

Lists all `type: accounting-period` notes. Each period has a start/end date, type (monthly/quarterly/annual), status (`open → soft-closed → hard-closed`), and currency. Hard-closed periods cannot be edited.

![finance_finance-setup__accounting-periods](images/finance_finance-setup__accounting-periods.png)

### Bank Accounts

Lists all `type: bank-account` notes. Each account has an account ID, bank name, IBAN, currency, and the GL account code it maps to. Bank accounts must exist here before bank reconciliations can reference them.

![finance_finance-setup__bank-accounts](images/finance_finance-setup__bank-accounts.png)

### FX Rates

Lists all `type: fx-rate-table` notes. Each table covers a period and records exchange rates per currency pair from a configured source. FX rates are used by invoice revaluation and foreign-currency GL postings.

![finance_finance-setup__fx-rates](images/finance_finance-setup__fx-rates.png)

### Inventory

Lists all `type: inventory-item` notes. Key fields: SKU, cost method (FIFO/weighted average), opening and closing quantities, net realisable value, write-down. Used for inventory valuation in financial statements.

![finance_finance-setup__inventory](images/finance_finance-setup__inventory.png)

---

## Tax

Tax groups all compliance filings under a tabbed surface.

### Overview

A dashboard of upcoming tax deadlines: VAT return due dates, corporate tax filing dates, document retention deadlines, and free zone status validity.

![finance_tax__overview](images/finance_tax__overview.png)

### VAT Returns

Lists all `type: vat-return` notes. Key fields: TRN, period start/end, standard-rated supplies, output VAT, input VAT, net payable, filing due date, status.

![finance_tax__vat-returns](images/finance_tax__vat-returns.png)

### Corporate Tax

Lists all `type: ct-return` notes. Key fields: return ID, entity type, taxable income, tax rate, tax payable, small business relief flag, filing due date, status.

![finance_tax__corporate-tax](images/finance_tax__corporate-tax.png)

### Deferred Tax

Lists all `type: deferred-tax` notes. Each assessment covers a period, records net deferred tax assets (DTA) and liabilities (DTL), the tax rate used, and a recoverability assessment.

![finance_tax__deferred-tax](images/finance_tax__deferred-tax.png)

### Transfer Pricing

Lists all `type: transfer-pricing` notes. Documents inter-company transactions with related parties — transaction type, amount, arm's-length method, and whether documented.

![finance_tax__transfer-pricing](images/finance_tax__transfer-pricing.png)

### Free Zone Status

Lists all `type: freezone-status` notes. Tracks qualifying vs. non-qualifying income, substance test results, and nexus maintenance per period — required for UAE free zone corporate tax compliance.

![finance_tax__free-zone-status](images/finance_tax__free-zone-status.png)

### Legal Rules

Lists all `type: legal-rule` notes — a reference library of tax regulations and compliance rules per jurisdiction. Each rule has a source, authority, effective dates, and a confidence rating. Used as a lookup when preparing returns.

![finance_tax__legal-rules](images/finance_tax__legal-rules.png)

### Document Retention

Lists all `type: retention-register` notes. Tracks document types, required retention periods, destroy-after dates, and responsible persons — for audit and regulatory compliance.

![finance_tax__document-retention](images/finance_tax__document-retention.png)
