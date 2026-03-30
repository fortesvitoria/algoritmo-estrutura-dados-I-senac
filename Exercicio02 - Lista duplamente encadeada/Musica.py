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

    def __str__(self):
        txt = f"Titulo: {self.titulo}\nAutor: {self.autor}\nDuração: {str(self.duracao)}\n{'-' * 50}"
        return txt