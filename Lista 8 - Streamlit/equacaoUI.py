import streamlit as st
import pandas as pd
import numpy as np
import math

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

            xmin = ((int(b)/(2*int(a)))-30)
            xmax = ((int(b)/(2*int(a)))+30)
            n = 100
            d = (xmax - xmin)/n  # 0.5
            px = []
            py = []
            x = xmin
            while x < xmax:
                y = int(a)*x**2 - int(b)*x + int(b)
                px.append(x)
                py.append(y)
                x = x + d
            x = xmax
            y = int(a)*x**2 - int(b)*x + int(b)
            px.append(x)
            py.append(y)

            dic = { "x" : px, "y" : py }
            chart_data = pd.DataFrame(dic)
            st.line_chart(chart_data, x = "x", y = "y") 