from modelos.usuario import *
from modelos.resposta import *
from modelos.questionario import *
from modelos.pergunta import *
from modelos.diretoria import *
from modelos.curso import *
from datetime import datetime


#USUARIO

# u = Usuario(0, "Igor", "9493-8539", "igor@email.com", "1234", "1234") #create
# Usuarios.inserir(u)
# v = Usuario(2, "Carolina", "3857-3465", "carolina@email.com", "4321", "4321")
# Usuarios.inserir(v)

# u = Usuario(1, "Igor", "4834-3754", "igor@yahoo.com", "1234", "1234") #update
# Usuarios.atualizar(u)

# u = Usuario(1, " ", " ", " ", " ", " ") #delete
# Usuarios.excluir(u)

# for x in Usuarios.listar(): #read
#     print(x)



#RESPOSTA

# r = Resposta(0, 1, 1, "#")
# Respostas.inserir(r)

# r = Resposta(1, 2, 2, "#")
# Respostas.atualizar(r)

# r = Resposta(1, "#", "#", "#")
# Respostas.excluir(r)

# for x in Respostas.listar():
#     print(x)


#QUESTIONARIO

q = Questionario(0, 1, datetime(2025, 2, 7), 500)
Questionarios.inserir(q)

q = Questionario(1, 1, datetime(2025, 2, 11), 300)
Questionarios.atualizar(q)

# q = Questionario(1, "", "", "")
# Questionarios.excluir(q)

for x in Questionarios.listar():
    print(x)