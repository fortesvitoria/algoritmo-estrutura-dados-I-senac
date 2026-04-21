def somarAte(n = 0):
    if n == 0:
        return 0
    else:
        return n + somarAte(n - 1)

# print(f"Resultado da soma de 0 até 5: {somarAte(2)}")

def fatorial(n = 0):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# print(f"Resultado do fatorial de 5: {fatorial(2)}")

'''
Exercicio01:
Peça ao usuario que informe um valor, e então usando recursividade, 
imprima os termos da sequencia fibonacci de 0 até o este valor.

Pesquisa internet:
A sequência é definida mediante a seguinte fórmula: Fn = Fn-1 + Fn-2.

Onde:
Fn é o n-ésimo termo da sequência de Fibonacci.
Fn-1 é o termo anterior ao n-ésimo termo, antecedente ao n-ésimo termo.
Fn-2 é o termo anterior ao termo anterior ao n-ésimo termo. Ou seja, duas posições antes do n-ésimo termo.

'''

#Classico
def fibonacci(n = 0):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    
    
# print(fibonacci(11))
# for i in range(11):
#     print(f"Sequencia exemplo 1: {fibonacci(i)}")

#Professor:
def fibonacci2(a,b,n):
    if a > n:
        return 
    print(a)
    fibonacci2(b, a+b, n) #o a é o b e o b é a soma de ambos, ou seja, o proximo numero da sequencia

# valor = int(input("Informe um valor: "))

# fibonacci2(0,1,valor)

'''
Exericicios:
1) Implemente uma funcao recursiva para calculo de potencia
2) Implemente uma funcao recursiva para contagem regressiva
3) Implemente uma funcao recursiva para inverter uma string
'''