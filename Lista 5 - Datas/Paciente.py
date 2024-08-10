from calendar import c
from datetime import datetime
from datetime import timedelta

class Paciente:
    def __init__(self):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__nascimento = datetime(1, 1, 1)

    def SetNome(self, n):
        if n != "": self.__nome = n
        else: raise ValueError()

    def SetCPF(self, c):
        if c != "": self.__cpf = c
        else: raise ValueError()

    def SetTelefone(self, t):
        if t != "": self.__telefone = t
        else: raise ValueError()

    def SetNascimento(self, n):
        if n != datetime.today(): self.__nascimento = n
        else: raise ValueError()
    
    def GetNome(self): return self.__nome
    def GetCPF(self): return self.__cpf 
    def GetTel(self): return self.__telefone 
    def GetNascimento(self): return self.__nascimento

    def Idade(self):
        x = self.__nascimento
        y = datetime.now()
        z = y-x
        dias = z.days
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} Anos e {meses} meses"

    def __str__(self):
        return f"   * Nome - {self.__nome} \n   * CPF - {self.__cpf} \n   * Telefone - {self.__telefone} \n   * Nascimento - {self.__nascimento} \n"

class UI:
    @staticmethod
    def menu():
        print("1 - Registrar paciente, 2 - Saber idade, 3 - Info, 4 - fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: p = UI.Registro()
            if op == 2: UI.idade(p)
            if op == 3: UI.info(p)
    
    @staticmethod
    def Registro():
        nome = input("Informe teu nome: ")
        cpf = input("Informe seu CPF: ")
        telefone = input("Informe teu telefone: ")
        nascimento = datetime.strptime(input("Informe teu nascimento em dd/mm/aaaa: "), "%d/%m/%Y")
        p = Paciente()
        p.SetNome(nome)
        p.SetCPF(cpf)
        p.SetTelefone(telefone)
        p.SetNascimento(nascimento)
        return p
    
    def idade(x):
        print(x.Idade())

    def info(x):
        print(x)
UI.main()