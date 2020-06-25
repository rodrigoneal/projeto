from database.database import Banco
from database.core_db import Manipular_sql
from datetime import datetime
from etc import calendario


def criar_tabelas():
    """
    Função que criar e inicializa as principais tabelas do banco de dados

    :rtype: object
    """
    # Inicializando o banco
    banco = Banco('dados')

    # Criando a tabela registro do banco de dados
    registro = ['data_queda TEXT NOT NULL',
                'hora_queda TEXT NOT NULL',
                'data_volta TEXT NOT NULL',
                'hora_volta TEXT NOT NULL',
                'tempo_sem TEXT NOT NULL']
    manipular_registro = Manipular_sql('registro')
    registro = manipular_registro.criar_tabela_sql(sql=registro)
    banco.executar_schema(registro)

    # Criando a tabela com as datas do banco
    ano = datetime.now().year
    datas = []
    for data in calendario.meses.values():
        datas.append(data + ' TEXT')

    manipular_datas = Manipular_sql(f'datas_{ano}')
    datas = manipular_datas.criar_tabela_sql(datas)
    banco.executar_schema(datas)
