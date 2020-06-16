import sqlite3

class Database:
    def __init__(self, nome):
        self.conn = sqlite3.connect(f'{nome}.db')
        self.cursor = self.conn.cursor()

    def tabela(self,sql):
        cursor = self.cursor.execute(sql)
        self.conn.commit()


