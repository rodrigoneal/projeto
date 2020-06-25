from core import Core
from inicializador import criar_tabelas


inicializar = criar_tabelas()
core = Core()
requisicao = core.requisicao()

if __name__ == '__main__':
    while True:
        requisicao = core.requisicao()
        if requisicao[0]:
            mes = requisicao[1][3:5]
            print(mes)
    # Todo: criar uma função para simplificar a inserção no banco de dados