from datetime import datetime
from datetime import timedelta
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

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
class Horario:

    def __init__(self, id, data, confirmado, idCliente, idServico):
        self.__id = id
        self.__data = data
        self.__confirmado = confirmado
        self.__idCliente = idCliente
        self.__idServico = idServico

        if data == datetime(1, 1, 1): ValueError()
        if confirmado == False: raise ValueError()
        if idCliente == 0: ValueError()
        if idServico == 0: ValueError()

    def __str__ (self):
        return f"{self.__id} - {self.__data}"

class Servico:

    def __init__ (self, id, descricao, valor, duracao):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        self.__duracao = duracao

        if descricao == "": raise ValueError()
        if valor == 0: raise ValueError()
        if duracao == 0: raise ValueError()
    def __str__(self):
       return f"{self.__id} - {self.__descricao} - {self.__valor} - {self.__duracao}"
