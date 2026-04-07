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


livros = Pilha()
livros.imprimir()

livros.add("Livro A", "Autor B", 250, 1995)
livros.add("Livro B", "Autor B", 800, 1992)
livros.add("Livro C", "Autor A", 300, 2021)

# livros.remover()

livros.buscaAutor("Autor B")