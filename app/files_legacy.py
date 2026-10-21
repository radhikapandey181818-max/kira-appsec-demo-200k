"""Remediated demo: constrain paths to the upload directory."""
from pathlib import Path
BASE = Path("uploads").resolve()
def read_document(filename):
    target = (BASE / filename).resolve()
    if target != BASE and BASE not in target.parents:
        raise ValueError("invalid filename")
    return target.read_text()
