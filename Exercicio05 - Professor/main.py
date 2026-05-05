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
from Fila import Fila
from Lista import Lista

#criando estruturas
fila = Fila()
lista = Lista()

#criando torres
t1 = Torre(1, "Torre B", "Rua B, nº 55")

#criando apts
a1 = Apartamento(1,"101",t1,1)
a2 = Apartamento(2,"102",t1,2)
a3 = Apartamento(3,"103",t1,3) 
a4 = Apartamento(4,"104",t1) 

# adicionando itens
lista.add(a1)
lista.add(a2)   
lista.add(a3)
fila.add(a4)

# # Liberando vagas
# print("\n--- Liberando vaga 1")
# apt = fila.remover(1)
# lista.add(apt)

# # Liberando vagas
# print("\n--- Liberando vaga 3")
# apt = fila.remover(3)
# lista.add(apt)

# # Imprimir tudo
# fila.imprimir()
# lista.imprimir()

# # Remover da lista
# removido = lista.remover(102)
# if removido:
#     fila.add(removido)

# # Imprimir tudo
# fila.imprimir()
# lista.imprimir()

def menu():
    print("\n------------- Menu ------------\n")
    print("1 - Adicionar apartamento")
    print("2 - Liberar vaga de garagem")
    print("3 - Imprimir lista de apartamentos")
    print("4 - Imprimir fila de apartamentos")
    print("0 - Sair")
    print("\n------------------------------\n")

    op = input("Digite a opção desejada: ")
    return op

opcao = -1
while opcao != "0":
    opcao = menu()
    if opcao == "1":
        id = int(input("Digite o id do apartamento: "))
        numeroApt = input("Digite o número do apartamento: ")
        novoAp = Apartamento(id, numeroApt, t1)
        fila.add(novoAp)
    if opcao == "2":
        numeroVaga = int(input("Digite o número da vaga a ser liberada: "))
        aptPerdeuVaga = lista.remover(numeroVaga)
        if aptPerdeuVaga:
            aptPerdeuVaga.numeroVaga = None
            fila.add(aptPerdeuVaga)
            apGanhouVaga = fila.remover(numeroVaga)
            if apGanhouVaga:
                apGanhouVaga.numeroVaga = numeroVaga
                lista.add(apGanhouVaga)
    if opcao == "3":
        lista.imprimir()
    if opcao == "4":
        fila.imprimir()
    if opcao < 0 or opcao > 4:
        print("Opção inválida! Tente novamente.")
    if opcao == "0":
        print("Saindo do programa...")