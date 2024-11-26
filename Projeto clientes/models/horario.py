import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__confirmado = False
        self.__id_cliente = None
        self.__id_servico = 0

    def set_id(self, id):
      if id > 0: self.__id = id
      else: raise ValueError("Id tem que ser maior que 0")

    def set_data(self, data):
      if data != datetime.now(): self.__data = data
      else: raise ValueError("data não pode ser agora")

    def set_confirmado(self, confirmado):
      if confirmado != False: self.__confirmado = confirmado
      else: raise ValueError("confirmado não pode ser falso")

    def set_id_cliente(self, id_cliente):
      if id_cliente > 0: self.__id_cliente = id_cliente
      else: raise ValueError("Id cliente tem que ser maior que 0")

    def set_id_servico(self, id_servico):
      if id_servico > 0: self.__id_servico = id_servico
      else: raise ValueError("Id serviço tem que ser maior que 0")


    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def __str__(self):
        return f"{self.__id} - {self.__data}"
    def to_json(self):
      dic = {}
      dic["id"] = self.__id
      dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M")
      dic["confirmado"] = self.__confirmado
      dic["id_cliente"] = self.__id_cliente
      dic["id_servico"] = self.__id_servico
      return dic    

class Horarios:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.get_id() > m: m = c.get_id()
    obj.set_id(m + 1)
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.get_id() == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.set_data(obj.get_data())
      c.set_confirmado(obj.get_confirmado)
      c.set_id_cliente(obj.get_id_cliente)
      c.set_id_servico(obj.get_id_servico)
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
          c.set_confirmado(obj["confirmado"])
          c.set_id_cliente(obj["id_cliente"])
          c.set_id_servico(obj["id_servico"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass



