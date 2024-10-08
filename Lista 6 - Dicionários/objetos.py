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
    
    def set_id(self, obj):  
        if obj != 0: self.__id = obj
    def get_id(self): return self.__id

    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
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

        def set_id(self, obj):  
            if obj != 0: self.__id = obj
        def get_id(self): return self.__id        
        def get_data(self): return self.__data
        def get_confirmado(self): return self.__confirmado
        def set_idCliente(self, id): 
            if id != 0: self.__idCliente = id
        def get_idCliente(self): return self.__idCliente

        def set_idCliente(self, id): 
            if id != 0: self.__idCliente = id
        def get_idServico(self): return self.__idServico

    def __str__ (self):
        return f"{self.__id} - Data: {self.__data} - Confirmado: {self.__confirmado}"

class Servico:

    def __init__ (self, id, descricao, valor, duracao):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        self.__duracao = duracao

        if descricao == "": raise ValueError()
        if valor == 0: raise ValueError()
        if duracao == 0: raise ValueError()

    def set_id(self, obj):  
        if obj != 0: 
            self.__id = obj
    def get_id(self): 
        return self.__id 
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor
    def get_duracao(self): return self.__duracao


    def __str__(self):
       return f"{self.__id} - {self.__descricao} - {self.__valor} reais - {self.__duracao} minutos"
