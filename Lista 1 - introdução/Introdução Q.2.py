class viagem:

  def __init__(self):
    self.distancia = 0  #m
    self.tempo = 0      #s

  def velocidade(self):
    return self.distancia / self.tempo


x = viagem()
x.distancia = int(input("Digite a distância em metros: "))
x.tempo = int(input("Digite o tempo em segundos"))
print(f"A velocidade calculada é de {x.velocidade()} m/s")