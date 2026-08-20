from __future__ import annotations

"""Schema and output validation for public and Tribal data workflows."""

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import pandas as pd


@dataclass(frozen=True)
class Schema:
    required: tuple[str, ...]
    sensitive: tuple[str, ...] = ()


SCHEMAS = {
    "pasture_conditions": Schema(("pasture_id", "date", "condition_score", "notes")),
    "grazing_log": Schema(("pasture_id", "date", "animal_count", "days_grazed", "pasture_area_acres")),
    "groundwater": Schema(("well_id", "date", "water_level_ft", "lat", "lon"), ("lat", "lon")),
    "animal_condition": Schema(("herd_id", "date", "condition_score", "notes")),
    "pasture_water_link": Schema(("pasture_id", "well_id"), ("well_id",)),
}


def validate_columns(frame: pd.DataFrame, schema_name: str) -> None:
    schema = SCHEMAS[schema_name]
    missing = sorted(set(schema.required) - set(frame.columns))
    if missing:
        raise ValueError(f"{schema_name}: missing required columns: {', '.join(missing)}")


def validate_ranges(frame: pd.DataFrame, schema_name: str) -> None:
    if schema_name == "pasture_conditions" and not frame["condition_score"].between(1, 5).all():
        raise ValueError("pasture condition_score must be between 1 and 5")
    if schema_name == "animal_condition" and not frame["condition_score"].between(1, 9).all():
        raise ValueError("animal condition_score must be between 1 and 9")
    if schema_name == "grazing_log":
        for column in ("animal_count", "days_grazed", "pasture_area_acres"):
            if (frame[column] < 0).any():
                raise ValueError(f"{column} cannot be negative")
    if schema_name == "groundwater":
        if not frame["lat"].between(-90, 90).all() or not frame["lon"].between(-180, 180).all():
            raise ValueError("groundwater coordinates are outside valid latitude/longitude ranges")


def load_and_validate(path: Path, schema_name: str) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required input not found: {path}")
    frame = pd.read_csv(path)
    validate_columns(frame, schema_name)
    validate_ranges(frame, schema_name)
    return frame


def require_outputs(directory: Path, names: Iterable[str]) -> None:
    missing = [name for name in names if not (directory / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required upstream outputs: " + ", ".join(missing))
