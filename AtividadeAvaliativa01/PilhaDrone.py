from drone import Drone
from veiculo import Veiculo


class PilhaDrone:
    def __init__(self):
        self.topo = None

    def add(self, drone):
        drone.prox = self.topo
        self.topo = drone

        self.imprimir()

    def imprimir(self):
        print("\n-------- Pilha de drones --------\n")
        if self.topo is None:
            print("\n-------- Pilha de drones vazia --------\n")
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