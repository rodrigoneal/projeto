def decorator(func):
    def decorado(caminho:'path', letra:str) -> decorator:
        with open(caminho, 'w') as arquivo:
            arquivo.write('Eu preciso dizer que te amo \n')
            arquivo.write(func(caminho, letra))
            arquivo.write('\nCazuza')
        return decorado

    return decorado


@decorator
def deco(letra: str, caminho: str):
    return letra


if __name__ == '__main__':
    a = deco
