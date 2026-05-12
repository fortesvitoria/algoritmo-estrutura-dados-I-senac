'''
Construa um software em Python que implemente uma Pilha de carros e uma Pilha de drones.

As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes.

A classe carro é composta dos atributos marca, modelo e portas. O atributo portas é fortemente privado.

A classe drone é composta dos atributos marca, modelo e quantidade de hélices. O atributo quantidade de hélices é fracamente privado.

Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.

Implemente uma tela com um menu (funcionando) que permita ao usuário:

-> Adicionar e remover carros da Pilha.

-> Adicionar e remover drones da Pilha.

-> Imprimir a Pilha de carros e a Pilha de drones.

Cole todo código desenvolvido, em sequência, separando as classes por uma linha.
'''

from PilhaDrone import PilhaDrone
from PilhaCarro import PilhaCarro
from drone import Drone
from carro import Carro
from veiculo import Veiculo

#criando estrutura drones
pilhaDrone = PilhaDrone()

#criando veiculo
v1 = Veiculo("Samsung", "A58954-1")

#criando drones
d1 = Drone()
d2 = Drone(3, v1)

#adicionando itens
pilhaDrone.add(d2)
pilhaDrone.add(d1)

pilhaDrone.imprimir()

pilhaDrone.remover()

#---------------------------------


#criando estrutura carros
pilhaCarro = PilhaCarro()

#criando veiculo
v2 = Veiculo("Fiat", "Doblo")

#criando Carros
c1 = Carro()
c2 = Carro(4, v2)

#adicionando itens
pilhaCarro.add(c2)
pilhaCarro.add(c1)

pilhaCarro.imprimir()

pilhaCarro.remover()


#----------------------------------

#MENU


def menu():
    print("\n------------- Menu ------------\n")
    print("1 - Adicionar Drone")
    print("2 - Remover Drone")
    print("3 - Adicionar Carro")
    print("4 - Remover Carro")
    print("5 - Imprimir Drones")
    print("6 - Imprimir Carros")
    print("0 - Sair")
    print("\n------------------------------\n")

    op = input("Digite a opção desejada: ")
    return op

opcao = -1
while opcao != "0":
    opcao = menu()
    if opcao == "1":
        helices = int(input("Digite o número de hélices: "))
        marca = input("Digite a marca do Drone: ")
        modelo = input("Digite o modelo do Drone: ")
        novoVeiculo = Veiculo(marca,modelo)
        novoDrone = Drone(helices,novoVeiculo)
        pilhaDrone.add(novoDrone)
    if opcao == "2":
        pilhaDrone.remover()
    if opcao == "3":
        portas = int(input("Digite o número de portas: "))
        marca = input("Digite a marca do Carro: ")
        modelo = input("Digite o modelo do Carro: ")
        novoVeiculo = Veiculo(marca,modelo)
        novoCarro = Carro(portas,novoVeiculo)
        pilhaCarro.add(novoCarro)
    if opcao == "4":
        pilhaCarro.remover()
    if opcao == "5":
        pilhaDrone.imprimir()
    if opcao == "6":
        pilhaCarro.imprimir()
    if opcao == "0":
        print("Saindo do programa...")