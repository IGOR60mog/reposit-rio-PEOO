import streamlit as st
import pandas as pd
from views import View
import time

class ConfirmarAgendamentoUI:

    def main():
        st.header("Confirmar Agendamento")
        solicitacoes = View.solicitacao_abrir()
        st.dataframe(solicitacoes, 1000, hide_index=True)

        

        if st.button("Confirmar"):
            print("X")


        

        
