"""Baseline demo routes; intentionally minimal and safe."""
from flask import Flask, jsonify, request
import os
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("APP_SECRET_KEY", "development-only-change-me")

def get_db():
    return sqlite3.connect(os.environ.get("APP_DB_PATH", "demo.db"))

@app.get("/")
def home():
    return jsonify({"message": "Kira AppSec Demo"})

@app.get("/hello")
def hello():
    name = request.args.get("name", "Guest")
    # Return data as JSON rather than building HTML from user input.
    return jsonify({"message": f"Hello, {name}!"})

@app.get("/user")
def get_user():
    user_id = request.args.get("id", "1")
    conn = get_db()
    try:
        row = conn.execute("SELECT id, username FROM users WHERE id = ?", (user_id,)).fetchone()
        if row is None:
            return jsonify({"error": "not found"}), 404
        return jsonify({"id": row[0], "username": row[1]})
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=False)
