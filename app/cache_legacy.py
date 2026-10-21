"""Remediated demo: use JSON for untrusted serialized data."""
import json
def load_cached_object(blob):
    return json.loads(blob)
