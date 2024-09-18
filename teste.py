import json

class diretoria:

    def __init__ (self, id, n, f, t, e):
        self.id = id
        self.nome = n
        self.finalidade = f
        self.telefone = t
        self.email = e

        if n == "": raise ValueError()
        if f == "": raise ValueError()
        if t == "": raise ValueError()
        if e == "": raise ValueError()

    def __str__ (self):
        return f"{self.id} - {self.nome} - {self.finalidade} - {self.telefone}"

class diretorias:

    diretorias = []

    @classmethod
    def inserir (cls, obj):
        if cls.diretorias != []:
            cls.abrir()
            m = 0
            for c in cls.diretorias:
                if c.id > m: m = c.id
                x = m + 1
                obj.id = x
        else:
            obj.id = 1
        cls.diretorias.append(obj)
        cls.salvar() 

    @classmethod
    def listar_id (cls, id):
        cls.abrir()
        for c in cls.diretorias:
            if c.id == id: 
                return c
        return None  

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.diretorias

    @classmethod
    def atualizar (cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            x = cls.diretorias.index(c)
            cls.diretorias[x] = diretoria(obj.id, obj.nome, obj.finalidade, obj.telefone, obj.email)
            cls.salvar() 
        else:
            raise ValueError("Id não identificado")
    @classmethod
    def excluir (cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.diretorias.remove(c)
            cls.salvar()

    @classmethod 
    def abrir(cls):
        with open("diretorias.json", mode="r") as arquivo:   
            texto = json.load(arquivo)
            cls.diretorias = []
        for obj in texto:   
            d = diretoria(obj["id"], obj["nome"], obj["finalidade"], obj["telefone"], obj["email"])
            cls.diretorias.append(d)

    @classmethod 
    def salvar(cls):
        with open("diretorias.json", mode="w") as arquivo: 
            json.dump(cls.diretorias, arquivo, default = vars)

class curso:

    def __init__ (self, id, idD, n, d, m, c):
        self.id = id
        self.idDiretoria = idD
        self.nome = n
        self.descricao = d
        self.modalidade = m
        self.carga_horaria = c

        if idD == -1: raise ValueError()
        if n == "": raise ValueError()
        if d == "": raise ValueError()
        if m == False: raise ValueError()
        if c == 0: raise ValueError()

    def __str__ (self):
        return f"{self.id} - {self.nome} - {self.descricao} - Presencial: {self.modalidade}"

class cursos:

    cursos = []

    @classmethod
    def inserir (cls, obj):
        if cls.cursos != []:
            cls.abrir()
            m = 0
            for c in cls.cursos:
                if c.id > m: m = c.id
                x = m + 1
                obj.id = x
        else:
            obj.id = 1
        cls.cursos.append(obj)
        cls.salvar() 

    @classmethod
    def listar_id (cls, id):
        cls.abrir()   
        for c in cls.cursos:
            if c.id == id: return c
        return None  

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.cursos

    @classmethod
    def atualizar (cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            x = cls.cursos.index(c)
            cls.cursos[x] = curso(obj.id, obj.idDiretoria, obj.nome, obj.descricao, obj.modalidade, obj.carga_horaria)
            cls.salvar() 

    @classmethod
    def excluir (cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.cursos.remove(c)
            cls.salvar()  

    @classmethod 
    def abrir(cls):
        with open("cursos.json", mode="r") as arquivo:   
            texto = json.load(arquivo)
            cls.cursos = []
        for obj in texto:   
            d = curso(obj["id"], obj["idDiretoria"], obj["nome"],  obj["descricao"], obj["modalidade"], obj["carga_horaria"])
            cls.cursos.append(d)

    @classmethod 
    def salvar(cls):
        with open("cursos.json", mode="w") as arquivo: 
            json.dump(cls.cursos, arquivo, default = vars)
    

class View:

    @staticmethod
    def inserir_diretoria(nome, finalidade, telefone, email):
        x = diretoria(0, nome, finalidade, telefone, email)
        diretorias.inserir(x)

    @staticmethod
    def listar_diretoria():
        return diretorias.listar()
    
    @staticmethod
    def atualizar_diretoria(id, nome, finalidade, telefone, email):
        x = diretoria(id, nome, finalidade, telefone, email)
        diretorias.atualizar(x)

    @staticmethod
    def excluir_diretoria(id):
        d = diretoria(id, "n", "f", "t", "e")
        diretorias.excluir(d)

    #CURSOS

    @staticmethod
    def inserir_curso(idD, nome, descricao, modalidade, ch):
        x = curso(0, idD, nome, descricao, modalidade, ch)
        cursos.inserir(x)

    @staticmethod
    def listar_curso():
        return cursos.listar()

    @staticmethod
    def atualizar_curso(id, idD, nome, descricao, modalidade, ch):
        x = curso(id, idD, nome, descricao, modalidade, ch)
        cursos.atualizar(x)

    @staticmethod
    def excluir_curso(id):
        c = curso(id, "idD", "n", "d", "m", "c")
        cursos.excluir(c)

class UI:
    @staticmethod
    def menu():
        print(" Diretoria" "\n"
        " 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir" "\n"
        " Curso" "\n"
        " 5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir" "\n"
        # " Professor" "\n"
        # " 9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir" "\n"
        "9 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():

        op = 0
        
        while op != 9:
            op = UI.menu()

            if op == 1: UI.inserir_diretoria()
            if op == 2: UI.listar_diretoria()
            if op == 3: UI.atualizar_diretoria()
            if op == 4: UI.excluir_diretoria()
            if op == 5: UI.inserir_curso()
            if op == 6: UI.listar_curso()
            if op == 7: UI.atualizar_curso()
            if op == 8: UI.excluir_curso()

    def inserir_diretoria():
        nome = input("Insira nome da diretoria: ")
        finalidade = input("Insira a finalidade da diretoria: ")
        telefone = input("Insira o telefone da diretoria: ")
        email = input("Insira o email da diretoria: ")
        View.inserir_diretoria(nome, finalidade, telefone, email)

    def listar_diretoria():
        for x in View.listar_diretoria():
            print(x)

    def atualizar_diretoria():
        UI.listar_diretoria()
        id = int(input("Informe o id do diretoria a ser atualizada: "))
        nome = input("Insira nome da diretoria: ")
        finalidade = input("Insira a finalidade da diretoria: ")
        telefone = input("Insira o telefone da diretoria: ")
        email = input("Insira o email da diretoria: ")
        View.atualizar_diretoria(id, nome, finalidade, telefone, email)

    def excluir_diretoria():
        UI.listar_diretoria()
        id = int(input("Informe o id da diretoria a ser excluído: "))
        View.excluir_diretoria(id)


    #Curso

    def inserir_curso():
        nome = input("Insira o nome do curso: ")
        descricao = input("Insira a descrição do curso: ")
        presencial = input("O curso é presencial (S/N)? ")
        if presencial == "S":
            modalidade = True
        else:
            modalidade = False
        ch = int(input("Insira a carga horária do curso em horas: "))
        UI.listar_diretoria()
        idD = int(input("Insira o id da diretoria que o curso pertence: "))
        View.inserir_curso(idD, nome, descricao, modalidade, ch)

    def listar_curso():
        for x in View.listar_curso():
         print(x)

    def atualizar_curso():
        UI.listar_curso()
        id = int(input("Informe o id do curso a ser atualizado: "))
        nome = input("Insira o nome do curso: ")
        descricao = input("Insira a descrição do curso: ")
        presencial = input("O curso é presencial (S/N)? ")
        if presencial == "S":
            modalidade = True
        else:
            modalidade = False
        ch = int(input("Insira a carga horária do curso em horas: "))
        UI.listar_diretoria()
        idD = int(input("Insira o id da diretoria que o curso pertence: "))
        View.atualizar_curso(id, idD, nome, descricao, modalidade, ch)

    def excluir_curso():
        UI.listar_curso()
        id = int(input("Informe o id do curso a ser excluído: "))
        View.excluir_curso(id)
    
UI.main()


