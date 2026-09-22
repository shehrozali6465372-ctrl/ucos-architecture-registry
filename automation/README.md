# Registry Automation

The registry is designed to stay synchronized with the implementation repository without pretending that synchronization is real-time until the automation is actually installed and verified.

## Target workflow
1. UCOS main repository push/change event identifies implementation SHA.
2. Registry workflow fetches that exact SHA.
3. Scanner maps 23 layer directories, modules, tests, shared boundaries and key documentation.
4. Generated evidence is compared with the registry.
5. Drift is reported or committed through a controlled registry update.
6. CI validates registry consistency.

## Current status
**DESIGN VERIFIED; automation runtime not yet claimed LIVE.**

A scheduled workflow may be used as a fallback if cross-repository dispatch permissions are unavailable. Secrets/tokens must never be stored in generated architecture files.
