from no import No

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, raiz: No, valor): #a raiz aqui é o parametro, de cada execução, nao a raiz da classe, aqui faço a tipagem, informo que recebo sempre um nó, diferente de valor dfault
        if raiz is None: #se raiz vazia, cria instancia do no
            nodo = No(valor)
            if self.raiz is None: #se a raiz da classe for vazia, atribui o nodo criado a raiz da classe
                self.raiz = nodo
            return nodo
        
        if valor < raiz.valor: #se o valor for menor que o valor da raiz, chama a função recursivamente para a subarvore esquerda
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        if valor > raiz.valor: #se o valor for maior que o valor da raiz, chama a função recursivamente para a subarvore direita
            raiz.direita = self.inserir(raiz.direita, valor)
        return raiz
    
    def imprimirEmOrdem(self, raiz: No): #Esqueda/Raiz/Direita
        if raiz is not None:
            self.imprimirEmOrdem(raiz.esquerda) #esqueda
            print(raiz.valor, end=' - ') #raiz
            self.imprimirEmOrdem(raiz.direita) #direita

    def imprimirPreOrdem(self, raiz: No): #Raiz/Esquerda/Direita
        if raiz is not None:
            print(raiz.valor, end=' - ')
            self.imprimirPreOrdem(raiz.esquerda)
            self.imprimirPreOrdem(raiz.direita)
    
    def imprimirPosOrdem(self, raiz: No): #Esquerda/Direita/Raiz
        if raiz is not None:
            self.imprimirPosOrdem(raiz.esquerda)
            self.imprimirPosOrdem(raiz.direita)
            print(raiz.valor, end=' - ')
    
    def imprimirReverso(self, raiz: No): #Direita/Raiz/Esquerda
        if raiz is not None:
            self.imprimirReverso(raiz.direita)
            print(raiz.valor, end=' - ')
            self.imprimirReverso(raiz.esquerda)