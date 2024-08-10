import random

class bingo:


    def __init__(self):
        self.__numbolas = 0
        self.__sorteados = []

    
        
    def iniciar(self, x):
        if x > 0 and x <= 100:
            self.__numbolas = x
        else:
            raise ValueError()

    def proximo(self):
        valor = random.randrange(1, self.__numbolas+1)
        while valor in self.__sorteados:
            valor = random.randrange(1, self.__numbolas+1)
        self.__sorteados.append(valor)
        
        return valor


    def sorteados(self):
        return self.__sorteados
         

x = bingo()
x.iniciar(5)
print(x.proximo())
print(x.proximo())
print(x.proximo())
print(x.proximo())
print(x.proximo())
print(x.sorteados())