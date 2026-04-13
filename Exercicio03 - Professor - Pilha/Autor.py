'''
Faça um algoritmo que implementa uma pilha de livros
    - Cada livro deverá conter: 
        - Titulo; qtde paginas e autor
    O autor deverá conter:
        - Nome e ano de nascimento

        um autor pra muitos livros.
        um livro para um unico autor.

    Implemente os método: 
        - add livros na pilha; 
        - remover livro 
        - imprimir livro
        - e um metodo em que o usuario informa o nome do autor e é informado 
        quantos livros tem na pilha com este autor
'''

class Autor:
    def __init__(self, nome = "Não informado", ano = None):
        self._nome = nome  # fracamente privado, encapsulameto
        self.__ano = ano # fortemente privado, encapsulamento
    
    def __str__(self): 
        return f"{self._nome} ({self.__ano})"
    
    def setNome(self, nome): #Método modificador
        if nome != "":
            self._nome = nome
    
    def getNome(self): #Método acessor
        return self._nome
    
    @property #decorator - transforma o método em um atributo - encapsulamento    
    def ano(self): #Método acessor
        return self.__ano
    
    @ano.setter #setter - decorador - método modificador
    def ano(self, ano): #Método modificador
        if ano != '' and ano < 2026:
            self.__ano = ano
