from core import Core
from inicializar_tabelas import criar_tabelas
from etc.carga_banco import periodo, inserir
from etc.speed import speed
from etc.calendario import desconto
from time import sleep

core = Core()
queda = ''
volta = ''
if __name__ == '__main__':
    while True:
        requisicao = core.requisicao()
        print(requisicao)
        try:
            if not requisicao[0] or not requisicao[0] == None:
                queda = requisicao[1:]
        except TypeError:
            print('Não há nenhuma rede conectada')
            sleep(60)
            continue
        while not requisicao[0]:
            print('Sem internet')
            requisicao = core.requisicao()
            if requisicao[0]:
                print('internet voltou')
                volta = requisicao[1:]
                tempo_sem = periodo(queda, volta)

                if str(tempo_sem) == '0:00:00':
                    break
                else:
                    desconto = desconto()
                    sql = {'data_queda':queda[0],'hora_queda':queda[1],
                               'data_volta':volta[0],'hora_volta':volta[1],
                               'tempo_sem':str(tempo_sem)}

                    inserir(sql, 'registro')
                    print('Realizando o teste')
                    speed = speed()
                    print(speed)
                    print(type(speed))
                    inserir(speed, 'testes')
                    sleep(10)





                    break
