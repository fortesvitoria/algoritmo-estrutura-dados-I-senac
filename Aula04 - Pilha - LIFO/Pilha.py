from No import No

class Pilha:
    def __init__(self):
        self.topo = None

    def add(self, valor):
        nodo = No(valor)

        nodo.prox = self.topo
        self.topo = nodo

        self.imprimir()

    def imprimir(self):
        print("\n-------- Pilha --------\n")
        if self.topo is None:
            print("XXXX Pilha vazia XXXX\n")
            return 
        aux = self.topo
        while aux: 
            print (aux.dado)
            aux = aux.prox
        print(f"{"-"*25}")

    def remover(self):
        if self.topo is not None:
            # aux = self.topo    --opcional
            self.topo = self.topo.prox
            # del(aux)    --- opcional
        self.imprimir()

