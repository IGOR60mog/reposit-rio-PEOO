import json
from datetime import datetime

class Horario:
    def __init__(self, id, data, confirmacao, idCliente, idServico):
        self.__id = id
        self.__data = data
        self.__confirmacao = confirmacao
        self.__id_Cliente = idCliente
        self.__id_Servico = idServico


    def set_id(self, obj): 
       if obj != 0: 
          self.__id = obj

    def set_data(self, obj):
       if obj != datetime(1, 1, 1): self.__data = obj

    def set_confirmacao(self, obj): 
       if obj == bool: self.__confirmacao = obj

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmacao(self): return self.__confirmacao
    def get_id_Cliente(self): return self.__id_Cliente
    def get_id_Servico(self): return self.__id_Servico

    def __str__(self):
        return f"{self.__id} - {self.__data}"
    def json(self):
      dic = {}
      dic["_Horario__id"] = self.__id
      dic["_Horario__data"] = self.__data.strftime("%d/%m/%Y %H:%M")
      dic["_Horario__confirmacao"] = self.__confirmacao
      dic["_Horario__id_Cliente"] = self.__id_Cliente
      dic["_Horario__id_Servico"] = self.__id_Servico
      return dic    

class Horarios:
  
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
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
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
      cls.objetos[x] = Horario(obj.get_id(), obj.get_data(), obj.get_confirmacao(), obj.get_id_Cliente(), obj.get_id_Servico())
      cls.salvar() #write

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()  #write
  
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.json)

  @classmethod 
  def abrir(cls):
    with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        cls.objetos = []
    for obj in texto:   
        data = datetime.strptime(obj["_Horario__data"], "%d/%m/%Y %H:%M")
        c = Horario(obj["_Horario__id"], data, obj["_Horario__confirmacao"], obj["_Horario__id_Cliente"], obj["_Horario__id_Servico"])
        cls.objetos.append(c)