# Implemente uma árvore binária de carros, que serão ordenados pela placa
# Cada carro será composto por modelo, placa e ano
# Implemente um Menu com as seguintes opções:
# -> 1) Adicionar carro
# -> 2) Imprimir em ordem (ERD)
# -> 3) Imprimir pré ordem (RED)
# -> 4) Imprimir pós ordem (EDR)
# -> 5) Imprimir ordem reversa (DRE)
# -> 6) Imprimir em nível reversa (DRE)
# -> 7) Procurar carro
# -> 0) Sair
# A opção 7 deverá perguntar ao usuário a placa do carro e informar se o carro está
# na árvore. Informe ao usuário, quantas iterações foram necessárias para encontrar
# ou não o carro

from arvoreCarros import ArvoreCarros

arvore = ArvoreCarros()


opcao = -1
while opcao != 0:

    print("\n===== MENU =====")
    print("1 - Adicionar carro")
    print("2 - Em Ordem")
    print("3 - Pré Ordem")
    print("4 - Pós Ordem")
    print("5 - Ordem Reversa")
    print("7 - Procurar carro")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        print("1 - Adicionar carro:")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))

        arvore.inserir(arvore.raiz, placa, modelo, ano)

    elif opcao == 2:
        print("2 - Em Ordem:")
        arvore.imprimirEmOrdem(arvore.raiz)
        print()

    elif opcao == 3:
        print("3 - Pré Ordem:")     
        arvore.imprimirPreOrdem(arvore.raiz)
        print()

    elif opcao == 4:
        print("4 - Pós Ordem")
        arvore.imprimirPosOrdem(arvore.raiz)
        print()

    elif opcao == 5:
        print("5 - Ordem Reversa")
        arvore.imprimirReverso(arvore.raiz)
        print()

    elif opcao == 7:
        placa = input("Informe a placa: ")
        carro_encontrado, iteracoes = arvore.procurarCarro(arvore.raiz, placa)
        
        print("\n" + "-"*30)
        if carro_encontrado is not None:
            print("Carro ENCONTRADO na árvore!")
            print(f"Modelo: {carro_encontrado.modelo}")
            print(f"Ano: {carro_encontrado.ano}")
        else:
            print("Carro NÃO encontrado na árvore.")
        
        print(f"Iterações necessárias: {iteracoes}")

        