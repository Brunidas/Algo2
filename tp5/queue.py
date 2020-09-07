# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401

from algo1 import *
from linkedlist import *
from stack import *


"""Ejercicio 2
Crear un modulo de nombre queue.py que implemente las siguientes especificaciones de las operaciones elementales para  un TAD cola  utilizando el TAD lista. Recordar que una Cola/Queue puede implementarse también sobre una estructura LinkedList donde, el primer elemento en ingresar a la lista es el primero en salir (FIFO).
enqueue(Q,element) 
Descripción: Agrega un elemento al comienzo de  Q, siendo Q una estructura de tipo  LinkedList. 
Entrada: La cola Q (LinkedList)  sobre la cual se quiere agregar el elemento  y el valor del elemento (element) a  agregar.
Salida:  No hay salida definida.


dequeue(S)
Descripción: extrae el último elemento de la cola Q, siendo Q una estructura de tipo LinkedList.
Poscondición: Se debe desvincular el Node a eliminar.  
Entrada: la cola Q (Linkedlist) sobre el cual se quiere realizar la eliminación. 
Salida: Devuelve el elemento de la cola. Devuelve None si la cola está vacía.
"""
def enqueue(Q,element):
    push(Q,element)  

def dequeue(S):
    if S.head == None :
        return None
    else:
        elemento = access(S, 0)
        delete(S, elemento)
        return elemento