"""Write checksums and revision metadata for currently available public artifacts."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.data.provenance import write_manifest  # noqa: E402
def main() -> int:
    outputs=[p for p in (ROOT/"outputs").rglob("*") if p.is_file() and p.name != "manifest.json"]
    inputs=[p for p in (ROOT/"data"/"cache").rglob("*") if p.is_file()]
    path=write_manifest(ROOT,outputs,inputs,notes="Availability manifest; presence does not imply scientific validation or release approval.")
    print(path); return 0
if __name__ == "__main__": raise SystemExit(main())
