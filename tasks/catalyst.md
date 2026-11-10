# Catalyst: extrapolate a partial scan and choose a record

> [Benchmark](../README.md) · [Data dictionary](../docs/data-dictionary.md)

**Question:** Given the beginning of an oxygen-evolution current–potential scan, which of two recordings will have higher signed current later in the scan?

The model sees each recording only through a recorded potential of 0.600 V. It predicts signed current in milliamperes at 0.800 V and the probability that the first candidate in each pair has the higher current. The evaluator obtains the target by linear interpolation between the two measured points bracketing 0.800 V. Interpolation defines a numerical endpoint from acquired measurements; it is not an AI-generated experimental observation.

The records are FeNC-labelled scans grouped by electrode/folder labels. Glassy carbon (GC) and nickel-foam blocks (NF-DC and NF-IMP) are scored separately as well as in the task total. DC and IMP are retained source labels, not independently validated preparation protocols. Acquisition points are not separate experimental cases, and scan labels do not establish independent specimens.

The primary baseline fits ordinary least squares current versus potential over 0.550–0.600 V and extrapolates to 0.800 V. The secondary baseline carries forward the last visible current. Convert amperes to milliamperes by multiplying by 1000; retain the recorded sign and do not clip predictions.

This task probes nonlinear extrapolation, changing rankings and uncertainty when only a partial response is visible. It does not measure intrinsic catalytic activity, overpotential versus a confirmed reference electrode, or synthesis-recipe quality. Electrode loading and area, electrolyte, potential reference and scan rate are unconfirmed. Rotation metadata is incomplete. The hidden endpoint is part of the same scan, not an independent characterization assay.

The pilot contains eight distinct sweeps and seven within-block comparisons. Pooled absolute error is dominated by the higher-current blocks, so results must also show block-level errors.
