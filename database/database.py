import sqlite3

caminho = '/Users/rodrgo/PycharmProjects/projeto/database/db'

class Connect:

    def __init__(self, db_name: str):
        try:
            self.conn = sqlite3.connect(f'{caminho}/{db_name}.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f'{e}... Erro ao abrir o banco {db_name}')

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print('Banco fechado')


class Banco:

    def __init__(self, db_name):
        self.db_name = db_name
        self.db = Connect(db_name)

    def close_connection(self):
        self.db.close_db()

    def commit(self):
        self.db.conn.commit()

    def criar_schema(self, schema, opcao=1):

        if opcao == 2:

            self.db.cursor.executescript(schema)
            self.commit()

        else:
            self.db.cursor.executescript(schema)

    def ler_schema(self, schema):
        self.db.cursor.execute(schema)
        resultado = self.db.cursor.fetchall()
        return resultado
