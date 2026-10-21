"""Intentional demo finding: missing object-level authorization."""
REPORTS = {"101": {"owner": "alice", "report": "demo"}}
def get_report(report_id):
    # Deliberately does not verify that the requester owns the report.
    return REPORTS.get(report_id)
