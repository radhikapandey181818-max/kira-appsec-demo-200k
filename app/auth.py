"""Authentication helpers for the synthetic demo."""
import hashlib
import hmac
import os

def verify_demo_token(token: str, expected: str) -> bool:
    """Compare a supplied demo token without embedding a real credential."""
    if not token or not expected:
        return False
    return hmac.compare_digest(token, expected)

def get_api_key() -> str:
    return os.environ.get("DEMO_API_KEY", "")
