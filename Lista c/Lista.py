class Agua:
    def __init__ (self):
        self.__mes = 0 
        self.__ano = 0 
        self.__consumo = 0 #m³

        def set_tempo(self, tempo):
            t = tempo.split("/")
            self.__mes = int(t[0])
            self.__ano = int(t[1])
        
            if self.__mes < 0 or self.__ano > 12 or self.__ano < 2000 or self.__ano >= 2024:
                raise ValueError("Mês e ano errado")
        
        def set_consumo(self, v):
            if v > 0:
                v = self.__consumo
            else: raise ValueError("Mês e ano errado")

        def valor(self):
            valor = 38
            if self.__consumo > 20:
                valor += (self.__consumo - 20)*6
            elif self.__consumo > 10 and self.consumo <= 20:
                valor += (self.__consumo - 10) * 5
            else:
                raise ValueError()
                return valor
    
        def get_tempo(self):
            return f"{self.__mes}/{self.__ano}"
        
        def get_consumo(self):
            return self.__consumo
        
        def get_mes(self):
            return self.__mes
        
        def get_ano(self):
            return self.__ano




class UI:
    @staticmethod
    def main():
        x = Agua()



UI.main()
