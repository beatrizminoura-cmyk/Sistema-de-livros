from functools import wraps

from flask import session, redirect, url_for
from app.models import Usuario


def guest_only(view):
    """Impede que usuários autenticados acessem páginas de visitantes.

    A sessão só é considerada válida quando o usuário ainda existe no banco.
    """
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        user_id = session.get("usuario_id")

        if user_id:
            usuario = Usuario.buscar_por_id(user_id)
            if usuario is not None:
                return redirect(url_for("main.home"))

            # Remove sessões antigas ou inválidas.
            session.clear()

        return view(*args, **kwargs)

    return wrapped_view
