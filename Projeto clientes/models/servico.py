import json

# Modelo
class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id = id
    self.__descricao = descricao
    self.__valor = valor
    self.__duracao = duracao

    if descricao == "": raise ValueError("descricao não pode ser vazio")
    if valor <= 0: raise ValueError("valor não pode ser vazio")
    if duracao <= 0: raise ValueError("duracao não pode ser vazio")

  def set_id(self, id):
    if id > 0: self.__id = id
    else: raise ValueError("id não pode ser 0")

  def set_descricao(self, descricao):
    if descricao != "": self.__descricao = descricao
    else: raise ValueError("descricao não pode ser vazio")

  def set_valor(self, valor):
    if valor > 0: self.__valor = valor
    else: raise ValueError("valor tem que ser maior que zero")

  def set_duracao(self, duracao):
    if duracao != "": self.__duracao = duracao
    else: raise ValueError("duração tem que ser maior que zero")

  def get_id(self): return self.__id
  def get_descricao(self): return self.__descricao
  def get_valor(self): return self.__valor
  def get_duracao(self): return self.__duracao

  def __str__(self):
    return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f} - {self.__duracao} min"

# Persistência
class Servicos:
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
    c = cls.listar_id(obj.get_id())
    if c != None:
      c.set_descricao(obj.get_descricao())
      c.set_valor(obj.get_valor())
      c.set_duracao(obj.get_duracao())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Servico(obj["_Servico__id"], obj["_Servico__descricao_"], obj["_Servico__valor_"], obj["_Servico__duracao_"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

