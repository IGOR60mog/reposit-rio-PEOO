from modelos.curso import *
from modelos.diretoria import *
from modelos.pergunta import *
from modelos.questionario import *
from modelos.resposta import *
from modelos.usuario import *
from datetime import *
import streamlit as st
import random

class View:

    def usuario_admin():
        for c in View.usuario_listar():
            if c.get_email() == "admin": 
                return None
        View.usuario_inserir("admin", "0000-0000", "admin", "1234", "1234")


    def usuario_autenticar(email, senha):
        for c in View.usuario_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome() }
        return None

    def curso_inserir(idD, n, d, du):
        x = Curso(0, idD, n, d, du)
        Cursos.inserir(x)

    def diretoria_inserir(n, f, e):
        x = Diretoria(0, n, f, e)
        Diretorias.inserir(x)

    def pergunta_inserir(idC, c):
        x = Pergunta(0, idC, c)
        Perguntas.inserir(x)

    def questionario_inserir(idU, d, p):
        x = Questionario(0, idU, d, p)
        Questionarios.inserir(x)

    def resposta_inserir(idP, idQ, r):
        x = Resposta(0, idP, idQ, int(r))
        Respostas.inserir(x)

    def usuario_inserir(n, t, e, s, cs):
        x = Usuario(0, n, t, e, s, cs)
        Usuarios.inserir(x)
        
    def curso_atualizar(id, idD, n, d, du):
        x = Curso(id, idD, n, d, du)
        Cursos.atualizar(x)

    def diretoria_atualizar(id, n, f, e):
        x = Diretoria(id, n, f, e)
        Diretorias.atualizar(x)

    def pergunta_atualizar(id, idC, c):
        x = Pergunta(id, idC, c)
        Perguntas.atualizar(x)

    def questionario_atualizar(id, idU, d, p):
        x = Questionario(id, idU, d, p)
        Questionarios.atualizar(x)

    def resposta_atualizar(id, idP, idQ, r):
        x = Resposta(id, idP, idQ, r)
        Respostas.atualizar(x)
        
    def usuario_atualizar(id, n, t, e, s, cs):
        x = Usuario(id, n, t, e, s, cs)
        Usuarios.atualizar(x)

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

    def get_cursos_id(id):
        return Cursos.listar_id(id) 
    def get_diretorias_id(id):
        return Diretorias.listar_id(id) 
    def get_perguntas_id(id):
        return Perguntas.listar_id(id) 
    def get_questionarios_id(id):
        return Questionarios.listar_id(id) 
    def get_respostas_id(id):
        return Respostas.listar_id(id) 
    def get_usuarios_id(id):
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

    def criar_questionario():
        data = datetime.now()
        idU = st.session_state["usuario_id"]
        View.questionario_inserir(idU, data, 0)
        q = None
        for x in View.questionario_listar():
            if x.get_id_usuario() == idU:
                q = x
        return q.get_id()        
    
    def calculo_pontos():
        pontos_por_curso = {}

        for curso in View.curso_listar():
            id_curso = curso.get_id()
            lista_pergunta_curso = [p for p in View.pergunta_listar() if p.get_id_curso() == id_curso]
            lista_respostas_curso = [r for r in View.resposta_listar() if r.get_id_pergunta() in {p.get_id() for p in lista_pergunta_curso}]

            # Calcular soma de pontos das respostas
            pontos = sum(r.get_resposta() for r in lista_respostas_curso)
            pontos_por_curso[id_curso] = pontos

        if not pontos_por_curso:
            return ["Nenhum curso encontrado", 0]

        # Determinar curso com maior pontuação
        id_curso_vencedor = max(pontos_por_curso, key=pontos_por_curso.get)
        curso_vencedor = View.get_cursos_id(id_curso_vencedor)

        return [curso_vencedor.get_nome(), pontos_por_curso[id_curso_vencedor]*10]
        
        
    def sortear_perguntas():
        lista_perguntas = []

        for curso in View.curso_listar():
            lista_perguntas_por_curso = []
            contador = 0 

            for pergunta in View.pergunta_listar():
                if pergunta.get_id_curso() == curso.get_id():
                    if contador < 3:
                        lista_perguntas_por_curso.append(pergunta)
                        contador += 1

            lista_perguntas += lista_perguntas_por_curso 

        random.shuffle(lista_perguntas)

        return lista_perguntas



                

        