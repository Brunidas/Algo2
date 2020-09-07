# FUENTES, Bruno
# 12401

#·······························································
#ESTO ES linkedList.py
from algo1 import *


#Ejercicio 1
'''
A partir de una estructura LinkedList definida de la siguiente manera:
'''
class LinkedList():
    head=None
'''
Y la estructura Node definida de la siguiente manera:
'''
class node():
    value=None
    nextNode=None

# Imprimir una linkedList
def printLinkedList(L):
    cadena = ""
    """➜"""
    currentNode = L.head
    while( currentNode != None):
        cadena = cadena + str( currentNode.value ) + ' ➜ ' 

        currentNode = currentNode.nextNode
    cadena = cadena + "None"
    print(cadena)

'''
Crear un modulo de nombre linkedlist.py que implemente las siguientes especificaciones de las operaciones elementales para el TAD secuencia  utilizando el TAD lista.


length(L)
Descripción: Calcula el número de elementos de la lista que representa el TAD secuencia.
Entrada: La lista sobre la cual se quiere calcular el número de elementos.
Salida: Devuelve el número de elementos. 
'''
def length(L):
    cont = 0
    currentNode = L.head
    while( currentNode != None):
        cont += 1
        currentNode = currentNode.nextNode
    return cont
'''
add(L,element) 
Descripción: Agrega un elemento al comienzo de  L, siendo L una LinkedList que representa el TAD secuencia. 
Entrada: La Lista sobre la cual se quiere agregar el elemento (LinkedList)  y el valor del elemento (element) a  agregar.
Salida:  No hay salida definida
'''
def add(L,element):
    newNode = node()
    newNode.value = element
    newNode.nextNode = L.head

    L.head = newNode 
'''
search(L,element)
Descripción: Busca un elemento de la lista que representa el TAD secuencia.
Entrada: la lista sobre el cual se quiere realizar la búsqueda (Linkedlist) y el valor del elemento (element) a buscar.
Salida: Devuelve la posición donde se encuentra la primera instancia del elemento. Devuelve None si el elemento no se encuentra.
'''
def search(L,element):
    retorno = None
    cont = 0
    currentNode = L.head
    while( currentNode != None):
        if (currentNode.value == element ):
            retorno = cont 
        cont += 1
        currentNode = currentNode.nextNode
    return retorno
'''
insert(L,element,position)
Descripción: Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
Entrada: la lista sobre el cual se quiere realizar la inserción (Linkedlist) y el valor del elemento (element) a insertar y la posición (position) donde se quiere insertar.
Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve None. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.
'''
def insert(L, element, position):
    #inserta el elemento en la primera posicion 
    if (position == 0):
        add(L, element)
        return position
    
    # si la posicion a insertar es en nodo "None"  el nodo se insertara ahi
    # y la lista tendra un nodo mas 
    elif position == length(L):
        newNode = node()
        newNode.value = element
        
        currentNode = L.head
        while( currentNode != None):
            if ( currentNode.nextNode == None):
                currentNode.nextNode = newNode
                break
            currentNode = currentNode.nextNode
        return length(L)
        
    #inserta el elemento en la position y desplaza los demas elementos 
    elif position < length(L) :
        newNode = node()
        newNode.value = element
        
        cont=1
        currentNode = L.head
        while( currentNode != None):
            if cont == position:
                newNode.nextNode = currentNode.nextNode
                currentNode.nextNode = newNode
                break
            cont += 1
            currentNode = currentNode.nextNode
        return cont
    else:  
        return None
'''
delete(L,element)
Descripción: Elimina un elemento de la lista que representa el TAD secuencia.
Poscondición: Se debe desvincular el Node a eliminar.  
Entrada: la lista sobre el cual se quiere realizar la eliminación (Linkedlist) y el valor del elemento (element) a eliminar.
Salida: Devuelve la posición donde se encuentra el elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
'''
def delete(L, element):
    position  = search(L, element)
    #verifica si esta el elemento a eliminar
    if(position==0):
        currentNode = L.head
        L.head = currentNode.nextNode

    elif (position != None) & (position!= 0):
        cont = 0
        currentNode = L.head
        while (currentNode!=None):
            #cuando lo encuentra la desvincula
            if position-1 == cont:
                currentNode.nextNode =  currentNode.nextNode.nextNode
                break
            cont += 1
            currentNode = currentNode.nextNode
        return position
    else:
        return None
'''
access(L,position)
Descripción: Permite acceder a un elemento de la lista en una posición determinada.
Entrada: La lista (LinkedList) y la position del elemento al cual se quiere acceder.
Salida: Devuelve el valor de un elemento en una position de la lista, devuelve None si no existe elemento para dicha posición.
'''
def access(L,position):
    retorno = None

    cont = 0
    currentNode = L.head
    while (currentNode != None):
        if cont == position :
            retorno = currentNode.value
            break
        cont +=1
        currentNode = currentNode.nextNode
    return retorno
'''
update(L,element,position)
Descripción: Permite cambiar el valor de un elemento de la lista en una posición determinada
Entrada: La lista (LinkedList) y la position sobre la cual se quiere asignar el valor de  element. 
Salida: Devuelve None si no existe elemento para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.
'''
def update(L,element,position):
    if position < (length(L)):
        cont = 0
        currentNode = L.head
        while (currentNode != None):
            if cont == position :
                currentNode.value = element
                break
            cont +=1
            currentNode = currentNode.nextNode
        return position
    else:
        return None


# URL
# https://repl.it/@BrunoFuentes/linkedlist
