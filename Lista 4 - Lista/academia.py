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
        if e == "": raise ValueError("Endereço não pode ser vazio")

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
        print("1 - Criar Academia, 2 - Inserir esporte, 3 - Listar esportes, 4 - Media Mensalidade, 5 - Info, 6 - fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: a = UI.criar_academia()
            if op == 2: UI.inserir_esporte(a)
            if op == 3: UI.listar_esportes(a)
            if op == 4: UI.media(a)
            if op == 5: UI.info(a)
    
    
    @staticmethod
    def criar_academia():
        nome = input("Informe o nome da academia: ")
        endereco = input("Informe o endereço da academia: ")
        a = Academia(nome, endereco)
        return a
    
    @staticmethod
    def inserir_esporte(x):
        nome = input("Informe nome do esporte: ")
        horario = input("Informe horário do esporte: ")
        mensalidade = int(input("Informe mensalidade do esporte: "))

        e = Esporte(nome, horario, mensalidade)
        x.Inserir(e)
    
    @staticmethod
    def listar_esportes(x):
        for e in x.Listar():
            print(e)


    @staticmethod
    def media(x):
        print(f"A Média da sua mensaldiade é de {x.Mensalidade()}")

    @staticmethod
    def info(x):
        print(x)

UI.main()



