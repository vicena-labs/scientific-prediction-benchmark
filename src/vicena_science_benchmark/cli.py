"""Offline commands. Private case paths must be supplied explicitly."""

import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path

from .core import baselines, grade, load, validate_inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("demo", help="Mechanical control with fabricated numbers, not laboratory data")
    for name in ("validate", "baselines", "pack"):
        p = commands.add_parser(name)
        p.add_argument("--family", required=True, choices=("battery", "catalyst"))
        p.add_argument("--task", required=True, type=Path)
        p.add_argument("--readings", required=True, type=Path)
        if name == "pack":
            p.add_argument("--out", required=True, type=Path)
    p = commands.add_parser("grade", help="Evaluator only: keep the reference out of the model workspace")
    p.add_argument("--answer", required=True, type=Path)
    p.add_argument("--reference", required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.command == "demo":
            output = demo()
        elif args.command == "grade":
            output = grade(load(args.answer), load(args.reference))
        else:
            packet = load(args.task)
            series = validate_inputs(args.family, packet, args.readings)
            if args.command == "baselines":
                output = baselines(args.family, packet, args.readings)
            else:
                output = {"valid": True, "candidates": len(series), "visible_values": sum(map(len, series.values())),
                          "sha256": {"task.json": digest(args.task), "readings.csv": digest(args.readings)}}
                if args.command == "pack":
                    with zipfile.ZipFile(args.out, "x", zipfile.ZIP_DEFLATED) as archive:
                        archive.writestr("task.json", args.task.read_bytes())
                        archive.writestr("readings.csv", args.readings.read_bytes())
                    output["archive"] = str(args.out)
                    output["archive_sha256"] = digest(args.out)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, f"Invalid input: {error}\n")
    print(json.dumps(output, indent=2, allow_nan=False))


def demo():
    # Deliberately fabricated, perfectly linear control; no laboratory measurements.
    packet = {"title": "Arithmetic control, not a scientific case", "question": "Check software wiring only.",
              "candidates": {k: {"id": k, "block": "toy"} for k in ("toy-a", "toy-b")},
              "pairs": [{"id": "toy-pair", "first": "toy-a", "second": "toy-b", "block": "toy"}],
              "baseline_definitions": {}, "answer_format": {}}
    reference = {"measured": {"toy-a": 100., "toy-b": 80.}, "pairs": packet["pairs"],
                 "blocks": {"toy": ["toy-a", "toy-b"]}}
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "control.csv"
        path.write_text("candidate,cycle,discharge_capacity_mAh\n" + "".join(
            f"{key},{cycle},{100 - slope * (cycle - 6.5)}\n"
            for key, slope in (("toy-a", 0.), ("toy-b", 20 / 349)) for cycle in range(1, 51)))
        predictions = baselines("battery", packet, path)
    return {"notice": "FABRICATED SOFTWARE CONTROL: these are not experiments or model results.",
            "model_calls": 0, "network_calls": 0,
            "scores": {name: grade(answer, reference) for name, answer in predictions.items()}}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
