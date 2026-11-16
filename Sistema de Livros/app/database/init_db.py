
import os

from config import Config
from app.database import ConnectionManager


def inicializar_banco():

    caminho_schema = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "dados",
        "schema.sql"
    )

    with open(caminho_schema, "r", encoding="utf-8") as arquivo:
        sql = arquivo.read()

    with ConnectionManager() as db:
        db.cursor.executescript(sql)

    print("Banco de dados inicializado com sucesso!")
