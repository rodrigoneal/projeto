import sqlite3


class DbTest:
    lista = []
    __table__ = None

    def __init__(self, db_nome: str):
        self.conn = sqlite3.connect(f'db/{db_nome}.db')
        self.cursor = self.conn.cursor()

    def coluna(self, sql):
        self.lista.append(sql)
    def decorator(self, sql):
        pass

    def mostrar(self):
        with open('sql/' + self.__table__, 'a+') as arquivo:
            for i in self.lista:
                arquivo.write(f'{i}\n')
        print(len(self.lista))
        self.lista.clear()


if __name__ == '__main__':
    a = DbTest('teste')

    a.coluna('Testando')
    a.__table__ = 'Curso.txt'
    a.coluna('É uma dwddwd')
    a.coluna('Porra')
    a.mostrar()
