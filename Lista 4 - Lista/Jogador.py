class Jogador:
    def __init__(self, n, c, g):
        self.__nome = ''
        self.__camisa = ''
        self.__gols = 0

        self.SetNome(n)
        self.SetCamisa(c)
        self.SetGols(g)
    
    def SetNome(self, n): 
        if n != '':
            self.__nome = n
        else: 
            raise ValueError()

    def SetCamisa(self, c):
        if c != '':
            self.__camisa = c
        else: 
            raise ValueError()
    def SetGols(self, g):
        if g != 0:
            self.__gols = g
        else:
            raise ValueError()

    def GetNome(self): return self.__gols
    def GetCamisa(self): return self.__camisa
    def GetGols(self): return self.__gols
    def __str__(self):
        return f"Nome - {self.__nome} Camisa - {self.__camisa} Gols - {self.__gols}"

class Time:

    def __init__ (self, n, c):
        if n == "": raise ValueError()
        if c == "": raise ValueError()
        self.__nome = n
        self.__estado = c
        self.__jogadores = []

    def Inserir(self, j):
        if j in self.__jogadores:
            raise ValueError()
        else:
            self.__jogadores.append(j)

    def Listar(self):
        return self.__jogadores[:]

    def Artilheiro(self):
        
        maior = self.__jogadores[0]
        for x in self.__jogadores:
            if x.GetGols() > maior.GetGols():
                maior = x
        return maior

    def __str__(self):
        return f"Nome - {self.__nome} Estado - {self.__estado}"


class UI:

    @staticmethod
    def menu():
        print(" 1 - Novo time, 2 - Inserir Jogadores, 3 - Listar Jogadores, 4 - Mostrar Artilheiro, 5 - Info, 6 - Fim")
        return int(input("Digite a opção escolhida: "))
    
    @staticmethod
    def main():

        op = 0

        while op != 5:

            op = UI.menu()
            if op == 1: p = UI.NovoTime()
            if op == 2: UI.InserirJg(p)
            if op == 3: UI.ListarJg(p)
            if op == 4: UI.MostrarArtilheiro(p)
            if op == 5: UI.info(p)

    @staticmethod
    def NovoTime():
        Nome = input("Nome do time: ")
        Estado = input("Estado do time: ")
        x = Time(Nome, Estado)
        return x

    @staticmethod
    def InserirJg(x):
        Nome = input("Nome do jogador: ")
        Camisa = input("Camisa do jogador: ")
        Gols = int(input("Gols do Jogador: "))

        m = Jogador(Nome, Camisa, Gols)
        x.Inserir(m)

    @staticmethod
    def ListarJg(x):
        for l in x.Listar():
            print(l)

    @staticmethod
    def MostrarArtilheiro(x):
        print(x.Artilheiro())

    @staticmethod
    def info(x):
        print(x)

UI.main()