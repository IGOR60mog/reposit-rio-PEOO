from Modelos.Clientes import *
from Modelos.Horarios import *
from Modelos.Servicos import *
from datetime import datetime, timedelta

class View:
   
   @staticmethod
   def cliente_listar():
      return Clientes.listar()
      
   
   @staticmethod
   def cliente_inserir(nome, email, fone, senha):
      c = Cliente(0, nome, email, fone, senha)
      if Clientes.listar() != []:
         for x in Clientes.listar():
            if x.get_email() == c.get_email():
               raise ValueError("Mesmo Email")
            else:
               Clientes.inserir(Clientes, c)
      else:
          Clientes.inserir(Clientes, c)
      
   
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
   def horario_abrir_agenda (data, hora_inicial, hora_final, intervalos):
       hora_inicial = datetime.strptime(data + " " + hora_inicial, "%d/%m/%Y %H:%M")
       hora_final = datetime.strptime(data + " " + hora_final, "%d/%m/%Y %H:%M")
       intervalos = timedelta(minutes=intervalos)

       while hora_inicial > hora_final:
           View.horario_inserir(hora_inicial)
           hora_inicial += intervalos
   
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