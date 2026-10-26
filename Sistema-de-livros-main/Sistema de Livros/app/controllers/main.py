
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from app.models import Livro
from app.middleware import login_required


main_bp = Blueprint("main", __name__)


@main_bp.route("/home")
@login_required
def home():

    livros = Livro.buscar_todos()

    return render_template(
        "home.html",
        livros=livros
    )


@main_bp.route("/livros/cadastrar", methods=["POST"])
@login_required
def cadastrar_livro():

    titulo = request.form.get("titulo", "").strip()
    autor = request.form.get("autor", "").strip()

    if not titulo or not autor:
        flash("Preencha o título e o autor do livro.", "erro")
        return redirect(url_for("main.home"))

    livro = Livro(
        titulo=titulo,
        autor=autor
    )

    livro.salvar()

    flash("Livro cadastrado com sucesso!", "sucesso")

    return redirect(url_for("main.home"))
