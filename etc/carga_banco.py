from dateutil import parser


def periodo(queda, volta):

    queda = ', '.join(queda)
    volta = ', '.join(volta)
    queda_parse = parser.parse(queda)
    volta_parse = parser.parse(volta)
    periodo = (volta_parse - queda_parse)
    return periodo

def inserir_relatorio():
    pass
