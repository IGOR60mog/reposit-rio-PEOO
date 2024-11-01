from view import View
import streamlit as st
import pandas as pd
import time
from datetime import datetime
from datetime import timedelta

class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Agenda do Dia")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        inicial = st.text_input("Informe o horário inicial no formato HH:MM")
        final = st.text_input("Informe o horário final no formato HH:MM")
        intervalos = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Inserir Horários"):
            View.horario_abrir_agenda(data, inicial, final, intervalos)
            


        

            

