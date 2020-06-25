from core import Core
from inicializador import criar_tabelas
from etc.carga_banco import periodo

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
                carga = periodo(queda, volta)
                a = [*queda, *volta, carga]
                print(a)
                break
