'''
Exercício: implemente uma playlist musical utilizando lista duplamente encadeada, onde o objeto musica tem os seguintes atributos: titulo, autor e duração
- add musicas pela ordem crescente pelo titulo
'''

class Musica:
    def __init__(self, titulo, autor, duracao):
        self.anterior = None
        self.titulo = titulo
        self.autor = autor
        self.duracao = duracao
        self.proximo = None
