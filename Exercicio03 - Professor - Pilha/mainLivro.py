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

from PilhaLivro import Pilha
from Autor import Autor
from Livro import Livro


a1 = Autor("Machado de Assis", 1839)
a2 = Autor("Jorge Amado", 1912)
a3 = Autor("Clarice Lispector", 1920)

l1 = Livro("Dom Casmurro", a1, 250)
l2 = Livro("Capitães de Abril", a2, 300)
l3 = Livro("A Paixão Segundo G.H.", a3, 280)
l4 = Livro("Memórias Póstumas de Brás Cubas", a1, 200)

livros = Pilha()
livros.imprimir()

livros.add(l1)
livros.add(l2)
livros.add(l3)
livros.add(l4)

# livros.remover()

livros.buscaAutor("Machado de Assis")
livros.buscaAutor("Valter Hugo Mãe")

livros.remover()