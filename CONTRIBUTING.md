# Contributing

> [Benchmark](README.md) · [Protocol](docs/protocol.md)

Useful contributions include a scorer bug with a minimal invented fixture, an independently measured task with a defensible endpoint, or a preregistered model comparison with matched tasks and execution settings.

Do not upload private laboratory data, recipes, reference answers, institutional identifiers, raw model sessions or credentials in issues or pull requests. Use a clearly labelled fabricated software example to reproduce a bug. Private data access is handled separately through Vicena.

For a proposed scientific task, describe the decision, visible evidence, withheld measured outcome, independent unit, missing metadata, baseline, metric and likely failure modes. Identify what additional laboratory confirmation is needed. Do not substitute simulated or AI-generated outputs for measured ground truth.

For a run, freeze the protocol before execution, include all registered attempts and retain complete evidence privately. Report model IDs, harness, prompt version, tool access, budgets, completion status, aggregate metrics and limitations. Never mix different task versions in one model-ranking table. Do not post per-record outcomes to demonstrate a result without an explicit data-release decision.

Run `PYTHONPATH=src python3 -m unittest discover -s tests -v` before submitting code. The package must keep working offline with no inference credentials.
