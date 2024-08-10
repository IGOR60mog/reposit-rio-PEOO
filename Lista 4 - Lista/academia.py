class Esporte:

    def __init__(self, n, h, m):
        self.__nome = n
        self.__horarios = h
        self.__mensalidade = m

        if n == "": raise ValueError("Nome não pode ser vazio")
        if h == "": raise ValueError("Horário não pode ser vazio")
        if m == 0: raise ValueError("Mensalidade não pode ser 0")
    
    def get_nome (self): return self.__nome
    def get_hoarios (self): return self.__horarios
    def get_mensalidade (self): return self.__mensalidade
    def __str__ (self):
        return f"Esporte - {self.__nome} - Horários - {self.__horarios} - Mensalidade - {self.__mensalidade} "
    
class Academia:

    def __init__ (self, n, e):
        self.__nome = n
        self.__endereço = e
        self.__esporte = []
        if n == "": raise ValueError("Nome não pode ser vazio")
        if e =="": raise ValueError("Endereço não pode ser vazio")

    def Inserir(self, e):
        if e in self.__esporte:
            raise ValueError("Esporte já incluso")
        else:
            self.__esporte.append(e)
    
    def Listar(self):
        return self.__esporte[:]
    
    def Mensalidade(self):
        soma = 0
        for x in self.__esporte:
            soma += x.get_mensalidade()
        media = soma / len(self.__esporte)
        return media
    
    def __str__ (self):
        return f"Academia - {self.__nome} - Endereço - {self.__endereço}"
    
class UI:
    @staticmethod
    def menu():
        print("1 - Criar Academia, 2 - Inserir esporte, 3 - Listar esportes, ")
        


