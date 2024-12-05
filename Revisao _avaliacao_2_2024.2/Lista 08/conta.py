import streamlit as st
from abc import ABC, abstractclassmethod

class conta(ABC):
    def __init__ (self, n, c):
        self.__numero = n
        self.__cliente = c
        self.__saldo = 0

    def Versaldo (self):
        return self.__saldo
    
    def Depositar (self, d):
        if d > 0: self.__saldo += d

    @abstractclassmethod
    def Sacar (self, s):
        pass

    def __str__ (self):
        return f"{self.__numero} - {self.__cliente} - {self.__saldo}"
    

class ContaEspecial(conta):
    def __init__ (self, n, c, l):
        super().__init__(n, c)
        self.__limite = l

    def Sacar(self, v)

class ContaComum(conta):
    super().__init__(n, c, s): 

    def Sacar (self)


class Poupanca(conta):
    super().__init__(n, c, s)
    
    def



        