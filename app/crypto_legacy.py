"""Intentional demo finding: weak hash for password-like values."""
import hashlib
def password_fingerprint(password):
    return hashlib.md5(password.encode()).hexdigest()
