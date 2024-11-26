# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
    self.__senha = senha

    if nome == "": raise ValueError("Nome não pode ser vazio")
    if email == "": raise ValueError("Email não pode ser vazio")
    if fone == "": raise ValueError("Fone não pode ser vazio")
    if senha == "": raise ValueError("Senha não pode ser vazio")
    
  def set_id(self, id):
    if id > 0: self.__id = id
    else: raise ValueError("Id não pode ser 0")
  def set_nome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError("Nome não pode ser vazio")
  def set_email(self, email):
    if email != "": self.__email = email
    else: raise ValueError("Email não pode ser vazio")
  def set_fone(self, fone):
    if fone != "": self.__fone = fone
    else: raise ValueError("Fone não pode ser vazio")
  def set_senha(self, senha):
    if senha != "": self.__senha = senha
    else: raise ValueError("Senha não pode ser vazio")


  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def get_senha(self): return self.__senha

  def __str__(self):
    return f"{self.__nome} - {self.__email} - {self.__fone}"

# Persistência
class Clientes:
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
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.email = obj.email
      c.fone = obj.fone
      c.senha = obj.senha
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda cliente: cliente.get_nome())
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"], obj["_Cliente__senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

