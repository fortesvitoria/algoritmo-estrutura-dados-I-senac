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

# 1. Setup inicial
t1 = Torre(1, "Torre A", "Rua das Flores, 123")
lista_vagas = Lista()
fila_espera = Fila()

# Criando alguns apartamentos
apt1 = Apartamento(101, "101", 10, t1) # Já tem vaga 10
apt2 = Apartamento(102, "102", 5, t1)  # Já tem vaga 5
apt3 = Apartamento(201, "201", "Aguardando", t1) # Sem vaga

# Adicionando na lista ordenada (o 102 deve vir antes do 101)
lista_vagas.add(apt1)
lista_vagas.add(apt2)
fila_espera.add(apt3)

print("ESTADO INICIAL:")
lista_vagas.imprimir()
fila_espera.imprimir()

# 2. PROCESSO DE TROCA (Requisito 3)
print("\n--- O Apt 102 está saindo e liberando a vaga 5 ---")
liberado = lista_vagas.remover("102") # Remove o 102 que tinha a vaga 5

if liberado:
    vaga_livre = liberado.numeroVaga
    liberado.numeroVaga = "Aguardando vaga"
    fila_espera.add(liberado) # Vai para o fim da fila
    
    # Primeiro da fila ganha a vaga
    proximo = fila_espera.remover(vaga_livre)
    if proximo:
        lista_vagas.add_ordenado(proximo)

print("\nESTADO FINAL:")
lista_vagas.imprimir()
fila_espera.imprimir()