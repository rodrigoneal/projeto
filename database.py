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
    add = []

    def __init__(self, db_name):
        self.db_name = db_name
        self.db = Connect(db_name)

    def close_connection(self):
        self.db.close_db()

    def lista(self, args):
        self.add.append(args)
        self.add[-1].replace(',', '')
        return self.add

    def criar_sql(self, tabela_nome) -> None:
        with open(f'sql/{tabela_nome}.sql', 'w') as arquivo:
            arquivo.write(f'CREATE TABLE {tabela_nome}(')
            for i in self.add:
                arquivo.write(f'\n{i}')
            arquivo.write('\n);')

    def criar_schema(self, schema_path):
        try:
            with open(schema_path, 'rt') as sql:
                schema = sql.read()
                self.db.cursor.executescript(schema)
        except sqlite3.OperationalError:
            print('A tabela já existe')




if __name__ == '__main__':
    banco = Clientedb('teste')
    id = 'id INT NOT NULL,'
    nome = 'nome TEXT NOT NULL,'
    idade = 'idade INT NOT NULL,'
    cidade = 'cidade TEXT NOT NULL'
    banco.lista(id)
    banco.lista(nome)
    banco.lista(idade)
    banco.lista(cidade)
    banco.criar_sql('tentando')
    banco.criar_schema('sql/tentando.sql')

