from app.database import ConnectionManager


class Livro:

    def __init__(
        self,
        titulo,
        autor,
        id=None
    ):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def salvar(self):

        with ConnectionManager() as conn:

            cursor = conn.cursor()

            if self.id is None:

                cursor.execute(
                    """
                    INSERT INTO livros
                    (titulo, autor)
                    VALUES (?, ?)
                    """,
                    (
                        self.titulo,
                        self.autor
                    )
                )

                self.id = cursor.lastrowid

            else:

                cursor.execute(
                    """
                    UPDATE livros
                    SET titulo = ?,
                        autor = ?
                    WHERE id = ?
                    """,
                    (
                        self.titulo,
                        self.autor,
                        self.id
                    )
                )

    @classmethod
    def buscar_por_id(cls, id_livro):

        with ConnectionManager() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id, titulo, autor
                FROM livros
                WHERE id = ?
                """,
                (id_livro,)
            )

            registro = cursor.fetchone()

            if registro is None:
                return None

            return cls(
                id=registro["id"],
                titulo=registro["titulo"],
                autor=registro["autor"]
            )

    @classmethod
    def buscar_todos(cls):

        with ConnectionManager() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id, titulo, autor
                FROM livros
                ORDER BY titulo
                """
            )

            registros = cursor.fetchall()

            livros = []

            for registro in registros:

                livro = cls(
                    id=registro["id"],
                    titulo=registro["titulo"],
                    autor=registro["autor"]
                )

                livros.append(livro)

            return livros