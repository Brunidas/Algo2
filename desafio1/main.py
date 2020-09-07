# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/desafio1

'''
El enfoque tomado para este desafio de el usar una lista con prioridad, tomando como prioridad la distancia de ese nodo hasta el pivote.
Haciendo lo arreglos correspondietes 
'''

from algo1 import*
from binarytree import*
from print_tree import*
from avltree import*
from priorityqueue import*
from advanced_sort import*
'''
Desafío 1:
Dados 3 números enteros a, b y p , se dice que a es más cercano a p que b si y sólo si se
cumple: | a - p | < | b - p | donde |x| representa la función módulo.
De cumplirse | a - p | = | b - p | se dice que ambos números, a y b están a la misma distancia
de p .
Usted deberá implementar un método que ordene los elementos de un array de enteros por
orden de cercanía a un entero p dado, al que llamaremos pivote. En caso de que existan varios
elementos en el array a la misma distancia del elemento pivote, estos se deberán ordenar de
menor a mayor.
'''

def desafio_uno_enqueue_priority(Q,element,priority):
    cont = 0 
    currentNode = Q.head
    while currentNode!=None:
        if priority > currentNode.priority:
            insertPriorityQueue(Q, element,cont ,priority)
            return cont
        
        if  priority == currentNode.priority:
            insertPriorityQueue(Q, element,cont ,priority)
            return cont
        cont += 1
        currentNode = currentNode.nextNode

    insertPriorityQueue(Q, element,cont ,priority)
    return cont


def desafio_uno( array, pivote ):
    L = LinkedList()
    Q = PriorityQueue()

    # conventir el array en una lista 
    for i in range(0, len(array) ):
        add(L, array[i] )

    # encolo los elementos de Q en la lista L
    currentNode = L.head
    while currentNode!=None:
        prioridad = abs( currentNode.value - pivote )
        
        # modificado enqueue_priority para que teniedo un elemento 
        # con prioridad 3 por ej y va a encolas otro de prirodad 3 
        # el nuevo elento esta antes que el que ya estaba en la cola
        desafio_uno_enqueue_priority( Q, currentNode.value ,prioridad  )

        currentNode = currentNode.nextNode

    # borro los elemento de L
    L = LinkedList()


    # desencolo los elemento de Q para agregarlos a L
    for i in range( len(array) ):
        add( L, dequeue(Q) )


    # reordeno la lista a la forna correcta
    listaAux = LinkedList()
    voltearlista( L, listaAux )


    # conventir el array en una lista 
    for i in range(0, len(array) ):
        array[i] = access(listaAux, i)
    
    return (array)





array = Array(4,0)
array[0] = 2
array[1] = 10
array[2] = 8
array[3] = 4

print(array)

p = 7

desafio_uno( array, p )

print(array)