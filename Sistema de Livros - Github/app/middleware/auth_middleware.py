from functools import wraps
from flask import session, redirect, url_for, g
from app.models import Usuario

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        user_id = session.get("usuario_id")
        usuario = Usuario.buscar_por_id(user_id) if user_id else None
        if usuario is None:
            session.clear()
            return redirect(url_for("auth.login"))
        g.usuario = usuario
        return view(*args, **kwargs)
    return wrapped_view
