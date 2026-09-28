import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "sua-chave-secreta"

    DATABASE = os.path.join(
        BASE_DIR,
        "database",
        "livros.db"
    )