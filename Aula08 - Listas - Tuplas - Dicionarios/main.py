carro01 = {
    "modelo": "Doblo",
    "ano": 2006,
}

carro02 = {
    "modelo": "Renegade",
    "ano": 2021,
}

carro03 = {
    "modelo": "Pulse",
    "ano": 2024,
}

carro03["placa"] = "ABC-1234"

# print(carro03)

frota = carro01, carro02
print(frota) #printa uma tupla com os dicionarios, a tupla é imutavel, ou seja, não pode ser alterada, mas os dicionarios dentro dela podem ser alterados.
carro01["modelo"] = "Uno Mille" #alterando o modelo do carro01, isso é permitido, pois o dicionario é mutavel.
# print(frota[0])
print(frota)

#frota[0] = carro03 #isso não é permitido, pois a tupla é imutavel, mas podemos alterar os dicionarios dentro dela. Se fosse uma lista, isso seria permitido.


def calcular(x,y):
    return x+y, x-y, x*y, x/y

result = calcular(5,2)
print(result) #retorna uma tupla

a,b,c,d = result #desempacotamento de tupla, atribuindo cada valor da tupla a uma variavel
print(f"Soma: {a}, Subtração: {b}, Multiplicação: {c}, Divisão: {d}")

print("------------------- função map -------------------")

def printNome(nome):
    print(f"Olá, {nome}!")

def somarValores(valores):
    total = 0
    for i in valores:
        total += i
    return total

numeros = ((1,2), [1,2,3], [10,20,30,40])

somas = map(somarValores, numeros) #aplica a função somarValores em cada elemento da tupla numeros, retornando um iterador com os resultados
print(list(somas)) #transforma o iterador em uma lista para imprimir os resultados

nomes = ["João", "Maria", "Pedro"]
# x = map(printNome, nomes) #aplica a função printNome em cada elemento da lista nomes, retornando um iterador com os resultados
list(map(printNome, nomes)) #transforma o iterador em uma lista para imprimir os resultados, nesse caso, a função printNome não retorna nada, então a lista será composta por None
