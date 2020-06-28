from dateutil import parser
from database.core_db import Manipular_sql
from types import MemberDescriptorType


def periodo(queda: list, volta: list) -> MemberDescriptorType:
    """
    Calcula o tempo que a internet ficou sem funcionar
    :param queda: data e hora que a internet caiu
    :param volta: data e hora que a internet voltou
    :return: datetime com o tempo que ficou sem internet
    """
    queda = ', '.join(queda)
    volta = ', '.join(volta)
    queda_parse = parser.parse(queda)
    volta_parse = parser.parse(volta)
    periodo = (volta_parse - queda_parse)
    return periodo


def registro(queda, volta):
    """
    Insere na tabela registro os valores da data e hora que a internet caiu e voltou

    :param queda: Uma lista com a data e hora que a internet caiu
    :param volta: Uma lista com a data e hora que a internet voltou
    """
    data_queda, hora_queda, data_volta, hora_volta = [*queda, *volta]
    sql = {'data_queda': data_queda, 'hora_queda': hora_queda,
           'data_volta': data_volta, 'hora_volta': hora_volta,
           'tempo_sem': periodo(queda, volta)}
    manipular = Manipular_sql('registro')
    manipular.criar_inserir_sql(sql)
    manipular.executar_sql()
