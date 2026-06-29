from noPilha import NoPilha

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def empilhar(self, noDaArvore):
        nodo = NoPilha(noDaArvore)
        # O novo nó aponta para o antigo topo
        nodo.prox = self.topo
        # O topo passa a ser o novo nó
        self.topo = nodo
        self.tamanho += 1

    def desempilhar(self):
        if self.topo is not None:
            aux = self.topo.noArvore
            self.topo = self.topo.prox
            self.tamanho -= 1
            return aux
        return None