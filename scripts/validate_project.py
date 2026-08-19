"""Validate repository structure and expected analysis products."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    "README.md", "environment.yaml", "config/config.yaml", "app/app.py",
    "scripts/run_pipeline.py", "scripts/run_notebooks.py", "docs/methodology.md",
    "docs/data_dictionary.md", "docs/field_guide.md",
]
EXPECTED_OUTPUTS = [
    "sd_tribal_land_base.csv", "sd_tribal_land_base.geojson",
    "sd_tribal_drought_statistics.csv", "sd_pdsi_monthly.csv",
    "sd_tribal_ndvi_annual.csv", "nass_tribal_ag_summary.csv",
    "groundwater_coverage_by_tribe.csv", "system_stress_index_annual.csv",
    "climate_projections_ensemble.csv",
]


def main() -> int:
    missing_structure = [p for p in REQUIRED_PATHS if not (ROOT / p).exists()]
    missing_outputs = [p for p in EXPECTED_OUTPUTS if not (ROOT / "outputs" / p).exists()]
    if missing_structure:
        print("Missing required project paths:", *missing_structure, sep="\n- ")
    if missing_outputs:
        print("Missing analysis outputs (rerun notebooks):", *missing_outputs, sep="\n- ")
    return 1 if missing_structure else 0


if __name__ == "__main__":
    raise SystemExit(main())
