"""Remediated demo: use secure temporary-file APIs."""
import tempfile
def create_temporary_file():
    return tempfile.NamedTemporaryFile(prefix="report_", delete=False)
