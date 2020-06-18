def decorator(caminho):
    def decorado(func):
        def porra(letra):
            with open(caminho, 'w') as arquivo:
                arquivo.write('Eu preciso dizer que te amo \n')
                arquivo.write(func(letra))
                arquivo.write('\nCazuza')
            return porra

    return decorado


@decorator(caminho='sql/caminho.txt')
def deco(letra):
    return letra


if __name__ == '__main__':
    a = deco
    a('cazuzaa')
