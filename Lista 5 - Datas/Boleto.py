from datetime import datetime
from datetime import timedelta

import enum

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoPartical = 2
    Pago = 3

class Boleto:

    def __init__(self, b, e, v, p, vb, vp ):
        self.__barras = b
        self.__emissao = e
        self.__vencimento = v
        self.__Pagto = p
        self.__valorBoleto = vb
        self.__valorPago = vp
        self.__situacao = 0
        
        if b == '': raise ValueError()
        if e == datetime(1, 1, 1): raise ValueError()
        if v == datetime(1, 1, 1): raise ValueError()
        if p == datetime(1, 1, 1): raise ValueError()
        if vb == 0.00: raise ValueError()
        if vp == 0.00: raise ValueError()

        def Pagar(self, vp):
            if self.__valorBoleto == vp:
                self.__situacao == 3
            elif self.__valorBoleto > vp:
                self.__situacao == 2
            elif vp < 0:
                self.__situacao == 1

