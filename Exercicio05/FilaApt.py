'''
1) Construa a classe Torre e a classe Apartamento. 
A classe Torre deve possuir os atributos id, nome e endereço. 
A classe Apartamento deve conter os atributos, id, número do
apartamento, número da vaga de garagem e torre.

--> 2) Este condomínio, não possui vagas de garagem para todos os apartamentos. 
Isso faz com que exista uma fila de espera por vagas. 
Implemente uma fila de espera que contenha os métodos para adicionar apartamentos na fila, 

--> retirar apartamentos informando o número da vaga que este apartamento receberá e um método para imprimir a fila de espera.

3) Os apartamentos que tem vaga de garagem, devem ficar em uma Lista Encadeada. 
Quando um apartamento libera uma vaga, este apartamento deve ir para a fila de espera 
e a vaga deve ir para o primeiro apartamento da fila. Este apartamento que recebeu a 
vaga de garagem, deve ir para a Lista Encadeada, que deverá estar ordenada pelo número da vaga.

'''

from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,apartamento):
        apartamento.prox = None
        if self.inicio is None:
            self.inicio = apartamento
        else:
            self.fim.prox = apartamento
        self.fim = apartamento
        self.imprimir()
    
    def imprimir(self):
        print("\n-------- Fila de espera--------\n")
        if self.inicio is None:
            print("-------- Fila de espera vazia --------\n")
            return 
        aux = self.inicio
        txt = ""
        while aux: 
            txt = '{aux.dado}'
            aux = aux.prox
        print (txt)
        print(f"{"-"*25}")
    
    def remover(self, numeroVaga):
        if self.inicio is not None:
            aptRemovido = self.inicio #guarda o primeiro apartamento da fila, para depois retornar ele
            aptRemovido.numeroVaga = numeroVaga # atribui a vaga que o apartamento irá receber
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
        return aptRemovido

