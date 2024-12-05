import json
from crud import *


class Diretoria:
    def __init__(self, id, n, f, e):
        self.__id = id
        self.__nome = n
        self.__finalidade = f
        self.__email = e

    def set_id(self, id):
      self.__id = id    
    def __str__(self):
        return f"id - {self.__id}, nome - {self.__nome}, finalidade - {self.__finalidade}, email - {self.__email}"
    
class Diretorias (CRUD):
  @classmethod
  def salvar(cls):
    with open("Diretorias.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("Diretorias.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Diretoria(obj["id"], obj["nome"], obj["finalidade"], obj["email"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass   