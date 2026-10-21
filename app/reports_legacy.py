"""Remediated demo: require ownership verification."""
REPORTS = {"101": {"owner": "alice", "report": "demo"}}
def get_report(report_id, requester):
    report = REPORTS.get(report_id)
    if report is None or report["owner"] != requester:
        return None
    return report
