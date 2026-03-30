'''
Exercício: implemente uma playlist musical utilizando lista duplamente encadeada, onde o objeto musica tem os seguintes atributos: titulo, autor e duração
- add musicas pela ordem crescente pelo titulo
'''
from Musica import Musica

class ListaMusica:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, titulo, autor, duracao):
        #criando lista por ordem de chegada
        musica = Musica(titulo, autor, duracao)

        if self.inicio is None:
            self.inicio = musica        
        else:
            self.fim.proximo = musica #proximo do fim recebe quem acaba de chegar
            musica.anterior = self.fim #quem acaba de chegar aponta pra quem era o fim
        
        self.fim = musica
        self.imprimir()

    #add no parametro uma musica default
    def addCrescente(self, musica = Musica("Sem Título", "Desconhecido", 0)):

        if self.inicio is None:
            self.inicio = musica
            self.fim = musica
        else:
            if musica.titulo < self.inicio.titulo: 
                musica.proximo = self.inicio
                self.inicio.anterior = musica
                self.inicio = musica
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if musica.titulo < aux.titulo: 
                        ant.proximo = musica
                        musica.anterior = ant
                        musica.proximo = aux
                        aux.anterior = musica
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux is None:
                    #add no fim da lista e no anterior aponta para o ultimo da lista
                    ant.proximo = musica
                    musica.anterior = ant  
                    self.fim = musica   
        
        self.imprimir()  
        

    def imprimir(self):
        print("\n---- Lista duplamente encadeada ----\n")
        if self.inicio is None:
            print("XXXX Playlist vazia XXXX\n")
            return 
        aux = self.inicio
        while aux: 
            print(aux)
            aux = aux.proximo
        print(f"{"-"*50}")

    
    def imprimirReverso(self):
        print("\n---- Lista duplamente encadeada ordem reversa ----\n")
        if self.inicio is None:
            print("XXXX Playlist vazia XXXX\n")
            return 
        aux = self.fim
        while aux: 
            print(aux)
            aux = aux.anterior
        print(f"{"-"*50}")
    
    def remover(self,valor):
        removeu = False
        if self.inicio == None:
            print("XXXX Playlist vazia XXXX\n")
        else: 
            if valor  == self.inicio.titulo: 
                self.inicio = self.inicio.proximo
                if self.inicio != None:
                    self.inicio.anterior = None 
                else:
                    self.fim = None
                removeu = True
            else:
                #variavel ant é variavel anteior, diferente do atributo anterior da classe nó
                ant = self.inicio 
                aux = self.inicio.proximo 
                while aux:
                    if valor == aux.titulo:
                        ant.proximo = aux.proximo 
                        if ant.proximo != None:
                            aux.proximo.anterior = ant 
                        else:
                            self.fim = ant
                        removeu = True
                        break
                    else:
                        ant  = aux
                        aux = aux.proximo
            if removeu:
                print(f"{valor} - Elemento removido!")
            else:
                print(f"{valor} - Não encontrado!")
            self.imprimir()