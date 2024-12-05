import streamlit as st
import pandas as pd
from views import View
import time

class ConfirmarAgendamentoUI:

    def main():
        st.header("Confirmar Agendamento")

        solicitacoes = []
        for x in View.solicitacao_abrir():
            Cliente = View.cliente_listar_id(x.id_cliente)
            Servico = View.servico_listar_id(x.id_servico)
            if Cliente != None: Cliente = Cliente.nome
            if Servico != None: Servico = Servico.descricao
            dic = {"id": x.id,"data": x.data,"cliente": Cliente,"servico": Servico}
            solicitacoes.append(dic)
        st.dataframe(solicitacoes, 1000, hide_index=True)

        op = st.selectbox("Escolha uma solicitação", View.solicitacao_abrir())

        if st.button("Confirmar"):
            View.solicitacao_confirmar(op)
            st.success("Soliticação confirmada com sucesso")
            time.sleep(2)
            st.rerun()
            


        

        
