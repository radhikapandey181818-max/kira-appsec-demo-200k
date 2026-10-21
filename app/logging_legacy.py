"""Intentional demo finding: sensitive value written to logs."""
import logging
logger = logging.getLogger(__name__)
def log_auth_token(token):
    logger.warning("Received authentication token: %s", token)
