import sqlite3


class Connect:
    def __init__(self, db_name: str):
        try:
            self.conn = sqlite3.connect(f'{db_name}.db')
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


class Clientedb():
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = Connect(db_name)

    def close_connection(self):
        self.db.close_db()

    def criar_schema(self, schema_path):
        try:
            with open(schema_path, 'rt') as sql:
                schema = sql.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print(f'A tabela {self.db_name}')
if __name__ == '__main__':
    path = 'sql/registro_conexão.sql'
    c = Clientedb('cliente')
    c.criar_schema(path)