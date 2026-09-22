# External Integrations

## Real integration boundary
UCOS contains real adapter paths for search/SEO, affiliate REST services, GA4 analytics and WordPress publishing. Availability is configuration-dependent.

## Production status semantics
- **LIVE:** credentials configured and a real runtime operation has been verified.
- **INTEGRATION_READY:** implementation exists and fail-closed behavior is tested, but live credential/runtime evidence is absent.
- **BLOCKED:** implementation or operational prerequisite prevents activation.

## Known integration-ready boundaries at the certified CI baseline
- SerpApi search adapter: real API-key boundary; no key means explicit failure.
- Generic affiliate REST adapter: real bearer-credential boundary.
- GA4 Data API adapter: real service-account boundary.
- WordPress REST adapter: real application-password boundary.
- Social platform adapters: account credentials and external mutation evidence required before calling them live.

No secrets belong in this registry.
