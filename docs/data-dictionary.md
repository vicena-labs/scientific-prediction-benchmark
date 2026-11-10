# Data dictionary

> [Benchmark](../README.md) · [Workflow](reproduce.md) · [Protocol](protocol.md)

Looking for the wider collection? The [all-samples data dictionary](sample-data-dictionary.md) covers experimental records, images, process recordings and specifications across materials, electrochemistry, biology and water studies. This page defines only the benchmark's battery/catalyst input and scoring schema.

Version 0.1, 10 November 2026. This describes the private evaluation interface; no source records or populated experimental examples are published here. Original acquisitions stay unchanged. Exported CSVs contain selected recorded values with aliases and explicit unit handling. Selection, aliasing and endpoint calculation are evaluation transformations, not claims that the exports are original native instrument files.

## File boundaries

| File | Reader | Purpose |
| --- | --- | --- |
| `task.json` | Tested model and evaluator | Question, candidate metadata, registered comparisons, baseline definitions and answer schema |
| `readings.csv` | Tested model and evaluator | Only measurements allowed before the cutoff |
| `answer.json` | Evaluator after submission | Model forecasts, pair probabilities, rationale and limitations |
| `reference.json` | Evaluator only | Measured target per candidate and the fixed pair/block mappings |
| Run manifest | Evaluator | Input/prompt hashes, requested and returned model IDs when exposed, settings, timestamps, completion and audit status |

The `pack` command includes only the two model input files. A file-format check cannot detect an answer concealed in prose or enforce model isolation; the evaluator must review the packet and keep the key in a separate inaccessible workspace.

## Battery measurements: `readings.csv`

| Column | Type | Unit | Meaning and checks |
| --- | --- | --- | --- |
| `candidate` | string | none | Opaque trace ID joining to `task.json`; no laboratory identity implied |
| `cycle` | integer | cycle number | Recorded cycle; model-visible range is 1–50, unique and increasing per candidate |
| `discharge_capacity_mAh` | number or empty | mAh | Recorded discharge capacity; empty means unavailable, not zero |

Absent cycles stay absent. Baselines use the available records in each specified window and fail when required windows cannot be computed. Capacity normalization uses the candidate's median recorded capacity at cycles 3–10. Report forecast error in **retention percentage points**, not percent relative error or mAh.

## Catalyst measurements: `readings.csv`

| Column | Type | Unit | Meaning and checks |
| --- | --- | --- | --- |
| `candidate` | string | none | Opaque recording ID joining to `task.json` |
| `acquisition_index` | integer | acquisition order | Original sample-order index; unique and increasing within the supplied prefix |
| `potential_V` | number | recorded V | Instrument potential axis; this version includes values ≤0.600 V and requires an increasing sweep |
| `current_A` | number | A | Signed recorded current; multiply by 1000 for the mA target |

Do not assume the potential is versus RHE or infer current density without confirmed reference and electrode area. The private endpoint uses the measured bracketing points at 0.800 V. Nonfinite values and unsupported sweep shapes are rejected; the tooling does not clean them into valid cases.

## Common `task.json` fields

| Field | Type | Meaning |
| --- | --- | --- |
| `title` | string | Human-readable task name |
| `question` | string | Exact scientific question, endpoint and evidence limits |
| `candidates` | object keyed by ID | Metadata for every visible candidate |
| `pairs` | array of objects | Registered within-block comparisons |
| `baseline_definitions` | object of strings | Mathematical definitions supplied to every model |
| `answer_format` | object | JSON Schema for the required answer, with exact candidate and pair IDs |

Each pair contains `id`, `block`, `first` and `second`. IDs are strings. `first` and `second` must identify distinct candidates in the named block. Pair order is frozen before model execution; a probability of exactly 0.5 selects `first` under this version's tie policy.

### Battery candidate metadata

| Field | Type/unit | Meaning |
| --- | --- | --- |
| `id` | string | Must match the candidates mapping key |
| `block` | string | Condition group; comparisons remain within it |
| `cohort` | string | Collection grouping, not proof of independence |
| `conditions.cell_chemistry` | string | Recorded cell chemistry |
| `conditions.temperature_c` | number, °C | Setpoint when documented |
| `conditions.temperature` | string | Qualitative temperature description when a numeric setpoint is unconfirmed |
| `conditions.voltage_limits_v` | two numbers, V | Documented lower and upper voltage limits |
| `conditions.charge_C`, `conditions.discharge_C` | number, C-rate | Recorded protocol rates; not current in amperes |
| `conditions.charge_C_planned`, `conditions.discharge_C_planned` | number, C-rate | Planned rates; do not silently treat them as confirmed acquisition settings |
| `electrolyte` | ingredient-to-number-or-null mapping | Nominal formulation entries; units depend on `recording_basis` |
| `recording_basis` | string | Meaning of recipe units, source inconsistencies and unknowns |

Optional condition fields are omitted when not supplied. Recipe nulls mean unreported. Some entries are solvent fractions, others nominal percentages or quantities under mixed headings. They must not all be interpreted as mass fractions, normalized to 100%, or treated as a complete formulation. No recipe values are included in this repository.

### Catalyst candidate metadata

| Field | Type/unit | Meaning |
| --- | --- | --- |
| `id` | string | Must match the candidates mapping key |
| `block` | string | Electrode/folder comparison block |
| `material_label` | string | Supplied material label, not structural ground truth |
| `electrode_label` | string | Supplied GC or NF subgroup label |
| `rotation_rpm` | number or null, RPM | Recorded rotation where supplied; null means unknown |

## Submitted answer

| Field | Type | Meaning |
| --- | --- | --- |
| `predictions` | ID-to-number mapping | One finite endpoint forecast per candidate, in retention percent or mA |
| `probability_first_wins` | pair-ID-to-number mapping | Probability in [0,1] that the first candidate has higher signed target |
| `rationale` | string | Brief account of the method and decision |
| `limitations` | string | Missing context, uncertainty assumptions and interpretation limits |

The choice is scored from the probability, not silently reconstructed from the point forecast. All registered IDs must be present, with no extras. Forecasts are model outputs, never measured labels. The numerical grader scores the first two fields; rationale and limitations require separate review.

## Evaluator-only reference and metrics

`reference.json` contains `measured` (candidate-to-target mapping), `pairs` (the same registered comparisons) and `blocks` (block-to-candidate-list mapping). Each candidate belongs to exactly one block. Laboratory provenance is retained privately outside the model inputs.

The grader emits aggregate `correct_pairs`, `scored_pairs`, `pair_accuracy`, `mae`, `mean_regret`, `brier`, and per-block choice counts and `mae`. Regret is the better endpoint minus the selected endpoint, in the task's units. Brier score averages squared probability error; constant 0.5 gives 0.25 for nontied pairs. Targets within absolute 1e-10 are treated as tied and excluded from choice accuracy and Brier score. Related pairs must not be treated as independent trials.
