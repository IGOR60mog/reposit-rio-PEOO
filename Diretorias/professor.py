import json

class professor:

    def __init__ (self, id, idD, n, m, g, t):
        self.id = id
        self.idDiretoria = idD
        self.nome = n
        self.matricula = m
        self.graduacao = g
        self.telefone = t

        if n == "": raise ValueError()
        if m == "": raise ValueError()
        if g == "": raise ValueError()
        if t == "": raise ValueError()

    def __str__ (self):
        return f"{self.id} - {self.nome} - {self.matricula} - {self.graduacao}"

class professores:

    professores = []

    @classmethod
    def inserir (cls, obj):
        if cls.professores != []:
            cls.abrir()
            m = 0
            for c in cls.professores:
                if c.id > m: m = c.id
                x = m + 1
                obj.id = x
        else:
            obj.id = 1
        cls.professores.append(obj)
        cls.salvar()

    @classmethod
    def listar_id (cls, id):
        cls.abrir()   
        for c in cls.professores:
            if c.id == id: return c
        return None  

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.professores

    @classmethod
    def atualizar (cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            x = cls.professores.index(c)
            cls.professores[x] = professor(obj.id, obj.idDiretoria, obj.nome, obj.matricula, obj.graduacao, obj.telefone)
            cls.salvar()

    @classmethod
    def excluir (cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.professores.remove(c)
            cls.salvar()  

    @classmethod 
    def abrir(cls):
        with open("professores.json", mode="r") as arquivo:   
            texto = json.load(arquivo)
            cls.professores = []
        for obj in texto:   
            p = professor(obj["id"], obj["idDiretoria"], obj["nome"], obj["matricula"], obj["graduacao"], obj["telefone"])
            cls.professores.append(p)

    @classmethod 
    def salvar(cls):
        with open("professores.json", mode="w") as arquivo: 
            json.dump(cls.professores, arquivo, default = vars)
