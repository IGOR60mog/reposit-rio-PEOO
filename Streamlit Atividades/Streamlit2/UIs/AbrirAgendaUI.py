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

        st.text_input("Informe a data no formato dd/mm/aaaa")
        inicial = datetime.strptime(st.text_input("Informe o horário inicial no formato HH:MM"), "%d/%m/%Y")
        final = datetime.strptime(st.text_input("Informe o horário final no formato HH:MM"), "%d/%m/%Y")
        intervalos = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Inserir Horários"):
               AbrirAgendaUI.AbrirAgenda(inicial, final, intervalos)


    @staticmethod
    def AbrirAgenda(inicial, final, intervalos):
            lista = []
            op = inicial
            contador = timedelta(minutes=int(intervalos))
            while op >= final:
                lista.append(op)
                op += contador
            return lista
        

        

            

