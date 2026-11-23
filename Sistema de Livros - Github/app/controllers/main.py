from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from app.models import Livro, Avaliacao
from app.middleware import login_required
main_bp=Blueprint("main", __name__)

@main_bp.route("/home")
@login_required
def home():
    return render_template("home.html", livros=Livro.buscar_todos(session["usuario_id"]), avaliacoes=Avaliacao.listar_por_usuario(session["usuario_id"]))

@main_bp.route("/livros/cadastrar", methods=["POST"])
@login_required
def cadastrar_livro():
    titulo=request.form.get("titulo", "").strip(); autor=request.form.get("autor", "").strip()
    if not titulo or not autor or len(titulo)>150 or len(autor)>100:
        flash("Informe título e autor (até 150 e 100 caracteres).", "erro")
    else:
        Livro(titulo, autor, session["usuario_id"]).salvar(); flash("Livro cadastrado com sucesso!", "success")
        current_app.logger.info("Livro cadastrado pelo usuario_id=%s", session["usuario_id"])
    return redirect(url_for("main.home"))


@main_bp.route("/livros/<int:id_livro>/editar", methods=["GET", "POST"])
@login_required
def editar_livro(id_livro):
    usuario_id = session["usuario_id"]

    # Busca o livro pertencente ao usuário
    livro = Livro.buscar_por_id(id_livro, usuario_id)

    if livro is None:
        flash("Livro não encontrado.", "erro")
        return redirect(url_for("main.home"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor = request.form.get("autor", "").strip()

        # Validação dos dados
        if not titulo or not autor or len(titulo) > 150 or len(autor) > 100:
            flash("Informe título e autor (até 150 e 100 caracteres).", "erro")
            return render_template("editar_livro.html", livro=livro)

        # Atualização através do Model
        livro.titulo = titulo
        livro.autor = autor

        if livro.atualizar():
            flash("Livro atualizado com sucesso!", "success")
            current_app.logger.info(
                "Livro atualizado: livro_id=%s usuario_id=%s",
                id_livro, usuario_id
            )
        else:
            flash("Não foi possível atualizar o livro.", "erro")

        return redirect(url_for("main.home"))

    return render_template("editar_livro.html", livro=livro)


@main_bp.route("/livros/<int:id_livro>/excluir", methods=["POST"])
@login_required
def excluir_livro(id_livro):
    if Livro.excluir(id_livro, session["usuario_id"]): flash("Livro excluído.", "success")
    else: flash("Livro não encontrado.", "erro")
    return redirect(url_for("main.home"))

@main_bp.route("/avaliacoes/cadastrar", methods=["POST"])
@login_required
def cadastrar_avaliacao():
    livro_id=request.form.get("livro_id", type=int); nota=request.form.get("nota", type=int); comentario=request.form.get("comentario", "").strip(); uid=session["usuario_id"]
    livro=Livro.buscar_por_id(livro_id, uid) if livro_id else None
    if not livro or nota is None or nota<1 or nota>5 or not comentario or len(comentario)>500:
        flash("Confira o livro, a nota (1 a 5) e o comentário (até 500 caracteres).", "erro")
    else:
        Avaliacao(nota, comentario, livro_id, uid).salvar(); flash("Avaliação cadastrada!", "success")
        current_app.logger.info("Avaliação cadastrada pelo usuario_id=%s", uid)
    return redirect(url_for("main.home"))

@main_bp.route("/avaliacoes/<int:id_avaliacao>/excluir", methods=["POST"])
@login_required
def excluir_avaliacao(id_avaliacao):
    if Avaliacao.excluir(id_avaliacao, session["usuario_id"]): flash("Avaliação excluída.", "success")
    else: flash("Avaliação não encontrada.", "erro")
    return redirect(url_for("main.home"))
