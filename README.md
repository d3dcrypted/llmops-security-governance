# LLMOps Security and Governance

A practical control-plane scaffold for safer LLM applications. It treats security as an application boundary: classify inputs, apply policy, redact sensitive values, and retain auditable decisions without storing raw secrets.

## Roadmap

- [x] deterministic baseline policy checks
- [x] minimal PII redaction example
- [x] structured decision record
- [ ] prompt-injection evaluation corpus
- [ ] provider-independent guardrail adapters
- [ ] retention and access-control reference
- [ ] red-team CI checks

## Run

```bash
python3 -m unittest discover -s tests -v
```

This is not a security certification or a substitute for threat modeling and human review.
