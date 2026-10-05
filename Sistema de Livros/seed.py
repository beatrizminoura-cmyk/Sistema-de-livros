from app.database.init_db import inicializar_banco
from app.models import Livro


inicializar_banco()


livros = [
    Livro(
        titulo="O Hobbit",
        autor="J. R. R. Tolkien"
    ),

    Livro(
        titulo="Harry Potter e a Pedra Filosofal",
        autor="J. K. Rowling"
    ),

    Livro(
        titulo="Orgulho e Preconceito",
        autor="Jane Austen"
    )
]


for livro in livros:

    livro.salvar()

    print(
        f"Livro cadastrado: {livro.titulo}"
    )