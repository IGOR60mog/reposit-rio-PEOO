from datetime import datetime
from datetime import timedelta

import enum

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
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
           
    def SetValorBoleto (self, b):
        if b != 0.0:
            self.__valorBoleto = b
        else:
            raise ValueError()


    def SetValorPago(self,p):
        if p != 0.0:
            self.__valorPago = p
        else:
            raise ValueError()
            
        
        
    def Pagar(self, v):
        self.SetPagto(datetime.now())
        if self.__vencimento < self.__pagto and self.__pagto > self.__emissao:
            self.SetValorPago(v)
        else:
            raise ValueError()
        
    def situacao(self):
        if self.__valorPago == self.valorBoleto:
            self.__situacao = Pagamento.Pago
        elif self.__valorPago < self.valorBoleto and self.__valorPago > 0:
            self.__situacao = Pagamento.PagoParcial
        else:
            self.__situacao = Pagamento.EmAberto
        return self.__situacao
        

    def __str__(self):
        return f"Código: {self.__barras} - Emissão: {self.__emissao} - Vencimento: {self.__vencimento} - Valor: {self.__valorBoleto}"

class UI:
    @staticmethod
    def main():
        print(" 1 - Novo boleto; 2 - Informações do Boleto; 3 - Pagar; 4 - Situacao; 5 - fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def menu():
        
        op = 0
        while op != 5:
            op = UI.main()
            if op == 1: b = UI.NovoBoleto()
            if op == 2: print(b)
            if op == 3: UI.Pagando(b)
            if op == 4: UI.SituacaoAtual(b)

        @staticmethod
        def NovoBoleto():
            cod = input("Insira código do boleto: ")
            Ems = input("Insira data de emissão dd/mm/aaaa: ")
            Venc = datetime(input("Insira data de vencimento dd/mm/aaaa"))
            Valor = float(input("Insira valor do boleto"))

            b = Boleto()
            b.SetBarras(cod)
            b.SetEmissao(Ems)
            b.SetVencimento(Venc)
            b.SetValorBoleto(Valor)
            return b

        @staticmethod
        def Pagando(x):
            ValorPago = float(input("Insira valor a pagar: "))
            x.Pagar(ValorPago)
            print("Pagamento concluído!")

        @staticmethod
        def SituacaoAtual(x):
            Situ = x.situacao()

            if Situ.value == 1:
                print("Pagando em aberto!")
            if Situ.value == 2:
                print("Pagamento parcialmente completo!")
            else:
                print("Pagamento completo!")

UI.main()



