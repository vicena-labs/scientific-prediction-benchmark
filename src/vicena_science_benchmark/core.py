"""Deterministic baselines and metrics; no network or laboratory data bundled."""

import csv
import json
import math
import statistics as st
from pathlib import Path


def baselines(family, packet, readings):
    series = validate_inputs(family, packet, readings)
    names = ("carry_forward", "robust_trend" if family == "battery" else "linear_tail")
    forecasts = {name: {} for name in names}
    for candidate, points in series.items():
        if family == "battery":
            reference = st.median(y for x, y in points if 3 <= x <= 10)
            if reference <= 0:
                raise ValueError("Battery normalization must be positive")
            forecasts[names[0]][candidate] = 100 * st.mean(y for x, y in points if 41 <= x <= 50) / reference
            tail = [(x, y) for x, y in points if 31 <= x <= 50]
            slopes = [(b[1] - a[1]) / (b[0] - a[0]) for i, a in enumerate(tail) for b in tail[i + 1:]]
            slope = st.median(slopes)
            intercept = st.median(y for _, y in tail) - slope * st.median(x for x, _ in tail)
            forecasts[names[1]][candidate] = 100 * (intercept + slope * 355.5) / reference
        else:
            forecasts[names[0]][candidate] = points[-1][1] * 1000
            xs, ys = zip(*[(x, y) for x, y in points if .550 <= x <= .600])
            slope, intercept = st.linear_regression(xs, ys)
            forecasts[names[1]][candidate] = 1000 * (intercept + slope * .800)
    return {name: {
        "predictions": values,
        "probability_first_wins": {
            p["id"]: 1.0 if values[p["first"]] > values[p["second"]] else
            0.0 if values[p["first"]] < values[p["second"]] else .5 for p in packet["pairs"]},
        "rationale": f"Deterministic {name} baseline; probabilities encode ordering, not calibrated confidence.",
        "limitations": "Extrapolation of recorded values; no mechanism or calibrated uncertainty."}
        for name, values in forecasts.items()}


def validate_inputs(family, packet, readings):
    if family not in ("battery", "catalyst"):
        raise ValueError("Unknown task family")
    if set(packet) != {"title", "question", "candidates", "pairs", "baseline_definitions", "answer_format"}:
        raise ValueError("Task must contain exactly the six documented fields; no answer key")
    candidates = packet["candidates"]
    if not isinstance(candidates, dict) or not candidates:
        raise ValueError("Nonempty candidates mapping required")
    fields = ({"id", "cohort", "conditions", "electrolyte", "recording_basis", "block"} if family == "battery"
              else {"id", "block", "material_label", "electrode_label", "rotation_rpm"})
    for key, value in candidates.items():
        if value.get("id") != key or not value.get("block") or set(value) - fields:
            raise ValueError("Candidate metadata has invalid ID, block or unexpected field")
    validate_pairs(packet["pairs"], {k: v["block"] for k, v in candidates.items()})
    columns = (["candidate", "cycle", "discharge_capacity_mAh"] if family == "battery" else
               ["candidate", "acquisition_index", "potential_V", "current_A"])
    series, seen, previous = {k: [] for k in candidates}, set(), {}
    with Path(readings).open(newline="") as file:
        rows = csv.DictReader(file)
        if rows.fieldnames != columns:
            raise ValueError("CSV columns must match the dictionary exactly")
        for row in rows:
            key = row["candidate"]
            if key not in series or None in row:
                raise ValueError("Unknown candidate or malformed CSV row")
            index = int(row["cycle" if family == "battery" else "acquisition_index"])
            if index < 0 or (key, index) in seen or index <= previous.get(key, -1):
                raise ValueError("Indices must be unique and increasing per candidate")
            seen.add((key, index))
            previous[key] = index
            x = index if family == "battery" else float(row["potential_V"])
            if not math.isfinite(x) or (family == "battery" and not 1 <= x <= 50) or (family == "catalyst" and x > .600):
                raise ValueError("Measurement exceeds the registered visible cutoff")
            raw = row["discharge_capacity_mAh" if family == "battery" else "current_A"]
            if raw == "" and family == "battery":
                continue
            y = float(raw)
            if not math.isfinite(y):
                raise ValueError("Measurements must be finite; do not impute missing values")
            if series[key] and x <= series[key][-1][0]:
                raise ValueError("This version requires an increasing cycle/potential prefix")
            series[key].append((x, y))
    if any(not points for points in series.values()):
        raise ValueError("Every candidate needs visible measurements")
    return series


def grade(answer, reference):
    expected, pairs, blocks = reference["measured"], reference["pairs"], reference["blocks"]
    reverse = {candidate: block for block, candidates in blocks.items() for candidate in candidates}
    if len(reverse) != sum(map(len, blocks.values())) or set(reverse) != set(expected):
        raise ValueError("Reference blocks must cover each candidate exactly once")
    validate_pairs(pairs, reverse)
    if not all(number(v) for v in expected.values()):
        raise ValueError("Reference endpoints must be finite")
    if not isinstance(answer, dict):
        raise ValueError("Answer must be an object")
    predictions, probabilities = answer.get("predictions"), answer.get("probability_first_wins")
    if not isinstance(predictions, dict) or set(predictions) != set(expected):
        raise ValueError("Predictions must cover exactly the candidate IDs")
    if not isinstance(probabilities, dict) or set(probabilities) != {p["id"] for p in pairs}:
        raise ValueError("Probabilities must cover exactly the pair IDs")
    if not all(number(v) for v in predictions.values()) or not all(number(v) and 0 <= v <= 1 for v in probabilities.values()):
        raise ValueError("Forecasts must be finite; probabilities must be in [0,1]")
    rows = []
    for pair in pairs:
        a, b = pair["first"], pair["second"]
        probability = probabilities[pair["id"]]
        gap = expected[a] - expected[b]
        tied = abs(gap) <= 1e-10
        choice = a if probability >= .5 else b
        rows.append({"block": pair["block"], "correct": None if tied else (choice == a) == (gap > 0),
                     "regret": max(expected[a], expected[b]) - expected[choice],
                     "brier": None if tied else (probability - float(gap > 0)) ** 2})
    scored = [r for r in rows if r["correct"] is not None]
    return {"status": "scored", "correct_pairs": sum(r["correct"] for r in scored),
            "scored_pairs": len(scored), "pair_accuracy": st.mean(r["correct"] for r in scored) if scored else None,
            "mae": st.mean(abs(predictions[k] - v) for k, v in expected.items()),
            "mean_regret": st.mean(r["regret"] for r in rows),
            "brier": st.mean(r["brier"] for r in scored) if scored else None,
            "blocks": {block: {
                "correct_pairs": sum(r["correct"] for r in scored if r["block"] == block),
                "scored_pairs": sum(r["block"] == block for r in scored),
                "mae": st.mean(abs(predictions[k] - expected[k]) for k in candidates)}
                for block, candidates in blocks.items()}}


def validate_pairs(pairs, blocks):
    seen = set()
    if not isinstance(pairs, list) or not pairs:
        raise ValueError("At least one pair required")
    for pair in pairs:
        if set(pair) != {"id", "first", "second", "block"} or pair["id"] in seen:
            raise ValueError("Pair schema or duplicate pair ID")
        if pair["first"] == pair["second"] or any(blocks.get(pair[k]) != pair["block"] for k in ("first", "second")):
            raise ValueError("Pairs must name distinct candidates in the same block")
        seen.add(pair["id"])


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def load(path):
    return json.loads(Path(path).read_text())
