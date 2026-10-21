"""Intentional demo finding: predictable temporary filename."""
def temporary_path(user_id):
    return "/tmp/report_" + str(user_id) + ".tmp"
