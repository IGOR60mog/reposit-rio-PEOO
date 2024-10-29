from view import View
import streamlit as st
import pandas as pd
import time

class ManterServicosUI:
    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])

        with tab1:
            ManterServicosUI.inserir()
        with tab2:
            ManterServicosUI.listar()
        with tab3:
            ManterServicosUI.atualizar()
        with tab4:
            ManterServicosUI.deletar()

    
    @staticmethod
    def inserir():
        desc = st.text_input("Informe descrição: ")
        v = st.text_input("Informe valor (em R$): ")
        d = st.text_input("Informe duração (em h): ")
        if st.button("Informe"):
            View.servico_inserir(desc, int(v), int(d))
            st.write("Servicos inserido com sucesso!")
            time.sleep(2)
            st.rerun()
    
    @staticmethod
    def listar():
        lista = []
        if View.servico_listar() != []:
            for x in View.servico_listar():
                list = [x.get_id(), x.get_descricao(), x.get_valor(), x.get_duracao()]
                lista.append(list)
            th = ["Id", "Descrição", "Valor", "Duração"]    
            data = pd.DataFrame(lista, columns=th)
            st.dataframe(data, 1000, hide_index=True)
        else:
            st.write("Nenhum servico inserido")

    @staticmethod
    def atualizar():
        servico = st.selectbox("Atualização de Servicos", View.servico_listar(), key=0)
        descricao = st.text_input("Informe nova Descriçao: ")
        valor = st.text_input("Informe novo valor (em R$): ")
        duracao = st.text_input("Informe novo Duração (em h): ")
        if st.button("Atualizar"):
            st.write("servico atualizado com sucesso!")
            View.servico_atualizar(servico.get_id(), descricao, int(valor), int(duracao))
            time.sleep(2)
            st.rerun()
    @staticmethod
    def deletar():
        servico = st.selectbox("Exclusão de Servicos", View.servico_listar(), key=1)
        if st.button("Deletar"):
         st.write("servico deletado com sucesso!")
         View.servico_excluir(servico.get_id())
         time.sleep(2)
         st.rerun()