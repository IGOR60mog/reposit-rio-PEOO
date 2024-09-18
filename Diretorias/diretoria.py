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
            if c.id == id: return c
        return None  

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.diretorias

    @classmethod
    def atualizar (cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c = diretoria(obj.id, obj.nome, obj.finalidade, obj.telefone, obj.email)
            print(cls.diretorias)
            cls.salvar() 

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



