import os
from random import randint
import sqlite3


def apagar(path):
    dir = '/Users/rodrgo/PycharmProjects/projeto/sql'
    os.remove(f'{dir}/{path}.sql')


def criar_sql(sql, tabela_nome: str, opcao: str ='inserir'.lower()) ->str:
    if opcao == 'criar':

        with open(f'sql/{tabela_nome}.sql', 'w') as arquivo:
            arquivo.write(f'CREATE TABLE IF NOT EXISTS {tabela_nome}(\n')
            virgula = len(sql)
            cont = 1
            for i in sql:
                if cont == virgula:
                    arquivo.write(f'{i} ')
                else:
                    arquivo.write(f'{i}, ')
                cont += 1
            arquivo.write('\n);')
        with open(f'sql/{tabela_nome}.sql', 'rt') as sql:
            schema = sql.read()
        return schema
    elif opcao == 'inserir':
        with open(f'sql/{tabela_nome}.sql', 'w') as arquivo:
            arquivo.write(f'INSERT INTO {tabela_nome} (')
            virgula = len(sql)
            cont = 1
            for i in sql:
                if cont == virgula:
                    arquivo.write(f'{i}) ')
                else:
                    arquivo.write(f'{i}, ')
                cont += 1

            arquivo.write('Values (')
            cont = 1
            for i in sql:
                if cont == virgula:

                    arquivo.write(f'"{sql[i]}"); ')
                else:
                    arquivo.write(f'"{sql[i]}", ')
                cont += 1
        with open(f'sql/{tabela_nome}.sql', 'rt') as sql:
            schema = sql.read()

        return schema


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


if __name__ == '__main__':
    banco = Banco('db/registro')
    tabela = ['dataqueda TEXT NOT NULL',
              'horaqueda TEXT NOT NULL',
              'datavolta TEXT NOT NULL',
              'horavolta TEXT NOT NULL',
              'periodo TEXT NOT NULL']
    tabela = criar_sql(sql=tabela, tabela_nome='registro', opcao='criar')
    banco.criar_schema(tabela)

    tabela = {'dataqueda': '10/08/2020', 'horaqueda': '05:20:00', 'datavolta': '10/08/2020', 'horavolta' : '05:04:00', 'periodo': '00:04:00'}
    tabela = criar_sql(tabela, 'registro', 'inserir')

    banco.criar_schema(tabela, 2)