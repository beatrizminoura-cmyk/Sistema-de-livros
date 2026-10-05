import os

from app.database import ConnectionManager


BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)


def inicializar_banco():

    caminho_schema = os.path.join(
        BASE_DIR,
        "database",
        "schema.sql"
    )

    with ConnectionManager() as conn:

        cursor = conn.cursor()

        with open(
            caminho_schema,
            encoding="utf-8"
        ) as arquivo:

            script = arquivo.read()

        cursor.executescript(script)