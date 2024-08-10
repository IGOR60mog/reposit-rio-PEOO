class Empresa:

    def __init__ (self, nome):
        if nome != "": self.__nome = nome
        else: raise ValueError("Informe um nome")
        self.__cliente = []

    def inserir(self, c):
        if c == str:
            self.__cliente.append(c)
        else:
            raise ValueError()

    def excluir(self, c):
        if c in self.__cliente:
            self.__cliente.remove(c)
        else:
            raise ValueError()

    def listar(self):
        return self.__cliente[:]
    
    def total(self):
        return len(self.__cliente[:])

    def __str__(self):
        return f"Nome - {self.__nome} Cliente(s) - {self.__cliente}"

