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


class Banco:

    def __init__(self, db_name):
        self.add = 0
        self.db_name = db_name
        self.db = Connect(db_name)
        self.tabela_nome = ''

    def close_connection(self):
        self.db.close_db()

    def lista(self, args):
        self.add = args

    def criar_sql(self, tabela_nome) -> None:
        self.tabela_nome = tabela_nome
        with open(f'sql/{tabela_nome}.sql', 'w') as arquivo:
            arquivo.write(f'CREATE TABLE IF NOT EXISTS {tabela_nome}(\n')
            for i in self.add:
                arquivo.write(f'{i}\n')
            arquivo.write('\n);')

    def criar_schema(self, ):
        try:
            with open(f'sql/{self.tabela_nome}.sql', 'rt') as sql:
                schema = sql.read()
                self.db.cursor.executescript(schema)
        except sqlite3.OperationalError:
            print('A tabela já existe')


if __name__ == '__main__':
    banco = Banco('db/registro')
    tabela = ['dataqueda TEXT NOT NULL,',
              'horaqueda TEXT NOT NULL,',
              'datavolta TEXT NOT NULL,',
              'horavolta TEXT NOT NULL,',
              'periodo TEXT NOT NULL'
              ]
    banco.lista(tabela)
    banco.criar_sql('registro')
    banco.criar_schema()
