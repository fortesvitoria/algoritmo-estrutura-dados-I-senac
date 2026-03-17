'''
Exercício 01: 
Construa uma lista encadeada de pessoas em que cada nó possui nome e idade.
A inserção deve ser por ordem decrescente de idade.

'''

from Pessoa import Pessoa

class Lista:
    def __init__(self):
        self.inicio = None #Inicia a lista com valor nulo

    def add(self, nome, idade): 
        pessoa = Pessoa( nome, idade) #guarda memoria uma instancia da classe pessoa com nome e idade

        if self.inicio is None: #verifica se vazia 
            self.inicio = pessoa #se estiver vazia, add o valor da instacia da classe Pessoa

        else:
            if pessoa.idade > self.inicio.idade: #se o idade do pessoa é maior que inicio 
                pessoa.prox = self.inicio #prox da pessoa recebe o que esta no inicio 
                self.inicio = pessoa #inicio recebe pessoa

            else: 
                ant = self.inicio #
                aux = self.inicio.prox #aux recebe o prox do inicio 

                while aux : #enquanto existir aux, continua
                    if pessoa.idade > aux.idade: #Se a idade da pessoa for menor que o idade do auxiliar 
                        pessoa.prox = aux #proximo recebe aux
                        ant.prox = pessoa #anterior do proximo recebe pessoa 
                        break 
                    else:
                        ant = aux #anterior recebe aux
                        aux = aux.prox #aux recebe o proximo

                if aux == None:
                    ant.prox = pessoa #proximo do anterior recebe pessoa

            self.imprimir()

    def imprimir(self):
        print("\n---- Lista encadeada ----\n")
        if self.inicio is None:
            print("XXXX Lista vazia XXXX\n")
            return 
        aux = self.inicio
        while aux: 
            print(f"Nome: {aux.nome},Idade: {aux.idade}")
            aux = aux.prox
        print(f"{"-"*25}")

    def remover(self,valor): #remove pelo nome
        removeu = False
        if self.inicio == None:
            print("XXXX Lista vazia XXXX\n")
        else: 
            #verifica se o valor está na primeira posição
            if valor  == self.inicio.nome: 
                self.inicio = self.inicio.prox # o inicio passa a ser o proximo do inicio
                removeu = True
            else: # quando a lista nao for vazia e quando o valor não é igual ao primeiro - testa a partir do segundo elemento
                ant = self.inicio #inicio ja testado
                aux = self.inicio.prox #testando o segundo elemento
                while aux: #enquanto aux for diferente de null/enquanto existir
                    if valor == aux.nome:
                        ant.prox = aux.prox #elemento anterior aponta para o proximo do que sera deletado
                        removeu = True
                        break
                    else:
                        # auxiliar nao é igual ao valor que quero remover, testo o proximo. estrutura para seguir percorrendo a lista
                        ant  = aux
                        aux = aux.prox
            if removeu:
                print(f"{valor} - Elemento removido!")
            else:
                print(f"{valor} - Não encontrado!")
            self.imprimir()