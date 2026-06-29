from no import No
from pilha import Pilha

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, raiz : No, valor):
        if raiz is None:
            nodo = No(valor)
            if self.raiz is None:
                self.raiz = nodo
            return nodo
        
        if valor < raiz.dado:
            raiz.esq = self.inserir(raiz.esq, valor)
        
        if valor > raiz.dado:
            raiz.dir = self.inserir(raiz.dir, valor)
        
        return raiz
    
    def imprimirEmOrdem(self, raiz : No ):
        if raiz is not None:
            self.imprimirEmOrdem( raiz.esq )
            print( raiz.dado, end = " - ")
            self.imprimirEmOrdem( raiz.dir )

    def imprimirPreOrdem(self, raiz : No ):
        if raiz is not None:
            print( raiz.dado, end = " - ")
            self.imprimirPreOrdem( raiz.esq )
            self.imprimirPreOrdem( raiz.dir )

    def imprimirPosOrdem(self, raiz : No ):
        if raiz is not None:
            self.imprimirPosOrdem( raiz.esq )
            self.imprimirPosOrdem( raiz.dir )
            print( raiz.dado, end = " - ")

    def imprimirReverso(self, raiz : No ):
        if raiz is not None:
            self.imprimirReverso( raiz.dir )
            print( raiz.dado, end = " - ")
            self.imprimirReverso( raiz.esq )

    # Método modificado para usar Pilha
    def imprimirComPilha(self, raiz : No ):
        if raiz == None:
            return
        
        pilha = Pilha()
        pilha.empilhar( raiz )

        while pilha.topo != None:
            atual = pilha.desempilhar()
            print( atual.dado , end=" - " )

            # Colocamos o nó direito primeiro para que o esquerdo 
            # fique no topo da pilha e seja processado antes.
            if atual.dir is not None:
                pilha.empilhar( atual.dir )

            if atual.esq is not None:
                pilha.empilhar( atual.esq )
        print("")