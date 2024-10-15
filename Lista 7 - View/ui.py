from view import View

class UI:
    @staticmethod
    def menu():
        print(" Diretoria" "\n"
        " 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir" "\n"
        " Curso" "\n"
        " 5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir" "\n"
        " Professor" "\n"
        " 9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir" "\n"
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

    def inserir_curso():
        nome = input("Insira o nome do curso: ")
        descricao = input("Insira a descrição do curso: ")
        presencial = input("O curso é presencial (S/N)? ")
        if presencial == "S":
            modalidade = True
        else:
            modalidade = False
        ch = int(input("Insira a carga horária do curso em horas: "))
        View.listar_diretoria()
        idD = int(input("Insira o id da diretoria que o curso pertence: "))
        View.inserir_curso(idD, nome, descricao, modalidade, ch)

    def listar_curso():
        View.listar_curso()

    def atualizar_curso():
        View.listar_curso()
        id = int(input("Informe o id do curso a ser atualizado: "))
        nome = input("Insira o nome do curso: ")
        descricao = input("Insira a descrição do curso: ")
        presencial = input("O curso é presencial (S/N)? ")
        if presencial == "S":
            modalidade = True
        else:
            modalidade = False
        ch = int(input("Insira a carga horária do curso em horas: "))
        View.listar_diretoria()
        idD = int(input("Insira o id da diretoria que o curso pertence: "))
        View.atualizar_curso(id, idD, nome, descricao, modalidade, ch)

    def excluir_curso():
        View.listar_curso()
        id = int(input("Informe o id do curso a ser excluído: "))
        View.excluir_curso(id)

    def inserir_professor():
        nome = input("Insira o nome do professor: ")
        matricula = input("Insira a matrícula do professor: ")
        graduacao = input("Insira a graduação do professor: ")
        telefone = input("Insira o número do professor: ")
        View.listar_diretoria()
        idD = int(input("Insira o id da diretoria que o professor pertence: "))
        View.inserir_professor(idD, nome, matricula, graduacao, telefone)

    def listar_professor():
        View.listar_professor()

    def atualizar_professor():
        View.listar_professor()
        id = int(input("Informe o id do professor a ser atualizado: "))
        nome = input("Insira o nome do professor: ")
        matricula = input("Insira a matrícula do professor: ")
        graduacao = input("Insira a graduação do professor: ")
        telefone = input("Insira o número do professor: ")
        View.listar_diretoria()
        idD = int(input("Insira o id da diretoria que o professor pertence: "))
        View.atualizar_professor(id, idD, nome, matricula, graduacao, telefone)

    def excluir_professor():
        View.listar_professor()
        id = int(input("Informe o id do professor a ser excluído: "))
        View.excluir_professor(id)

UI.main()