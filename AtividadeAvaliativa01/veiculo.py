class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self): 
        return f"Marca: {self.marca}\nModelo: {self.modelo}"
    
    def imprimir(self):
        print(self) #retorna metorodo __str__()