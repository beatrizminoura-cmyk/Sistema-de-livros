from functools import wraps

from flask import session, redirect, url_for


def guest_only(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if "usuario" in session:
            return redirect(url_for("main.home"))

        return view(*args, **kwargs)

    return wrapped_view