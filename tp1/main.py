from algo1 import*
from linkedlist import*
from math import*
from stack import*


'''
Ejercicio 5:
Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y un entero n y devuelve True si existen en A un par de elementos que sumados den n. Analice el costo computacional.
'''
def ContieneSuma(A,n):
    for i in range(0,length(A) ):
        for j in range(i+1,length(A)):
            suma = access(A,i) + access(A,j)
            if (suma == n):
                return True
    return False
'''
La complejidad de este algoritmo es de O(n^2) ya que son 2 bucles anidados
'''





'''
Ejercicio 4:
Implementar un algoritmo que ordene una lista de elementos donde siempre el elemento del medio de la lista contiene antes que él en la lista la mitad de los elementos menores que él. Explique la estrategia de ordenación utilizada.
'''
def mitadDeMenores(L):
    printLinkedList(L)

    # obtengo valor y ubicacion del valor medio
    indiceNumeroMedio = trunc( (length(L)-1) /2 )
    valorNumeroMedio = access(L,indiceNumeroMedio)

    # creo un array con los numeros menos al medio
    listaAux = LinkedList()
    currentNode = L.head
    while (currentNode!=None):
        if (currentNode.value < valorNumeroMedio ):
            add(listaAux, currentNode.value) 
        currentNode = currentNode.nextNode


    # obtengo la cantidad moviento para ordenar
    cantidadMovientos = trunc ( length(listaAux) / 2 )

    
    # a patir de la lista auxiliar ordeno la cantidad de veces nesaria, ya que tengo los movimentos que hay que hacer 
    while(cantidadMovientos != 0):
        numeroAOrdenar = pop(listaAux)
        delete(L,numeroAOrdenar)
        insert(L,numeroAOrdenar,indiceNumeroMedio)

        cantidadMovientos -= 1

    printLinkedList(L)






L = LinkedList()
add(L,1)
add(L,2)
add(L,3)
add(L,6)
add(L,7)
add(L,10)

mitadDeMenores(L)
