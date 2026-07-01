# Reconciler Contract

The reconciler is the named toolchain that turns `agent.manifest.yaml` into reality.

## Inputs

- `agent.manifest.yaml`
- `contracts/required-secrets.yaml`
- `policies/*.yaml`
- `workflows/*.yaml`

## Outputs

At minimum, the reconciler should generate or validate:

- Helm values
- Kubernetes StatefulSet
- ConfigMaps for runtime config, scripts, skills pins, and OpenFeature flags
- ExternalSecrets mappings
- Cron/job registrations
- PVC and state-maintenance configuration
- ArgoCD Application
- conformance test fixtures

## Required Checks

```text
schema-valid
secrets-declared-not-committed
secrets-verification-defined
approval-gates-present
external-side-effects-gated
private-data-redaction
immutable-runtime-boundary
generated-kubernetes-renders
workflow-schedules-declared
```

## Non-Declarative Prerequisites

Some setup cannot be fully automated:

- OAuth user consent
- Telegram bot creation
- Unipile account connection
- GitHub app/token issuance
- cloud secret-store creation

Those are allowed only as documented prerequisites whose outputs are referenced by declared secret mappings.

