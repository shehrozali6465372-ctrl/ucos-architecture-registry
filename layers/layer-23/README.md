# Layer 23 — Website Manager

**Implementation mapping:** `layers/layer23_website_manager`.

**Responsibility:** website operations, AtoZ bridge, website publishing, traffic, Pinterest and affiliate-facing website workflows.

**Verified architecture:** request IDs and external mutation boundaries require durable idempotency/reconciliation; website publishing requires explicit policy authorization; caller-supplied asset paths must be confined to an approved asset root and validated as regular image files.

**Status:** VERIFIED architecture; live website/social operation requires configured accounts and real runtime evidence.

**Boundary:** website orchestration must not bypass global quality, safety, account-identity or mutation controls.