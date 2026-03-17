'''
Exercício 01: 
Construa uma lista encadeada de pessoas em que cada nó possui nome e idade.
A inserção deve ser por ordem decrescente de idade.

'''

from Lista import Lista

lista = Lista() 

lista.imprimir()

lista.add("Vitoria", 34)
lista.add("Eduardo", 40)
lista.add("Fran", 23)
lista.add("Gabriel", 6)

lista.remover("Fran")
lista.remover("Eduardo")
lista.remover("Lucas")