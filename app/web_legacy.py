"""Remediated demo: do not enable debug mode in deployment."""
from flask import Flask
legacy_app = Flask(__name__)
# Start the server from a deployment entry point with debug disabled.
