from view import View
import streamlit as st
import pandas as pd
import time

class ManterClientesUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])

        with tab1:
            ManterClientesUI.inserir()
        with tab2:
            ManterClientesUI.listar()
        with tab3:
            ManterClientesUI.atualizar()
        with tab4:
            ManterClientesUI.deletar()

    
    @staticmethod
    def inserir():
        nome = st.text_input("Informe nome: ")
        email = st.text_input("Informe email: ")
        fone = st.text_input("Informe telefone: ")
        senha = st.text_input("Informe senha: ")
        if st.button("Informe"):
            View.cliente_inserir(nome, email, fone, senha)
            st.write("Cliente inserido com sucesso!")
            time.sleep(2)
            st.rerun()
    
    @staticmethod
    def listar():
        lista = []
        if View.cliente_listar() != []:
            for x in View.cliente_listar():
                list = [x.get_id(), x.get_nome(), x.get_email(), x.get_fone()]
                lista.append(list)
            th = ["Id", "Nome", "Email", "Telefone"]    
            data = pd.DataFrame(lista, columns=th)
            st.dataframe(data, 1000, hide_index=True)
        else:
            st.write("Nenhum cliente inserido")

    @staticmethod
    def atualizar():
        cliente = st.selectbox("Atualização de clientes", View.cliente_listar(), key=0)
        nome = st.text_input("Informe novo nome: ", cliente.get_nome())
        email = st.text_input("Informe novo email: ", cliente.get_email())
        fone = st.text_input("Informe novo telefone: ", cliente.get_fone())
        senha = st.text_input("Informe nova senha: ", cliente.get_senha())
        if st.button("Atualizar"):
            st.write("Cliente atualizado com sucesso!")
            View.cliente_atualizar(cliente.get_id(), nome, email, fone, senha)
            time.sleep(2)
            st.rerun()
    
    @staticmethod
    def deletar():
        cliente = st.selectbox("Exclusão de clientes", View.cliente_listar(), key=1)
        if st.button("Deletar"):
         st.write("Cliente deletado com sucesso!")
         View.cliente_excluir(cliente.get_id())
         time.sleep(2)
         st.rerun()