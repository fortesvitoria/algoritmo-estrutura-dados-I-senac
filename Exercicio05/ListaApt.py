'''
1) Construa a classe Torre e a classe Apartamento. 
A classe Torre deve possuir os atributos id, nome e endereço. 
A classe Apartamento deve conter os atributos, id, número do
apartamento, número da vaga de garagem e torre.

2) Este condomínio, não possui vagas de garagem para todos os apartamentos. 
Isso faz com que exista uma fila de espera por vagas. 
Implemente uma fila de espera que contenha os métodos para adicionar apartamentos na fila, 
retirar apartamentos informando o número da vaga que este apartamento receberá e um método para imprimir a fila de espera.

3) Os apartamentos que tem vaga de garagem, devem ficar em uma Lista Encadeada. 
Quando um apartamento libera uma vaga, este apartamento deve ir para a fila de espera 
e a vaga deve ir para o primeiro apartamento da fila. Este apartamento que recebeu a 
vaga de garagem, deve ir para a Lista Encadeada, que deverá estar ordenada pelo número da vaga.

'''

from Apartamento import Apartamento

class Lista:
    def __init__(self):
        self.inicio = None 

    def add(self, apartamento): 
        if self.inicio is None:
            self.inicio = apartamento
        else: 
            aux = self.inicio
            while aux is not None:
                aux = aux.prox
            aux.prox = apartamento
        self.imprimir()

    def imprimir(self):
        print("\n---- Lista de apartamentos ----\n")
        if self.inicio is None:
            print("---- Lista de apartamentos vazia ----\n")
            return 
        aux = self.inicio
        while aux: 
            print(aux.dado)
            aux = aux.prox
        print(f"{"-"*25}")

    def remover(self,valor):
        removeu = False
        if self.inicio == None:
            print("XXXX Lista vazia XXXX\n")
        else: 
            if valor  == self.inicio.dado: 
                self.inicio = self.inicio.prox 
                removeu = True
            else: 
                ant = self.inicio
                aux = self.inicio.prox 
                while aux: 
                    if valor == aux.dado:
                        ant.prox = aux.prox 
                        removeu = True
                        break
                    else:                       
                        ant  = aux
                        aux = aux.prox
            if removeu:
                print(f"{valor} - Elemento removido!")
            else:
                print(f"{valor} - Não encontrado!")
            self.imprimir()