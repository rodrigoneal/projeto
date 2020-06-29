from database.database import Banco
from database.core_db import Manipular_sql
from datetime import datetime
from etc import calendario

__registro__ = 'registro'
ano = datetime.now().year
__datas__ = f'datas_{ano}'
__qualidade__ = 'qualidade'

def criar_tabelas():
    """
    Função que criar e inicializa as principais tabelas do banco de dados

    """
    # Inicializando o banco

    banco = Banco('dados')

    # Criando a tabela registro do banco de dados
    registro = ['data_queda TEXT NOT NULL',
                'hora_queda TEXT NOT NULL',
                'data_volta TEXT NOT NULL',
                'hora_volta TEXT NOT NULL',
                'tempo_sem TEXT NOT NULL',]
    manipular_registro = Manipular_sql(__registro__)
    manipular_registro.criar_tabela_sql(sql=registro)
    manipular_registro.executar_sql()

    # Criando a tabela com as datas do banco
    datas = []
    for data in calendario.meses().values():
        datas.append(data + ' REAL')

    manipular_datas = Manipular_sql(__datas__)
    manipular_datas.criar_tabela_sql(datas)
    manipular_datas.executar_sql()

    # Criando a tabela com velocidades, ping e perda
    testes = ['download INTEGER', 'upload INTEGER',
              'ping INTEGER', 'perda_pacote TEXT',
              'atualizado DATETIME']
    manipula_status = Manipular_sql(__qualidade__)
    manipula_status.criar_tabela_sql(testes)
    manipula_status.executar_sql()

