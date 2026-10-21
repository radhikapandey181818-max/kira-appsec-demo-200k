"""Intentional demo finding: command injection pattern. Never run with real input."""
import os
def check_host(host):
    # Deliberately unsafe training example; not called by the application.
    return os.popen("ping -c 1 " + host).read()
