from view import View
from diretoria import diretorias

class UI:
    @staticmethod
    def menu():
        print(" Diretoria" "\n"
        " 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir" "\n"
        # " Curso" "\n"
        # " 5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir" "\n"
        # " Professor" "\n"
        # " 9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir" "\n"
        "13 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():

        op = 0
        
        while op != 13:
            op = UI.menu()

            if op == 1: UI.inserir_diretoria()
            if op == 2: UI.listar_diretoria()
            if op == 3: UI.atualizar_diretoria()
            if op == 4: UI.excluir_diretoria()
            if op == 5: UI.inserir_curso()
            if op == 6: UI.listar_curso()
            if op == 7: UI.atualizar_curso()
            if op == 8: UI.excluir_curso()
            if op == 9: UI.inserir_professor()
            if op == 10: UI.listar_professor()
            if op == 11: UI.atualizar_professor()
            if op == 12: UI.excluir_professor()
    
    def inserir_diretoria():
        nome = input("Insira nome da diretoria: ")
        finalidade = input("Insira a finalidade da diretoria: ")
        telefone = input("Insira o telefone da diretoria: ")
        email = input("Insira o email da diretoria: ")
        View.inserir_diretoria(nome, finalidade, telefone, email)

    def listar_diretoria():
        View.listar_diretoria()

    def atualizar_diretoria():
        View.listar_diretoria()
        id = int(input("Informe o id do diretoria a ser atualizada: "))
        nome = input("Insira nome da diretoria: ")
        finalidade = input("Insira a finalidade da diretoria: ")
        telefone = input("Insira o telefone da diretoria: ")
        email = input("Insira o email da diretoria: ")
        View.atualizar_diretoria(id, nome, finalidade, telefone, email)

    def excluir_diretoria():
        View.listar_diretoria
        id = int(input("Informe o id da diretoria a ser excluído: "))
        View.excluir_diretoria(id)

UI.main()