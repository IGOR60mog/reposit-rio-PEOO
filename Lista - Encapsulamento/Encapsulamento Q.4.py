class entrada:

  def __init__(self):
    self.__dia = ""
    self.__hora = 0
    self.__meia = ''

  def set_dia(self, v):
    lista = [
        "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"
    ]
    for x in lista:
      if v == x:
        self.__dia = v
    if v == "":
      raise ValueError()

  def set_hora(self, v):
    if v > 0 and v < 24:
      self.__hora = v
    else:
      raise ValueError()

  def set_meia(self, v):
    if v != 'sim':
      raise ValueError()
    else:
      self.__meia = v

  def get_dia(self):
    return self.__dia

  def get_hora(self):
    return self.__hora

  def get_meia(self):
    return self.__meia

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
x.set_dia("segunda")
x.set_hora(18)
x.set_meia("sim")

print(x.get_dia())
print(x.get_hora())
print(x.get_meia())

print(x.valor())
