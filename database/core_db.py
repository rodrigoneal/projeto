import os

try:
    os.mkdir(os.path.dirname(__file__) + '/sql')
except:
    pass


class Manipular_sql:

    def __init__(self, nome_da_tabela: str):
        self.nome = nome_da_tabela
        self.pasta = os.path.dirname(__file__) + '/sql'
        self.tabela = f'{self.pasta}/{nome_da_tabela}.sql'

    def _apagar(self):
        """
        Apaga  os comandos sql para não gerar conflito
        :rtype: object
        """
        os.remove(f'{self.pasta}/{self.nome}.sql')

    def _ler_sql(self):
        """
        Abre um arquivo SQL para usar no banco

        :return: str fortamado em SQL
        """
        with open(self.tabela, 'rt') as sql:
            schema = sql.read()
        self._apagar()
        return schema

    def criar_tabela_sql(self, sql:list, nome_tabela:str = None) -> str:
        """
        Formata um arquivo str e gera um arquivo SQL para criação de uma
        tabela de dados.
        :param sql: str para formatar um SQL
        :return: str formatado para criação de uma tabela SQL
        """
        if not nome_tabela:
            nome_tabela = self.nome
        with open(self.tabela, 'w') as arquivo:
            virgula = len(sql)
            cont = 1
            arquivo.write(f'CREATE TABLE IF NOT EXISTS {nome_tabela}(\n')
            for i in sql:
                if cont == virgula:
                    arquivo.write(f'{i}\n')
                else:
                    arquivo.write(f'{i},\n')
                cont += 1
            arquivo.write('\n);')
        leitura = self._ler_sql()
        return leitura

    def criar_inserir_sql(self, sql: dict, nome_tabela: str = None) -> str:
        """
        Formata um arquivo SQL para insert no banco


        :param sql: str para formatar um arquivo SQL
        :return: str com o comando SQl para insert já formatado
        """
        if not nome_tabela:
            nome_tabela = self.nome
        with open(self.tabela, 'w') as arquivo:
            arquivo.write(f'INSERT INTO {nome_tabela} (')
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
        leitura = self._ler_sql()
        return leitura

    def criar_select_sql(self, sql: str, nome_tabela:str=None) -> str:
        """
        Formata um arquivo de str para um SQL de consulta no banco
        :param sql: str para formatar em um arquivo SQL
        :return: str formatado para consultara um banco
        """
        if not nome_tabela:
            nome_tabela = self.nome
        with open(self.tabela, 'w') as arquivo:
            arquivo.write(f'SELECT {sql} FROM {nome_tabela}')
        leitura = self._ler_sql()
        return leitura
