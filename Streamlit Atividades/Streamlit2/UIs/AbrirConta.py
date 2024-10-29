from view import View
import streamlit as st
import pandas as pd
import time

class AbrirConta:

    @staticmethod
    def main():

        st.header("Abrir Conta")

        nome = st.text_input("Informe nome: ")
        email = st.text_input("Informe email: ")
        telefone = st.text_input("Informe telefone: ")
        senha = st.text_input("Informe senha: ")
        confenha =  st.text_input("confirme senha: ")

        if senha == confenha:
            View.cliente_inserir(nome, email, telefone, senha)
            st.write("Cliente inserido com sucesso!")
            time.sleep(2)
            st.rerun()
        else:
            st.write("Senha diferente")
            time.sleep(2)
            st.rerun()
