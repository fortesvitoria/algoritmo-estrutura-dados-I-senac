from node import Node

#lista = []
#lista.append(7)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        if self.head: 
            #inseção quando a lista já possui elementos
            pointer = self.head #pointer (aux) recebe head(inicio)

            while(pointer.next): #enquanto houver proximo
                pointer = pointer.next 
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)
        self.size = self.size + 1