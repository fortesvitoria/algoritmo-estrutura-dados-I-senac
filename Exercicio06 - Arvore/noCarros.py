# Implemente uma árvore binária de carros, que serão ordenados pela placa
# Cada carro será composto por modelo, placa e ano

class Carros:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.esquerda = None
        self.direita = None