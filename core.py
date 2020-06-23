from datetime import datetime
from requests import get
import subprocess
import platform


def darwin():
    gateway = subprocess.getoutput('netstat -nr | grep default')
    start = gateway.replace(' ', '').find('t') + 1
    end = gateway.replace(' ', '').find('G') - 1
    ip = gateway.replace(' ', '')[start:end]
    return ip


def data_hora() -> tuple:
    """
Converte a data e hora para o formato brasileiro
    :return: data e hora
    """
    agora = datetime.now()
    tempo = agora.strftime('%d/%m/%Y, %H:%M:%S').split(',')
    data = tempo[0]
    hora = tempo[1]
    return (data, hora)


def status_conexao() -> bool:
    """
Verifica se o computador está conectado a alguma rede


    :return: True se estiver conectado
    :return: False se não estiver
    """
    sistema = platform.system()
    if sistema == 'Darwin':
        proc = subprocess.getoutput('route get default | grep gateway')
    proc = subprocess.getoutput('ipconfig')
    a = proc.strip().split(':')[-1].strip()
    if a[0].isdigit():
        return True
    else:
        return False


def perda_dados(ip: str = '8.8.8.8', eco: str = '8') -> str:
    """
    Verifica o valor de perda de dados da conexão
    :param ip: ip do servidor que deseja pingar
    :param eco: numero de tentativa de conexão
    :return: O valor de perda de dados
    """

    proc = subprocess.getoutput('ping ' + ip + ' -n ' + eco)
    parente = proc.find('(') + 1
    porc = proc.find('%') + 1
    if not parente:
        raise ('IP informado é invalido')
    return proc[parente:porc]


class Core:
    def requisicao(self):
        """
        Faz um requisição no site do google para verificar se a internet está conectada

        :return:True se o get retornar 200
        :return: False se o get retornar 400
        :returns: Data e hora da requisição
        """
        urls = 'http://google.com'
        data = data_hora()[0]
        hora = data_hora()[1]
        try:
            status = get(urls, timeout=5)
            if status:
                return True, data, hora
        except:
            estado = status_conexao()
            if estado:
                return False, data, hora
            else:
                print("Verifique se você está conectado a alguma rede")


if __name__ == '__main__':
    a = status_conexao()
    print(a)
