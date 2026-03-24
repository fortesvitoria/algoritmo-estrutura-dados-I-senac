'''
Exercício: implemente uma playlist musical utilizando lista duplamente encadeada, onde o objeto musica tem os seguintes atributos: titulo, autor e duração
- add musicas pela ordem crescente pelo titulo
'''
from Musica import Musica

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, valor):
        #criando lista por ordem de chegada
        nodo = No(valor)

        if self.inicio is None:
            self.inicio = nodo        
        else:
            self.fim.proximo = nodo #proximo do fim recebe quem acaba de chegar
            nodo.anterior = self.fim #quem acaba de chegar aponta pra quem era o fim
        
        self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print("\n---- Lista duplamente encadeada por ordem de chegada ----\n")
        if self.inicio is None:
            print("XXXX Lista vazia XXXX\n")
            return 
        aux = self.inicio
        while aux: 
            print(aux.dado)
            aux = aux.proximo
        print(f"{"-"*60}")