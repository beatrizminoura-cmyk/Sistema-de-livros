from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.database import ConnectionManager


def buscar_por_email(email):

    conn = ConnectionManager.conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, nome, email, senha
        FROM usuarios
        WHERE email = ?
        """,
        (email,)
    )

    usuario = cursor.fetchone()

    ConnectionManager.fechar(conn)

    return usuario


def autenticar(email, senha):

    usuario = buscar_por_email(email)

    if usuario is None:
        return None

    if check_password_hash(usuario["senha"], senha):
        return usuario

    return None


def criar_usuario(nome, email, senha):

    conn = ConnectionManager.conectar()
    cursor = conn.cursor()

    senha_hash = generate_password_hash(senha)

    cursor.execute(
        """
        INSERT INTO usuarios
        (nome, email, senha)
        VALUES (?, ?, ?)
        """,
        (nome, email, senha_hash)
    )

    conn.commit()

    ConnectionManager.fechar(conn)


def buscar_por_id(id_usuario):

    conn = ConnectionManager.conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, nome, email
        FROM usuarios
        WHERE id = ?
        """,
        (id_usuario,)
    )

    usuario = cursor.fetchone()

    ConnectionManager.fechar(conn)

    return usuario