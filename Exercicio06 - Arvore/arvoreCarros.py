# Implemente uma árvore binária de carros, que serão ordenados pela placa
# Cada carro será composto por modelo, placa e ano
# Implemente um Menu com as seguintes opções:
# -> 1) Adicionar carro
# -> 2) Imprimir em ordem (ERD)
# -> 3) Imprimir pré ordem (RED)
# -> 4) Imprimir pós ordem (EDR)
# -> 5) Imprimir ordem reversa (DRE)
# -> 6) Imprimir em nível reversa (DRE) ****
# -> 7) Procurar carro
# -> 0) Sair
# A opção 7 deverá perguntar ao usuário a placa do carro e informar se o carro está
# na árvore. Informe ao usuário, quantas iterações foram necessárias para encontrar
# ou não o carro

from noCarros import Carros

class ArvoreCarros:
    def __init__(self):
        self.raiz = None

# -> 1) Adicionar carro
    def inserir(self, raiz: Carros, placa, modelo, ano): #a raiz aqui é o parametro, de cada execução, nao a raiz da classe, aqui faço a tipagem, informo que recebo sempre um nó, diferente de valor dfault
        if raiz is None: #se raiz vazia, cria instancia do no
            carro = Carros(placa, modelo, ano)
            if self.raiz is None: #se a raiz da classe for vazia, atribui o nodo criado a raiz da classe
                self.raiz = carro
            return carro
        
        if placa < raiz.placa: #se o valor for menor que o valor da raiz, chama a função recursivamente para a subarvore esquerda
            raiz.esquerda = self.inserir(raiz.esquerda, placa, modelo, ano)
        if placa > raiz.placa: #se o valor for maior que o valor da raiz, chama a função recursivamente para a subarvore direita
            raiz.direita = self.inserir(raiz.direita, placa, modelo, ano)
        return raiz
    
# -> 2) Imprimir em ordem (ERD)
    def imprimirEmOrdem(self, raiz: Carros): #Esqueda/Raiz/Direita
        if raiz is not None:
            self.imprimirEmOrdem(raiz.esquerda) #esqueda
            print(raiz.placa, end=' - ') #raiz
            self.imprimirEmOrdem(raiz.direita) #direita

# -> 3) Imprimir pré ordem (RED)
    def imprimirPreOrdem(self, raiz: Carros): #Raiz/Esquerda/Direita
        if raiz is not None:
            print(raiz.placa, end=' - ')
            self.imprimirPreOrdem(raiz.esquerda)
            self.imprimirPreOrdem(raiz.direita)

# -> 4) Imprimir pós ordem (EDR)
    def imprimirPosOrdem(self, raiz: Carros): #Esquerda/Direita/Raiz
        if raiz is not None:
            self.imprimirPosOrdem(raiz.esquerda)
            self.imprimirPosOrdem(raiz.direita)
            print(raiz.placa, end=' - ')

# -> 5) Imprimir ordem reversa (DRE)
    def imprimirReverso(self, raiz: Carros): #Direita/Raiz/Esquerda
        if raiz is not None:
            self.imprimirReverso(raiz.direita)
            print(raiz.placa, end=' - ')
            self.imprimirReverso(raiz.esquerda)

# -> 7) Procurar carro
    def procurarCarro(self, raiz: Carros, placa, iteracoes=0):
        iteracoes += 1 # Conta a iteração atual
        
        if raiz is None:
            return None, iteracoes
        
        if raiz.placa == placa:
            return raiz, iteracoes
        
        if placa < raiz.placa:
            return self.procurarCarro(raiz.esquerda, placa, iteracoes)
        else:
            return self.procurarCarro(raiz.direita, placa, iteracoes)