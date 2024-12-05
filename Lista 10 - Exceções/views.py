from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
            for x in View.cliente_listar():
                if x.get_email() == email:
                    raise ValueError("Erro! Email já cadastrado!")
            c = Cliente(0, nome, email, fone, senha)
            Clientes.inserir(c)


    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        for x in View.cliente_listar():
                if x.get_email() == email:
                    raise ValueError("Erro! Email já cadastrado!")
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        for x in View.horario_listar():
            if x.get_id_cliente() == id:
                raise ValueError("Erro! Você não pode excluir cliente com horário marcado")
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)    

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome() }
        return None

    def horario_inserir(data, confirmado, e, s):

        if View.cliente_listar_id(int(e)) == None or View.servico_listar_id(int(s)) == None:
            raise ValueError("Erro! Id do cliente e Id do serviço têm que ser válidos!")

        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(int(e))
        c.set_id_servico(int(s))
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.get_data() >= datetime.now() and h.get_id_cliente() == 0: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):

        if View.cliente_listar_id(id_cliente) == None or View.servico_listar_id(id_servico) == None:
            raise ValueError("Erro! Id do cliente e Id do serviço têm que ser válidos!")
        
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        Horarios.atualizar(c)

    def horario_excluir(id):

        for x in View.horario_listar():
            if x.get_id() == id:
                if x.get_id_cliente() > 0:
                    raise ValueError("Erro! Não pode excluir horário com cliente já cadastrado")
    
        c = Horario(id, None)
        Horarios.excluir(c)    

    def solicitacao_abrir():
        lista_revisao = []
        lista_solicitacao = []
        for x in View.horario_listar():
            if x.get_data() not in lista_revisao:
                lista_revisao.append(x.get_data())
            else:
                lista_solicitacao.append(x)
        return lista_solicitacao
    
    def solicitacao_confirmar(h):
        for x in View.horario_listar():
            if x.get_data() == h.get_data():
                View.horario_atualizar(x.get_id(), x.get_data(), h.get_confirmado(), h.get_id_cliente(), h.get_id_servico())
                View.horario_excluir(h.get_id())

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):

        if data == datetime.now(): raise ValueError("Erro! Data não pode ser agora")
        if hora_inicio <= 0: raise ValueError("Erro! Hora inicial tem que ser maior que zero")
        if hora_fim <=0: raise ValueError("Erro! Hora final tem que ser maior que zero")
        if intervalo <=0: raise ValueError("Erro! intervalo tem que ser maior que zero")

        i = data + " " + hora_inicio   
        f = data + " " + hora_fim      
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            #cadastrar o horário x
            View.horario_inserir(x, False, None, None)
            #passar para o próximo horário
            x = x + d

    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        for x in View.horario_listar():
            if x.get_id_servico() == id:
                raise ValueError("Erro! Você não pode excluir serviço com horário marcado")
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)    

    