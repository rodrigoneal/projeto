import inicializar_tabelas
from database.core_db import Manipular_sql
from setup import setup
from .calendario import meses


def desc(tempo_sem: float) -> float:
    """
    Calcula o valor de desconto pelo tempo sem internet

    :param tempo_sem: tempo total sem conexão com a internet
    :return: retorna o valor em float para se inserido no banco de dados
    """
    preco = setup.ler_setup()['internet']
    dia = preco / 30
    hora = dia / 24
    minutos = (hora / 60)
    segundos = minutos / 60
    desc = tempo_sem * segundos
    return desc


def inserir_desconto(data: str, tempo_sem):
    """
     Insere o valor de desconto na tabela com o mês da queda
    :param data: dia e hora que a internet caiu
    :param tempo_sem: tempo que ficou sem internet
    """
    slice = data[0:2]
    data_inserir = inicializar_tabelas.__datas__
    mes = meses()[slice]
    inserir = Manipular_sql(data_inserir)
    desconto = desc(tempo_sem)
    inserir.criar_inserir_sql({mes: desconto})
    inserir.executar_sql()
