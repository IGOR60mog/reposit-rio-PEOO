from calendar import c
from datetime import datetime
from datetime import timedelta


class Paciente:
    def __init__(self):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__nascimento = datetime()

# Métodos Sets e Gets
    def SetNome(self, n):
        if n != "":
            self.__nome = n
        else:
            raise ValueError()

    def SetCPF(self. c):
        if c != "":
            self.__cpf = c
        else:
            raise ValueError()

    def SetTelefone(self, t):
        if t != "":
            self.__telefone = t
        else:
            raise ValueError()

    def SetNascimento(self, n):
        if n != datetime.today():
            self.__nascimento = n
        else:
            raise ValueError()
    
    def GetNome(self):
        return self.__nome

    def GetCPF(self):
        return self.__cpf 

    def GetTel(self):
        return self.__telefone 

    def GetNascimento(self):
        return self.__nascimento

# Métodos diferentes
    def Idade(self):
        x = self.__nascimento
        y = datetime.now()
        z = y-x
        z = datetime.strptime(z, "%m/%Y")
        return z
    def __str__(self):
        return f"Nome - {self.__nome} \n CPF - {self.__cpf} \n Telefone - {self.__telefone} \n  Nascimento - {self.__nascimento} \n"

class UI:
    @staticmethod