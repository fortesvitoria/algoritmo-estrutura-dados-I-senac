from veiculo import Veiculo

class Drone:
    def __init__(self, helices = 0, veiculo = Veiculo(marca = "Sem marca", modelo = "Sem modelo"), proximo = None):
        self.__helices = helices
        self.veiculo = veiculo
        self.proximo = proximo

    def __str__(self): 
        return f"------- Drone ------- \n{str(self.veiculo)} \nQuantidade de hélices: {self.__helices}"
    
    def imprimir(self):
        print(self) #retorna metorodo __str__()