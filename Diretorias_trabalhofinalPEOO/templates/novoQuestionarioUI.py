import streamlit as st
from datetime import datetime
import random
from view import View
from datetime import *
import time

class NovoQuestionarioUI:
    @staticmethod
    def main():
        st.header("QUESTIONARIO")


        # st.write(st.session_state['sorteio'])

        if 'novo_questionario' not in st.session_state:
            if st.button("começar questionário"):

                #Cria questionário 
                st.session_state['novo_questionario'] = View.criar_questionario()
                #Sorteia as perguntas
                st.session_state['sorteio'] = View.sortear_perguntas()
                #Cria lista com respostas no session state, pois precisamos desse dado msm após o rerun
                st.session_state['respostas'] = []

                #só guardei numa variável msm
                q = st.session_state['novo_questionario']

                #Inserimos todas os objetos resposta no json com sua pergunta
                for x in st.session_state['sorteio']:
                        idp = x.get_id()
                        r = 0
                        View.resposta_inserir(idp, q, r)

                #Inserimos todos os objetos resposta no session_state
                for x in View.resposta_listar():
                    if x.get_id_questionario() == q:
                        st.session_state['respostas'].append(x)

                time.sleep(2)
                st.rerun()
                    
        else:
            #Mostra as perguntas 
            NovoQuestionarioUI.exibir_perguntas(st.session_state['novo_questionario'], st.session_state['respostas'])
             

    def exibir_perguntas(id, respostas):

        respostas = list(set(respostas))
        st.write(respostas)
        if st.button('cancelar questionário'):
             View.questionario_excluir(id)
             del st.session_state['novo_questionario']
             del st.session_state['sorteio']
             del st.session_state['respostas']

            
        #INSERIR TODAS AS RESPOSTAS A PARTIR DO SORTEIO, E APENAS EXIBIR OS OBJETOS. EX.: MOSTRAR PERGUNTA DA RESPOSTA ID 2. 
        # TODA VEZ QUE O OBJETO TIVER RESPOSTA > 0, ATUALIZAR OBJETO.
        op = ['1', '2', '3', '4', '5']
        key = 0
        for x in respostas:
                key +=1
                pergunta = View.get_perguntas_id(x.get_id_pergunta())
                p_conteudo = pergunta.get_conteudo()
                resposta_radio = st.radio(p_conteudo, op, index=None, key=key)
                if resposta_radio != None:
                     View.resposta_atualizar(x.get_id(), x.get_id_pergunta(), id, int(resposta_radio))
                st.write(resposta_radio)

        if st.button('Enviar Questionário'):
            lista = View.calculo_pontos()
            st.write(f'SEU CURSO É {lista[0]} com {lista[1]} pontos!')
            questionario = View.get_questionarios_id(st.session_state['novo_questionario'])
            View.questionario_atualizar(questionario.get_id(), questionario.get_id_usuario(), questionario.get_data(), lista[1])
            del st.session_state['novo_questionario']
            del st.session_state['respostas']
            if st.button('Reiniciar Questionário'):
                 st.rerun()