from database.core_db import Manipular_sql
from database.database import Banco
from etc import calendario

banco = Banco('teste')
manipular = Manipular_sql('datas')
calendario = calendario.meses
sql = []
for i in calendario.values():
    sql.append(f'{i} TEXT')
criar = manipular.criar_tabela_sql(sql)

banco.commitar_schema(criar)
ler = manipular.criar_select_sql('dataqueda','teste')

