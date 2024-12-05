from modelos.usuario import *
from modelos.resposta import *
from modelos.questionario import *
from modelos.pergunta import *
from modelos.diretoria import *
from modelos.curso import *


u = Usuario(1, "Igor", "9493-8539", "igor@email.com", "1234", "1234") #create
Usuarios.inserir(u)

for x in Usuarios.listar(): #read
    print(x)


