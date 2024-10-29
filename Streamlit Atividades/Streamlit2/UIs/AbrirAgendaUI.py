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
            lista = []
            op = datetime.strptime(f"{data} {inicial}", "%d/%m/%Y %H:%M")
            contador = timedelta(minutes=int(intervalos))
            finale = datetime.strptime(f"{data} {final}", "%d/%m/%Y %H:%M")
            while op <= finale:
                lista.append(op)
                op += contador
            AbrirAgendaUI.AbrirAgenda(lista)

    @staticmethod
    def AbrirAgenda(lista):
        compromissos = []
        
        for x in lista:
            compromisso = {"Hora": x, "Compromisso": 0} 

            for y in View.horario_listar():
                if x == y.get_data():
                    for z in View.servico_listar():
                        if z.get_id() == y.get_id_Servico():
                            compromisso["Compromisso"] = z
                            break 
                            
            if compromisso not in compromissos:
                compromissos.append(compromisso)
        
        data = pd.DataFrame(compromissos)
        st.dataframe(data, 1000, hide_index=True)


        

        

            

