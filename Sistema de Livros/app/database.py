import sqlite3

from config import Config


def conectar():

    conexao = sqlite3.connect(Config.DATABASE)

    conexao.row_factory = sqlite3.Row

    return conexao