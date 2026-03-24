from No import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, valor):
        #criando lista por ordem de chegada
        nodo = No(valor)

        if self.inicio is None:
            self.inicio = nodo        
        else:
            self.fim.proximo = nodo #proximo do fim recebe quem acaba de chegar
            nodo.anterior = self.fim #quem acaba de chegar aponta pra quem era o fim
        
        self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print("\n---- Lista duplamente encadeada por ordem de chegada ----\n")
        if self.inicio is None:
            print("XXXX Lista vazia XXXX\n")
            return 
        aux = self.inicio
        while aux: 
            print(aux.dado)
            aux = aux.proximo
        print(f"{"-"*60}")


    def imprimirReverso(self):
        print("\n---- Lista duplamente encadeada ordem reversa de chegada ----\n")
        if self.inicio is None:
            print("XXXX Lista vazia XXXX\n")
            return 
        aux = self.fim
        while aux: 
            print(aux.dado)
            aux = aux.anterior
        print(f"{"-"*60}")


    def remover(self,valor):
        removeu = False
        if self.inicio == None:
            print("XXXX Lista vazia XXXX\n")
        else: 
            if valor  == self.inicio.dado: 
                self.inicio = self.inicio.proximo
                if self.inicio != None:
                    self.inicio.anterior = None 
                else:
                    self.fim = None
                removeu = True
            else:
                #variavel ant é variavel anteior, diferente do atributo anterior da classe nó
                ant = self.inicio 
                aux = self.inicio.proximo 
                while aux:
                    if valor == aux.dado:
                        ant.proximo = aux.proximo 
                        if ant.proximo != None:
                            aux.proximo.anterior = ant 
                        else:
                            self.fim = ant
                        removeu = True
                        break
                    else:
                        ant  = aux
                        aux = aux.proximo
            if removeu:
                print(f"{valor} - Elemento removido!")
            else:
                print(f"{valor} - Não encontrado!")
            self.imprimir()