"""Intentional demo finding: unsafe deserialization."""
import pickle
def load_cached_object(blob):
    # Never deserialize untrusted bytes with pickle.
    return pickle.loads(blob)
