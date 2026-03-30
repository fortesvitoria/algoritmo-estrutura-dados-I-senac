'''
Exercício: implemente uma playlist musical utilizando lista duplamente encadeada, onde o objeto musica tem os seguintes atributos: titulo, autor e duração
- add musicas pela ordem crescente pelo titulo
'''
from ListaMusica import ListaMusica
from Musica import Musica

#teste Lista.py
lista = ListaMusica() 

lista.imprimir()

# lista.add("Quimera", "Jorge Dextler", 3,38)
# lista.add("Los Rios", "La Muchacha", 2,23)
# lista.add("Lationoamerica", "Calle 13", 5,01)

m1 = Musica("Quimera", "Jorge Dextler", 3.3)
m2 = Musica("Rios", "La Muchacha", 2.23)
m3 = Musica("Lationoamerica", "Calle 13", 5)

lista.addCrescente(m1)
lista.addCrescente(m2)
lista.addCrescente(m3)

lista.imprimirReverso()

lista.remover("Quimera")


