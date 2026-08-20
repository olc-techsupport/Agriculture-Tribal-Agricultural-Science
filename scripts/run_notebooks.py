from __future__ import annotations

"""Execute the public-data notebooks in dependency order."""

import argparse
import subprocess
import sys
from pathlib import Path

NOTEBOOKS = [
    "01_land_base_context.ipynb",
    "02_drought_climate_context.ipynb",
    "03_vegetation_condition_ndvi.ipynb",
    "04_usda_nass_agricultural_context.ipynb",
    "05_water_availability.ipynb",
    "06_system_stress_index.ipynb",
    "07_climate_projections_agriculture.ipynb",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, choices=range(1, 8), default=1)
    parser.add_argument("--end", type=int, choices=range(1, 8), default=7)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--allow-errors", action="store_true")
    parser.add_argument("--kernel", default="tribal-ag-sd")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    executed = root/"outputs"/"executed_notebooks"
    executed.mkdir(parents=True, exist_ok=True)
    for index, name in enumerate(NOTEBOOKS, start=1):
        if not args.start <= index <= args.end:
            continue
        source = root / "notebooks" / name
        destination = executed / name
        command = [
            sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
            str(source), "--output", str(destination), f"--ExecutePreprocessor.timeout={args.timeout}",
            f"--ExecutePreprocessor.allow_errors={str(args.allow_errors)}",
            f"--ExecutePreprocessor.kernel_name={args.kernel}",
        ]
        print(f"Executing {name}", flush=True)
        subprocess.run(command, cwd=root, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
