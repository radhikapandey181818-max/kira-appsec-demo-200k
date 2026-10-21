"""Remediated demo: do not log tokens."""
import logging
logger = logging.getLogger(__name__)
def log_auth_token(_token):
    logger.info("Authentication event received; token redacted")
