from datetime import datetime, timedelta
from objetos import Cliente, Horario, Servico
from ClassesEstaticas import Clientes, Horarios, Servicos
import json


class UI:
  @staticmethod
  def menu():
    print("1 - Inserir cliente, 2 - Listar clientes, 3 - atualizar cliente, 4 - excluir cliente" "\n" 
          "5 - Inserir Horario, 6 - Listar Horario, 7 - atualizar horario, 8 - excluir horario" "\n" 
          "9 - Inserir Serviço, 10 - Listar Serviços, 11 - atualizar serviços, 12 - excluir serviços" "\n"   
          "                                     13 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 13:
      op = UI.menu()
      if op == 1: UI.cliente_inserir()
      if op == 2: UI.cliente_listar()
      if op == 3: UI.cliente_atualizar()
      if op == 4: UI.cliente_excluir()
      if op == 5: UI.servico_inserir()
      if op == 6: UI.servico_listar()
      if op == 7: UI.servico_atualizar()
      if op == 8: UI.servico_excluir()
      if op == 9: UI.horario_inserir()
      if op == 10: UI.horario_listar()
      if op == 11: UI.horario_atualizar()
      if op == 12: UI.horario_excluir()    

#1
  @staticmethod
  def cliente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    x = Cliente(0, nome, email, fone)
    Clientes.inserir(Clientes, x)

#2
  @staticmethod
  def cliente_listar():  
    for c in Clientes.listar():
      print(c)

#3
  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

#4
  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    c = Cliente(id, "qual", "quer", "coisa")
    Clientes.excluir(c)

#5
  @staticmethod
  def servico_inserir():
    descricao = input("Informe a descrição do serviço: ")
    valor = int(input("Informe o valor do serviço em reais: "))
    duracao = int(input("Informe a duração do serviço em minutos: "))
    s = Servico(0, descricao, valor, duracao)
    Servicos.inserir(s)

 #6
  @staticmethod
  def servico_listar():  
    for c in Servicos.listar():
      print(c)

#7
  @staticmethod
  def servico_atualizar():
    UI.servico_listar()
    id = int(input("Informe o id do serviço a ser atualizado: "))
    descricao = input("Informe a descrição do serviço: ")
    valor = int(input("Informe o valor do serviço em reais: "))
    duracao = int(input("Informe a duração do serviço em minutos: "))
    c = Servico(id, descricao, valor, duracao)
    Servicos.atualizar(c)

#8
  @staticmethod
  def servico_excluir():
    UI.servico_listar()
    id = int(input("Informe o id do serviço a ser excluído: "))
    c = Servico(id, "qual", "quer", "coisa")
    Servicos.excluir(c)

#9
  @staticmethod
  def horario_inserir():
    print("Horário só pode ser inserido após a adição de um cliente e um serviço")
    data = datetime.strptime(input("Informe a data dd/mm/aaa: "), "%d/%m/%Y")
    SN = input("Informe a confirmação S/N: ")
    if SN == "S":
      confirmado = True
    else:
      confirmado = False
    x = Horario(0, data, confirmado, "", "")
    Horarios.inserir(Horarios, x)

UI.main()