from datetime import datetime
from requests import get
import subprocess
import platform

_sistema = platform.system()

def _darwin():
    """
    Comando para pegar o gateway do MacOs
    :return: ip da gateway
    """
    gateway = subprocess.getoutput('netstat -nr | grep default')
    start = gateway.replace(' ', '').find('t') + 1
    end = gateway.replace(' ', '').find('G') - 1
    ip = gateway.replace(' ', '')[start:end]
    return ip

def _windows():
    """
       Comando para pegar o gateway do Windows
       :return: ip da gateway
       """
    gateway = subprocess.getoutput('ipconfig')
    ip = (gateway.replace(' ', '').split(':')[-1])
    return ip

def _linux():
    """
       Comando para pegar o gateway do Linux
       PS: preciso instalar o sistema para testar os comandos.
       :return: ip da gateway
       """
    pass


def _data_hora() -> tuple:
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
    if _sistema == 'Darwin':
        gateway = _darwin()
        conf = gateway[0].isnumeric()
        if conf:
            return True
        else:
            return False
    if _sistema == 'Windows':
        gateway = _windows()
        if gateway:
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
    if _sistema == 'Windows':
        proc = subprocess.getoutput('ping ' + ip + ' -n ' + eco)
        start = proc.find('(') + 1
        end = proc.find('%') + 1
        ip = proc[start:end]
        if not end:
            raise ('IP informado é invalido')
        return ip
    else:
        proc = subprocess.getoutput('ping ' + ip + ' -c ' + eco)
        start = proc.find('ived') + 4
        end = proc.find('%') + 1
        ip = proc[start:end].replace(',','').rstrip().strip()
        return ip



class Core:
    def requisicao(self):
        """
        Faz um requisição no site do google para verificar se a internet está conectada

        :return:True se o get retornar 200
        :return: False se o get retornar 400
        :returns: Data e hora da requisição
        """
        urls = 'http://google.com'
        data = _data_hora()[0]
        hora = _data_hora()[1]
        try:
            status = get(urls, timeout=5)
            return True, data, hora
        except:
            estado = status_conexao()
            if estado:
                return False, data, hora
            else:
                print("Verifique se você está conectado a alguma rede")

