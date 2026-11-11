# Assessment of the current benchmark

> [Benchmark](../README.md) · [Multi-model results](multi-model-results.md) · [Earlier runs](results.md)

Updated 10 November 2026. We have an audited development benchmark on real laboratory records, a completed multi-model extrapolation comparison, and focused Astra follow-ups. The evidence is sufficient to describe the observed tasks, scores and model behavior. It is not sufficient for a general scientific-model leaderboard, a claim of unavoidable model incapability, or a claim that training on these data improves performance.

## What the evidence shows

The shared OpenRouter comparison contains 30 completed scientific attempts across nine distinct models: 16 battery attempts and 14 catalyst attempts. Each task uses the same allowed inputs and hidden measured endpoint across models. Provider routes and format adaptations are disclosed, and incomplete attempts remain unscored. Repetitions are unequal; pairs share records.

For battery forecasts, 15 of 16 completed attempts had lower error than the primary carry-forward baseline. Only three had more correct pair choices than its 5/12. Eleven had lower forecast error than the stronger robust-trend baseline, which also scored 5/12. For catalyst forecasts, all 14 completed attempts had lower error than the primary linear-tail baseline; only one exceeded its 5/7 choices. These counts describe completed attempts, not independent experiments or model-wide success rates.

Astra's battery choices were 6/12 and 4/12 in this common harness, averaging the baseline's 5/12. Its numerical error was lower. The older Vicena notebook result of 3/12 remains historical evidence, but it is no longer an adequate standalone headline for all Astra results. The two Opus provider routes are separate configurations; a single favorable run is not used to select a winning model.

## Which questions are scientifically useful?

| Track | Scientific use | Present evidence |
| --- | --- | --- |
| Early cycling to later recorded capacity | Forecast a specified later response and prioritize candidates | Real hidden outcomes on the same traces. Missing context, abrupt excursions and small differences limit physical interpretation. This is not remaining useful life. |
| Partial catalyst scan to a withheld potential | Estimate response continuation and compare recordings | A measured within-scan target. It does not establish prediction from synthesis, intrinsic activity or new-catalyst discovery. |
| Early cell measurements to grading priority | Prioritize which cell to test using labelled calibration examples | Same-cell worksheet links and hidden targets. Astra's revised method-assisted assignment succeeded in 6/6 attempts, matching voltage regression. |
| Interpret measured formulation performance | Select for the correct objective and avoid a misleading proxy | Exact numerical references. Astra passed both sessions; retain these as competence controls. |
| Formulation properties to hidden rate performance | Screen candidates before measuring their cell performance | Useful goal, but only one uncalibrated five-dose series. Astra and the conductivity policy missed both winners with low-confidence predictions. Recoverability from these inputs is unproven. |
| Propose the next experiment | Distinguish competing explanations before spending laboratory effort | Plausible proposals under assistant review. Independent scientist adjudication and actual follow-up outcomes remain outstanding. |

## Why a wrong choice is not automatically a reasoning failure

A model can reduce forecast error while preserving an incorrect order. Several battery differences are small, and near-50/50 probabilities can cross the choice threshold between repeats. All completed models and both battery baselines missed one later ordering reversal at 45 degrees C; that shared miss does not establish that the early prefix uniquely determines the later result.

The formulation prediction lacked labelled calibration and important experimental context. Astra explicitly acknowledged that the input did not identify a unique winner. By contrast, the grading task supplied calibration outcomes, and a voltage predictor available from those inputs recovered all three choices. After the prompt, candidate methods and validation objective changed together, Astra's score improved from 1/6 to 6/6 on the same records. That is a method-assisted development result, not a controlled attribution to one prompt change or a training intervention.

Scientific relevance, replayable scoring and information sufficiency are separate requirements. A useful screening question can still be underdetermined. A reliable baseline or qualified scientist succeeding on the same permitted evidence across independent cases would strengthen the case for an avoidable model weakness. Successes belong in the assessment alongside misses.

## What is ready to share

Task definitions, aggregate results, original result history, model/provider coverage, scoring rules, the data dictionary and figures can be shared without releasing laboratory records. Maintainer audits replayed saved answers, model identities, request-history continuity, source extraction and baseline calculations. The repository's software demo and offline scorer can be run without model calls. Reproducing experimental scores still requires authorized access to the private case bundle.

The figures show individual completed attempts rather than confidence intervals or best-of-two results. They identify the baseline and metric, keep provider configurations distinct, and label related records and unequal repetitions. Execution failures are not plotted as zero scientific accuracy.

## What the next benchmark version needs

1. Laboratory confirmation of specimen/batch links, units, acquisition conditions, stage timing and the meaning of unusual readings.
2. Independent calibration and held-out specimens or batches, with all modalities and repeats for one specimen kept together.
3. A practical effect or equivalence threshold established before examining new test outcomes.
4. Balanced, fixed model configurations and repetitions, with execution success, forecast error, choice regret and probability quality reported separately.
5. Blinded domain review for experimental-design questions. A proposed experiment is not a measured answer key.

These are proposed next steps, not completed features or authorized new model spending. No new inference was used for this assessment. The central supported result is that improved forecasts did not reliably produce better experimental choices on these records. A benefit from training on Vicena data remains an empirical question for a separate intervention and independent test.
