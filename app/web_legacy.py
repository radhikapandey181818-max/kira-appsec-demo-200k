"""Intentional demo finding: debug mode enabled."""
from flask import Flask
legacy_app = Flask(__name__)
legacy_app.run(debug=True)
