# PRM — Partner Relationships

The PRM module manages co-sell, co-delivery, referral, and certification partners — separate from clients and suppliers. Partners live under `{partner.root}`. The module can be toggled off via **Settings → Modules**.

The Partners nav item contains six tabs covering the full partner lifecycle.

---

## Overview

A dashboard summarising partner activity: active partner count, open registrations, pending commissions, certifications expiring soon, and recent partner interactions.

![prm_partners__overview](images/prm_partners__overview.png)

---

## Partners

Lists all `type: partner` notes. Key fields: partner name, relationship type (co-sell / co-delivery / referral / certification), agreement type, status. Status lifecycle: `lead → qualified → active → inactive → archived`.

The **Bases dropdown** reflects named views in `{vault.bases}/partner.base`. Add views for *Active only*, *By relationship type*, or *Certifications due for renewal*.

![prm_partners__partners](images/prm_partners__partners.png)

---

## Registrations

Lists all `type: registration` notes under partner folders. Registrations track deal registrations submitted to a partner (e.g. a vendor portal submission). Key fields: title, partner reference, submitted date, expiry date, value, status.

![prm_partners__registrations](images/prm_partners__registrations.png)

---

## Commissions

Lists all `type: commission` notes. Tracks commission amounts earned per partner per period. Key fields: reference, partner reference, amount, earned date, period, status.

The **Bases dropdown** reflects `{vault.bases}/commission.base` — useful for views filtered by status (pending / paid) or grouped by partner.

![prm_partners__commissions](images/prm_partners__commissions.png)

---

## Certifications

Lists all `type: certification` notes. Tracks vendor or programme certifications held by partners (e.g. Anthropic Partner, AWS Advanced). Key fields: name, partner reference, level, issued date, expiry date, status.

Add a view in `{vault.bases}/certification.base` filtered to `status: active` and sorted by `expires_date` to monitor upcoming renewals.

![prm_partners__certifications](images/prm_partners__certifications.png)

---

## Analytics

A read-only report view aggregating partner performance: deals influenced, revenue attributed, commission paid, and registration conversion rates per partner.

![prm_partners__analytics](images/prm_partners__analytics.png)
