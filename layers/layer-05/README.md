# Layer 05 — Image

## Verification state
**Status: HARDENED — NOT YET PRODUCTION CERTIFIED**

Certification is blocked until the current UCOS main commit passes the repository CI suite and a real Gemini image-generation smoke test is executed with a valid provider credential. Source-code presence alone is not treated as certification.

## Responsibility
Image planning, prompt construction, layout, accessibility checks, visual-quality evaluation, provider orchestration, real image generation, optimization, infographic generation, thumbnail/carousel planning, and asset provenance.

## Implementation inventory
- Implementation root: layers/layer05_image
- Python modules: 30
- Classes: 32
- Functions/methods: 103
- Inventory source commit: f41eaeb1791208367dc7d12af225fff9775a8945

## Production-hardening changes applied
- Gemini provider changed to supported native image-capable Gemini models.
- Provider authentication is fail-closed; no prompt-only/synthetic success is returned.
- API key is sent through the x-goog-api-key header rather than URL query parameters.
- Real image bytes are required and persisted atomically.
- Asset SHA-256 provenance is recorded.
- Mock providers are explicitly rejected by the production orchestrator.
- Orchestrator requires a complete real asset.
- Image planning, prompt, carousel, thumbnail and infographic IDs use UUIDs instead of time-based IDs.
- Invalid platforms, image types, styles, chart types, dimensions, layouts and colors fail closed.
- Boundary tests were added for missing credentials, invalid sizes and real-response persistence.

## Critical flow
topic → image plan → prompt → layout → configured provider → real image bytes → atomic persistence → provenance hash → optimization → Layer 5 result

## Remaining certification gates
1. Full CI green on the post-hardening main commit.
2. Layer 05 targeted tests green in CI.
3. Full system boot remains 23/23 with zero errors.
4. Real Gemini credential/model smoke test produces a non-empty image asset.
5. Generated asset is persisted and its SHA-256 provenance is verifiable.
6. End-to-end Layer 04 → Layer 05 → downstream asset consumer flow passes.
7. Failure-path verification: auth failure, 429, timeout/network failure, malformed response, empty image response, invalid input, and storage failure.
8. Concurrency/idempotency verification for repeated generation requests.
9. No mock/synthetic result can cross the production boundary.

**Certification rule:** Until all gates above have evidence, Layer 05 remains NOT CERTIFIED.
