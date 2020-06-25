from core import Core
from inicializador import criar_tabelas
from etc.carga_banco import periodo, inserir

inicializar = criar_tabelas()
core = Core()
queda = ''
volta = ''

if __name__ == '__main__':
    while True:
        requisicao = core.requisicao()
        print(requisicao)
        if not requisicao[0]:
            queda = requisicao[1:]
        while not requisicao[0]:
            requisicao = core.requisicao()
            if requisicao[0]:
                volta = requisicao[1:]
                tempo_sem = periodo(queda, volta)
                if tempo_sem == '0:00:00':
                    break
                else:
                    sql = {'data_queda':queda[0],'hora_queda':queda[1],
                               'data_volta':volta[0],'hora_volta':volta[1],
                               'tempo_sem':str(tempo_sem)}
                    inserir(sql)


                    break
