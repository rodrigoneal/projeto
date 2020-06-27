import inicializar_tabelas
from database.core_db import Manipular_sql

datas = inicializar_tabelas.__datas__

def desc(valor, tempo_sem):
    preco = valor
    dia = preco / 30
    hora = dia / 24
    minutos = round(hora / 60, 3)
    print(minutos)
    segundos = minutos / 60
    desc = tempo_sem * segundos
    return desc

def inserir():
