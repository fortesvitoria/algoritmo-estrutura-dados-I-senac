from veiculo import Veiculo

class Carro:
    def __init__(self, portas = 0, veiculo = Veiculo(marca = "Sem marca", modelo = "Sem modelo"), proximo = None):
        self.__portas = portas
        self.veiculo = veiculo
        self.proximo = proximo

    def __str__(self): 
        return f"------- Carro ------- \n{self.veiculo} \nQuantidade de portas: {self.__portas}"
    
    def imprimir(self):
        print(self) #retorna metorodo __str__()
