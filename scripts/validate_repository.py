#!/usr/bin/env python3
"""Validate the documented GPADS-OS v0.3 tree using Python stdlib."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = json.loads((ROOT / "scripts/expected_cells.json").read_text(encoding="utf-8"))
ESSENTIAL = [
    "README.md", "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE",
    "docs/08-decisoes/fontes-e-rastreabilidade.md",
    "docs/04-gestao-de-produtos/hierarquia-de-trabalho.md",
    "docs/05-processos-operacionais/relatorios-quinzenais.md",
    "standards/definition-of-done/dod-geral.md",
    "templates/relatorio-quinzenal.md",
    "templates/relatorio-consolidado.md",
    "products/_template-produto/README.md",
    "platform/integrations/base44.md",
]

def inspect_repository(root=ROOT):
    errors = []
    for relative in ESSENTIAL:
        if not (root / relative).is_file():
            errors.append("Arquivo essencial ausente: " + relative)
    for cell, members in EXPECTED.items():
        base = root / "cells" / cell
        for doc in ("README.md", "integrantes.md", "relatorios/consolidado-quinzenal/2026/README.md"):
            if not (base / doc).is_file():
                errors.append("Documento de célula ausente: " + str(base / doc))
        for person in members:
            for doc in ("README.md", "relatorios-quinzenais/2026/README.md"):
                if not (base / "membros" / person / doc).is_file():
                    errors.append("Arquivo de vínculo ausente: " + f"{cell}/{person}/{doc}")
    number = sum(map(len, EXPECTED.values()))
    if number != 37:
        errors.append(f"Esperados 37 vínculos, obtidos {number}")
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if not text.lstrip().startswith("# "):
            errors.append("Markdown sem título de nível 1: " + str(path.relative_to(root)))
        if not text.strip():
            errors.append("Markdown vazio: " + str(path.relative_to(root)))
        # Reject accidentally generated historic individual reports.
        if "relatorios-quinzenais" in path.parts and re.fullmatch(r"20\d{2}-\d{2}-Q[12]\.md", path.name):
            errors.append("Relatório individual supostamente real criado sem fonte: " + str(path.relative_to(root)))
    return errors

if __name__ == "__main__":
    errors = inspect_repository()
    if errors:
        print("FALHA: " + str(len(errors)) + " problema(s)")
        for error in errors:
            print("-", error)
        sys.exit(1)
    count = len(list(ROOT.rglob("*.md")))
    print(f"OK: {len(EXPECTED)} células, 37 vínculos, {count} arquivos Markdown, templates e estrutura essenciais.")
