from datetime import datetime
from datetime import timedelta

class Boleto:

    def __init__(self):
        self.__barras = ""
        self.__emissao = datetime(1, 1, 1)
        self.__vencimento = datetime(1, 1, 1)
        self.__Pagto = datetime(1, 1, 1)
        