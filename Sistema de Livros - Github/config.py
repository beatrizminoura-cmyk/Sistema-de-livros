import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "chave-de-desenvolvimento-altere-na-entrega")
    DATABASE = os.path.join(BASE_DIR, "dados", "livros.db")
