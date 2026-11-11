# Multi-model results

> [Benchmark](../README.md) · [Assessment](assessment.md) · [Aggregate JSON](../results/multi-model-summary.json)

Completed 10 November 2026: 30 scored attempts across nine distinct models. The shared tasks and isolated Python harness use hidden measured outcomes. Counts below are correct related pair comparisons per attempt, not independent experiment counts. Every completed attempt is shown. No results are pooled with the earlier Vicena or subscription studies.

## Battery

| Model / provider configuration | Completed / planned | Correct choices, each attempt | Forecast MAE, each attempt |
| --- | ---: | --- | --- |
| Astra | 2/2 | 6/12, 4/12 | 3.134, 3.054 |
| Sol 6.1 Pro | 2/2 | 5/12, 4/12 | 3.751, 3.129 |
| Fable 5.2 | 2/2 | 4/12, 4/12 | 2.421, 2.570 |
| Opus 5.5 · Anthropic route | 2/2 | 6/12, 3/12 | 2.223, 2.450 |
| Opus 5.5 · Google route | 1/2 | 6/12 | 2.621 |
| Gemini 4 Carbon | 0/2 | No score | No score |
| Grok 4.7 | 1/2 | 4/12 | 3.412 |
| DeepSeek V4 Pro 0813† | 1/2 | 5/12 | 3.164 |
| DeepSeek V4.1 Flash 1017 | 1/2 | 5/12 | 3.884 |
| GLM 5.3† | 2/2 | 2/12, 4/12 | 8.111, 3.968 |
| Luna | 2/2 | 5/12, 5/12 | 3.306, 3.313 |
| Sol 6.1 | 0/2 | No score | No score |

MAE units: retention percentage points; lower is better. Each task reuses 10 records and 12 related comparisons.

| Baseline | Correct choices | Forecast MAE |
| --- | ---: | ---: |
| carry forward | 5/12 | 5.562 |
| robust trend | 5/12 | 3.313 |

## Catalyst

| Model / provider configuration | Completed / planned | Correct choices, each attempt | Forecast MAE, each attempt |
| --- | ---: | --- | --- |
| Astra | 1/2 | 5/7 | 14.174 |
| Sol 6.1 Pro | 2/2 | 4/7, 4/7 | 13.433, 12.518 |
| Fable 5.2 | 1/2 | 5/7 | 3.458 |
| Opus 5.5 · Anthropic route | 2/2 | 6/7, 5/7 | 3.256, 8.820 |
| Opus 5.5 · Google route | 0/2 | No score | No score |
| Gemini 4 Carbon | 0/2 | No score | No score |
| Grok 4.7 | 1/2 | 5/7 | 11.490 |
| DeepSeek V4 Pro 0813† | 2/2 | 5/7, 5/7 | 13.474, 13.475 |
| DeepSeek V4.1 Flash 1017 | 2/2 | 5/7, 5/7 | 13.780, 12.945 |
| GLM 5.3† | 2/2 | 5/7, 5/7 | 14.727, 15.037 |
| Luna | 1/2 | 5/7 | 14.857 |
| Sol 6.1 | 0/2 | No score | No score |

MAE units: mA; lower is better. Each task reuses 8 records and 7 related comparisons.

| Baseline | Correct choices | Forecast MAE |
| --- | ---: | ---: |
| carry forward | 4/7 | 16.914 |
| linear tail | 5/7 | 15.454 |

Uniform random pair selection has an expected score of 6/12 for battery and 3.5/7 for catalyst. These are mathematical expectations, not observed runs. The battery baselines themselves are below that expected choice count, despite being useful forecast controls. With related pairs and few records, none of these descriptive differences establishes statistical superiority.

[Condition-block results](block-results.md) accompany the pooled errors; catalyst blocks have substantially different current scales.

The [summary bar charts](../figures/README.md) average every completed attempt and show observed run ranges. They combine Opus hosting routes for a compact view; these detailed rows retain the separate routes. The [derived bar data](../results/model-bar-summary.json) provides all means, ranges and route counts.

## Completion and comparability

Two attempts were planned per configuration/task. Some repeats were stopped before grading to reserve the approved budget for wider model coverage; others reached provider, response or time limits. Gemini produced no scorable final answer within the limits. Standard Sol failed interface qualification; Sol Pro completed both tasks. These are execution outcomes, not zero scientific scores. The JSON retains every attempt status.

Opus's Anthropic and Google provider routes are shown separately. A dagger marks GLM 5.3 and DeepSeek V4 Pro: they omit API-level response_format and validate the same answer schema locally. DeepSeek routes use DeepInfra FP8; GLM uses Novita FP8. Exact model IDs, canonical versions, precision and route metadata are in the aggregate JSON. Same effort labels do not imply equal internal compute.

Limits were 600 seconds, 60 Python calls, 16 responses and 16,384 output tokens per response, with high reasoning and no web. A synthetic file-reading test preceded scientific work. Source and execution audits passed on all 30 completed attempts. No private measurements or per-record predictions are included here.

These small retrospective results do not support an unrestricted model leaderboard. Pairs share records, completions differ, and acquisition context is incomplete. The assessment preserves all successes and failures and separates numerical prediction, choices, probabilities and execution.
