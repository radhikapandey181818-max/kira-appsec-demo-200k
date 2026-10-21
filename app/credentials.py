"""Remediated demo: load credentials from environment."""
import os
DEMO_API_KEY = os.environ.get("DEMO_API_KEY", "")
