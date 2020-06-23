import os


class Manipular_sql:
    pasta = '/Users/rodrgo/PycharmProjects/projeto/database/sql'

    def __init__(self, nome_da_tabela: str):
        self.nome = nome_da_tabela
        self.tabela = f'{self.pasta}/{nome_da_tabela}.sql'

    def _apagar(self):
        os.remove(f'{self.pasta}/{self.nome}.sql')

    def ler_sql(self):
        with open(self.tabela, 'rt') as sql:
            schema = sql.read()
        self._apagar()
        return schema

    def criar_sql(self, sql) -> str:
        with open(self.tabela, 'w') as arquivo:
            virgula = len(sql)
            cont = 1
            arquivo.write(f'CREATE TABLE IF NOT EXISTS {self.nome}(\n')
            for i in sql:
                if cont == virgula:
                    arquivo.write(f'{i}\n')
                else:
                    arquivo.write(f'{i},\n')
                cont += 1
            arquivo.write('\n);')
        leitura = self.ler_sql()
        return leitura

    def inserir_sql(self, sql: str) -> str:
        with open(self.tabela, 'w') as arquivo:
            arquivo.write(f'INSERT INTO {self.nome} (')
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
        leitura = self.ler_sql()
        return leitura

    def select_sql(self, sql: str) -> str:
        with open(self.tabela, 'w') as arquivo:
            arquivo.write(f'SELECT {sql} FROM {self.nome}')
        leitura = self.ler_sql()
        return leitura
