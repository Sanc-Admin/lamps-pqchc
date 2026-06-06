# IETF Final Draft — draft-vicente-lamps-pqchc

**Sanctum SecOps LLC | PATENT PENDING**

## Abstract

This repository contains the IETF Internet-Draft for the PQC Hybrid Commitment (PQCHC) X.509 extension, targeting the LAMPS Working Group.

| Field | Value |
|---|---|
| Draft name | `draft-vicente-lamps-pqchc-01` |
| Working Group | IETF LAMPS |
| Author | Brian Vicente `<brian@sanctumsecops.com>` |
| Status | Individual Submission |
| Date | 2026-06-05 |

## Problem Domain

PKI infrastructure lacks a machine-verifiable, cryptographically bound mechanism for certificate holders to commit to a specific future post-quantum key before migration is complete. Existing mechanisms (`draft-reddy-lamps-x509-pq-commit`) provide only temporal declarations (`continuityPeriod INTEGER`) with no cryptographic binding to a future `subjectPublicKeyInfo`. This leaves relying parties unable to detect algorithm downgrade at renewal time during the NIST IR 8547 migration window.

## Files

| File | Description |
|---|---|
| `draft-vicente-lamps-pqchc-01.md` | Full kramdown-rfc (mmark) I-D source |

## Related Work

- `draft-ietf-lamps-pq-composite-sigs` (-19, IESG 2026-04-21)
- `draft-reddy-lamps-x509-pq-commit` (-01, 2026-02-25)
- RFC 9773 (ACME-ARI, June 2025)
- RFC 9794 (PQ/T Hybrid Terminology, June 2025)
- RFC 5280

## IPR Notice

PATENT PENDING — Sanctum SecOps LLC · EIN 42-2733487  
Disclosure per BCP79/RFC8179. No trade secrets disclosed.
