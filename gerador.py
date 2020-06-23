from random import randint


def data():
    # Gerador de Mês
    mes1 = randint(0, 1)
    if mes1 == 1:
        mes2 = randint(0, 2)
    elif mes1 == 0:
        mes2 = randint(1, 9)
    else:
        mes2 = randint(0, 9)
    mes = int(f'{mes1}{mes2}')


    # Gerador de dia
    dia1 = randint(0, 3)
    if dia1 == 3:
        dia2 = randint(0, 1)
    elif dia1 == 0:
        dia2 = randint(1, 9)
    else:
        dia2 = randint(0, 9)
    dia = int(f'{dia1}{dia2}')
    if mes == 2 and dia > 28:
        dia = 28
        return f'{dia}/{mes}/2020'
    elif mes == 4 and dia > 30:
        dia = 30
        return f'{dia}/{mes}/2020'
    elif mes == 6 and dia > 30:
        dia = 30
        return f'{dia}/{mes}/2020'
    elif mes == 9 and dia > 30:
        dia = 30
        return f'{dia}/{mes}/2020'
    elif mes == 11 and dia > 30:
        dia = 30
        return f'{dia}/{mes}/2020'
    else:
        return f'{dia1}{dia2}/{mes1}{mes2}/2020'


def hora():
    cont = 0
    while True:
        hora1 = randint(0, 2)
        if hora1 == 2:
            hora2 = randint(0, 3)
        else:
            hora2 = randint(0, 9)



        minuto1 = randint(0, 5)
        minuto2 = randint(0, 9)

        segundo1 = randint(0, 5)
        segundo2 = randint(0, 9)

        return f'{hora1}{hora2}:{minuto1}{minuto2}:{segundo1}{segundo2}'

