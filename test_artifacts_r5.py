#!/usr/bin/env python3
"""
test_artifacts_r5.py - Full positive + negative validation suite for R5 artifacts.
Run from the repo root. Artifact directory resolved via R5_ARTIFACT_DIR env var,
or falls back to ./r5-artifacts then /home/cyadmin/sanctum/r5-artifacts.
"""
import os, sys, hashlib
from pathlib import Path
from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend

ARTDIR = Path(os.environ.get("R5_ARTIFACT_DIR", "./r5-artifacts"))
if not ARTDIR.exists():
    ARTDIR = Path("/home/cyadmin/sanctum/r5-artifacts")

PASS_STR = "\033[92m\u2705 PASS\033[0m"
FAIL_STR = "\033[91m\u274c FAIL\033[0m"
results = []

def record(name, passed, detail=""):
    status = PASS_STR if passed else FAIL_STR
    print(f"  {status}  {name}" + (f" \u2014 {detail}" if detail else ""))
    results.append((name, passed))

def ta_files(): return sorted(ARTDIR.glob("*_ta.der"))
def all_ders(): return sorted(ARTDIR.glob("*.der"))

print("\n" + "=" * 60)
print("  R5 ARTIFACT VALIDATION SUITE")
print(f"  Artifact dir: {ARTDIR.resolve()}")
print("=" * 60)

print("\n[ POSITIVE TESTS ]")

all_d = list(all_ders())
record("P1: 24 artifact files present", len(all_d) == 24, f"found {len(all_d)}")

ta_certs = {}
for f in ta_files():
    try:
        ta_certs[f.name] = x509.load_der_x509_certificate(f.read_bytes(), default_backend())
    except Exception as e:
        record(f"P2: Parse {f.name}", False, str(e))
ta_list = list(ta_files())
record("P2: All TA certs parse as X.509", len(ta_certs) == len(ta_list),
       f"{len(ta_certs)}/{len(ta_list)}")

bad = [n for n, c in ta_certs.items() if c.issuer != c.subject]
record("P3: All TA certs self-signed", len(bad) == 0,
       f"not self-signed: {bad}" if bad else "")

csvs = list(ARTDIR.glob("*.csv"))
record("P4: CSV file present", len(csvs) >= 1, f"found {len(csvs)}")

for f in ta_files():
    raw = f.read_bytes()
    has_pk = b'\x02\x01\x00' in raw[:20]
    record(f"P5: No privkey marker in {f.name}", not has_pk)

now = datetime.now(timezone.utc)
for name, cert in ta_certs.items():
    nb = cert.not_valid_before_utc
    na = cert.not_valid_after_utc
    record(f"P6: Validity sane {name}", nb < na and na > now,
           f"{nb.date()}\u2192{na.date()}")

stray = [f.name for f in ARTDIR.iterdir()
         if f.is_file() and f.suffix not in (".der", ".csv")]
if stray:
    print(f"  \u26a0\ufe0f  WARN  P7: Stray files detected: {stray}")
else:
    record("P7: No stray files in artifact dir", True)

print("\n[ NEGATIVE TESTS ]")

first = list(ta_files())[0]
raw = first.read_bytes()

try:
    x509.load_der_x509_certificate(raw[:50], default_backend())
    record("N1: Truncated DER rejected", False, "parsed without error")
except Exception:
    record("N1: Truncated DER rejected", True)

flipped = bytearray(raw)
flipped[-10] ^= 0xFF
record("N2: Bit-flip changes cert hash",
       hashlib.sha256(bytes(flipped)).digest() != hashlib.sha256(raw).digest())

try:
    x509.load_der_x509_certificate(b"", default_backend())
    record("N3: Empty DER rejected", False)
except Exception:
    record("N3: Empty DER rejected", True)

try:
    x509.load_der_x509_certificate(os.urandom(512), default_backend())
    record("N4: Random bytes rejected", False)
except Exception:
    record("N4: Random bytes rejected", True)

priv_files = (list(ARTDIR.glob("*_priv.der")) +
              list(ARTDIR.glob("*_seed.der")) +
              list(ARTDIR.glob("*_expandedkey.der")) +
              list(ARTDIR.glob("*_both.der")))
for f in priv_files:
    try:
        x509.load_der_x509_certificate(f.read_bytes(), default_backend())
        record(f"N5: {f.name} rejected as cert", False, "parsed as cert - BAD")
    except Exception:
        record(f"N5: {f.name} rejected as cert", True)

print("\n" + "=" * 60)
total = len(results)
passed = sum(1 for _, p in results if p)
failed = total - passed
print(f"  RESULTS: {passed}/{total} passed  |  {failed} failed")
print("=" * 60 + "\n")
if failed:
    print("FAILED TESTS:")
    for name, p in results:
        if not p:
            print(f"  \u274c {name}")
sys.exit(0 if failed == 0 else 1)
