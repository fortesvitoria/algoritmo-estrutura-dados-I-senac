'''
Faça um algoritmo que implementa uma pilha de livros
    - Cada livro deverá conter: 
        - Titulo; qtde paginas e autor
    O autor deverá conter:
        - Nome e ano de nascimento

        um autor pra muitos livros.
        um livro para um unico autor.

    Implemente os método: 
        - add livros na pilha; 
        - remover livro 
        - imprimir livro
        - e um metodo em que o usuario informa o nome do autor e é informado 
        quantos livros tem na pilha com este autor

        
'''

from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None

    def add(self, livro):
        livro.prox = self.topo
        self.topo = livro
        self.imprimir()

    def imprimir(self):
        print("\n-------- Pilha --------\n")
        if self.topo is None:
            print("XXXX Pilha vazia XXXX\n")
            return 
        aux = self.topo

        while aux:
            print(aux)
            aux = aux.prox
        print(f"{"-"*25}")

    def remover(self):
        if self.topo is not None:
            self.topo = self.topo.prox
        self.imprimir()
    
    def buscaAutor(self, nomeBusca):
        if self.topo is not None:
            contador = 0
            aux = self.topo
            while aux:
                if nomeBusca == aux.autor.getNome():
                    contador += 1
                aux = aux.prox
            
            if contador == 0:
                print(f'O autor {nomeBusca} não foi encontrado!')
            else:        
                print(f'O {nomeBusca} possui {contador} livros registrados.')


