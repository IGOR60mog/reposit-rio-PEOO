from datetime import datetime, timedelta
from objetos import Cliente, Horario, Servico
from ClassesEstaticas import Clientes, Horarios
import json


class UI:
  @staticmethod
  def menu():
    print("1 - Cliente, 2 - Horario, 3 - servico")

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
      if op == 5: UI.horario_inserir()
      if op == 6: UI.horario_listar()
      if op == 7: UI.horario_atualizar()
      if op == 8: UI.horario_excluir()
      if op == 9: UI.servico_inserir()
      if op == 10: UI.servico_listar()
      if op == 11: UI.servico_atualizar()
      if op == 12: UI.servico_excluir()

  @staticmethod
  def cliente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    x = Cliente(0, nome, email, fone)
    Clientes.inserir(Clientes, x)

  @staticmethod
  def cliente_listar():  
    for c in Clientes.listar():
      print(c)

  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    c = Cliente(id, "qual", "quer", "coisa")
    Clientes.excluir(c)


#5
  @staticmethod
  def horario_inserir():
    data = input("Informe a data dd/mm/aaa: ")
    SN = input("Informe a confirmação S/N: ")
    if SN == "S":
      confirmado = True
    else:
      confirmado = False
    x = Horario(0, data, confirmado, "", "")
    Horarios.inserir(Horarios, x)

#9
  @staticmethod
  def servico_inserir():
    descricao = input("Informe a data dd/mm/aaa: ")
    valor = int(input("Informe o valor: "))
    duracao = int(input("Informe a duracao: "))
    x = Servico(0, descricao, valor, duracao)
    Servicos.inserir(Servicos, x)
UI.main()




