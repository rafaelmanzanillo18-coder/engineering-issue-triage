import csv
import tempfile
import unittest
from pathlib import Path

from triage import classify, process


class TestTriage(unittest.TestCase):
    def test_critical(self):
        self.assertEqual(classify("Smoke detected"), "Critical")

    def test_high(self):
        self.assertEqual(classify("Communication lost"), "High")

    def test_overtemperature_high(self):
        self.assertEqual(classify("Overtemperature detected during simulated testing"), "High")

    def test_default_low(self):
        self.assertEqual(classify("Cosmetic label issue"), "Low")

    def test_csv_export(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.csv"
            output = Path(folder) / "output.csv"
            source.write_text("issue_id,description\n1,Timeout during monitoring\n", encoding="utf-8")
            self.assertEqual(process(str(source), str(output)), 1)
            with output.open(newline="", encoding="utf-8") as file:
                row = next(csv.DictReader(file))
            self.assertEqual(row["suggested_priority"], "Medium")
            self.assertEqual(row["review_status"], "Needs human review")

    def test_empty_description(self):
        self.assertEqual(classify(""), "Needs Information")
        self.assertEqual(classify("   "), "Needs Information")


if __name__ == "__main__":
    unittest.main()
