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
from Autor import Autor

class Livro:
    def __init__(self, titulo, autorNome, paginas, autorAno):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = Autor(autorNome, autorAno)
        self.prox = None 
