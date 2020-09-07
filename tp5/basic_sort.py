# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401

# basic_sort.py
from linkedlist import*

#····················································
def bubblesort(L):
    # i es la referencia del nodo que flota hasta el final
    for i in range(length(L)-1,0,-1):
        currentNodeFinal = L.head
        cont = 0
        # currentNodeFinal es nodo de refencia a flotar
        while currentNodeFinal!=None:
            if cont == i:
                break
            cont += 1
            currentNodeFinal = currentNodeFinal.nextNode
         
        currentNode = L.head
        while currentNode != currentNodeFinal:
            # si el nodo actual es mayor a siguiente se intercanvian los valores
            if currentNode.value > currentNode.nextNode.value:
                max = currentNode.value
                currentNode.value = currentNode.nextNode.value 
                currentNode.nextNode.value = max

            currentNode = currentNode.nextNode
#····················································
def selectionsort(L):
    # cont es el "indice" del menor en la seleccion
  cont=0
  while cont<length(L):
    menor = cont
    
    #guarda el indice del menor
    for i in range(cont,length(L)):
      if access(L,i)<access(L,menor):
        menor=i
    
    e1=access(L,menor)
    e2=access(L,cont)
    update(L,e2,menor)
    update(L,e1,cont)
    
    cont += 1
  return L
#····················································
def insertionsort(L):
    desordenado = 1 
    for i in range(desordenado,length(L)):
        for j in range(0,desordenado):
            if access(L,j) > access(L,desordenado):
                elemento = access(L,desordenado)
                delete(L,elemento)
                insert(L,elemento,j)
        desordenado += 1   
#····················································


# URL: https://repl.it/@BrunoFuentes/ordenamientos-basicos