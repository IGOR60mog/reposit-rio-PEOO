from datetime import datetime
from datetime import timedelta
import enum

class Dias (enum.IntFlag):
    segunda = 1
    terça = 2
    quarta = 4
    quinta = 8
    sexta = 16

class Turno (enum.IntFlag):
    matutino = 1
    vespertino = 2
    noturno = 4

class Estagiario:
    def __init__(self, n, c, t):
        self.__nome = n
        self.__cpf = c
        self.__tel = t
        self.__dias = Dias
        self.__turno = Turno

        if n == "": raise ValueError("Nome Inválido!")
        if c == "": raise ValueError("CPF Inválido!")
        if t == "": raise ValueError("Telefone Inválido!")

    def SetDias(self, d):
        Lista = d.split()
        OSDIAS = Dias.Lista[0]
        for x in Lista:
            OSDIAS |= Dias.x
        self.__dias = OSDIAS
        

    def SetTurno(self, t):
        Lista = t.split(" ")
        osturnos = ''
        for x in Lista:
            osturnos |= Turno.x
        self.__turno = osturnos
    def GetDias(self):
        return self.__dias
    def GetTurno(self):
        return self.__turno
    def __str__(self):
        return f"Nome - {self.__nome} CPF - {self.__cpf} Telefone - {self.__tel}"
    
class UI:
    @staticmethod
    def menu():
        print("1 - Inscrição estágio, 2 - definir horários, 3 - definir turnos, 4 - informações, 5 - fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: e = UI.Inscricao()
            if op == 2: UI.dias(e)
            if op == 3: UI.turnos(e)
            if op == 4: UI.infos(e)
    @staticmethod
    def Inscricao():
        nome = input("Insira seu nome: ")
        cpf = input("Insira seu cpf: ")
        tel = input("Insira seu telefone: ")

        e = Estagiario(nome, cpf, tel)
        return e
    @staticmethod
    def dias(x):
        Dias = input("Insira os dias desejados: ")
        x.SetDias(Dias)
    @staticmethod
    def turnos(x):
        Turno = input("Insira os turnos desejados: ")
        x.SetTurno(Turno)
    @staticmethod
    def infos(x):
        print(x)
        print(f"Dias: {x.GetDias().name}")
        print(f"Turno: {x.GetTurno().name}")
UI.main()