import os



def apagar(path):
    dir = '/Users/rodrgo/PycharmProjects/projeto/sql'
    os.remove(f'{dir}/{path}.sql')


def criar_sql(sql, tabela_nome: str, opcao: str ='inserir'.lower()) ->str:
    if opcao == 'criar':
        with open(f'sql/{tabela_nome}.sql', 'w') as arquivo:
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
        with open(f'sql/{tabela_nome}.sql', 'rt') as sql:
            schema = sql.read()
        apagar(tabela_nome)
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
        apagar(tabela_nome)
        return schema