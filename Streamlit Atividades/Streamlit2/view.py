from Modelos.Clientes import *
from Modelos.Horarios import *
from Modelos.Servicos import *
from datetime import datetime

class View:
   
   @staticmethod
   def cliente_listar():
      return Clientes.listar()
      
   
   @staticmethod
   def cliente_inserir(nome, email, fone):
      c = Cliente(0, nome, email, fone)
      for x in Clientes.listar():
          if x.get_email() == c.get_email():
              raise ValueError("Mesmo Email")
          else:
            Clientes.inserir(Clientes, x)
      
   
   @staticmethod
   def cliente_atualizar(id, nome, email, fone):
        x = Cliente(id, nome, email, fone)
        Clientes.atualizar(x)
      
   
   @staticmethod
   def cliente_excluir(id):
        c = Cliente(id, "n", "e", "f")
        Clientes.excluir(c)     

   @staticmethod
   def horario_listar():
      return Horarios.listar()
      
   
   @staticmethod
   def horario_inserir(data, confirmacao, idCliente, idServico):
      x = Horario(0, data, confirmacao, idCliente, idServico)
      Horarios.inserir(x)
      
   
   @staticmethod
   def horario_atualizar(id, data, confirmacao, idCliente, idServico):
        x = Horario(id, data, confirmacao, idCliente, idServico)
        Horarios.atualizar(x)
      
   
   @staticmethod
   def horario_excluir(id):
        c = Horario(id, "d", "c", "c", "s")
        Horarios.excluir(c)     

   @staticmethod
   def servico_listar():
      return Servicos.listar()
      
   
   @staticmethod
   def servico_inserir(desc, v, d):
      x = Servico(0, desc, v, d)
      Servicos.inserir(x)
      
   
   @staticmethod
   def servico_atualizar(id, desc, v, d):
        x = Servico(id, desc, v, d)
        Servicos.atualizar(x)
      
   
   @staticmethod
   def servico_excluir(id):
        c = Servico(id, "n", "e", "f")
        Servicos.excluir(c)    