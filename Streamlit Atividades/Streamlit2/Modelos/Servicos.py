import json

class Servico:

    def __init__ (self, id, descricao, valor, duracao):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        self.__duracao = duracao

        if descricao == "": raise ValueError()
        if valor == 0: raise ValueError()
        if duracao == 0: raise ValueError()

    def set_id(self, obj):  
        if obj != 0: 
            self.__id = obj
    def get_id(self): 
        return self.__id 
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor
    def get_duracao(self): return self.__duracao


    def __str__(self):
       return f"{self.__id} - {self.__descricao} - {self.__valor} reais - {self.__duracao} horas"

class Servicos:
  
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    if cls.objetos != []:
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.get_id() > m: m = c.get_id()
            x = m + 1
            obj.set_id(x)
    else:
      obj.set_id(1)
    cls.objetos.append(obj)
    cls.salvar()  

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()   #read
    for c in cls.objetos:
      if c.get_id() == id: return c
    return None  

  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      x = cls.objetos.index(c)
      cls.objetos[x] = Servico(obj.get_id(), obj.get_descricao(), obj.get_valor(), obj.get_duracao())
      cls.salvar() #write

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()  #write
  
  @classmethod 
  def abrir(cls):
    with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        cls.objetos = []
    for obj in texto:   
        c = Servico(obj["_Servico__id"], obj["_Servico__descricao"], obj["_Servico__valor"], obj["_Servico__duracao"])
        cls.objetos.append(c)

  @classmethod 
  def salvar(cls):
    with open("servicos.json", mode="w") as arquivo:   # w - write
        json.dump(cls.objetos, arquivo, default = vars)