# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401

from algo1 import *
from linkedlist import *
from stack import*
from queue import*


"""Ejercicio 3
A partir de las estructuras definidas como:
"""
class PriorityQueue():
    head=None

class PriorityNode():
    value=None
    nextNode=None
    priority=None
# Imprimir una PriorityQueue
def printPriorityQueue(L):
    cadena = ""
    """➜"""
    currentNode = L.head
    while( currentNode != None):
        cadena = cadena + str( currentNode.value )+"("+ str(currentNode.priority)+")" + ' ➜ ' 

        currentNode = currentNode.nextNode
    cadena = cadena + "None"
    print(cadena)

"""
Crear un módulo de nombre priorityqueue.py que implemente una cola con prioridad. Una cola con prioridad es un TAD similar a una cola en la que los elementos tienen adicionalmente, una prioridad asignada. En una cola de prioridades un elemento con mayor prioridad será desencolado antes que un elemento de menor prioridad. Si dos elementos tienen la misma prioridad, se desencolarán siguiendo el orden de cola.

enqueue(Q,element,priority) 
Descripción: Agrega un elemento a  Q con la prioridad priority (entero), siendo Q una estructura de tipo PriorityQueue 
Entrada: La cola Q sobre la cual se quiere agregar el elemento (PriorityQueue), el valor del elemento (element) a  agregar y un número que indica la prioridad.
Salida:  Devuelve la posición donde se inserto el elemento.

dequeue(Q)
Descripción: extrae el primer elemento de la cola Q con la la mayor prioridad (un valor mayor del campo priority, indica una mayor prioridad), siendo Q una estructura de tipo PriorityQueue
Poscondición: Se debe desvincular el Node a eliminar.  
Entrada: la cola sobre el cual se quiere realizar la eliminación (PriorityQueue)
Salida:  Devuelve el elemento con mayor prioridad. Devuelve None si la cola está vacía.
"""
def insertPriorityQueue(Q, element, position, prioridad):
    nuevoNodo = PriorityNode()
    nuevoNodo.value = element
    nuevoNodo.priority = prioridad
    #inserta el elemento en la primera posicion 
    if (position == 0):
        nuevoNodo.nextNode = Q.head
        Q.head = nuevoNodo
    
    # si la posicion a insertar es en nodo "None"  el nodo se insertara ahi
    # y la lista tendra un nodo mas 
    elif position == length(Q):

        currentNode = Q.head
        while( currentNode != None):
            if ( currentNode.nextNode == None):
                currentNode.nextNode = nuevoNodo
                break
            currentNode = currentNode.nextNode
        
    #inserta el elemento en la position y desplaza los demas elementos 
    elif position < length(Q) :

        cont=1
        currentNode = Q.head
        while( currentNode != None):
            if cont == position:
                nuevoNodo.nextNode = currentNode.nextNode
                currentNode.nextNode = nuevoNodo
                break
            cont += 1
            currentNode = currentNode.nextNode
        return cont


def enqueue_priority(Q,element,priority):
    cont = 0 
    currentNode = Q.head
    while currentNode!=None:
        if priority > currentNode.priority:
            insertPriorityQueue(Q, element,cont ,priority)
            return cont
        
        if  priority == currentNode.priority:
            insertPriorityQueue(Q, element,cont+1 ,priority)
            return cont+1
        cont += 1
        currentNode = currentNode.nextNode

    insertPriorityQueue(Q, element,cont ,priority)
    return cont

def dequeue_priority(Q):
    return dequeue(Q)



# URL
# https://repl.it/@BrunoFuentes/colasandlistas