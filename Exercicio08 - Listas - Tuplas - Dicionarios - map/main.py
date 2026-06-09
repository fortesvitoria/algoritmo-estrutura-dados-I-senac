'''
Exercícios
1) Construa um algoritmo que possua uma tupla com os números escritos
por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
condicionais (if e switch).
'''

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")

numero = int(input("Digite um número de um a nove: "))

print(numeros[numero])



'''
▷2) Construa um algoritmo que peça ao usuário para informar o nome, a
nota01 e a nota02 de um aluno. Guarde estas informações em um
dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
e adicione ao dicionário. Ao final, imprima todos os dados do
dicionário.
'''
dic = {}

nome = input("Digite seu nome: ")

dic["Nome"] = nome

for i in range(2):
    nota = float(input(f"Digite a nota {i+1}: "))
    dic[f"Nota{i+1}"] = nota

calc = (dic['Nota1'] + dic['Nota2'])/2

print(f"Nome: {dic['Nome']}, Nota1: {dic['Nota1']}, Nota2: {dic['Nota2']}, Nota final: {calc}")