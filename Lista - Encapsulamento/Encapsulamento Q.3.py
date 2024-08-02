class conta:

  def __init__(self):
    self.__titular = ""
    self.__conta = 0
    self.__saldo = 0

  def set_titular(self, v):
    if v != "":
      self.__titular = v
    else:
      raise ValueError()

  def set_conta(self, v):
    if v > 0:
      self.__conta = v
    else:
      raise ValueError()

  def set_saldo(self, v):
    if v > 0:
      self.__saldo = v
    else:
      raise ValueError()

  def get_titular(self):
    return self.__titular

  def get_conta(self):
    return self.__conta

  def get_saldo(self):
    return self.__saldo

  def deposito(self, v):
    if v > 0:
      self.__saldo += v
    else:
      raise ValueError()

  def saque(self, v):
    if v <= self.__saldo:
      self.__saldo -= v
    else:
      raise ValueError()


x = conta()
x.set_titular("IGOR")
x.set_conta(456776785356783)
x.set_saldo(3000)

print(x.get_titular())
print(x.get_conta())
print(x.get_saldo())
x.deposito(500)
print(x.get_saldo())
x.saque(1000)
print(x.get_saldo())
