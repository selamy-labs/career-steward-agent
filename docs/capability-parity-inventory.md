# Capability Parity Inventory

The machine-readable inventory is `docs/capability-parity-inventory.yaml`.

Evidence is sourced from:

- local read-only copy of the source-agent GitOps bundle outside this reusable repo
- live source-agent coordination thread around messages `26824-26926`

The live read-only inventory artifact was not discoverable, so this v1 inventory uses observable thread activity plus copied bundle files. That is a recorded evidence limitation, not a hidden assumption.

Every row maps:

```text
source-agent capability -> declarative surface -> proving test
```

Parity exceptions: none for v1. Live-account sends and real publishing are intentionally out of scope and represented as approval-gated or forbidden surfaces.
