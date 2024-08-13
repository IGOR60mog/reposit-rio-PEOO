from datetime import datetime
from datetime import timedelta

import enum

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoPartical = 2
    Pago = 3

class Boleto:

    def __init__(self):
        self.__barras = ""
        self.__emissao = datetime(1, 1, 1)
        self.__vencimento = datetime(1, 1, 1)
        self.__Pagto = datetime(1, 1, 1)
        self.__valorBoleto = 0.0
        self.__valorPago = 0.0
        self.__situacao = Pagamento.EmAberto

        def SetBarras (self, v):
            if v != "":
                self.__barras = v
            else:
                raise ValueError()
        
        def SetEmissao (self, e):
            if e != datetime(1, 1, 1):
                self.__emissao = e
            else:
                raise ValueError()
    
        def SetVencimento(self, v):
            if v != datetime(1, 1, 1):
                self.__vencimento = v
            else:
                raise ValueError()

        def SetPagto (self, p):
            if p != datetime(1, 1, 1):
                self.__Pagto = p
            else:
                raise ValueError()    
           
        def SetValorBoleto (self. b):
            if b != 0.0:
                self.__


        def ValorPago(self,p):
        def situacao(self, s):
