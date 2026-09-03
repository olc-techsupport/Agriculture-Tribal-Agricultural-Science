from __future__ import annotations

"""Apply OLC-owned learning stubs and clean source notebook state."""

import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = {
    "01": ("distinguish statistical boundaries from jurisdiction; inspect regional land-context coverage", "Choose one mapped boundary and state what it represents and cannot support."),
    "02": ("interpret a regional drought proxy; inspect period, scale, and missingness", "Compare one drought observation with the evidence needed for a Pine Ridge-specific conclusion."),
    "03": ("interpret NDVI as a vegetation proxy; inspect quality, seasonality, and resolution", "Explain one way satellite greenness can disagree with pasture condition observed on the land."),
    "04": ("interpret county agricultural statistics as regional context; avoid Nation-specific inference", "Trace one statistic to county, year, unit, and suppression status before describing it."),
    "05": ("assess public groundwater monitoring coverage; distinguish evidence absence from condition evidence", "Select one site or gap and list what the public record cannot establish."),
    "06": ("explain an exploratory composite index; compare only matched periods and component availability", "Remove one component hypothetically and explain why unmatched scores should not be ranked."),
    "07": ("distinguish scenarios, projections, and forecasts; communicate model and spatial uncertainty", "Rewrite one projected change naming model, scenario, period, spatial support, and uncertainty."),
}


def cell(text: str) -> dict:
    lines = text.strip().splitlines()
    return {"cell_type": "markdown", "metadata": {}, "id": uuid.uuid4().hex[:8], "source": [line + "\n" for line in lines[:-1]] + [lines[-1]]}


def main() -> None:
    for path in sorted((ROOT/"notebooks").glob("[0-9][0-9]_*.ipynb")):
        number = path.name[:2]
        notebook = json.loads(path.read_text(encoding="utf-8"))
        cells = []
        for existing in notebook["cells"]:
            source = "".join(existing.get("source", []))
            if existing["cell_type"] == "markdown" and any(marker in source for marker in ("## Learning Objectives", "## Learner Checkpoint")):
                continue
            if existing["cell_type"] == "code":
                existing["execution_count"] = None
                existing["outputs"] = []
            source = source.replace("**Primary Focus:** Oglala Lakota (Pine Ridge), Sicangu Lakota (Rosebud)", "**Primary instructional focus:** Pine Ridge and Oglala Lakota")
            source = source.replace("**In Scope:** All South Dakota Tribal Nations", "**Regional context:** Public-data comparisons elsewhere in South Dakota; inclusion does not imply representation")
            source = source.replace("Primary focus (Pine Ridge, Rosebud)", "Primary instructional focus (Pine Ridge)")
            source = source.replace("Bold = Primary focus (Pine Ridge, Rosebud)", "Bold = Primary instructional focus (Pine Ridge)")
            if existing.get("source"):
                existing["source"] = source.splitlines(keepends=True)
            existing.setdefault("id", uuid.uuid4().hex[:8])
            cells.append(existing)
        outcomes, checkpoint = MODULES[number]
        objectives = "\n".join(f"- {item.strip()}" for item in outcomes.split(";"))
        cells.insert(1, cell(f"""
## Learning Objectives

By the end of this notebook, learners will be able to:

{objectives}

## Prerequisites and Timing

Allow 75-100 minutes. Activate the project environment, read `docs/data_governance.md`, and complete the preceding notebook where applicable. Work in pairs and rotate analyst, data-steward, skeptic, and documentarian roles.

## Governance Checkpoint

This public-data notebook is an educational analysis with Pine Ridge as the primary instructional focus. Other Nations and geographies are regional context only. Do not add operational records, sensitive locations, personal information, or community knowledge. Results are screening-level and not approved OLC/OST conclusions.
"""))
        cells.append(cell(f"""
## Learner Checkpoint

{checkpoint}

## Interpretation Protocol

Separate **observation** from the selected public data, **interpretation** as a plausible explanation, **additional evidence** needed, and **decision authority** over thresholds, release, or action. Do not convert a regional proxy, monitoring gap, association, configured flag, or scenario into a Nation-specific, causal, operational, or policy conclusion.

## Contribution Activity

Improve one label, unit, provenance note, limitation, citation, or reproducibility check. Review it with a partner and explain what became more defensible.

## Evidence Record and Next Step

Record one result, source, geography, period, transformation, limitation, and question requiring additional evidence or locally authorized expertise. Proceed to the next numbered notebook where applicable.
"""))
        notebook["cells"] = cells
        path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
