import json

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
    