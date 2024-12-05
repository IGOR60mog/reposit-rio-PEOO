import streamlit as st
import pandas as pd
from views import View
import time


class ProfissionalAgendaUI:
    def main():
        st.header("Horários Disponíveis")
        ProfissionalAgendaUI.agenda()

    # def agenda():