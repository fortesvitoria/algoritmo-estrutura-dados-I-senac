'''
Exercício 01: 
Construa uma lista encadeada de pessoas em que cada nó possui nome e idade.
A inserção deve ser por ordem decrescente de idade.

'''

from Lista import Lista

#imports codigo professor
from ListaCodigoProfessor import Lista
from Pessoa import Pessoa

#teste Lista.py
lista = Lista() 

lista.imprimir()

lista.add("Vitoria", 34)
lista.add("Eduardo", 40)
lista.add("Fran", 23)
lista.add("Gabriel", 6)

lista.remover("Fran")
lista.remover("Eduardo")
lista.remover("Lucas")


#Teste ListaCodigoProfessor.py
pessoas = Lista()

pessoas.imprimir()

p1 = Pessoa("Joao", 20)
p2 = Pessoa("Maria", 25)
p3 = Pessoa("Julia", 22)

pessoas.add(p1)
pessoas.add(p2)
pessoas.add(p3)
pessoas.add()
pessoas.add(Pessoa("José", 30))

