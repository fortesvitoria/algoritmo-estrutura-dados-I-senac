'''
Exercício 01: 
Construa uma lista encadeada de pessoas em que cada nó possui nome e idade.
A inserção deve ser por ordem decrescente de idade.

'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.prox = None