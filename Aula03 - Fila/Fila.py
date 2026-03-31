from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
            # self.fim = nodo - remmovido pq repete no else
        else:
            self.fim.prox = nodo
            # self.fim = nodo
        self.fim = nodo
        self.imprimir()
    
    def imprimir(self):
        print("\n-------- Fila --------\n")
        if self.inicio is None:
            print("XXXX Fila vazia XXXX\n")
            return 
        aux = self.inicio
        txt = ""
        while aux: 
            txt = '{aux.dado} - '
            aux = aux.prox
        print (txt)
        print(f"{"-"*25}")
    
    def remover(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
        self.imprimir()
