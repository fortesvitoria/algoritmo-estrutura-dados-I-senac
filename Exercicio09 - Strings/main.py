#1. Receba um nome e exiba-o em maiúsculas e minúsculas.
nome = input("Digite um nome: ")
print(nome.upper())
print(nome.lower())


#2. Conte quantas vezes uma letra aparece em uma frase.
frase = "Algotimos e estrutura de dados"
print(f"A letra 'a' foi encontrada {frase.lower().count("a")}") #transforma em lower para pegar maisculas e minusculas


#3. Verifique se uma string representa um número inteiro.        
palavra = input("Digite uma palavra para verificar se é um número inteiro: ")
palavra.isnumeric()
print(f"A palavra '{palavra}' é um número inteiro? {palavra.isnumeric()}")

#4. Inverta uma string utlizando fatiamento.
texto = input("Digite uma palavra para ser escrita ao contrário: ")
print(f"A palavra {texto} ao contrário é: {texto[::-1]}")