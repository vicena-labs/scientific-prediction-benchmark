"""Invented numerical controls only; this file contains no laboratory records."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from vicena_science_benchmark.cli import demo
from vicena_science_benchmark.core import baselines, grade, validate_inputs


class WorkflowTest(unittest.TestCase):
    def test_baselines_and_packet_exclude_adjacent_answer_key(self):
        packet = {"title": "Invented control", "question": "Software test only",
                  "candidates": {k: {"id": k, "block": "toy"} for k in ("a", "b")},
                  "pairs": [{"id": "p", "first": "a", "second": "b", "block": "toy"}],
                  "baseline_definitions": {}, "answer_format": {}}
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "task.json").write_text(json.dumps(packet))
            readings = root / "readings.csv"
            readings.write_text("candidate,acquisition_index,potential_V,current_A\n" + "".join(
                f"{candidate},{i},{x},{multiplier * (2*x-.3)/1000}\n"
                for candidate, multiplier in (("a", 1), ("b", 2))
                for i, x in enumerate((.55, .56, .57, .58, .59, .60))))
            (root / "reference.json").write_text('{"secret_control":true}')
            methods = baselines("catalyst", packet, readings)
            self.assertAlmostEqual(methods["linear_tail"]["predictions"]["a"], 1.3)
            self.assertAlmostEqual(methods["carry_forward"]["predictions"]["b"], 1.8)
            args = [sys.executable, "-m", "vicena_science_benchmark", "pack", "--family", "catalyst",
                    "--task", str(root / "task.json"), "--readings", str(readings), "--out", str(root / "packet.zip")]
            subprocess.run(args, check=True, capture_output=True)
            with zipfile.ZipFile(root / "packet.zip") as archive:
                self.assertEqual(set(archive.namelist()), {"task.json", "readings.csv"})
                self.assertEqual(archive.read("readings.csv"), readings.read_bytes())
            with readings.open("a") as file:
                file.write("b,6,0.8,0.004\n")
            with self.assertRaises(ValueError):
                validate_inputs("catalyst", packet, readings)

    def test_decision_is_separate_from_forecast_and_ties_are_excluded(self):
        reference = {"measured": {"a": 10., "b": 20.}, "blocks": {"toy": ["a", "b"]},
                     "pairs": [{"id": "p", "first": "a", "second": "b", "block": "toy"}]}
        answer = {"predictions": {"a": 11., "b": 19.}, "probability_first_wins": {"p": .8}}
        result = grade(answer, reference)
        self.assertEqual((result["correct_pairs"], result["mae"], result["mean_regret"]), (0, 1., 10.))
        self.assertAlmostEqual(result["brier"], .64)
        tied = copy.deepcopy(reference); tied["measured"]["b"] = 10.
        self.assertIsNone(grade(answer, tied)["pair_accuracy"])
        for invalid in (float("nan"), float("inf"), True, 1.1):
            bad = copy.deepcopy(answer); bad["probability_first_wins"]["p"] = invalid
            with self.assertRaises(ValueError):
                grade(bad, reference)

    def test_demo_is_explicitly_not_experimental_evidence(self):
        result = demo()
        self.assertIn("FABRICATED", result["notice"])
        self.assertEqual(result["model_calls"], 0)
        self.assertLess(result["scores"]["robust_trend"]["mae"], 1e-9)


if __name__ == "__main__":
    unittest.main()
