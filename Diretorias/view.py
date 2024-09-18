from diretoria import diretoria, diretorias
from curso import curso, cursos
from professor import professor, professores

class View:

    @staticmethod
    def inserir_diretoria(nome, finalidade, telefone, email):
        x = diretoria(0, nome, finalidade, telefone, email)
        diretorias.inserir(x)

    @staticmethod
    def listar_diretoria():
        for d in diretorias.listar():
            print(d)
    
    @staticmethod
    def atualizar_diretoria(id, nome, finalidade, telefone, email):
        x = diretoria(id, nome, finalidade, telefone, email)
        diretorias.atualizar(x)

    @staticmethod
    def excluir_diretoria(id):
        d = diretoria(id, "n", "f", "t", "e")
        diretorias.excluir(d)

    @staticmethod
    def inserir_curso(idD, nome, descricao, modalidade, ch):
        x = curso(0, idD, nome, descricao, modalidade, ch)
        cursos.inserir(x)

    @staticmethod
    def listar_curso():
        for c in cursos.listar():
            print(c)

    @staticmethod
    def atualizar_curso(id, idD, nome, descricao, modalidade, ch):
        x = curso(id, idD, nome, descricao, modalidade, ch)
        cursos.atualizar(x)

    @staticmethod
    def excluir_curso(id):
        c = curso(id, "idD", "n", "d", "m", "c")
        cursos.excluir(c)

    @staticmethod
    def inserir_professor(idD, nome, matricula, graduacao, telefone):
        x = professor(0, idD, nome, matricula, graduacao, telefone)
        professores.inserir(x)

    @staticmethod
    def listar_professor():
        for p in professores.listar():
            print(p)

    @staticmethod
    def atualizar_professor(id, idD, nome, matricula, graduacao, telefone):
        x = professor(id, idD, nome, matricula, graduacao, telefone)
        diretorias.atualizar(x)

    @staticmethod
    def excluir_professor(id):
        p = professor(id, "idD","n", "m", "g", "t")
        professores.excluir(p)