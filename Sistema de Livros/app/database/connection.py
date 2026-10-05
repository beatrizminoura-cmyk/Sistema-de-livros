import sqlite3
from config import Config


class ConnectionManager:

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(Config.DATABASE)
        self.connection.row_factory = sqlite3.Row

        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):

        if self.connection:
            if exc_type:
                self.connection.rollback()
            else:
                self.connection.commit()

            self.connection.close()
            self.connection = None