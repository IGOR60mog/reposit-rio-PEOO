from calendar import c
from datetime import datetime
from datetime import timedelta


class Musica:
    def __init__(self):
        self.__titulo = ""
        self.__artista = ""
        self.__album = ""
        self.__data = datetime()
        self.__duracao = timedelta()

    def set_titulo(self, titulo):
        if titulo != "": self.__titulo = titulo
        else: raise ValueError()

    def set_artista(self, artista):
        if artista != "": self.__artista = artista
        else: raise ValueError()

    def set_album(self, album):
        if album != "": self.__album = album
        else: raise ValueError()
    
    def set_duracao (self, duracao):
        t1 = datetime.timedelta(seconds=0)
        if duracao != t1: self.__duracao = duracao

    def set_data (self, data):
        self.__data = data

    def get_titulo(self): return self.__titulo

    def get_artista(self): return self.__artista

    def get_album(self): return self.__album

    def get_data(self): return self.__data

    def get_duracao(self): return self.__duracao

    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album}"



class PlayList:
    def __init__(self, nome, descricao):
        if nome != "": self.__nome = nome
        else: raise ValueError("Informe um nome")
        self.__descricao = descricao
        self.__musicas = []

    def inserir(self, m):  # m é um objeto da classe Música
        self.__musicas.append(m)

    def listar(self):
        return self.__musicas[:]
    
    def TempoTotal(self):

        Listaduracao = []
        for n in self.__musicas:
            Listaduracao.append(n.get_duracao())
        return sum(Listaduracao)

    def __str__(self):
        return f"Playlist {self.__nome} - {self.__descricao} tem {len(self.__musicas)} música(s)"

    


class UI:
    @staticmethod
    def menu():
        print("1-Nova Playlist, 2-Inserir Música, 3-Listar Músicas, 4-Info, 5-Fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: p = UI.nova_playlist()
            if op == 2: UI.inserir_musica(p)
            if op == 3: UI.listar_musica(p)
            if op == 4: UI.info(p)
    
    @staticmethod
    def nova_playlist():
        nome = input("Informe o nome da playlist: ")
        desc = input("Informe a descrição da playlist: ")
        p = PlayList(nome, desc)
        return p
    
    @staticmethod
    def inserir_musica(p):
        titulo = input("Informe o título da música: ")
        artista = input("Informe o artista: ")
        album = input("Informe o álbum: ")
        x = input("Informe da duração da música: ")
        l = x.split(':')
        M = int(l[0])
        S = int([1])
        duracao = timedelta(minutes=M, seconds=S)
        data = datetime.now()
        m = Musica()
        m.set_titulo(titulo)
        m.set_artista(artista)
        m.set_album(album)
        m.set_duracao(duracao)
        m.set_data(data)
        p.inserir(m)
    @staticmethod
    def listar_musica(p):
        for m in p.listar():
            print(m)
    def info(p):
        print(p)   

UI.main()  







