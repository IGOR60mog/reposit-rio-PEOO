from datetime import datetime
import json

class Paciente:

    def __init__ (self, id, n, f, nc):
        self.id = id
        self.nome = n
        self.fone = f
        self.nascimento = nc

    def __str__(self):
        return f" {self.id} - {self.nome} - {self.fone} - {self.nascimento.strftime('%d/%m/%Y')}"

    def to_json(self):
       dic = {}
       dic["id"] = self.id
       dic["nome"] = self.nome
       dic["fone"] = self.fone
       dic["nascimento"] = datetime.strftime(self.nascimento, "%d/%m/%Y")
       return dic
    
class NPaciente:

    Pacientes = []

    @classmethod
    def inserir(cls, p):
        if cls.Pacientes != []:
            cls.abrir()
        m = 0
        for c in cls.Pacientes:
            if c.id > m: m = c.id
            x = m + 1
            p.id = x
        else:
            p.id = 1
            cls.Pacientes.append(p)
            cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.Pacientes

    @classmethod
    def listar_id(cls, id):
        cls.abrir()   #read
        for c in cls.Pacientes:
          if c.id == id: return c
        return None  

    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            x = cls.Pacientes.index(c)
            cls.Pacientes[x] = Paciente(obj.id, obj.nome, obj.fone, obj.nascimento)
            cls.salvar() #write

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
          cls.Pacientes.remove(c)
        cls.salvar()  #write
    
    @classmethod 
    def abrir(cls):
        with open("NPaciente.json", mode="r") as arquivo:   # r - read
            texto = json.load(arquivo)
            cls.Pacientes = []
        for obj in texto:   
            c = Paciente(obj["id"], obj["nome"], obj["fone"], datetime.strptime(obj["nascimento"], "%d/%m/%Y"))
            cls.Pacientes.append(c)

    @classmethod 
    def salvar(cls):
        with open("NPaciente.json", mode="w") as arquivo:   # w - write
          json.dump(cls.Pacientes, arquivo, default = Paciente.to_json )
    
    @classmethod
    def aniversariante(cls, mes):
       niver = []
       for x in cls.Pacientes:
          if x.nascimento.month == mes:
             niver.append(x)
       return x
       

class UI:
  @staticmethod
  def menu():
    print("1 - Inserir Paciente, 2 - Listar NPaciente, 3 - atualizar Paciente, 4 - excluir Paciente, 5  Aniversariante, 6 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 6:
      op = UI.menu()
      if op == 1: UI.Paciente_inserir()
      if op == 2: UI.Paciente_listar()
      if op == 3: UI.Paciente_atualizar()
      if op == 4: UI.Paciente_excluir()
      if op == 5: UI.Paciente_aniversario()  

  @staticmethod
  def Paciente_inserir():
    nome = input("Informe o nome: ")
    fone = input("Informe o fone: ")
    nascimento = datetime.strptime(input("Nova data de nascimento dd/mm/aaaa: "), "%d/%m/%Y")
    x = Paciente(0, nome, fone, nascimento)
    NPaciente.inserir(x)

  @staticmethod
  def Paciente_listar():  
    for c in NPaciente.listar():
      print(c)

  @staticmethod
  def Paciente_atualizar():
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    fone = input("Informe o novo fone: ")
    nascimento = datetime.strptime(input("Nova data de nascimento dd/mm/aaaa: "), "%d/%m/%Y")
    c = Paciente(id, nome, fone, nascimento)
    NPaciente.atualizar(c)

  @staticmethod
  def Paciente_excluir():
    UI.Paciente_listar()
    id = int(input("Informe o id do Paciente a ser excluído: "))
    c = Paciente(id, "qual", "quer", "coisa")
    NPaciente.excluir(c)

  @staticmethod
  def Paciente_aniversario():
     mes = int(input("Informe o número do mês escolhido. Ex.: Janeiro = 1: "))
     print(NPaciente.aniversariante(mes))

UI.main()