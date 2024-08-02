#CLASSE DO CIRCULO

class circulo:  #modelo de objeto

  def __init__(self):  #método construtor
    self.raio = 0  #atributo encapsulado: não pode ser acessado fora da classe

  def calc_area(self):
    return 3.14 * self.raio**2

  def calc_circunferencia(self):
    return 2 * 3.14 * self.raio


x = circulo()  #objeto
x.raio = int(input("Digite o raio em metros do círculo: "))
print(f"A área calculada é de {x.calc_area()} metros")
print (f"A circunferência calculada é de {x.calc_circunferencia()} metros")