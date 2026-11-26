> **Moved.** This project now lives in [d3dcrypted/llmops](https://github.com/d3dcrypted/llmops), in the [`security-governance/`](https://github.com/d3dcrypted/llmops/tree/main/security-governance) directory, together with the rest of the stack. This repository is archived and stays readable.

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

## Authorship

Human thought, machine hand. The author set the direction, took the decisions and reviewed the result; an AI assistant produced the drafting, the code and the prose in this file. Mistakes are the author's.
