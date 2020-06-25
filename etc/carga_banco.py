from dateutil import parser
from database.core_db import Manipular_sql
from database.database import Banco


def periodo(queda, volta):
    queda = ', '.join(queda)
    volta = ', '.join(volta)
    queda_parse = parser.parse(queda)
    volta_parse = parser.parse(volta)
    periodo = (volta_parse - queda_parse)
    return periodo

def inserir(dados:dict):
    manipular = Manipular_sql('registro')
    inserir = manipular.criar_inserir_sql(dados)
    banco = Banco('dados')
    banco.executar_schema(inserir)
