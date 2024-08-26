from datetime import datetime, timedelta
from objetos import Cliente, Horario, Servico
import json


class Clientes:
  
  objetos = []    # atributo estático

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
      cls.objetos[x] = Cliente(obj.get_id(), obj.get_nome(), obj.get_email(), obj.get_fone())
      cls.salvar() #write

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()  #write
  
  @classmethod 
  def abrir(cls):
    with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        cls.objetos = []
    for obj in texto:   
        c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"])
        cls.objetos.append(c)

  @classmethod 
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
        json.dump(cls.objetos, arquivo, default = vars)

class Horarios:
  
  objetos = []    # atributo estático

  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.__id > m: m = c.id
    obj.id = m + 1
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
      if c.id == id: return c
    return None 

  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.id = obj.nome
      c.data = obj.email
      c.fone = obj.fone
      cls.salvar() #write

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()  #write
  
  @classmethod 
  def abrir(cls):
    with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
    for obj in texto:   
        c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
        cls.objetos.append(c)

  @classmethod 
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:   # w - write
        json.dump(cls.objetos, arquivo, default = vars)
  
  objetos = []    # atributo estático

  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.__id > m: m = c.__id
    obj.__id = m + 1
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
      if c.id == id: return c
    return None  

  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.__id)
    if c != None:
      c.__id = obj.__id
      c.__data = obj.__data
      c.__confirmado = obj.__fone
      c.__idCliente = obj.__idCliente
      c.__idservico = obj.__idServico
      cls.salvar() #write

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()  #write
  
  @classmethod 
  def abrir(cls):
    with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
    for obj in texto:   
        c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
        cls.objetos.append(c)

  @classmethod 
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
        json.dump(cls.objetos, arquivo, default = vars)          
