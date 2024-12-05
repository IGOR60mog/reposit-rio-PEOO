import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:    
            #for obj in clientes: st.write(obj)
            dic = []
            for obj in clientes: 
                Cliente = obj.__dict__
                del(Cliente["_Cliente__senha"])
                dic.append(Cliente)
            df = pd.DataFrame(dic)
            st.dataframe(df, 1000, hide_index=True)

    def inserir():
        try:
            nome = st.text_input("Informe o nome do cliente")
            email = st.text_input("Informe o e-mail")
            fone = st.text_input("Informe o fone")
            senha = st.text_input("Informe a senha", type="password")
            if st.button("Inserir"):
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente inserido com sucesso")
                time.sleep(2)
                st.rerun()
        except Exception as erro:
            st.error(erro)

    def atualizar():
        try:
            clientes = View.cliente_listar()
            if len(clientes) == 0: 
                st.write("Nenhum cliente cadastrado")
            else:
                op = st.selectbox("Atualização de cliente", clientes)
                nome = st.text_input("Informe o novo nome do cliente", op.get_nome())
                email = st.text_input("Informe o novo e-mail", op.get_email())
                fone = st.text_input("Informe o novo fone", op.get_fone())
                senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
                if st.button("Atualizar"):
                    View.cliente_atualizar(op.id, nome, email, fone, senha)
                    st.success("Cliente atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
        except ValueError as erro:
            st.error(erro)


    def excluir():
        try:
            clientes = View.cliente_listar()
            if len(clientes) == 0: 
                st.write("Nenhum cliente cadastrado")
            else:
                op = st.selectbox("Exclusão de cliente", clientes)
                if st.button("Excluir"):
                    View.cliente_excluir(op.id)
                    st.success("Cliente excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
        except ValueError as erro:
            st.write(erro.args)
