from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.database import ConnectionManager


class Usuario:

    def __init__(
        self,
        nome,
        email,
        senha,
        id=None,
        senha_hash=False
    ):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.senha_hash = senha_hash

    def salvar(self):

        with ConnectionManager() as conn:

            cursor = conn.cursor()

            if self.id is None:

                senha_hash = generate_password_hash(self.senha)

                cursor.execute(
                    """
                    INSERT INTO usuarios
                    (nome, email, senha)
                    VALUES (?, ?, ?)
                    """,
                    (
                        self.nome,
                        self.email,
                        senha_hash
                    )
                )

                self.id = cursor.lastrowid
                self.senha = senha_hash
                self.senha_hash = True

            else:

                senha = self.senha

                if not self.senha_hash:
                    senha = generate_password_hash(senha)
                    self.senha = senha
                    self.senha_hash = True

                cursor.execute(
                    """
                    UPDATE usuarios
                    SET nome = ?,
                        email = ?,
                        senha = ?
                    WHERE id = ?
                    """,
                    (
                        self.nome,
                        self.email,
                        senha,
                        self.id
                    )
                )

    def verificar_senha(self, senha):

        return check_password_hash(
            self.senha,
            senha
        )

    @classmethod
    def buscar_por_id(cls, id_usuario):

        with ConnectionManager() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id, nome, email, senha
                FROM usuarios
                WHERE id = ?
                """,
                (id_usuario,)
            )

            registro = cursor.fetchone()

            if registro is None:
                return None

            return cls(
                id=registro["id"],
                nome=registro["nome"],
                email=registro["email"],
                senha=registro["senha"],
                senha_hash=True
            )

    @classmethod
    def buscar_por_email(cls, email):

        with ConnectionManager() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id, nome, email, senha
                FROM usuarios
                WHERE email = ?
                """,
                (email,)
            )

            registro = cursor.fetchone()

            if registro is None:
                return None

            return cls(
                id=registro["id"],
                nome=registro["nome"],
                email=registro["email"],
                senha=registro["senha"],
                senha_hash=True
            )

    @classmethod
    def autenticar(cls, email, senha):

        usuario = cls.buscar_por_email(email)

        if usuario is None:
            return None

        if usuario.verificar_senha(senha):
            return usuario

        return None