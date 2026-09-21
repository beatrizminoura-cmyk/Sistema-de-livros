from flask import Blueprint, render_template, request, redirect, url_for, session

from app.models import autenticar_usuario
from app.middleware import guest_only, login_required


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET", "POST"])
@guest_only
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        user = autenticar_usuario(usuario, senha)

        if user:
            session["usuario"] = user["usuario"]

            return redirect(url_for("main.home"))

        return render_template(
            "login.html",
            erro="Usuário ou senha inválidos."
        )

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():

    session.pop("usuario", None)

    return redirect(url_for("auth.login"))