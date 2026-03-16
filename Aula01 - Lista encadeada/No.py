class No:
    def __init__(self, valor):
        self.dado = valor
        self.prox = None


# print(f"{"-"*5} Instancias da classe Nó {"-"*5}")
# node0=No("A")
# node1=No("C")
# node2=No("B")
# print(f"\n-- Dados:")
# print(node0.dado, node1.dado, node2.dado)

# print(f"\n-- Proximos:")
# print(node0.prox) #null
# node0.prox = node2.dado # A -> B
# node2.prox = node1.dado #B -> C e C -> Null
# print(node0.prox, node2.prox, node1.prox)

# print(f"\n-- Dados e próximos:")
# print(f"- Dado - Proximo -")
# print(f"-- {node0.dado} ------ {node0.prox} --")
# print(f"-- {node2.dado} ------ {node2.prox} --")
# print(f"-- {node1.dado} ------ {node1.prox}")

