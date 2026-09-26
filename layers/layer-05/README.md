# Layer 05 — Image

## Verification state
**Status: HARDENED — NOT YET PRODUCTION CERTIFIED**

Certification is blocked until the current UCOS main commit passes the repository CI suite and a real image-generation smoke test succeeds through a configured production provider. Source-code presence alone is not treated as certification.

## Responsibility
Image planning, prompt construction, layout, accessibility checks, visual-quality evaluation, provider orchestration, real image generation, optimization, infographic generation, thumbnail/carousel planning, and asset provenance.

## Implementation inventory
- Implementation root: layers/layer05_image
- Python modules: 30
- Classes: 32
- Functions/methods: 103
- Inventory source commit: f41eaeb1791208367dc7d12af225fff9775a8945

## Production-hardening changes applied
- Gemini provider remains supported, with fail-closed handling of current API errors.
- OpenRouter image provider added as the temporary production image-generation path using `OPENROUTER_API_KEY`.
- Provider authentication is fail-closed; no prompt-only/synthetic success is returned.
- API key is sent through the x-goog-api-key header rather than URL query parameters.
- Real image bytes are required and persisted atomically.
- Asset SHA-256 provenance is recorded.
- Mock providers are explicitly rejected by the production orchestrator.
- Orchestrator requires a complete real asset.
- Image planning, prompt, carousel, thumbnail and infographic IDs use UUIDs instead of time-based IDs.
- Invalid platforms, image types, styles, chart types, dimensions, layouts and colors fail closed.
- Boundary tests were added for missing credentials, invalid sizes, real-response persistence, and reference URL fail-closed behavior.
- ImageMemory now rejects empty/invalid records and bounds in-memory history to 1,000 records.
- ImagePlan and LayoutSpec constructors reject unsupported values instead of silently falling back.
- Main CI now includes a Layer 5 Ruff lint gate in addition to the targeted provider tests.
- Latest UCOS hardening commits: `75d6d7761b74e93024a49749b069fc50d79e5915`, `23bf3124f83a3ff48e850145c4c44fee5b2fa766`, `b5362797c95e9846a1186d9b7e356b9e60a37fbf`, `d9392372b358e145bfba6f6f5070aec7e41637d5`, `7118219945d3568f644ec71d51680ab56d49649c`.

## Critical flow
topic → image plan → prompt → layout → configured provider → real image bytes → atomic persistence → provenance hash → optimization → Layer 5 result

## Remaining certification gates
1. Full CI green on the post-hardening main commit.
2. Layer 05 targeted tests green in CI.
3. Full system boot remains 23/23 with zero errors.
4. Real configured image-provider smoke test produces a non-empty image asset.
5. Generated asset is persisted and its SHA-256 provenance is verifiable.
6. End-to-end Layer 04 → Layer 05 → downstream asset consumer flow passes.
7. Failure-path verification: auth failure, 429, timeout/network failure, malformed response, empty image response, invalid input, and storage failure.
8. Concurrency/idempotency verification for repeated generation requests.
9. No mock/synthetic result can cross the production boundary.

**Certification rule:** Until all gates above have evidence, Layer 05 remains NOT CERTIFIED.


## Latest hardening evidence
- UCOS commit: `333a09023d6ccaa6b124c3488a2f35b326cbc0d1` — corrected the Gemini image-generation request contract to use the documented `responseFormat.image` fields and added supported 1K/2K/4K resolution mapping.
- UCOS commit: `3312ebf45342b2b2d59e0136caf571e06570c9c5` — added regression coverage for the current Gemini request contract and fail-closed reference URL behavior.
- UCOS commit: `e7228c9b7e5f83120f9d53feefd0f8af3253819e` — added the Layer 5 provider tests to the main CI workflow.
- Current certification state remains **NOT CERTIFIED**. The latest real OpenRouter smoke reached the API but returned HTTP 402 (`insufficient credits`), so no real image bytes/provenance evidence exists yet. CI therefore remains blocking rather than treating a skipped or failed provider smoke as certification.
