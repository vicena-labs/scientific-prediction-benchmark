# Results by condition block

> [Benchmark](../README.md) · [Overall comparison](multi-model-results.md) · [Aggregate JSON](../results/multi-model-summary.json)

Each cell gives correct choices followed by forecast mean absolute error (MAE). Attempt numbers identify the registered repetition; incomplete attempts are listed in the overall result table. Blocks reuse records and are not independent replications.

## Battery

Error unit: retention percentage points. Columns show **correct / total · MAE**.

| Configuration / attempt | 25 °C | 45 °C | High temperature, setpoint unconfirmed |
| --- | ---: | ---: | ---: |
| Baseline: carry forward | 3/3 · 2.594 | 1/3 · 12.026 | 1/6 · 2.940 |
| Baseline: robust trend | 2/3 · 1.279 | 2/3 · 8.101 | 1/6 · 1.248 |
| Astra / 1 | 3/3 · 1.285 | 2/3 · 7.887 | 1/6 · 0.955 |
| Astra / 2 | 2/3 · 1.285 | 2/3 · 7.754 | 0/6 · 0.855 |
| Sol 6.1 Pro / 1 | 3/3 · 1.068 | 1/3 · 9.237 | 1/6 · 1.649 |
| Sol 6.1 Pro / 2 | 2/3 · 1.301 | 2/3 · 7.941 | 0/6 · 0.890 |
| Fable 5.2 / 1 | 3/3 · 0.980 | 1/3 · 5.587 | 0/6 · 1.126 |
| Fable 5.2 / 2 | 2/3 · 1.255 | 1/3 · 4.321 | 1/6 · 2.244 |
| Opus 5.5 · Anthropic route / 1 | 2/3 · 1.489 | 2/3 · 5.254 | 2/6 · 0.501 |
| Opus 5.5 · Anthropic route / 2 | 2/3 · 1.989 | 1/3 · 4.321 | 0/6 · 1.394 |
| Opus 5.5 · Google route / 1 | 3/3 · 1.722 | 1/3 · 6.221 | 2/6 · 0.595 |
| Grok 4.7 / 1 | 2/3 · 1.461 | 1/3 · 8.374 | 1/6 · 1.152 |
| DeepSeek V4 Pro 0813† / 1 | 2/3 · 1.251 | 2/3 · 7.721 | 1/6 · 1.180 |
| DeepSeek V4.1 Flash 1017 / 1 | 3/3 · 1.285 | 1/3 · 9.587 | 1/6 · 1.556 |
| GLM 5.3† / 1 | 2/3 · 3.922 | 0/3 · 3.457 | 0/6 · 14.744 |
| GLM 5.3† / 2 | 2/3 · 1.011 | 1/3 · 9.657 | 1/6 · 1.919 |
| Luna / 1 | 2/3 · 1.278 | 2/3 · 8.076 | 1/6 · 1.250 |
| Luna / 2 | 2/3 · 1.278 | 2/3 · 8.101 | 1/6 · 1.248 |

## Catalyst

Error unit: mA. Columns show **correct / total · MAE**.

| Configuration / attempt | GC | NF-DC | NF-IMP |
| --- | ---: | ---: | ---: |
| Baseline: carry forward | 0/1 · 0.390 | 1/3 · 26.806 | 3/3 · 18.038 |
| Baseline: linear tail | 1/1 · 0.215 | 1/3 · 24.589 | 3/3 · 16.478 |
| Astra / 1 | 1/1 · 0.100 | 1/3 · 22.488 | 3/3 · 15.241 |
| Sol 6.1 Pro / 1 | 1/1 · 0.106 | 0/3 · 21.322 | 3/3 · 14.428 |
| Sol 6.1 Pro / 2 | 1/1 · 0.104 | 0/3 · 20.012 | 3/3 · 13.301 |
| Fable 5.2 / 1 | 1/1 · 0.074 | 1/3 · 5.685 | 3/3 · 3.486 |
| Opus 5.5 · Anthropic route / 1 | 0/1 · 0.215 | 3/3 · 5.148 | 3/3 · 3.392 |
| Opus 5.5 · Anthropic route / 2 | 1/1 · 0.075 | 1/3 · 8.918 | 3/3 · 14.552 |
| Grok 4.7 / 1 | 1/1 · 0.127 | 1/3 · 18.792 | 3/3 · 11.764 |
| DeepSeek V4 Pro 0813† / 1 | 1/1 · 0.071 | 1/3 · 21.612 | 3/3 · 14.271 |
| DeepSeek V4 Pro 0813† / 2 | 1/1 · 0.071 | 1/3 · 21.615 | 3/3 · 14.271 |
| DeepSeek V4.1 Flash 1017 / 1 | 1/1 · 0.074 | 1/3 · 22.015 | 3/3 · 14.681 |
| DeepSeek V4.1 Flash 1017 / 2 | 1/1 · 0.134 | 1/3 · 20.615 | 3/3 · 13.814 |
| GLM 5.3† / 1 | 1/1 · 0.065 | 2/3 · 23.615 | 2/3 · 15.614 |
| GLM 5.3† / 2 | 1/1 · 0.134 | 1/3 · 23.978 | 3/3 · 16.031 |
| Luna / 1 | 1/1 · 0.165 | 1/3 · 23.695 | 3/3 · 15.814 |

Catalyst current scales differ across electrode groups, so the pooled MAE must be read with these block results. The target is signed current from the same scan, with no area normalization or independently verified intrinsic-activity ranking. Battery strict pair choices also include small gaps; their practical significance needs laboratory confirmation.
