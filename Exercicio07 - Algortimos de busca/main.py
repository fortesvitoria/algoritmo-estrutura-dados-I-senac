'''
Desafio
1) Construa um algoritmo de busca contendo um vetor de números 
inteiros de 20 posições. 
2) O algoritmo deve ter duas funções, uma para busca sequencial e 
outra para busca binária.
3) Coloque um contador em cada função para contar as iterações de 
cada função.
4) Peça ao usuário que informe o valor que deseja procurar.
5) Então informe ao usuário se este valor existe no vetor e quantas 
iterações foram necessárias em cada função.

'''

# 1 - vetor de números inteiros de 20 posições
vetor = [10,20,30,40,55,66,77,88,99,100,110,121,132,145,156,168,179,180,190,201]

tamVetor = len(vetor)

# 4 - usuario informa valor
numero = int(input('Digite um numero: '))

# 2.1 - busca sequencial
def buscaSeq(vetor, numero):
    # 3 - contador
    count = 0
    for i in range(tamVetor):
        count += 1
        print(f"contador: {count}")
        if vetor[i] == numero:
            return i
    return -1

# 5 - mostra se o valor existe e numero de iterações
print(buscaSeq(vetor,numero))

# 2.2 - busca binaria
def buscaBin(vetor, numero):
    inicio = 0
    fim = tamVetor - 1
    # 3 - contador
    count = 0
    while inicio <= fim:
        count += 1
        print(f"contador: {count}")
        
        centro = round(inicio+(fim-inicio)/2)
        if numero == vetor[centro]:
            return centro
        elif (numero > vetor[centro]):
            inicio = centro + 1
        else:
            fim = centro -1
    return -1

# 5 - mostra se o valor existe e numero de iterações
print(buscaBin(vetor,numero))