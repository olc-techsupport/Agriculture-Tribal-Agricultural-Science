"""Small, local provenance manifests for generated artifacts."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_revision(repo_root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() or "unknown"


def write_manifest(repo_root: Path, outputs: list[Path], inputs: list[Path], *, notes: str = "") -> Path:
    existing_outputs = [path for path in outputs if path.exists()]
    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_revision": git_revision(repo_root),
        "notes": notes,
        "inputs": [{"path": str(p.relative_to(repo_root)), "sha256": sha256(p)} for p in inputs if p.exists()],
        "outputs": [{"path": str(p.relative_to(repo_root)), "sha256": sha256(p)} for p in existing_outputs],
    }
    destination = repo_root / "outputs" / "manifest.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return destination
