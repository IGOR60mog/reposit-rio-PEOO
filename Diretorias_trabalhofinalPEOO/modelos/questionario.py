import json
from crud import *


class Questionario:
    def __init__(self,id, idU, d, p):
        self.__id = id
        self.__id_usuario = idU
        self.__data = d
        self.__pontos = p

    def set_id(self, id):
      self.__id = id

    def to_json(self):
       dic = {}
       dic["id"] = self.__id
       dic["id_pergunta"] = self.__id_pergunta
       dic["id_questionario"] = self.__id_questionario
       dic["resposta"] = self.__resposta
       return dic
    
    def __str__(self):
        return f"id - {self.__id}, usuario - {self.__id_usuario} data - {self.__data} - pontos {self.__pontos}"
    
class Questionarios (CRUD):
  @classmethod
  def salvar(cls):
    with open("questionarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Questionario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("questionarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Questionario(obj["id"], obj["id_usuario"], obj["data"], obj["pontos"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass   