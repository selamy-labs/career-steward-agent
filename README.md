# Declarative Reeve Agent Repo Blueprint

This is a repository-shaped blueprint for a Reeve-like agent whose behavior is declared in source and reconciled into a running agent.

The central idea: the repo is not just code plus docs. The repo is the agent contract.

The repo is a source vessel, not the deployment itself. It should produce immutable delivery artifacts such as an OCI image and Helm chart, then downstream infrastructure repos decide when and how to deploy them.

## Objective

Represent a complete Reeve-class agent declaratively:

- identity and mandate
- model/runtime configuration
- tools and connectors
- skills and workflows
- knowledge stores and writable state
- schedules and event triggers
- approval gates and side-effect policy
- required secrets and account prerequisites
- deployment and reconciliation path
- observability and verification

The repository may depend on secrets, OAuth grants, bot accounts, browser profiles, or API keys. It must declare those dependencies explicitly, but it must not commit secret values.

## Source Of Truth

`agent.manifest.yaml` is the intended root declaration. Everything else should either be referenced by it or generated/validated from it:

```text
agent.manifest.yaml
  -> contracts/required-secrets.yaml
  -> workflows/*.yaml
  -> policies/*.yaml
  -> Helm/OpenTofu/ExternalSecret output
  -> runtime config
  -> cron/job registrations
  -> tests and conformance checks
```

## What This Fixes

Current Reeve already has many declarative pieces: Helm, ExternalSecrets, ArgoCD, ConfigMaps, OpenFeature flags, read-only managed scripts, cron bootstrap, state retention, and tests.

The missing layer is a single typed agent manifest that says, in one place:

- what the agent can do
- what accounts it acts through
- what secrets must exist
- what side effects are allowed
- what schedules run
- what durable state it owns
- what validation proves the agent is correctly instantiated

## Repository Shape

```text
.
├── agent.manifest.yaml
├── contracts/
│   └── required-secrets.yaml
├── docs/
│   ├── adr-001-vessel-and-distribution.md
│   └── repo-spec.md
├── policies/
│   └── approval-gates.yaml
├── reconcile/
│   └── README.md
├── schemas/
│   └── agent.manifest.schema.json
└── workflows/
    ├── career-steward.yaml
    ├── content-inbound.yaml
    ├── state-maintenance.yaml
    └── whatsapp-intake.yaml
```

## Secret Contract

Secrets are declared as required inputs:

- name
- provider
- external secret key
- runtime mount/env target
- scope of use
- verification command or check
- whether the credential is required for boot or only for a workflow

Secret values do not belong in git. The reconciler should fail fast when a required secret reference is missing or unverified.

## First Implementation Slice

The first real implementation should not clone all Reeve scripts by hand. It should implement the manifest contract and prove that these declared surfaces generate or validate:

1. ExternalSecrets mappings
2. runtime config
3. cron registrations
4. OpenFeature flags
5. approval-gate policy
6. capability inventory
7. conformance tests

After that, workflows can be ported one by one.

## Build And Distribution Position

The preferred vessel model is:

```text
source repo -> CI -> OCI image + Helm chart -> downstream infra repo -> deployment
```

Bazel can be the internal build graph for reproducible image/chart production. It should not be the only consumption path. Most downstream users should be able to pin an image digest and chart version without adopting Bazel.
