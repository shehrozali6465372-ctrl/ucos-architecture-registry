# Layer 17 — Security

Registry status: **CERTIFIED — dedicated production gate passed**

## Responsibility
Layer 17 is the security boundary for authentication, authorization, token handling, encryption/signatures, input/SSRF validation, security policies, firewall/rate limiting, secret handling, and security audit primitives.

## Implementation source of truth
shehrozali6465372-ctrl/universal-content-operating-system

Production-certified merge commit:
733457c310d65ffbf3ccc4169662d485373beb6d

Merged PR:
#46 — Layer 17 production certification — security hardening

## Verified hardening
- Passwords use PBKDF2-HMAC-SHA256 with per-user random salt.
- API-key lookup uses a SHA-256 digest rather than plaintext storage.
- Encryption uses AES-GCM with authenticated ciphertext and no fallback/default key.
- HMAC signing fails closed when the requested key is absent.
- JWT validation pins HS256, validates issuer/expiry, and rejects malformed tokens.
- Production requires strong configured JWT/encryption key material; short test credentials remain non-production compatibility only.
- Permission evaluation defaults to deny and explicit deny overrides allow.
- Firewall rate limiting is bounded and thread-safe.
- Expired token cleanup removes reverse-index references.
- In-memory secret storage is disabled in production.
- URL validation rejects local, private, loopback, link-local, multicast, reserved, unspecified, and cloud-metadata targets.

## Dedicated certification evidence
Workflow: .github/workflows/layer17-production-certification.yml

Successful run: Layer 17 Production Certification #13

Verified steps:
1. Python compilation — PASS
2. Strict Ruff E/F/W gate — PASS
3. High-confidence secret pattern scan — PASS
4. Layer 17 production security gate — PASS
5. Legacy security regression suite (tests/test_phase4_security.py) — PASS
6. Layer 17 module regression gate — PASS
7. Certification evidence artifact upload — PASS

## Regression boundary
The repository-wide CI run after the merge did not become globally green. Its failure was a pytest collection collision between:
- tests/layer19_analytics_engine/test_production_certification.py
- tests/layer20_image_pipeline/test_production_certification.py

The failure occurred during test collection and was unrelated to Layer 17. Layer 17's dedicated production certification remained green.

## Certification scope
This certificate covers the Layer 17 implementation and its dedicated executable security/regression gates at the certified commit. It does not claim live external-provider credentials, live traffic, or globally green repository CI.