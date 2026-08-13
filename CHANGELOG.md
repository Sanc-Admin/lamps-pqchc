# Changelog — draft-vicente-lamps-pqchc

## -03 (2026-08-12)

### Added
- **Differentiation section** (§1.2): explicit differentiation from
  draft-ietf-lamps-pq-composite-sigs and draft-ietf-lamps-cert-binding-for-multi-auth.
  PQCHC is a non-critical commitment extension, not a composite-signature scheme.
- **Posture B IPR notice**: soft "may hold or apply" + prior-art anchor.
- **REQ-PQCHC-6**: normative requirement that the extension MUST NOT alter
  the certificate's signatureAlgorithm or primary signature.
- **`evidence/pqchc-gap-evidence.json`**: machine-readable gap and adjacency
  differentiation evidence with RFC/FIPS citations.
- Security consideration: classical signature on commitment (§6.3).

### Modified
- Abstract updated to reflect -03 additions and differentiation clarification.
- Date updated to 2026-08-12.

---

## -02 and earlier
- Initial PQCHC extension definition: OID, ASN.1 syntax, validation procedure,
  REQ-PQCHC-1 through REQ-PQCHC-5.
