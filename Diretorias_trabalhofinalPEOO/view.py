from modelos.curso import *
from modelos.diretoria import *
from modelos.pergunta import *
from modelos.questionario import *
from modelos.resposta import *
from modelos.usuario import *
from datetime import *
import streamlit as st



class View:

    def usuario_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234", 0)

    def usuario_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    def curso_inserir(idD, n, d, du):
        x = Curso(0, idD, n, d, du)
        Cursos.inserir(x)

    def diretoria_inserir(n, f, e):
        x = Diretoria(0, n, f, e)
        Cursos.inserir(x)

    def pergunta_inserir(idC, c):
        x = Pergunta(0, idC, c)
        Cursos.inserir(x)

    def questionario_inserir(idU, d):
        x = Questionario(0, idU, d)
        Cursos.inserir(x)

    def resposta_inserir(idP, idQ, r):
        x = Resposta(0, idP, idQ, r)
        Cursos.inserir(x)

    def usuario_inserir(n, t, e, s, cs):
        x = Usuario(0, n, t, e, s, cs)
        Cursos.inserir(x)
        
    def curso_atualizar(id, idD, n, d, du):
        x = Curso(id, idD, n, d, du)
        Cursos.atualizar(x)

    def diretoria_atualizar(id, n, f, e):
        x = Diretoria(id, n, f, e)
        Cursos.atualizar(x)

    def pergunta_atualizar(id, idC, c):
        x = Pergunta(id, idC, c)
        Cursos.atualizar(x)

    def questionario_atualizar(id, idU, d):
        x = Questionario(id, idU, d)
        Cursos.atualizar(x)

    def resposta_atualizar(id, idP, idQ, r):
        x = Resposta(id, idP, idQ, r)
        Cursos.atualizar(x)
        
    def usuario_atualizar(id, n, t, e, s, cs):
        x = Usuario(id, n, t, e, s, cs)
        Cursos.atualizar(x)

    def curso_listar():
        return Cursos.listar()
    def diretoria_listar():
        return Diretorias.listar()
    def pergunta_listar():
        return Perguntas.listar()
    def questionario_listar():
        return Questionarios.listar()
    def resposta_listar():
        return Respostas.listar()
    def usuario_listar():
        return Usuarios.listar()

    def perfil_cursos_id(id):
        return Cursos.listar_id(id) 
    def perfil_diretorias_id(id):
        return Diretorias.listar_id(id) 
    def perfil_perguntas_id(id):
        return Perguntas.listar_id(id) 
    def perfil_questionarios_id(id):
        return Questionarios.listar_id(id) 
    def perfil_respostas_id(id):
        return Respostas.listar_id(id) 
    def perfil_usuarios_id(id):
        return Usuarios.listar_id(id) 
    
    def curso_excluir(id):
        x = Curso(id, 0, "#", "#", 0)
        Cursos.excluir(x)

    def diretoria_excluir(id):
        x = Diretoria(id, "#", "#", "#")
        Diretorias.excluir(x)

    def pergunta_excluir(id):
        x = Pergunta(id, 0, "#")
        Perguntas.excluir(x)

    def questionario_excluir(id):
        x = Questionario(id, 0, "#", 0)
        Questionarios.excluir(x)

    def resposta_excluir(id):
        x = Resposta(id, 0, 0, 0)
        Respostas.excluir(x)

    def usuario_excluir(id):
        x = Usuario(id, "#", "#", "#", "#", "#")
        Usuarios.excluir(x)

    #def calculo_pontos()