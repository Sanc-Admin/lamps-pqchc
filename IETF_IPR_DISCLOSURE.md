# IPR Disclosure Discipline — Sanctum SecOps LLC

**Scope:** IETF intellectual-property obligations for the Internet-Drafts in this
repository. Governed by **BCP 79 ([RFC 8179](https://www.rfc-editor.org/rfc/rfc8179))**
and **BCP 78 ([RFC 5378](https://www.rfc-editor.org/rfc/rfc5378))**.

> **NOT LEGAL ADVICE.** This file is procedural guidance distilled from primary
> IETF sources. Bar-date timing, claim scope, and licensing-commitment decisions
> are legal questions for qualified patent counsel. Verify every date and number
> before relying on it.

---

## 0. The one rule that matters most

**Posting an Internet-Draft is a public disclosure.** The datatracker repository
is public and the archive is permanent. Under U.S. law this starts the 12-month
AIA grace clock; under the EPO and most other jurisdictions, a public disclosure
*before* filing generally destroys novelty
([35 U.S.C. §102(b)(1)](https://www.law.cornell.edu/uscode/text/35/102)).

**Therefore: file the patent application BEFORE posting the matching draft.**
For Sanctum's claim families with ~July 2026 filing deadlines, the draft posting
date must come *after* the application filing date — not the other way around.

```
   ┌─────────────────────┐      ┌──────────────────────┐      ┌─────────────────────┐
   │ 1. File application  │  →   │ 2. Post I-D (-00)     │  →   │ 3. File IETF IPR     │
   │    (provisional or   │      │    on datatracker     │      │    disclosure (same  │
   │    nonprovisional)   │      │                       │      │    day if possible)  │
   └─────────────────────┘      └──────────────────────┘      └─────────────────────┘
   establishes priority date     public disclosure starts       satisfies BCP 79
   BEFORE public disclosure      the AIA grace clock            obligation
```

---

## 1. Per-draft IPR posture

| Draft | Reads on a Sanctum claim family? | Action before posting |
|---|---|---|
| `draft-vicente-lamps-pqchc-00` | **Yes** — hybrid forward-commitment / pre-commitment to a future PQC key+algorithm is a recited element of a Sanctum claim family. | Confirm the corresponding application is **on file**, then post, then file the IPR disclosure referencing `draft-vicente-lamps-pqchc-00`. |
| `draft-vicente-oauth-apm-00` | **Yes** — IdP-side per-transaction cert+token+posture consistency enforcement is a recited element of a Sanctum claim family. | Same sequence: application on file → post → disclose, referencing `draft-vicente-oauth-apm-00`. |

> Both drafts are written **disclosure-safe** (mechanism / recited-element level
> only). They deliberately omit trade-secret numerics — risk-band thresholds,
> scoring weights, decision budgets, window lengths, and any OID numerics beyond
> the public PEN root `1.3.6.1.4.1.65953`. Keeping those out of the draft text
> preserves them as trade secrets and does not affect the patent disclosure
> obligation, which is about the *invention as claimed*, not the I-D text.

---

## 2. Do I have to disclose? (RFC 8179 §5.1.1 + §5.6)

You **MUST** disclose if you (or Sanctum SecOps LLC as your employer/sponsor)
own, control, have the right to license, derive a pecuniary benefit from, or are
a named inventor on a patent or patent application that **Covers or may Cover**
the contribution ([RFC 8179 §5.6](https://www.rfc-editor.org/rfc/rfc8179)).

For both drafts in this repo, the answer is **yes** — Brian Vicente is the
inventor and Sanctum SecOps LLC is the owner. The obligation is triggered the
moment the draft is posted **or** the moment you discuss the technology on a WG
mailing list / in a session (whichever comes first — see the Note Well below).

- **No patent search is required** ([RFC 8179 §1.m](https://www.rfc-editor.org/rfc/rfc8179)).
  The standard is "reasonably and personally known." You already know about your
  own applications, so the obligation applies.
- The obligation can be **satisfied by the owner** (Sanctum SecOps LLC) filing
  the disclosure in place of the individual contributor.

---

## 3. When to disclose (RFC 8179 §5.2)

> "As soon as reasonably possible after the Contribution is submitted or made."

**Best practice:** file the IPR disclosure **the same day** you post the `-00`,
or immediately after. Do not wait. If you discuss the mechanism on the WG list
before posting a draft, the obligation attaches to that post too.

---

## 4. What to disclose for an UNPUBLISHED application (RFC 8179 §5.4.1)

Patent applications are not published by the USPTO until ~18 months after the
earliest filing date. Until then you disclose **without** the application number:

The disclosure form lets you state that **"this disclosure is based on
unpublished patent applications."** Provide:

1. **Holder:** Sanctum SecOps LLC.
2. **Inventor:** Brian Vicente.
3. **Affected document:** the exact draft name **and version** —
   e.g. `draft-vicente-lamps-pqchc-00`.
4. **Statement:** disclosure is based on one or more **unpublished** patent
   applications (no number disclosed at this stage).
5. **Licensing declaration** (optional but strongly encouraged — see §5).

You do **not** reveal the application number, the claims, or any trade-secret
detail at this stage.

---

## 5. Licensing declaration (RFC 8179 §5.5)

Not mandatory, but WGs strongly prefer **royalty-free (RF)** terms, and an RF
declaration materially improves the odds of WG adoption. Options:

| Declaration | Effect on adoptability |
|---|---|
| **Royalty-Free + RAND** | Best for adoption; functionally expected for security protocols. |
| **RAND** (royalty-bearing) | Permissible; may slow or block WG adoption. |
| **No license needed** (covenant not to sue) | Equivalent to RF for adoption. |
| **No commitment** (terms reserved) | Disclosure still valid; WG may be cautious. |

> **Licensing declarations are IRREVOCABLE once made** and attach to the IPR
> even if it is later sold/transferred ([RFC 8179 §5.5.C](https://www.rfc-editor.org/rfc/rfc8179)).
> Decide the licensing posture with counsel **before** filing — you cannot walk
> it back. If undecided, file the disclosure first and add the licensing
> declaration in a later update (§5.5.B permits this).

A **blanket RF+RAND commitment** covering all of Sanctum's IPR on the specific
document fully satisfies the obligation (§5.4.3). Note: a vague "we'll license
everything under RAND" does **not** satisfy it — the commitment must be specific
to the document(s).

---

## 6. Keep disclosures updated (RFC 8179 §5.4.2)

Update the existing disclosure **promptly** when:

- the application **publishes** (~18 months) → add the published application number;
- a patent **issues** → add the issued patent number;
- an application is **abandoned** → withdraw the earlier disclosure;
- a **material change** to the draft causes it to cover additional IPR.

Disclosures are automatically **inherited** by later draft revisions
(`-01`, `-02`, …) and by any RFC published from the draft, unless updated or
withdrawn. No new disclosure is needed for foreign filings with substantially
identical claims (§5.4.2.B).

---

## 7. The Note Well — the obligation precedes the draft

The **[Note Well](https://www.ietf.org/about/note-well/)** binds every
participant: *if you are aware that any IETF contribution is covered by your (or
your employer's) patents or applications, you must disclose that fact or not
participate.*

> **Practical consequence:** the disclosure obligation is triggered by the
> **earliest** of: posting a draft, posting to a WG mailing list, or speaking in
> a WG session about the covered technology. If you intend to email
> `spasm@ietf.org` (LAMPS) or `oauth@ietf.org` about these mechanisms before the
> draft is posted, the application should already be on file and the disclosure
> ready.

---

## 8. Consequences of non-disclosure (RFC 8179 §6)

Failing to disclose is a violation of IETF policy and can, under applicable law,
**render the IPR unenforceable** against implementers
([RFC 8179 §6](https://www.rfc-editor.org/rfc/rfc8179);
sanctions per [RFC 6701](https://www.rfc-editor.org/rfc/rfc6701)). This is the
single largest avoidable risk — disclose on time.

---

## 9. Copyright vs. patent — they are separate (RFC 5378)

By posting with `ipr="trust200902"` you grant the IETF Trust a perpetual,
royalty-free **copyright** license to the *text*
([RFC 5378 §5.3](https://www.rfc-editor.org/rfc/rfc5378)). This grant explicitly
**does not** grant any patent license
([RFC 5378 §5.5](https://www.rfc-editor.org/rfc/rfc5378)). Your patent rights are
governed solely by BCP 79 and your licensing declaration. Posting a draft does
**not** give away your patent.

---

## 10. Pre-post checklist (per draft)

- [ ] Corresponding patent application **on file** (confirmed with counsel).
- [ ] Draft is disclosure-safe: no trade-secret numerics; OID numerics limited to
      public PEN root `1.3.6.1.4.1.65953`; IANA uses `TBD`/PEN-arc placeholders.
- [ ] `idnits` clean (run via `make` / CI / <https://author-tools.ietf.org/idnits3/>).
- [ ] Decide licensing posture with counsel (RF strongly recommended) **or**
      decide to defer the licensing declaration to a later update.
- [ ] Post the `-00` at <https://datatracker.ietf.org/submit/>.
- [ ] **Same day:** file IPR disclosure via
      <https://datatracker.ietf.org/ipr/add/holder/>, referencing the exact draft
      name + version, marked "based on unpublished patent applications."
- [ ] Save the disclosure confirmation URL/email.
- [ ] Calendar: update disclosure on application publication and on issuance.

---

### Key references

| Document | Relevance |
|---|---|
| [BCP 79 / RFC 8179](https://www.rfc-editor.org/rfc/rfc8179) | The IPR policy — disclosure, timing, licensing, consequences. |
| [BCP 78 / RFC 5378](https://www.rfc-editor.org/rfc/rfc5378) | Copyright grant to the IETF Trust (separate from patents). |
| [RFC 6701](https://www.rfc-editor.org/rfc/rfc6701) | Sanctions for IPR-policy violations. |
| [Note Well](https://www.ietf.org/about/note-well/) | Participation-level IPR obligation. |
| [IPR disclosure form](https://datatracker.ietf.org/ipr/add/holder/) | "Your IPR related to a specific IETF contribution." |
| [35 U.S.C. §102](https://www.law.cornell.edu/uscode/text/35/102) | U.S. novelty / grace-period statute. |

---

*© 2026 Sanctum SecOps LLC — Brian Vicente, Inventor. Patent pending.
PEN root: `1.3.6.1.4.1.65953`. NOT LEGAL ADVICE.*
