import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        
        if nome == "": raise ValueError()
        if email == "": raise ValueError()
        if fone == "": raise ValueError()
    
    def set_id(self, obj):  
        if obj != 0: self.__id = obj
    def get_id(self): return self.__id

    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
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


class View:
   
   @staticmethod
   def cliente_listar():
      return Clientes.listar()
      
   
   @staticmethod
   def cliente_inserir(nome, email, fone):
      x = Cliente(0, nome, email, fone)
      Clientes.inserir(Clientes, x)
      
   
   @staticmethod
   def cliente_atualizar(id, nome, email, fone):
        x = Cliente(id, nome, email, fone)
        Clientes.atualizar(x)
      
   
   @staticmethod
   def cliente_excluir(id):
        c = Cliente(id, "n", "e", "f")
        Clientes.excluir(c)      
    