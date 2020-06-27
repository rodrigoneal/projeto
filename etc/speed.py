from speedtest import Speedtest
from core import perda_dados
from datetime import datetime

def speed():
    """
    Realizar um teste na velocidade de download, upload e ping
    :return: uma tupla com velocidade de download, upload e ping
    """
    atualizado = datetime.now().date()
    s = Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    down = (round(res["download"] / 1024 / 1024))
    up = (round(res["upload"] / 1024 / 1024))
    ping = (round(res["ping"]))
    perda = perda_dados()
    resp = {'download':down, 'upload':up, 'ping': ping, 'perda_pacote':perda, 'atualizado':atualizado}
    return resp

