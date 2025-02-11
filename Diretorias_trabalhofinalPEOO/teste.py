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

# r = Resposta(0, 1, 1, 5)
# Respostas.inserir(r)

# r = Resposta(1, 2, 2, 5)
# Respostas.atualizar(r)

# r = Resposta(1, "#", "#", 0)
# Respostas.excluir(r)

for x in Respostas.listar():
    print(x)



#QUESTIONARIO

# q = Questionario(0, 1, datetime(2025, 2, 7), 500)
# Questionarios.inserir(q)

# q = Questionario(1, 1, datetime(2025, 2, 11), 300)
# Questionarios.atualizar(q)

# q = Questionario(1, "", "", 0)
# Questionarios.excluir(q)

# for x in Questionarios.listar():
#     print(x)



#PERGUNTA

# p = Pergunta(0, 1, "Você gosta de computadores?")
# Perguntas.inserir(p)

# p = Pergunta(1, 2, "Você se interessa em saber como funciona uma máquina?")
# Perguntas.atualizar(p)

# p = Pergunta(1, "#", "#")
# Perguntas.excluir(p)

# for x in Perguntas.listar():
#     print(x)



#DIRETORIA

# d = Diretoria(0, "DIATINF", "Tecnologia da informação", "diatinf@email.com")
# Diretorias.inserir(d)

# d = Diretoria(1, "DIATINF", "Gestão e tecnologia da informação", "diatinf@email.com")
# Diretorias.atualizar(d)

# d = Diretoria(1, "#", "#", "#")
# Diretorias.excluir(d)

# for x in Diretorias.listar():
#     print(x)



#CURSO

# c = Curso(0, 1, "INFOWEB", "Área de desenvolvedor web", 4)
# Cursos.inserir(c)

# c = Curso(1, 1, "Informática para Internet", "Área de desenvolvedor web", 4)
# Cursos.atualizar(c)

# c = Curso(1, 1, "#", "#", 0)
# Cursos.excluir(c)

# for x in Cursos.listar():
#     print(x)
