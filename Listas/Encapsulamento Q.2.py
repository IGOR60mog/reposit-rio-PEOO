class viagem:

  def __init__(self):
    self.__distancia = 0
    self.__tempo = 0

  def set_distancia(self, v):
    if v > 0:
      self.__distancia = v
    else:
      raise ValueError(self, v)

  def set_tempo(self, v):
    if v > 0:
      self.__tempo = v
    else:
      raise ValueError()

  def get_distancia(self):
    return self.__distancia

  def get_tempo(self):
    return self.__tempo

  def velocidade(self):
    return self.__distancia / self.__tempo


x = viagem()
x.set_distancia(100)
x.set_tempo(2)
print(x.get_distancia())
print(x.get_tempo())
print(x.velocidade())