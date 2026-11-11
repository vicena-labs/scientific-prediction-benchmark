# Astra follow-up tasks

> [Benchmark](../README.md) · [Assessment](../docs/assessment.md) · [Aggregate results](../results/astra-followups.json)

These separate subscription studies use `gpt-6-astra` at `xhigh` reasoning, fresh sessions and isolated Python. They are not pooled with the common OpenRouter comparison. The public CLI currently implements the original battery/catalyst paired tasks; these follow-ups are documented study specifications, not additional supported CLI task types. Private data and run implementations are not included.

## Additional early cycling measurements

Repeat the fixed later-window forecast with prefixes through cycles 50, 100 and 150 on the same ten traces. Compare against carry-forward and robust trend at each cutoff. Astra's mean errors were 2.64, 2.01 and 0.78 percentage points. The target is the specified later mean-window percentage, including recorded excursions. A post-hoc median-window sensitivity changes the forecast ordering at 150 cycles. Cutoffs are nested views, not additional specimens.

## Cell grading priority

Give pre-grading measurements for eight identified cells in three formulation groups. For each group, expose the other groups' later capacities as calibration and hide that group's outcomes. Choose the cell likely to have the lowest recorded 0.5C grading capacity. Score choice correctness and regret separately from capacity forecast error.

The initial task produced 1/6 correct Astra choices. A revised task made selection primary, added voltage regression and required calibration validation against the selection objective. It produced 6/6 correct choices, matching voltage regression and exceeding formation scaling at 2/6. The prompt, methods and validation changed together after outcome-aware development; no single causal effect is isolated. No unused complete cells for independent confirmation were found in the reviewed archive.

## Formulation interpretation and prediction

In the interpretation condition, provide nominal formulation properties and measured rate results; ask for the leaders under conductivity, absolute 2C capacity and mean within-specimen 2C/0.1C retention. Both Astra sessions passed all numerical checks. Proposed next experiments were plausible under assistant review, with no measured outcomes or independent expert adjudication.

In the prediction condition, provide recipe context, conductivity, water content and acidity, withholding all rate results, low-rate capacities and derived statistics. Ask for the best candidate and probabilities for retention and absolute capacity. Both sessions matched the highest-conductivity policy and scored 0/2 for each objective. Retaining the control succeeded for retention and failed for absolute capacity. The models expressed near-uniform confidence. One reused series with no labelled calibration does not establish that the correct winners were inferable.

The task changes test interpretation, forecasting and planning separately. They do not demonstrate a general inability to reason about formulations or a benefit from fine-tuning.
