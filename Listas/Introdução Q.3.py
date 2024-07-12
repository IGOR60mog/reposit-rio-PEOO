class conta:

  def __init__(self):
    self.titular = ""
    self.conta = 0
    self.saldo = 0


  def deposito(self, v):
    if v > 0:
      self.saldo += v
    else:
      raise ValueError()

  def saque(self, v):
    if v <= self.saldo:
      self.saldo -= v
    else:
      raise ValueError()


x = conta()
x.titular = input("Digite o nome de titular: ")
x.conta = int(input("Digite o número da sua conta: "))
x.saldo = int(input("Digite teu saldo: "))

print(f"Olá, {x.titular()}!")
print(f"O número da sua conta é {x.conta()}")
print(f"O saldo da sua é de {x.saldo()}")
x.deposito = int(input("Digite o valor a depositar: "))
print(f"Seu saldo atual é de {x.saldo()} reais")
x.saque = int(input("Digite o valor a sacar: "))
print(f"Seu saldo atual é de {x.saldo()} reais")
