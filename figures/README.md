# Battery and catalyst comparison charts

> [Benchmark](../README.md) · [Assessment](../docs/assessment.md) · [All individual results](../docs/multi-model-results.md)

The current [two-page square PDF](Vicena_Scientific_Benchmark_Results.pdf), revised 10 November 2026, contains these two charts. Each is also available as a 2160 × 2160 PNG and an editable SVG.

| Chart | PNG | SVG | Scientific question |
| --- | --- | --- | --- |
| Battery | [PNG](02-battery-models.png) | [SVG](02-battery-models.svg) | Given formulation context and cycles 1–50, predict retention at cycles 351–360 and choose the sample with higher retention in each pair. |
| Catalyst | [PNG](03-catalyst-models.png) | [SVG](03-catalyst-models.svg) | Given a scan through 0.600 V, predict signed current at 0.800 V and choose the higher value in each pair. |

## How to read the charts

- Left panel: mean absolute forecast error, in retention percentage points or milliamperes. Shorter bars are better.
- Right panel: mean correct pair choices out of 12 for battery or 7 for catalyst. Longer bars are better. A fractional mean such as 4.5 is the average across runs, not half of a scored comparison.
- Each bar averages all completed attempts for that model. Whiskers span the observed minimum and maximum, not confidence intervals or standard errors. Printed values are means. With one completed run there is no spread estimate; repeated identical scores have zero observed range.
- Models are grouped by supplier, with supplier logos and corresponding colours. The run column gives the number of completed attempts. This is not a sorted leaderboard.
- Each chart has one baseline row. Battery uses robust trend: 3.313 percentage points of error and 5/12 choices. Catalyst uses linear tail: 15.454 mA and 5/7 choices. Original carry-forward scores remain in the complete results.

The bar data are available in [model-bar-summary.json](../results/model-bar-summary.json), derived from [the unchanged individual-attempt aggregate](../results/multi-model-summary.json). No measurements or per-record model outputs are included.

## Combined Opus and comparison limits

The owner requested one Opus row. Battery combines two Anthropic-route runs and one Google-route run with equal weight per completed attempt: mean error 2.431 percentage points, range 2.223–2.621; mean choice count 5/12, range 3–6. Catalyst has two completed Anthropic-route runs and no scored Google-route answer: mean error 6.038 mA, range 3.256–8.820; mean choice count 5.5/7, range 5–6. The detailed tables keep the routes separate. Pooling is descriptive and does not make provider configurations equivalent.

The † marks the disclosed API-format adaptation for GLM 5.3 and DeepSeek V4 Pro. Exact IDs, precision, route metadata and incomplete statuses remain in the underlying result records. Gemini 4 Carbon and standard Sol 6.1 produced no scored scientific answer; they are not drawn as zero accuracy. Unequal run counts and related case comparisons prevent a general model ranking. [Condition-block results](../docs/block-results.md) accompany pooled errors, especially because catalyst current scales differ across blocks.

## Earlier figures

The [forecast-versus-choice overview](01-forecast-and-choice.png), [Astra cycling-prefix follow-up](04-astra-more-data.png) and [Astra cell-selection follow-up](05-astra-selection.png) remain available as earlier figures. The original five-page PDF is preserved at [revision ad67e15](https://github.com/vicena-labs/scientific-prediction-benchmark/blob/ad67e15771ceb694997a29c652d7aee80dec3913/figures/Vicena_Scientific_Benchmark_Results.pdf). The two subscription follow-ups are separate studies and are not pooled into the current comparison.
