import streamlit as st
import pandas as pd
from views import View
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        AgendarServicoUI.inserir()

    def inserir():

        servico = st.selectbox("Serviços", View.servico_listar() )
        horario = st.selectbox("Horários disponíveis", View.horario_listar_disponiveis())
        confirmado = st.checkbox("Confirmado")
        cliente = st.session_state["cliente_nome"]
        
        for x in View.horario_listar_disponiveis:
            z = type(x)

        if st.button("Inserir"):
            View.horario_inserir(horario, confirmado, cliente.id, servico)
            View.solicitacao_abrir()
            st.success("Servico inserido com sucesso")
            time.sleep(2)
            st.rerun()
            

            
