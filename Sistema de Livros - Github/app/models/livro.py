
from app.database import ConnectionManager


class Livro:

    def __init__(self, titulo, autor, usuario_id, id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.usuario_id = usuario_id

    def salvar(self):
        with ConnectionManager() as db:

            if self.id is None:
                db.cursor.execute(
                    """
                    INSERT INTO livros (titulo, autor, usuario_id)
                    VALUES (?, ?, ?)
                    """,
                    (self.titulo, self.autor, self.usuario_id)
                )

                self.id = db.cursor.lastrowid

            else:
                db.cursor.execute(
                    """
                    UPDATE livros
                    SET titulo = ?, autor = ?
                    WHERE id = ? AND usuario_id = ?
                    """,
                    (self.titulo, self.autor, self.id, self.usuario_id)
                )

    
    def atualizar(self):
        with ConnectionManager() as db:
            db.cursor.execute(
                """
                UPDATE livros
                SET titulo = ?, autor = ?
                WHERE id = ? AND usuario_id = ?
                """,
                (self.titulo, self.autor, self.id, self.usuario_id)
            )

            return db.cursor.rowcount > 0


    @classmethod
    def buscar_por_id(cls, id_livro, usuario_id):
        with ConnectionManager() as db:
            db.cursor.execute(
                """
                SELECT id, titulo, autor, usuario_id
                FROM livros
                WHERE id = ? AND usuario_id = ?
                """,
                (id_livro, usuario_id)
            )

            registro = db.cursor.fetchone()

            if registro is None:
                return None

            return cls(
                id=registro["id"],
                titulo=registro["titulo"],
                autor=registro["autor"],
                usuario_id=registro["usuario_id"]
            )

    @classmethod
    def buscar_todos(cls, usuario_id):
        with ConnectionManager() as db:
            db.cursor.execute(
                """
                SELECT id, titulo, autor, usuario_id
                FROM livros
                WHERE usuario_id = ?
                ORDER BY titulo
                """,
                (usuario_id,)
            )

            registros = db.cursor.fetchall()

            return [
                cls(
                    id=registro["id"],
                    titulo=registro["titulo"],
                    autor=registro["autor"],
                    usuario_id=registro["usuario_id"]
                )
                for registro in registros
            ]

    @classmethod
    def excluir(cls, id_livro, usuario_id):
        with ConnectionManager() as db:
            db.cursor.execute(
                """
                DELETE FROM livros
                WHERE id = ? AND usuario_id = ?
                """,
                (id_livro, usuario_id)
            )

            return db.cursor.rowcount > 0
