import json


def escrever_setup(valor: float, download: int, upload: int, operadora: str) -> None:
    """
    Cria um arquivo Json com as informações da internet do usuario
    :param valor: Valor pago mensalmente pela internet
    :param download: velocidade de download contratada
    :param upload: velocidade de upload contratada
    :param operadora: nome da operadora de serviço
    """
    with open('setup.json', 'w') as setup:
        status = {'internet': valor, 'download': download, 'upload': upload, 'operadora': operadora}
        status = json.dumps(status)
        setup.write(status)


def ler_setup() -> dict:
    """
    Lê um arquivo JSON e converte pra Dict

    :return: Um dicionario com os dados do usuario
    """
    with open('setup.json', 'r') as setup:
        conf = json.load(setup)
        return (conf)
