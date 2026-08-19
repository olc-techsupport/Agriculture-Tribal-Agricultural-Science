"""Generate field-entry workbooks from canonical schemas."""
from pathlib import Path
import sys, pandas as pd
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from src.data.validation import SCHEMAS  # noqa: E402
def main() -> int:
    destination=ROOT/"data"/"templates"; destination.mkdir(parents=True, exist_ok=True)
    for name,schema in SCHEMAS.items():
        with pd.ExcelWriter(destination/f"{name}_template.xlsx", engine="openpyxl") as writer:
            pd.DataFrame(columns=schema.required).to_excel(writer, sheet_name="data", index=False)
            pd.DataFrame({"field":schema.required,"sensitive":[f in schema.sensitive for f in schema.required]}).to_excel(writer,sheet_name="schema",index=False)
    print(f"Created {len(SCHEMAS)} templates"); return 0
if __name__ == "__main__": raise SystemExit(main())
