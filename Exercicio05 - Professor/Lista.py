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
            if apartamento.numeroVaga < self.inicio.numeroVaga:
                apartamento.prox = self.inicio
                self.inicio = apartamento
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if apartamento.numeroVaga < aux.numeroVaga:
                        apartamento.prox = aux
                        ant.prox = apartamento
                        break
                    else:
                        ant = aux
                        aux = aux.prox  
                if aux is None:
                    ant.prox = apartamento
        print(f"Apartamento nº {apartamento.numeroApt} adicionado!")

    def imprimir(self):
        print("\n---- Lista de apartamentos ----\n")
        if self.inicio is None:
            print("---- Lista de apartamentos vazia ----\n")
            return 
        aux = self.inicio
        while aux: 
            print(aux)
            aux = aux.prox
            print("-" * 10)

    def remover(self,numeroVaga):
        apRemovido = None
        if self.inicio == None:
            print("---- Lista vazia ----\n")
        else: 
            if numeroVaga  == self.inicio.numeroVaga: 
                apRemovido = self.inicio
                self.inicio = self.inicio.prox 
 
            else: 
                ant = self.inicio
                aux = self.inicio.prox 
                while aux: 
                    if numeroVaga == aux.numeroVaga:
                        ant.prox = aux.prox 
                        apRemovido = aux
                        break
                    else:                       
                        ant  = aux
                        aux = aux.prox
            if apRemovido:
                print(f"Apartamento nº {apRemovido.numeroApt} removido!")
                apRemovido.prox = None
            else:
                print(f"Apartamento vaga nº {numeroVaga} não encontrado!")
        return apRemovido