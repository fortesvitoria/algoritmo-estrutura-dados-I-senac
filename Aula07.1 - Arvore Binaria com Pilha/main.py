from arvore import Arvore

a = Arvore()

a.inserir( a.raiz, 48 )
a.inserir( a.raiz, 22 )
a.inserir( a.raiz, 17 )
a.inserir( a.raiz, 13 )
a.inserir( a.raiz, 64 )
a.inserir( a.raiz, 75 )
a.inserir( a.raiz, 52 )
a.inserir( a.raiz, 31 )
a.inserir( a.raiz, 19 )
a.inserir( a.raiz, 100 )

print( "\n--- Em Ordem (ERD) --------")
a.imprimirEmOrdem( a.raiz )
print( "\n--- Pré Ordem (RED)--------")
a.imprimirPreOrdem( a.raiz )
print( "\n--- Pós Ordem (EDR)--------")
a.imprimirPosOrdem( a.raiz )
print( "\n--- Ordem reversa (DRE) ---")
a.imprimirReverso( a.raiz )

print( "\n--- Impressão Iterativa com Pilha ---")
a.imprimirComPilha( a.raiz )