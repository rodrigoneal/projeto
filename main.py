from database.database import Banco
from gerador import data, hora
from database.core_db import Manipular_sql

from dateutil import parser

banco = Banco('teste')

tabela = ['dataqueda TEXT NOT NULL',
          'horaqueda TEXT NOT NULL',
          'datavolta TEXT NOT NULL',
          'horavolta TEXT NOT NULL',
          'periodo TEXT NOT NULL']
teste = Manipular_sql('teste')
tabela = teste.criar_sql(tabela)

banco.criar_schema(tabela)

data1 = data()
data2 = data()
hora1 = hora()
hora2 = hora()

converte1 = parser.parse(f'{data1} {hora1}')
converte2 = parser.parse(f'{data2} {hora2}')
periodo = str(converte1 - converte2)

tabela = {'dataqueda': f'{data1}', 'horaqueda': f'{hora1}', 'datavolta': f'{data2}', 'horavolta': f'{hora2}',
          'periodo': f'{periodo}'}
print(tabela)
tabela = teste.inserir_sql(tabela)

banco.criar_schema(tabela, 2)


