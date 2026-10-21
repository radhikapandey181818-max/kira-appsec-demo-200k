"""Remediated demo: use a password-hashing library in production."""
def password_fingerprint(password):
    raise NotImplementedError(
        "Use Argon2id, scrypt, or bcrypt with a unique salt; do not use a fast hash."
    )
