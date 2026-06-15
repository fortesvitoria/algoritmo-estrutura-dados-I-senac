txt = "Python"
txt1 = "algoritmo de dados"
txt2 = "DADOS"
txt3 = "   Python   "

print(txt[1])  # Printa o segundo caractere da string
print(txt[-1])  # Printa o último caractere da string
print(txt[1:])  # Printa a string a partir do segundo caractere até o final
print(txt[2:5])  # Printa os caracteres do terceiro ao quinto da string
print(txt[:3])  # Printa os três primeiros caracteres da string
print(txt[::-1])  # Printa a string em ordem inversa

print("th" in txt)  # Verifica se a letra "th" está presente na string
print("ab" in txt)  # Verifica se a letra "ab" está presente na string
print("th" not in txt)  # Verifica se a letra "th" não está presente na string
print("ab" not in txt)  # Verifica se a letra "ab" não está presente na string

print(txt.upper())  # Converte a string para maiúscula
print(txt.lower())  # Converte a string para minúscula
print(txt1.swapcase())  # Inverte a caixa das letras da string
print(txt2.swapcase())  # Inverte a caixa das letras da string 
print(txt1.capitalize())  # Converte a primeira letra da string para maiúscula e as demais para minúscula
print(txt1.title())  # Converte a primeira letra de cada palavra da string para maiúsc

print(txt3.strip())  # Remove os espaços em branco do início e do final da string
print(txt3.lstrip())  # Remove os espaços em branco do início da string
print(txt3.rstrip())  # Remove os espaços em branco do final da string

url = "http://www.google.com"
print(url.startswith("http"))  # Verifica se a string começa com "http"
print(url.endswith(".com"))  # Verifica se a string termina com ".com"
print(url.removeprefix("http://"))  # Remove o prefixo "http://" da string
print(url.removesuffix(".com"))  # Remove o sufixo ".com" da string
print(url.removeprefix("http://").removesuffix(".com"))  # Tenta remover o prefixo "https://" da string (não presente)

print(txt.find("ho")) # Retorna o índice da primeira ocorrência da substring "ho" na string, ou -1 se não for encontrada
print(txt.find("ab")) # Retorna o índice da primeira ocorrência da substring "ab" na string, ou -1 se não for encontrada
print(txt1.count("o")) # Retorna o número de vezes que a substring "o" aparece na string

print(txt.replace("th", "thho")) #Troca as letras escolhidas
print(txt.maketrans('o', '0')) #Cria uma tabela de tradução para substituir caracteres
print(txt.translate(txt.maketrans('o', '0'))) #Aplica a tabela de tradução à string

lista = "Joao; Maria; Pedro"
print(lista.split(";")) # Divide a string em uma lista de substrings usando o delimitador ";"
print(lista.partition(";")) # Divide a string em três partes usando o delimitador ";": a parte antes do delimitador, o delimitador em si e a parte depois do delimitador
separador = "-"
print(separador.join(["Julia", "Carlos", "Ana"])) # Junta os elementos da lista em uma única string, usando o separador "-" entre eles

print(txt.isalpha()) # Verifica se todos os caracteres da string são letras
print(txt.isdigit()) # Verifica se todos os caracteres da string são dígitos
txt4 = "123"
txt5 = "123abc"
print(txt4.isdigit()) # Verifica se todos os caracteres da string são dígitos
print(txt5.isdigit()) # Verifica se todos os caracteres da string são dígitos
print(txt4.isalnum()) # Verifica se todos os caracteres da string são alfanuméricos (letras ou dígitos
print(txt5.isalnum()) # Verifica se todos os caracteres da string são alfanuméricos (letras ou dígitos)
print(txt4.isnumeric()) # Verifica se todos os caracteres da string são numéricos
print(txt5.isnumeric()) # Verifica se todos os caracteres da string são numéricos

txt.islower() # Verifica se todos os caracteres da string estão em minúscula
txt.isupper() # Verifica se todos os caracteres da string estão em maiúscula

txt1.isspace() # Verifica se todos os caracteres da string são espaços em branco
txt2.isspace() # Verifica se todos os caracteres da string são espaços em branco

