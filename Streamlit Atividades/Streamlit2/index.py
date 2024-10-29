
from UIs.ManterClienteUI import *
from UIs.ManterHorarioUI import *
from UIs.ManterServicoUI import *

class Index:

    @staticmethod
    def main():
        lista = ["Cadastro de Clientes", "Cadastro de Horario", "Cadastro de Serviços", "Abrir Agenda do dia"]
        item = st.sidebar.selectbox("Menu", lista)
        if item:
            if item == "Cadastro de Clientes": ManterClientesUI.main()
            elif item == "Cadastro de Serviços": ManterServicosUI.main()
            elif item == "Cadastro de Horario": ManterHorariosUI.main()


Index.main()
