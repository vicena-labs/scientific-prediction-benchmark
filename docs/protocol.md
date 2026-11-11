# Evaluation protocol

> [Benchmark](../README.md) · [Task dictionary](data-dictionary.md) · [Run workflow](reproduce.md)

Version 0.1 describes the existing paired-outcome pilot. Scientific cutoffs, targets, pair assignments, units, baselines and grading stay fixed when changing the application workflow. A change to evidence, labels or scoring requires a new version; a new prompt or harness requires a separate run record.

## Evidence and execution

1. An evaluator verifies specimen/record linkage and independently computes each target from measured observations. Resolve interpretation before scoring; do not turn an unconfirmed mechanistic guess into a label.
2. Freeze the exact question, candidate and pair IDs, allowed measurements, baseline definitions, answer schema, model IDs, effort, tool access, repetition count and limits. Hash input files and prompts before inference.
3. Give each model the same allowed packet. Keep outcomes, earlier answers and evaluator files outside the model's accessible workspace. No web search, unrelated evidence or cross-session retrieval is permitted. A prompt restriction alone is not a security boundary.
4. Use a fresh session and analysis workspace per attempt. For the native Vicena profile, allow its required notebook tool under a fresh `/root` task folder. Read-only installed guidance is permitted; prior notebook contents and saved memory are not evidence. High effort, Fast off, one attempt per task, five-minute monitored stop, no credit purchases.
5. Save the final answer, full recorded tool actions, model/settings evidence and completion state before opening the key for grading. Report access failures, timeouts and excluded attempts separately from scientific scores. Do not recover a missing final answer from intermediate calculations.
6. Replay the baseline calculations and score the submitted answer independently. Publish all registered attempts; do not select the most dramatic failure or strongest success.

The earlier isolated local profile used a ten-minute limit and an OS-restricted Python tool. Its results are kept separate from Vicena's native notebooks. Provider interfaces, reasoning budgets and automatic account context may differ; the current app pilot is a model-plus-application evaluation.

## Shared OpenRouter comparison, 10 November

The later comparison preserves the original task packets, measured endpoints, pair assignments and scorer. It uses an isolated Python workspace with no web, high reasoning, a 600-second attempt limit, 60 Python calls, 16 responses and at most 16,384 output tokens per response. Two attempts were planned per model/provider configuration and task. All completed attempts and every incomplete status are retained; completions are unequal. The [result table](multi-model-results.md) and [aggregate metadata](../results/multi-model-summary.json) identify exact models, provider routes, execution outcomes and API-format adaptations.

A synthetic file-reading qualification preceded scientific calls. GLM 5.3 and DeepSeek V4 Pro use prompt-specified JSON with local validation because their route does not accept the same API response-format control. The scientific schema is unchanged. Opus's Anthropic and Google routes remain separate configurations. Equal effort labels and time limits do not establish equal internal compute. Saved request prefixes, input hashes, tool isolation and scoring were audited offline; no new inference was used for this release.

The [Astra follow-ups](../tasks/followups.md) are separate subscription studies with their own prompts, targets and controls. They must not be averaged into this comparison. The public CLI implements the original battery and catalyst tasks, not the follow-up runners.

## Scores

The primary score is pairwise selection accuracy **separately for each task**. Probability ≥0.5 selects the first candidate. Equal measured endpoints within absolute 1e-10 are excluded from accuracy and Brier calculations. Secondary metrics are endpoint mean absolute error, decision regret and Brier score. Report each electrode/condition block as well as the task total.

The endpoint value and the probability of winning are different statistical quantities. A good point forecast can still choose the wrong record. Deterministic baseline probabilities are 0/1 encodings of their order, not calibrated confidence; compare model Brier scores with the 0.25 constant-probability control, rather than claiming baseline confidence calibration.

Do not combine battery percentage points and catalyst milliamperes into one score. Catalyst pooled error reflects different current scales and must be accompanied by per-block results. Pair combinations and repeated model attempts are correlated; do not calculate a binomial confidence interval that treats them as independent experimental cases.

## Interpretation and next version

This is retrospective development evidence on previously inspected records. The held-out numbers were hidden from each tested attempt, but the data is not a pristine, newly collected benchmark. Outcomes are recorded experimental measurements; the task questions, aliases and grading are authored evaluation materials. The public demo is fabricated software test data and is never scored as laboratory evidence.

The present tasks test outcome extrapolation and choice. They do not validate autonomous experimental design, causal discovery, formulation optimization, safety of a laboratory procedure, or a benefit from training on these records. A stronger study needs independently held-out batches/specimens and confirmed acquisition context. Additional model runs should be preregistered, with the same packets and controls for every selected model.

Private laboratory records remain private. Public reports may include aggregate metrics and protocol metadata, but no per-record predictions, endpoints, recipes, original filenames, institutions or data-bearing transcripts without a separate release decision.
