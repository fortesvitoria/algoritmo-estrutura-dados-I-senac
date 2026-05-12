from carro import Carro
from veiculo import Veiculo


class PilhaCarro:
    def __init__(self):
        self.topo = None

    def add(self, carro):
        carro.prox = self.topo
        self.topo = carro

        self.imprimir()

    def imprimir(self):
        print("\n-------- Pilha de carros --------\n")
        if self.topo is None:
            print("\n-------- Pilha de carros vazia --------\n")
            return 
        aux = self.topo
        while aux: 
            print (aux)
            aux = aux.prox
        print(f"{"-"*25}")

    def remover(self):
        if self.topo is not None:
            # aux = self.topo    --opcional
            self.topo = self.topo.prox
            # del(aux)    --- opcional
        self.imprimir()
