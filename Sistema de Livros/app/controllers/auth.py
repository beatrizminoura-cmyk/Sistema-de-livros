from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    url_for
)

from app.models import autenticar
from app.middleware import guest_only, login_required


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET", "POST"])
@guest_only
def login():

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        usuario = autenticar(email, senha)

        if usuario:

            session.clear()

            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]

            return redirect(url_for("main.home"))

        return render_template(
            "login.html",
            erro="E-mail ou senha inválidos."
        )

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect(url_for("auth.login"))