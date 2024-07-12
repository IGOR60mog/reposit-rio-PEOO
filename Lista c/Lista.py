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

        def get_tempo
            return 
        def get_consumo(self):
            return self.__consumo
        