import json
from crud import CRUD

# Modelo
class Profissional:
  def __init__(self, id, nome, esp, cons):
    self.id = id
    self.nome = nome
    self.especialidade = esp
    self.conselho = cons

  def __str__(self):
    return f"{self.id} - {self.nome} - {self.especialidade}"

# Persistência
class Profissionais(CRUD):
  objetos = []    # atributo estático

  @classmethod
  def salvar(cls):
    with open("profissionais.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("profissionais.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Profissional(obj["id"], obj["nome"], obj["especialidade"], obj["conselho"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass