
# 1) Implemente uma funcao recursiva para calculo de potencia
# def calcPotencia(n,x):
#     if x == 0:
#         return 1
#     else:
#         # return n ** x
#         return n * calcPotencia(n, x-1)

# valor = int(input("Digite um numero: "))
# potencia = int(input("Digite a potencia: "))

# print(f"Resultado de {valor}^{potencia}: {calcPotencia(valor,potencia)}")


#2) Implemente uma funcao recursiva para contagem regressiva
# def regressiva(n):
#     if n == 0:
#         return 0
#     else:
#        print(f'Contagem regressiva: {n}')
#        return regressiva(n-1)

# print(f'Contagem regressiva: {regressiva(10)}')



#3) Implemente uma funcao recursiva para inverter uma string
def reverteString(t):
    if t == "":
        return t
    else:
        return reverteString(t[1:]) + t[0] #slicing, começa no 1, guarda o zero (primeira letra) para colocar no final.

print(reverteString("Vitoria"))

