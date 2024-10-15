import streamlit as st
from equacao import *

class EquacaoUI:

    @staticmethod
    def main():
        st.header("Equacao do II Grau: y = ax**2 + bx + c")
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        if st.button("Calcular"):
            e = Equacao(int(a), int(b), int(c))
            st.write(e)
            st.write(f"Delta = {e.delta()}")
            st.write(f"x1 = {e.Raiz1()}")
            st.write(f"x2 = {e.Raiz2()}")

            st.plotly_chart(figure_or_data=e, use_container_width=False, theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), **kwargs)
            
            