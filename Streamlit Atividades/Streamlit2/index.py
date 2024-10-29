from UIs.ManterClienteUI import *
from UIs.ManterHorarioUI import *
from UIs.ManterServicoUI import *
from UIs.AbrirAgendaUI import *
from UIs.AbrirConta import *

class Index:

    @staticmethod
    def main():
        lista = ["Cadastro de Clientes", "Cadastro de Horario", "Cadastro de Serviços", "Abrir Agenda do dia", "Abrir conta"]
        item = st.sidebar.selectbox("Menu", lista)
        if item:
            if item == "Cadastro de Clientes": ManterClientesUI.main()
            elif item == "Cadastro de Serviços": ManterServicosUI.main()
            elif item == "Cadastro de Horario": ManterHorariosUI.main()
            elif item == "Abrir Agenda do dia": AbrirAgendaUI.main()
            elif item == "Abrir conta": AbrirConta.main()


Index.main()
