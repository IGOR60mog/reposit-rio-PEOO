class cliente:
    def __init__(self, n, c, l):
        self.__nome = self.SetNome(n)
        self.__cpf = self.SetCPF(c)
        self.__limite = self.SetLimite(l)
    
    def SetNome(self, x):
        if x != '': self.__nome = x
        else: raise ValueError()
    def SetCPF(self, x):
        if x != '': self.__cpf = x
        else: raise ValueError()       
    def SetLimite(self, x):
        if x != '': self.__limite = x
        else: raise ValueError() 
    def GetNome(self):
        return self.__nome
    def GetCPF(self):
        return self.__CPF
    def GetLimite(self):
        return self.__Limite
    def __str__(self):
        return print(f"Nome - {self.__nome} CPF - {self.__cpf} Limite - {self.__limite}")