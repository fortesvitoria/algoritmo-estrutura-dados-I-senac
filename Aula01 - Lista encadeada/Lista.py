from No import No

class Lista:
    def __init__(self):
        self.inicio = None

    def add(self, valor): #adiciona de forma crescente
        nodo = No(valor) #guarda memoria

        if self.inicio is None: #verifica se vazia
            self.inicio = nodo

        else:
            if nodo.dado < self.inicio.dado: #se nodo é menor que inicio
                nodo.prox = self.inicio #nodo.prox recebe o que esta no inicio
                self.inicio = nodo #inicio recebe nodo

            else: 
                ant = self.inicio #começa pelo segundo elemento
                aux = self.inicio.prox #aux recebe o prox do inicio

                while aux : #enquanto existir aux, continua
                    if nodo.dado < aux.dado:
                        nodo.prox = aux #proximo recebe aux
                        ant.prox = nodo #anterior do proximo recebe nodo
                        break
                    else:
                        ant = aux #anterior recebe aux
                        aux = aux.prox #aux recebe o proximo

                if aux == None:
                    ant.prox = nodo #proximo do anterior recebe nodo

            self.imprimir()


    def imprimir(self):
        print("\nLista encadeada\n")
        if self.inicio is None:
            print("\nLista vazia\n")
            return 
        aux = self.inicio
        while aux: 
            print("\n", aux.dado)
            aux = aux.prox