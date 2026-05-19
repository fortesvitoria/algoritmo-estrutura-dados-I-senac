from arvore import Arvore

arvore = Arvore()
arvore.inserir(arvore.raiz, 50)
arvore.inserir(arvore.raiz, 60)
arvore.inserir(arvore.raiz, 43)
arvore.inserir(arvore.raiz, 5)
arvore.inserir(arvore.raiz, 55)

print(f'--------  Em Ordem (ERD) --------')

arvore.imprimirEmOrdem(arvore.raiz)

print(f'\n--------  Pré Ordem (RED)  --------')
arvore.imprimirPreOrdem(arvore.raiz)

print(f'\n--------  Pós Ordem (EDR)  --------')
arvore.imprimirPosOrdem(arvore.raiz)

print(f'\n--------  Reverso (DRE)  --------')
arvore.imprimirReverso(arvore.raiz)