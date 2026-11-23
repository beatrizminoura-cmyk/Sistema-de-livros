
import sqlite3
from config import Config


class ConnectionManager:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(Config.DATABASE)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

        self.cursor.execute("PRAGMA foreign_keys = ON")

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        self.conn.close()
