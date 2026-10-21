"""Remediated demo: parameterized SQL."""
def find_user(conn, username):
    return conn.execute(
        "SELECT id, username FROM users WHERE username = ?",
        (username,)
    ).fetchall()
