'''
--> 1) Construa a classe Torre e a classe Apartamento. 
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

class Torre:
    def __init__(self, id, nome, endereco):
        self.__id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self): 
        return f"Nome: {self.nome} - Endereço: {self.endereco}"