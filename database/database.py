import sqlite3
import os
try:
    os.mkdir(os.path.dirname(__file__) + '/db')
except:
    pass
caminho = os.path.dirname(__file__)+'/db'


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
        self.conn = self.db.conn
        self.cursor = self.conn.cursor()
        self.conn.commit()


    def executar_schema(self, sql: str) -> list:
        """
        Executa um comando SQL para criação ou inserção

        :param: sql: comando que será executado pelo sqlite3
        """
        self.cursor.execute(sql)
        self.conn.commit()

        resp = self.cursor.fetchall()
        if resp:
            return resp
        else:
            return None


