class Equacao:
    def __init__ (self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def delta (self):
        return self.__b**2 - 4*self.__a*self.__c
    
    def TemRaizesReais(self):
        if self.delta() >= 0:
            return True
        else:
            return False
    def Raiz1 (self):
        raiz = (-self.__b + self.delta()**0.5)/(2*self.__a)
        return raiz
    
    def Raiz2 (self):
        raiz = (-self.__b - self.delta()**0.5)/(2*self.__a)
        return raiz
    
    def __str__(self):
        return f"y = {self.__a}x² + {self.__b}x + {self.__c}"
    


    