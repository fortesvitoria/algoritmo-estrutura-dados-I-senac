'''
Exercício: implemente uma playlist musical utilizando lista duplamente encadeada, onde o objeto musica tem os seguintes atributos: titulo, autor e duração
- add musicas pela ordem crescente pelo titulo
'''
from ListaMusica import ListaMusica

#teste Lista.py
lista = ListaMusica() 

lista.imprimir()

lista.add("Quimera", "Jorge Dextler", "3:38")
lista.add("Los Rios", "La Muchacha", "2:23")
lista.add("Lationoamerica", "Calle 13", "5:01")


