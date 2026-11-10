# Run the toolkit

> [Benchmark](../README.md) · [Data dictionary](data-dictionary.md) · [Protocol](protocol.md)

The toolkit is offline and makes no inference calls. Its public demo tests arithmetic and file handling with invented controls. Reproducing the reported experimental results requires the private data; cloning this repository does not provide it. To discuss access, contact [Vicena](https://vicena.ai/experimental-data).

## No-data demo

```sh
PYTHONPATH=src python3 -m vicena_science_benchmark demo
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

No dependencies are needed beyond Python 3.12+. Alternatively, `uv run --locked vicena-science-benchmark demo` installs the local package using the lockfile.

## Bring a private task bundle

Store your task and measurements outside this repository, following the [data dictionary](data-dictionary.md). Substitute your own paths below. Use a separate evaluator workspace for the reference; never mount that workspace into the tested model environment.

```sh
uv run --locked vicena-science-benchmark validate --family battery \
  --task /private/case/task.json --readings /private/case/readings.csv

uv run --locked vicena-science-benchmark pack --family battery \
  --task /private/case/task.json --readings /private/case/readings.csv \
  --out /private/battery-inputs.zip

uv run --locked vicena-science-benchmark baselines --family battery \
  --task /private/case/task.json --readings /private/case/readings.csv

uv run --locked vicena-science-benchmark grade \
  --answer /private/submissions/answer.json \
  --reference /evaluator-only/reference.json
```

Use `--family catalyst` for catalyst scans. Each reference file describes one task family. The baseline command returns one answer-shaped object per method; save the chosen method's object as an answer file to grade it. It never reads the reference.

`pack` checks the visible cutoffs, IDs and file structure, copies only `task.json` and `readings.csv`, and refuses to overwrite an archive. It retains their bytes. It does not anonymize arbitrary inputs, inspect prose for hidden answers or enforce operating-system isolation. Review metadata and the question before sharing a packet.

## Run a model

Use your own approved model application or harness. This release intentionally has no API-key configuration, automatic retries or paid inference launcher. Follow the same registered protocol for Astra (`openai/gpt-6-astra`), Sol (`openai/gpt-6.1-sol`) and Luna (`openai/gpt-6-luna`); those are the IDs in the existing evaluation records, not a guarantee that every provider currently exposes them.

Record model and returned provider ID when available, effort, prompt/file hashes, tool capabilities, start/end times, completion status, full transcript location and usage. An application picker label alone does not prove the actual provider route. Keep application-generated context and tool differences visible in the report.

For Vicena notebooks, the registered task instructions require a unique directory under `/root`, retaining its exact path, and a new `Analysis.ipynb` there. Permit only the packet and installed static scientific guidance; prohibit web access, unrelated records, prior results and saved-memory use. Audit all visible actions before scoring. This does not turn a shared app computer into an enforced sandbox.

## Review and contribute

Freeze submissions before grading. Review scientific correctness, process and communication separately. A score checks the numerical fields; it does not certify explanations or causal claims. Keep complete evidence privately and submit only the agreed public aggregates. See [contribution requirements](../CONTRIBUTING.md).
