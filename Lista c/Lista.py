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




class Ingresso:
    def _init_(self):
        self.__dia = '' #dia da semana
        self.__horario = 0 #hora

    def set_dia(self, v):
        lista = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        if v in lista:
                self.__dia = v
        else:
            raise ValueError("Dia incorreto")
        
    def get_dia(self, v):
        return self.__dia

    def set_horario(self, v):
        if v >= 0 and v < 24:
            self.__horario = v
        else:
            raise ValueError("Dia incorreto")

    def get_horario(self, v):
        return self.__horario

    def valor(self):
        valor = 0
        


dia = input('dia: ').upper()
horario = input('horario: ')
entrada = Ingresso(dia, horario)

print(entrada.valor())


class UI:
    @staticmethod
    def main():
        x = Agua()



UI.main()
