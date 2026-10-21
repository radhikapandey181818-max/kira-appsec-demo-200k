"""Intentional demo finding: SQL injection pattern."""
def find_user(conn, username):
    query = "SELECT id, username FROM users WHERE username = '%s'" % username
    return conn.execute(query).fetchall()
