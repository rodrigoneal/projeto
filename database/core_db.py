import os

pasta = '/Users/rodrgo/PycharmProjects/projeto/database/sql'


def _apagar(path):
    os.remove(f'{pasta}/{path}.sql')


def ler_sql(tabela_nome):
    with open(f'{pasta}/{tabela_nome}.sql', 'rt') as sql:
        schema = sql.read()
        _apagar(tabela_nome)
        return schema


def criar_sql(sql, tabela_nome: str) -> str:
    with open(f'{pasta}/{tabela_nome}.sql', 'w') as arquivo:
        virgula = len(sql)
        cont = 1
        arquivo.write(f'CREATE TABLE IF NOT EXISTS {tabela_nome}(\n')
        for i in sql:
            if cont == virgula:
                arquivo.write(f'{i}\n')
            else:
                arquivo.write(f'{i},\n')
            cont += 1
        arquivo.write('\n);')
    leitura = ler_sql(tabela_nome)
    return leitura


def inserir_sql(sql: str, tabela_nome: str) -> str:
    with open(f'{pasta}/{tabela_nome}.sql', 'w') as arquivo:
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
    leitura = ler_sql(tabela_nome)
    return leitura


def select_sql(sql: str, tabela_nome: str) -> str:
    valor = ''
    with open(f'{pasta}/{tabela_nome}.sql', 'w') as arquivo:
        arquivo.write(f'SELECT ')
        for i in sql.keys():
            valor = i
            arquivo.write(i)

        arquivo.write(f' FROM {sql[valor]}')

    leitura = ler_sql(tabela_nome)
    return leitura
