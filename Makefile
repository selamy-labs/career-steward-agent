.PHONY: verify test sim

PYTHON ?= python3
export PYTHONPATH := src

verify:
	$(PYTHON) scripts/verify.py
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) -m reeve_spec.sim --manifest agent.manifest.yaml --input examples/sim/inbound-message.json --out generated/sim-run.json

test:
	$(PYTHON) -m unittest discover -s tests -v

sim:
	$(PYTHON) -m reeve_spec.sim --manifest agent.manifest.yaml --input examples/sim/inbound-message.json --out generated/sim-run.json
