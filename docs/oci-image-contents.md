# OCI Image Contents

## Decision

The v1 OCI image contains both the reference runtime payload and the reference reconciler tools. The image is a delivery artifact, not a deployment.

## Included

- Hermes-compatible entrypoint and runtime bootstrap hooks
- `reeve_spec` Python reference package
- manifest validator
- reconciler
- sim-mode runner
- workflow manifests
- policy manifests
- schemas
- default fake fixtures for sim mode
- conformance test runner

## Excluded

- real credentials
- real OAuth tokens
- source-operator private data
- live browser profiles
- cluster-specific kubeconfig
- downstream secret-store values
- environment-specific deployment decisions

## Consumer Contract

Consumers pin the image by digest. The Helm chart mounts or embeds the selected manifest and wires declared secret references from the downstream environment.
