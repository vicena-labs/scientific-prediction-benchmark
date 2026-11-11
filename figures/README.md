# Scientific prediction figures

> [Benchmark](../README.md) · [Assessment](../docs/assessment.md) · [All multi-model results](../docs/multi-model-results.md)

Five square figures, dated 10 November 2026, are supplied as a [PDF](Vicena_Scientific_Benchmark_Results.pdf), 2160 × 2160 PNGs and vector SVGs. They use only the [multi-model aggregate](../results/multi-model-summary.json) and [Astra follow-up summary](../results/astra-followups.json). No source records are included.

| Figure | PNG | SVG | Description |
| --- | --- | --- | --- |
| Forecasting and choice | [PNG](01-forecast-and-choice.png) | [SVG](01-forecast-and-choice.svg) | On the battery task, 15/16 completed attempts improve on carry-forward forecast error, while 3/16 exceed its 5/12 correct choices. Eleven also improve on robust-trend forecast error. |
| Battery by model | [PNG](02-battery-models.png) | [SVG](02-battery-models.svg) | Forecast error in retention percentage points and correct choices out of 12. Both baseline errors and every completed attempt are shown. |
| Catalyst by model | [PNG](03-catalyst-models.png) | [SVG](03-catalyst-models.svg) | Forecast error in milliamperes and choices out of 7. The target is a withheld point from the same scan. |
| More early data | [PNG](04-astra-more-data.png) | [SVG](04-astra-more-data.svg) | In separate subscription runs, Astra's error falls from 2.64 to 2.01 to 0.78 percentage points as the prefix grows from 50 to 100 to 150 cycles. Two baselines and the endpoint sensitivity are disclosed. |
| Revised cell selection | [PNG](05-astra-selection.png) | [SVG](05-astra-selection.svg) | Astra's initial assignment scores 1/6, the revised assignment 6/6, voltage regression 6/6 and formation scaling 2/6. These are attempts on three reused groups, not independent cases. |

## Reading the model plots

Each marker is a completed attempt: circles for the first, diamonds for the second. Connecting segments span those attempts and are not confidence intervals. The run column gives completed out of two planned attempts. Model rows are grouped rather than ranked; Opus provider routes remain separate. Dashed vertical lines mark robust trend for battery and linear tail for catalyst; dotted lines mark carry-forward. Both battery baselines choose 5/12. All axes begin at zero and the choice axis shows its full possible score.

GLM 5.3 and DeepSeek V4 Pro use a disclosed API-format adaptation, marked †. Exact model IDs, canonical versions, precision and provider metadata are in the aggregate JSON. Gemini 4 Carbon and standard Sol 6.1 produced no scored scientific answer and are omitted from the plotted nine-model roster; their statuses remain in the result table. Opus's Google route has no scored catalyst answer and is labelled accordingly. Failures to complete are never plotted as zero accuracy.

The [condition-block results](../docs/block-results.md) accompany the pooled model plots, especially because catalyst current scales differ across blocks.

The two subscription figures are separate studies, not additional repeats of the shared comparison. The revised cell-selection assignment changed prompt, methods and calibration validation together after outcomes were known to the evaluators. It does not isolate a causal intervention. For the cycling-prefix study, a median-window sensitivity changes forecast ordering at 150 cycles; the plot uses the specified mean-window target. No figure establishes a benefit from training, an independent test-set result or a general model ranking.
