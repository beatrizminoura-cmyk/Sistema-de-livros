from flask import Blueprint, render_template, request, redirect, session, url_for, flash, make_response, current_app
from app.models import Usuario
from app.middleware import guest_only, login_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
@guest_only
def login():
    if request.method == "POST":
        email=request.form.get("email", "").strip().lower(); senha=request.form.get("senha", "")
        usuario=Usuario.autenticar(email, senha)
        if usuario:
            session.clear(); session["usuario_id"]=usuario.id; session["usuario_nome"]=usuario.nome
            current_app.logger.info("Login realizado: usuario_id=%s", usuario.id)
            flash("Bem-vindo à sua estante!", "success")
            resp = redirect(url_for("main.home"))
            if request.form.get("lembrar_email"):
                resp.set_cookie(
                    "ultimo_email", email,
                    max_age=30 * 24 * 60 * 60,
                    httponly=True,
                    samesite="Lax"
                )
            else:
                # Se a pessoa desmarcar a opção, remove o cookie anterior.
                resp.delete_cookie("ultimo_email")
            return resp
        current_app.logger.warning("Falha de autenticação para email informado")
        flash("E-mail ou senha inválidos.", "erro")
    return render_template("login.html", ultimo_email=request.cookies.get("ultimo_email", ""))

@auth_bp.route("/cadastro", methods=["GET", "POST"])
@guest_only
def cadastro():
    if request.method == "POST":
        nome=request.form.get("nome", "").strip(); email=request.form.get("email", "").strip().lower(); senha=request.form.get("senha", "")
        if not nome or not email or not senha or len(nome)>100 or len(senha)<6:
            flash("Preencha todos os campos. A senha deve ter pelo menos 6 caracteres.", "erro")
        elif Usuario.buscar_por_email(email):
            flash("Este e-mail já está cadastrado.", "erro")
        else:
            usuario=Usuario(nome, email, senha); usuario.salvar()
            current_app.logger.info("Novo usuário cadastrado: usuario_id=%s", usuario.id)
            flash("Cadastro realizado! Faça login.", "success")
            return redirect(url_for("auth.login"))
    return render_template("cadastro.html")

@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    session.clear(); flash("Você saiu da sua conta.", "success")
    return redirect(url_for("auth.login"))
