"""Smoke tests for the GPADS-OS documentation repository."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_repository import inspect_repository

class StructureTests(unittest.TestCase):
    def test_repository_contract(self):
        self.assertEqual([], inspect_repository())

    def test_seven_cells_and_unique_members(self):
        data = json.loads((ROOT / "scripts/expected_cells.json").read_text(encoding="utf-8"))
        self.assertEqual(7, len(data))
        self.assertEqual(37, sum(map(len, data.values())))
        self.assertEqual(26, len({person for members in data.values() for person in members}))

    def test_reports_are_not_fabricated(self):
        self.assertEqual([], [path for path in (ROOT / "cells").rglob("2026-*-Q*.md")])

    def test_models_present(self):
        for model in ("templates/relatorio-quinzenal.md", "templates/relatorio-consolidado.md", "templates/microentrega/template-microentrega.md"):
            self.assertTrue((ROOT / model).exists(), model)

if __name__ == "__main__":
    unittest.main()
