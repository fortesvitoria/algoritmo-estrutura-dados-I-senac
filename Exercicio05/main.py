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

from Torre import Torre
from Apartamento import Apartamento
from FilaApt import Fila
from ListaApt import Lista

#criando estruturas
fila = Fila()
lista = Lista()

#criando torres
t1 = Torre(1,"Torre A","Rua A, nº 55")

#criando apts
a1 = Apartamento(1,101,t1)
a2 = Apartamento(2,102,t1)
a3 = Apartamento(3,103,t1) 
a4 = Apartamento(4,104,t1) 

#add na fila
fila.add(a1)
fila.add(a2)    
fila.add(a3)
fila.add(a4)

# Liberando vagas
print("\n--- Liberando vaga 1")
apt = fila.remover(1)
lista.add(apt)

# Liberando vagas
print("\n--- Liberando vaga 3")
apt = fila.remover(3)
lista.add(apt)

# Imprimir tudo
fila.imprimir()
lista.imprimir()

# Remover da lista
removido = lista.remover(102)
if removido:
    fila.add(removido)

# Imprimir tudo
fila.imprimir()
lista.imprimir()
