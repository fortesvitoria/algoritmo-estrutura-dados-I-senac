'''
Exercício: implemente uma playlist musical utilizando lista duplamente encadeada, onde o objeto musica tem os seguintes atributos: titulo, autor e duração
- add musicas pela ordem crescente pelo titulo
'''
from Musica import Musica

class ListaMusica:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, titulo, autor, duracao):
        #criando lista por ordem de chegada
        musica = Musica(titulo, autor, duracao)

        if self.inicio is None:
            self.inicio = musica        
        else:
            self.fim.proximo = musica #proximo do fim recebe quem acaba de chegar
            musica.anterior = self.fim #quem acaba de chegar aponta pra quem era o fim
        
        self.fim = musica
        self.imprimir()

    def imprimir(self):
        print("\n---- Lista duplamente encadeada por ordem de chegada ----\n")
        if self.inicio is None:
            print("XXXX Lista vazia XXXX\n")
            return 
        aux = self.inicio
        while aux: 
            print(aux.titulo)
            aux = aux.proximo
        print(f"{"-"*60}")
    
    # def addCrescente(self, titulo, autor, duracao):
    #     musica = Musica(titulo, autor, duracao)

    #     if self.inicio is None:
    #         self.inicio = musica
    #     else:
    #         if musica.titulo > self.inicio.titulo: # se o titulo da musica for maior que o titulo do inicio
    #             musica.proximo = self.inicio
    #             self.inicio = musica
            
    #         else: 
                
    #         self.fim.proximo = musica
    #         musica.anterior = self.fim
        
    #     self.fim = musica
    #     self.imprimir()

    