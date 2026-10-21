"""Admin access example."""
from functools import wraps
from flask import abort, request

def require_admin(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        # Demo placeholder: real applications must validate server-side identity/roles.
        role = request.headers.get("X-Demo-Role", "")
        if role != "admin":
            abort(403)
        return view(*args, **kwargs)
    return wrapped
