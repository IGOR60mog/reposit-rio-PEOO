#CLASSE DO CIRCULO

class circulo:  #modelo de objeto

  def __init__(self):  #método construtor
    self.__raio = 0  #atributo encapsulado: não pode ser acessado fora da classe

  def set_raio(self, v):  #método
    if v > 0:
      self.__raio = v
    else:
      raise ValueError()

  def get_raio(self):
    return self.__raio

  def calc_area(self):
    return 3.14 * self.__raio**2

  def calc_circunferencia(self):
    return 2 * 3.14 * self.__raio


x = circulo()  #objeto
x.set_raio(2)
print(x.get_raio())
print(x.calc_area())
print(x.calc_circunferencia())
x = x