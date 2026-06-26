#!/usr/bin/env python3
"""
generate_r5_artifacts.py - Generate stub R5 artifact files for CI validation.

Produces exactly 24 .der files + 1 .csv in ./r5-artifacts/:
  8 x _ta.der   (self-signed X.509 TA certificates)
  8 x _priv.der (private key blobs, not parseable as certs)
  4 x _seed.der
  2 x _expandedkey.der
  2 x _both.der
  1 x   .csv    (artifact manifest)
"""
import os, csv, hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

OUTDIR = Path(os.environ.get("R5_ARTIFACT_DIR", "./r5-artifacts"))
OUTDIR.mkdir(parents=True, exist_ok=True)

now = datetime.now(timezone.utc)
manifest = []


def gen_ta(name: str) -> bytes:
    """Generate a self-signed DER-encoded X.509 TA cert."""
    key = ec.generate_private_key(ec.SECP256R1())
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, name),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Sanctum SecOps LLC"),
    ])
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=1))
        .not_valid_after(now + timedelta(days=3650))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(key, hashes.SHA256())
    )
    return cert.public_bytes(serialization.Encoding.DER)


def write(filename: str, data: bytes):
    p = OUTDIR / filename
    p.write_bytes(data)
    sha = hashlib.sha256(data).hexdigest()
    manifest.append({"filename": filename, "size": len(data), "sha256": sha})
    print(f"  wrote {filename} ({len(data)} bytes)")


print(f"Generating R5 artifacts -> {OUTDIR.resolve()}")

# 8 TA certificates
ta_names = [
    "R5-Root-CA-1", "R5-Root-CA-2", "R5-Root-CA-3", "R5-Root-CA-4",
    "R5-Root-CA-5", "R5-Root-CA-6", "R5-Root-CA-7", "R5-Root-CA-8",
]
for name in ta_names:
    der = gen_ta(name)
    write(f"{name.lower().replace('-', '_')}_ta.der", der)

# 8 private key blobs (raw bytes that will not parse as X.509 certs)
for i in range(1, 9):
    priv_data = b"PRIVKEY:" + os.urandom(120)
    write(f"r5_key_{i:02d}_priv.der", priv_data)

# 4 seed blobs
for i in range(1, 5):
    write(f"r5_seed_{i:02d}_seed.der", b"SEED:" + os.urandom(64))

# 2 expanded-key blobs
for i in range(1, 3):
    write(f"r5_expkey_{i:02d}_expandedkey.der", b"EXPKEY:" + os.urandom(96))

# 2 combined blobs
for i in range(1, 3):
    write(f"r5_both_{i:02d}_both.der", b"BOTH:" + os.urandom(88))

# CSV manifest
csv_path = OUTDIR / "r5_artifact_manifest.csv"
with open(csv_path, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["filename", "size", "sha256"])
    w.writeheader()
    w.writerows(manifest)
print(f"  wrote r5_artifact_manifest.csv ({len(manifest)} entries)")

total = len(list(OUTDIR.glob("*.der")))
print(f"\nDone. {total} .der files + 1 .csv in {OUTDIR}")
assert total == 24, f"Expected 24 .der files, got {total}"
