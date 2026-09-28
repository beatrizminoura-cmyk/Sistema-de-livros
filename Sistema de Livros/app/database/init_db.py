from pathlib import Path

from app.database import ConnectionManager


def inicializar_banco():

    conn = ConnectionManager.conectar()

    cursor = conn.cursor()

    with open("database/schema.sql", encoding="utf-8") as arquivo:
        cursor.executescript(arquivo.read())

    conn.commit()

    ConnectionManager.fechar(conn)