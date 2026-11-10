# Battery: forecast later retention and choose a record

> [Benchmark](../README.md) · [Data dictionary](../docs/data-dictionary.md)

**Question:** Given the first 50 recorded cycles and nominal formulation/context, which of two traces will retain more recorded discharge capacity at cycles 351–360?

The model receives `task.json` and `readings.csv`. Each candidate represents an NCM622/graphite formulation-group trace. Nominal recipes contain incomplete or ambiguous entries; unreported ingredients are not zeros. Comparisons stay within the supplied condition blocks. The exact setpoint of one high-temperature block is unconfirmed.

For every candidate, forecast:

```text
retention_percent = 100 × mean(recorded capacities at cycles 351–360)
                        / median(recorded capacities at cycles 3–10)
```

For each registered pair, also return the probability that the first candidate has higher retention. The decision uses that probability, even if ordering the point forecasts would choose differently. Give a short rationale and describe uncertainty.

The evaluator retains later recorded capacities. The target includes all recorded values in its specified window, including abrupt excursions. It does not substitute a smoothed curve, lifetime, or an assumed physical degradation mechanism. Missing records are not manufactured.

The primary baseline carries forward the mean normalized capacity at cycles 41–50. The secondary baseline fits a Theil–Sen slope to cycles 31–50 with intercept `median(y) - slope × median(x)`, evaluates at cycle 355.5, then applies the same normalization.

The task probes whether early trends support a later numerical forecast, whether the model distinguishes a forecast from a decision under uncertainty, and whether it qualifies incomplete conditions. It does not establish causal additive effects or identify the best formulation outside the recorded alternatives. Ten related traces generate twelve comparisons in the pilot. More comparisons are not more independent specimens.
