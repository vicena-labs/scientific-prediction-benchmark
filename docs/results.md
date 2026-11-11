# Earlier Astra pilots and evidence limits

> [Benchmark](../README.md) · [Protocol](protocol.md) · [Aggregate JSON](../results/pilot-summary.json)

This historical page records the 9 November 2026 Astra pilots, plus the excluded application attempt. The [10 November multi-model comparison](multi-model-results.md) and [current assessment](assessment.md) supersede this page as the overall result summary. The source records, targets and comparisons are the same; the harnesses and prompts differ. Rows are not repeated independent trials and are not pooled.

| Setup, all run on 9 November | Battery correct choices | Battery error, percentage points | Catalyst correct choices | Catalyst error, mA |
| --- | ---: | ---: | ---: | ---: |
| Astra, isolated Python tool, High, 10-minute limit | 4/12 | 3.254 | 4/7 | 13.558 |
| Astra, first Vicena app protocol, High, 5-minute limit | 6/12 | 3.571 | Excluded | — |
| Astra, native Vicena notebooks, High, 5-minute limit | 3/12 | 3.519 | 5/7 | 11.717 |

The first Vicena catalyst attempt had an incomplete final answer after a protocol conflict: the user prompt prohibited notebooks even though the application required them, and the requested notebook path was unsupported. It is not a scientific failure score. The notebook-compatible rerun resolved that conflict. Its battery and catalyst answers completed within observed windows of 189 and 160 seconds.

## Baselines

| Task | Method | Correct choices | Mean absolute error |
| --- | --- | ---: | ---: |
| Battery | Carry-forward, primary | 5/12 | 5.562 percentage points |
| Battery | Robust trend, secondary | 5/12 | 3.313 percentage points |
| Catalyst | Linear tail, primary | 5/7 | 15.454 mA |
| Catalyst | Carry-forward, secondary | 4/7 | 16.914 mA |

In the notebook run, Astra made fewer correct battery selections than either baseline despite lower forecast error than carry-forward. For catalyst scans, it matched the primary baseline's selection count with lower forecast error. These findings support keeping choice and numerical prediction as separate metrics. They do not establish a general model ranking or that training on these data would improve performance.

## Notebook run by block

| Task/block | Astra choices | Astra mean absolute error |
| --- | ---: | ---: |
| Battery, 25 °C | 2/3 | 1.685 percentage points |
| Battery, 45 °C | 1/3 | 8.367 percentage points |
| Battery, high-temperature setpoint unconfirmed | 0/6 | 1.257 percentage points |
| Catalyst, GC | 1/1 | 0.071 mA |
| Catalyst, NF-DC | 1/3 | 19.101 mA |
| Catalyst, NF-IMP | 3/3 | 12.096 mA |

Astra's Brier scores were 0.273 for battery and 0.176 for catalyst, against 0.25 for a constant 50/50 forecast. Its probability distributions were based on explicit judgmental assumptions, not independently calibrated frequencies. Small numerical errors can still reverse close rankings, and uncertainty over future behavior remains substantial.

## Model coverage in these earlier setups

| Model | Requested ID | Status for this exact paired-outcome version |
| --- | --- | --- |
| Astra | `openai/gpt-6-astra` | Completed in the three setups above |
| Sol | `openai/gpt-6.1-sol` | Not run in these setups |
| Luna | `openai/gpt-6-luna` | Not run in these setups |

Sol and Luna were used in earlier studies with different questions; those scores are not pooled here. The later shared-harness comparison now includes Astra, Sol 6.1 Pro, Luna and six other models. See [all completed attempts](multi-model-results.md). No new inference was performed to update this public release.

## Evidence and reproducibility

The private audit replayed source values and target calculations, verified unchanged source files and input hashes, reproduced baseline calculations and independently checked submitted numerical scores. The public standalone grader was then replayed locally against the saved answers and references. Its outputs matched the existing scorer to floating-point tolerance. These are maintainer verification statements; the public repository excludes the underlying evidence files.

The recorded native-app tool actions showed only permitted inputs and static guidance. Shared account context was not OS-isolated, and exports identified requested models without exposing returned provider IDs or actual authentication routes. The data had been inspected during earlier development. Ten battery traces and eight catalyst scans yield correlated comparisons, with incomplete experimental context. Consequently this release is a documented private-data pilot with an open scoring toolkit, not an independently reproducible public-data leaderboard.
