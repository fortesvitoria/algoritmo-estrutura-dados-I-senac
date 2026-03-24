from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()
lista.imprimir()

lista.add("Joao")
lista.add("Maria")
lista.add("Julia")
lista.add("Abel")

lista.imprimirReverso()

lista.remover("Joao")
lista.remover("Lucas")
lista.remover("Abel")

lista.imprimirReverso()