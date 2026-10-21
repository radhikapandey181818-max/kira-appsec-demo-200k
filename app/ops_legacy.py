"""Remediated demo: avoid shell interpretation."""
import subprocess
def check_host(host):
    # In real code, validate host against an allowlist before use.
    return subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True, text=True, check=False, timeout=5
    ).stdout
