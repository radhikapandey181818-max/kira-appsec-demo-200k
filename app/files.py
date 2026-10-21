"""File handling examples for the synthetic demo."""
from pathlib import Path

UPLOAD_ROOT = Path("uploads").resolve()

def resolve_upload(filename: str) -> Path:
    """Resolve a filename and reject paths outside the upload directory."""
    target = (UPLOAD_ROOT / filename).resolve()
    if target != UPLOAD_ROOT and UPLOAD_ROOT not in target.parents:
        raise ValueError("invalid filename")
    return target
