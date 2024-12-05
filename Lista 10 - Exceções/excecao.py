try:
  a = int(input("Informe o dividendo: "))
  b = int(input("Informe o divisor: "))
  print(a/b)
except ValueError as erro:
  print(type(erro))
  print(erro)
  print(vars(erro))