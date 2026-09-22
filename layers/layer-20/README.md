# Layer 20 — Image Pipeline

**Implementation mapping:** `layers/layer20_image_pipeline`.

**Responsibility:** image-provider routing, capability negotiation, validation, provenance and multimodal asset handling.

**Verified architecture:** production paths fail closed without a real configured provider; provider/job identifiers, hashes and provenance are required where available.

**Status:** VERIFIED fail-closed boundary; real provider runtime is INTEGRATION_READY until externally verified.

**Boundary:** no mock/synthetic provider result may reach production publishing.