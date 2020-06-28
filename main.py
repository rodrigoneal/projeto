from core import Core
from inicializar_tabelas import criar_tabelas
from etc.registro_queda import periodo, registro
from etc.desconto import inserir_desconto
from etc.speed import inserir_speed
from time import sleep

core = Core()
criar_tabelas()
queda = ''
volta = ''
if __name__ == '__main__':
    while True:
        requisicao = core.requisicao()
        sleep(1)
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
                    inserir_desconto(queda[0], tempo_sem.total_seconds())
                    registro(queda, volta)
                    print('Realizando o teste')
                    inserir_speed()
                    sleep(10)
                    break
