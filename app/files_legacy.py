"""Intentional demo finding: path traversal pattern."""
from pathlib import Path
def read_document(filename):
    # Deliberately missing base-directory containment validation.
    return Path("uploads/" + filename).read_text()
