import streamlit as st
import pandas as pd
from views import View
import time


class AlterardadosUI:
    def main():
        st.header("Horários Disponíveis")
        AlterardadosUI.alterar()

    # def alterar():