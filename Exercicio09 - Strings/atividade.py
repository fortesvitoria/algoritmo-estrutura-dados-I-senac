'''
Manipulação de Strings - Exercício
texto = "João da Silva - Rua A, 132; Maria dos Santos - Rua B, 225"
Construa um código em Python que manipule a string texto, a fim de construir um JSON conforme o exemplo a seguir
JSON = ' 
    [ 
        { 
             "nome" : "João da Silva" ,
             "endereco" : "Rua A" ,
             "numero" : "132" 
        } ,
        { 
            "nome" : "Maria dos Santos" , 
            "endereco" : "Rua B" ,
            "numero" :  "225"
        }
    ] '

'''

texto = "João da Silva - Rua A, 132; Maria dos Santos - Rua B, 225"

#cria uma lista vazia para armazenar os dados em formato JSON
dados_json = []

# separa os contatos por ponto e virgula, criando uma lista com nome e endereço de cada contato
contatos = texto.split(";")

#loop para separar os dados de cada contato e armazenar em formato JSON
for contato in contatos:
    #separa o nome do endereco com numero e armazena o nome em uma variavel
    lista_dados = contato.split("-")
    nome = lista_dados[0].strip()
    #armazena o endereco com numero em outra variavel
    endereco_completo = lista_dados[1]
    #separa endereco do numero através da virgula e armazena cada parte em uma variavel
    endereco = endereco_completo.split(",")[0].strip()
    numero = endereco_completo.split(",")[1].strip()
    #adiciona os dados no formato json usando o append
    dados_json.append ({
        "nome": nome,
        "endereco": endereco,
        "numero": numero
    })

print(dados_json)

for i in range(len(dados_json)):
    print(f"\n------------------------------------")
    print(f"Contato {i+1}:")
    print(f"Nome: {dados_json[i]['nome']}")
    print(f"Endereço: {dados_json[i]['endereco']}")
    print(f"Número: {dados_json[i]['numero']}")