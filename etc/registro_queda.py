from dateutil import parser
from database.core_db import Manipular_sql


def periodo(queda, volta):
    queda = ', '.join(queda)
    volta = ', '.join(volta)
    queda_parse = parser.parse(queda)
    volta_parse = parser.parse(volta)
    periodo = (volta_parse - queda_parse)
    return periodo


def registro(queda, volta):
    data_queda, hora_queda, data_volta, hora_volta = [*queda, *volta]
    sql = {'data_queda': data_queda, 'hora_queda': hora_queda,
           'data_volta': data_volta, 'hora_volta': hora_volta,
           'tempo_sem': periodo(queda, volta)}
    manipular = Manipular_sql('registro')
    manipular.criar_inserir_sql(sql)
    manipular.executar_sql()
