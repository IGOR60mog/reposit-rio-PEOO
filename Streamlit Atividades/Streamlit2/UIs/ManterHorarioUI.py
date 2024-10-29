from view import View
import streamlit as st
import pandas as pd
import time
from datetime import datetime
from AbrirAgendaUI import *


class ManterHorariosUI:
    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])

        with tab1:
            ManterHorariosUI.inserir()
        with tab2:
            ManterHorariosUI.listar()
        with tab3:
            ManterHorariosUI.atualizar()
        with tab4:
            ManterHorariosUI.deletar()

    
    @staticmethod
    def inserir():
        data =  datetime.strptime(st.text_input("Informe data (em dd/mm/aaaa): "), "%d/%m/%Y %H:%M")
        confirmacao = False
        idCliente = st.selectbox("Seleção de Cliente", View.cliente_listar(), key=1)
        idServico = st.selectbox("Seleção de Servico", View.servico_listar(), key=2)
        if st.button("Informe"):
            View.horario_inserir(data, confirmacao, idCliente.get_id(), idServico.get_id())
            st.write("Horarios inserido com sucesso!")
            time.sleep(2)
            st.rerun()
    
    @staticmethod
    def listar():
        lista = []
        if View.horario_listar() != []:
            for x in View.horario_listar():
                list = [x.get_id(), x.get_data(), x.get_confirmacao(), x.get_id_Cliente(), x.get_id_Servico()]
                lista.append(list)
            th = ["Id", "data", "confirmacao", "idCliente", "idServiço"]    
            data = pd.DataFrame(lista, columns=th)
            st.dataframe(data, 1000, hide_index=True)
        else:
            st.write("Nenhum horario inserido")

    @staticmethod
    def atualizar():
        horario = st.selectbox("Atualização de Horarios", View.horario_listar(), key=0)
        data = st.text_input("Informe novo data: ")
        horarios = st.selectbox("Horários disponíveis", )
        confirmacao = False
        idCliente = st.selectbox("Seleção de Cliente", View.cliente_listar(), key=3)
        idServico = st.selectbox("Seleção de Servico", View.servico_listar(), key=4)
        if st.button("Atualizar"):
            st.write("Horário atualizado com sucesso!")
            View.horario_atualizar(horario.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmacao, idCliente.get_id(), idServico.get_id())
            time.sleep(2)
            st.rerun()    
    @staticmethod
    def deletar():
        horario = st.selectbox("Exclusão de Horarios", View.horario_listar(), key=5)
        if st.button("Deletar"):
         st.write("horario deletado com sucesso!")
         View.horario_excluir(horario.get_id())
         time.sleep(2)
         st.rerun()