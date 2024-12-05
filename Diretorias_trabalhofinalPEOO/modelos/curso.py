import json
from crud import *


class Curso:
    def __init__(self,id, idD, n, d, du):
        self.__id = id
        self.__idDiretoria = idD
        self.__nome = n
        self.__descricao = d
        self.__duracao = du

    def set_id(self, id):
      self.__id = id    
    def __str__(self):
        return f"id - {self.__id}, diretoria - {self.__idDiretoria}, nome - {self.__nome}, descricao {self.__descricao}, duração {self.__duracao}"
    
class Cursos (CRUD):
  @classmethod
  def salvar(cls):
    with open("cursos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("cursos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Curso(obj["id"], obj["idDiretoria"], obj["nome"], obj["descricao"], obj["duracao"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass   