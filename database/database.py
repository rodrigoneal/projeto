import sqlite3
import os
from core_db import inserir_sql, criar_sql, select_sql
conn = sqlite3.connect('registro.db')



class Connect:

    def __init__(self, db_name: str):
        try:
            self.conn = sqlite3.connect(f'database/db/{db_name}.db')
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




if __name__ == '__main__':
    banco = Banco('registro')
    """
    tabela = ['dataqueda TEXT NOT NULL',
              'horaqueda TEXT NOT NULL',
              'datavolta TEXT NOT NULL',
              'horavolta TEXT NOT NULL',
              'periodo TEXT NOT NULL']

    tabela = criar_sql(sql=tabela, tabela_nome='registro')
    print(tabela)
    banco.criar_schema(tabela)
    tabela = {'dataqueda': '10/08/2020', 'horaqueda': '05:20:00', 'datavolta': '10/08/2020', 'horavolta': '05:04:00', 'periodo': '00:04:00'}
    tabela = inserir_sql(tabela, 'registro')
    print(tabela)
    banco.criar_schema(tabela, 2)"""
    sql = {'dataqueda':'registro'}

    a = select_sql(sql, 'registro')
    print(a)
    b = banco.ler_schema(a)
    print(b)