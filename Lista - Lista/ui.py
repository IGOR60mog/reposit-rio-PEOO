from cliente import cliente
from empresa import Empresa

class UI:
    @staticmethod
    def menu():
        print("1 - Nova empresa <\n> 2 - Inserir cliente <\n> 3 - Excluir cliente <\n> 4 - Listar clientes <\n> 5 - Total de clientes <\n> 6 - Fim")    
        return int(input("Qual opção você deseja? "))
    
    @staticmethod
    def main():
        op = 0
        while op != 6 and op != 0:
            op = UI.menu()
            if op == 1: p = UI.nova_empresa()
            if op == 2: UI.inserir_cliente(p)
            if op == 3: UI.excluir_cliente(p)
            if op == 4: UI.listar_clientes(p)
            if op == 5: UI.total_clientes(p)
    
    @staticmethod
    def nova_empresa():
        nome = input("Qual o nome da empresa? ")
        p = Empresa(nome)
        return p

    def inserir_cliente(x):
        nome = input("Qual o nome do cliente? ")
        cpf = input("Qual o cpf do cliente? ")
        limite = input("Qual o limite do cliente? ")

        c = cliente(nome, cpf, limite)
        x.inserir(c)

    def excluir_cliente(x):
        c = input("Quem vc quer excluir?")
        if c in x:
            x.excluir(c)
        else: 
            raise ValueError()

    def listar_clientes(x):
        print(x.listar())
    
    def total_clientes(x):
        print(x.total())

UI.menu()
UI.main()