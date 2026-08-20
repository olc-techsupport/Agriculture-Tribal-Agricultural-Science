from __future__ import annotations

"""Validate and process locally governed Tribal observational data."""

import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data.validation import SCHEMAS, load_and_validate  # noqa: E402
INPUTS = {name: f"{name}.csv" for name in SCHEMAS}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-partial", action="store_true")
    args = parser.parse_args()
    raw, processed, records, missing = ROOT/"data"/"raw", ROOT/"data"/"processed", [], []
    for name, filename in INPUTS.items():
        source = raw/filename
        if not source.exists():
            missing.append(filename); continue
        frame = load_and_validate(source, name)
        if "date" in frame: frame["date"] = pd.to_datetime(frame["date"], errors="raise").dt.date
        destination = processed/f"{name}.parquet"; destination.parent.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(destination, index=False)
        records.append({"dataset": name, "rows": len(frame), "output": destination.name,
                        "sensitive_fields": list(SCHEMAS[name].sensitive)})
    if missing and not args.allow_partial: raise FileNotFoundError("Missing required inputs: " + ", ".join(missing))
    manifest = {"generated_at_utc": datetime.now(timezone.utc).isoformat(),
                "governance_notice": "Tribal data; distribution requires documented Tribal authority.",
                "datasets": records, "missing": missing}
    processed.mkdir(parents=True, exist_ok=True)
    (processed/"manifest.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
    print(f"Processed {len(records)} dataset(s); missing {len(missing)}."); return 0
if __name__ == "__main__": raise SystemExit(main())
