from __future__ import annotations
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("[0-9][0-9]_*.ipynb"))
MARKERS = ("## Learning Objectives", "## Prerequisites and Timing", "## Governance Checkpoint", "## Learner Checkpoint", "## Interpretation Protocol", "## Contribution Activity")


def test_seven_ordered_scaffolded_notebooks() -> None:
    assert [p.name[:2] for p in NOTEBOOKS] == [f"{i:02d}" for i in range(1, 8)]
    for path in NOTEBOOKS:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        markdown = "\n".join("".join(c.get("source", [])) for c in notebook["cells"] if c["cell_type"] == "markdown")
        assert all(marker in markdown for marker in MARKERS)
        assert all(c.get("id") for c in notebook["cells"])


def test_notebooks_clean_and_code_parses() -> None:
    for path in NOTEBOOKS:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        code = []
        for c in notebook["cells"]:
            if c["cell_type"] == "code":
                assert c.get("outputs", []) == []
                assert c.get("execution_count") is None
                code.extend(line for line in "".join(c.get("source", [])).splitlines() if not line.lstrip().startswith(("%", "!")))
        ast.parse("\n".join(code), filename=path.name)


def test_project_role_and_curriculum_ownership() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    learning = (ROOT / "docs" / "learning_design.md").read_text(encoding="utf-8")
    assert "geospatial code, workflows, and documentation under contract" in readme
    assert "OLC will develop the full instructional materials" in learning
    assert "instructional materials under contract" not in readme
