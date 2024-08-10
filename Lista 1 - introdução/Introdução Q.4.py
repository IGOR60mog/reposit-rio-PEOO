class entrada:

  def __init__(self):
    self.__dia = ""
    self.__hora = 0
    self.__meia = ''

  
  def valor(self):
    lista = [
        "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"
    ]
    valor = 0
    for x in range(0, len(lista)):
      if x == 0 or x == 1 or x == 3:
        if self.__dia == lista[x]:
          if self.__hora >= 17:
            valor = 24
          else:
            valor = 16
      elif x == 2:
        if self.__dia == lista[x]:
          valor = 8
      else:
        if self.__dia == lista[x]:
          if self.__hora >= 17:
            valor = 30
          else:
            valor = 20
    if self.__meia == 'sim':
      valor /= 2
    return valor


x = entrada()
x.dia = input("Digite o dia da semana: ")
x.hora = input("Digite o horário: ")
x.meia = input("Digite se teu ingresso é meia: ")

print(f"O dia da semana é {x.dia()}")
print(f"A hora é {x.hora()}")
print(f"Sua ingresso {x.meia()} é meia")

print(f"O valor do ingresso é de {x.valor()} reais")
