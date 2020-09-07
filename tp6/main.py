# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp6

from algo1 import *
from linkedlist import *
from dictionary import *
from binarytree import *
from random import *
from queue import *
import math

# Recorridos de un grafo

# -------------------------------------------------
# breadth first search


def bfs(G):
    # eligo el nodo s
    for i in range(len(G)):
        if G[i] != None:
            nodoS = G[i].head
            break

    # print( nodoS.value )
    Q = LinkedList()
    nodoS.color = "GREY"
    enqueue(Q, nodoS)

    # analiza el nodo gris
    while length(Q) != 0:

        nodoAnalizado = dequeue(Q)

        L = LinkedList()
        L.head = nodoAnalizado

        currentNode = nodoAnalizado
        for i in range(length(L)):
            if i != 0:

                # guardo la key
                for j in range(len(G)):
                    if G[j] != None:
                        if G[j].head.value == currentNode.value:
                            key = j

                if G[key].head.color == "WHITE":
                    
                    G[key].head.parent = nodoAnalizado

                    G[key].head.color = "GREY"
                    G[key].head.distance = nodoAnalizado.distance + 1
                    enqueue(Q, G[key].head)

            currentNode = currentNode.nextNode

        nodoAnalizado.color = "BLACK"

    return 


# -------------------------------------------------
# depth first search


def dfsV2(G, nodoU, time):
    cont = time[0] + 1
    time[0] = cont

    nodoU.moment = time[0]
    nodoU.color = "GREY"

    # imprime resultado
    print("nodo analizado:", nodoU.value)

    L = LinkedList()
    L.head = nodoU

    currentNode = nodoU
    for i in range(length(L)):

        if i != 0:

            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            if G[key].head.color == "WHITE":
                G[key].head.parent = nodoU
                dfsV2(G, G[key].head, time)

        currentNode = currentNode.nextNode

    nodoU.color = "BLACK"
    cont = time[0] + 1
    time[0] = cont
    nodoU.finalized = time[0]


def dfs(G):

    time = Array(1, 0)
    time[0] = 0

    for i in range(len(G)):
        if G[i] != None:
            if G[i].head.color == "WHITE":
                dfsV2(G, G[i].head, time)


# -------------------------------------------------
'''
A partir de la siguiente definición:

Graph = Array(n,LinkedList())

Donde Graph es una representación de un grafo simple mediante listas de adyacencia resolver los siguiente ejercicios
Ejercicio 1
Implementar la función crear grafo que dada una lista de vértices y una lista de aristas cree un grafo con la representación por Lista de Adyacencia.

def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo
'''

# n = 9  --> es la cantidad de vertices
# Graph = Array( n, LinkedList() )


def createGraph(V, A):
    # V -> vertices
    # A -> aristas

    n = length(V)
    Graph = Array(n, LinkedList())

    for i in range(n):
        valor = access(V, i)
        insertD(Graph, i, valor)

    currentNode = A.head
    for i in range(length(A)):
        if i % 2 != 0:
            # agrega las llegadas

            # esto dice en que lugar lo tengo que poner
            key = search(V, currentNode.value)

            value = access(A, i - 1)

            insertD(Graph, key, value)

            #----------------------------------
            # agrega las salidas
            newCurrentNodeValue = access(A, i - 1)

            newKey = search(V, newCurrentNodeValue)

            newValue = access(A, i)

            insertD(Graph, newKey, newValue)

        currentNode = currentNode.nextNode

    return Graph


'''Ejercicio 2
Implementar la función que responde a la siguiente especificación.

def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.'''


def existPathV2(G, nodoU, time):
    cont = time[0] + 1
    time[0] = cont

    nodoU.moment = time[0]
    nodoU.color = "GREY"

    L = LinkedList()
    L.head = nodoU

    currentNode = nodoU
    for i in range(length(L)):

        if i != 0:

            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            if G[key].head.color == "WHITE":
                existPathV2(G, G[key].head, time)

        currentNode = currentNode.nextNode

    nodoU.color = "BLACK"
    cont = time[0] + 1
    time[0] = cont
    nodoU.finalized = time[0]


def existPath(G, v1, v2):

    time = Array(1, 0)
    time[0] = 0

    for i in range(len(G)):
        if G[i] != None:
            if G[i].head.color == "WHITE":
                existPathV2(G, G[i].head, time)

    # si el valor finalized del grafo en v2.key es igual a
    # el doble de la cantidad de vertices => hay un camino
    # que une v1 con v2
    if G[v2.key].head.finalized == (2 * len(G)):
        return False
    else:
        return True


'''
Ejercicio 3
Implementar la función que responde a la siguiente especificación.
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vertices, False en caso contrario.
'''


def isConnectedV2(G, nodoU, time):
    cont = time[0] + 1
    time[0] = cont

    nodoU.moment = time[0]
    nodoU.color = "GREY"

    # print( nodoU.value )

    L = LinkedList()
    L.head = nodoU

    currentNode = nodoU
    for i in range(length(L)):

        if i != 0:

            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            if G[key].head.color == "WHITE":
                isConnectedV2(G, G[key].head, time)

        currentNode = currentNode.nextNode

    nodoU.color = "BLACK"
    cont = time[0] + 1
    time[0] = cont
    nodoU.finalized = time[0]


def isConnected(G):

    time = Array(1, 0)
    time[0] = 0

    for i in range(len(G)):
        if G[i] != None:
            if G[i].head.color == "WHITE":
                isConnectedV2(G, G[i].head, time)

    # si el valor finalized del grafo en v1.key es igual a
    # el doble de la cantidad de vertices
    if G[0].head.finalized == (2 * len(G)):
        return True
    else:
        return False


'''
Ejercicio 4
Implementar la función que responde a la siguiente especificación.
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
'''


def isTree(G):

    CantVertices = len(G)

    CantAristas = 0
    for i in range(len(G)):
        CantAristas += length(G[i]) - 1
    CantAristas = CantAristas / 2

    # print("aristas:",CantAristas)
    # print("vertices:",CantVertices)

    if CantAristas == CantVertices - 1 and isConnected(G):
        return True
    return False


'''Ejercicio 5
Implementar la función que responde a la siguiente especificación.
def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.

Nota: Tener en cuenta que  un grafo es completo cuando existe una arista entre todo par de vértices.
'''


def isComplete(G):
    cantidadAristas = len(G)

    for i in range(len(G)):
        aristasDeEsteNodo = length(G[i])
        if cantidadAristas != aristasDeEsteNodo:
            return False

    return True


'''
Ejercicio 6
Implementar una función que dada un grafo devuelva una lista de aristas que si se eliminan el grafo se convierte en un árbol. Respetar la siguiente especificación

def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.
'''


def convertTree(G):
    L = LinkedList()
    cont = 0

    # eligo el nodo s
    for i in range(len(G)):
        if G[i] != None:
            nodoS = G[i].head
            break

    # print( nodoS.value )
    Q = LinkedList()
    nodoS.color = "GREY"
    enqueue(Q, nodoS)

    cont = 0
    aristas = LinkedList()

    contTodasA = 0
    todasLasAristas = LinkedList()

    # analiza el nodo gris
    while length(Q) != 0:

        nodoAnalizado = dequeue(Q)

        L.head = nodoAnalizado

        currentNode = nodoAnalizado
        for i in range(length(L)):

            if i != 0:

                # guardo la key
                for j in range(len(G)):
                    if G[j] != None:
                        if G[j].head.value == currentNode.value:
                            key = j

                insert(todasLasAristas, nodoAnalizado.value, contTodasA)
                contTodasA += 1
                insert(todasLasAristas, currentNode.value, contTodasA)
                contTodasA += 1

                if G[key].head.color == "WHITE":

                    # aristas del arbol
                    insert(aristas, nodoAnalizado.value, cont)
                    cont += 1
                    insert(aristas, currentNode.value, cont)
                    cont += 1

                    G[key].head.color = "GREY"
                    G[key].head.distance = nodoAnalizado.distance + 1
                    enqueue(Q, G[key].head)

            currentNode = currentNode.nextNode

        nodoAnalizado.color = "BLACK"

    # marco con None las artitas que no forman parte del arbol
    for i in range(0, length(aristas), +2):

        aristas1 = access(todasLasAristas, i)
        aristas2 = access(todasLasAristas, i + 1)

        for j in range(0, length(todasLasAristas), +2):

            todasLasAristas1 = access(todasLasAristas, j)
            todasLasAristas2 = access(todasLasAristas, j + 1)

            # print( "compara:",aristas1,"-",aristas2,"con : ",todasLasAristas1,"-",todasLasAristas2 )

            if aristas1 == todasLasAristas1 and aristas2 == todasLasAristas2:
                update(todasLasAristas, None, j)
                update(todasLasAristas, None, j + 1)

            if aristas1 == todasLasAristas2 and aristas2 == todasLasAristas1:
                update(todasLasAristas, None, j)
                update(todasLasAristas, None, j + 1)

    # elimino los nodos node
    for i in range(length(todasLasAristas)):
        delete(todasLasAristas, None)

    # elimino las aristas del grafo
    for i in range(0, length(todasLasAristas), +2):
        a = access(todasLasAristas, i)
        b = access(todasLasAristas, i + 1)

        # guardo la key
        for j in range(len(G)):
            if G[j] != None:
                if G[j].head.value == a:
                    key = j

        delete(G[key], b)

    # marco con None las aristas repeditas
    for i in range(0, length(todasLasAristas), +2):

        valorA = access(todasLasAristas, i)
        valorB = access(todasLasAristas, i + 1)

        for j in range(0, length(todasLasAristas), +2):

            valorParaBorarA = access(todasLasAristas, j)
            valorParaBorarB = access(todasLasAristas, j + 1)

            if valorA == valorParaBorarB and valorB == valorParaBorarA:
                update(todasLasAristas, None, j)
                update(todasLasAristas, None, j + 1)

    # elimino los nodos node
    for i in range(length(todasLasAristas)):
        delete(todasLasAristas, None)

    return todasLasAristas


'''
Ejercicio 7
Implementar la función que responde a la siguiente especificación.
def countConnections(Grafo): 
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.
'''


def countConnectionsV2(G, nodoU, time):
    cont = time[0] + 1
    time[0] = cont

    nodoU.moment = time[0]
    nodoU.color = "GREY"

    # imprime resultado
    # print("nodo analizado:", nodoU.value )

    L = LinkedList()
    L.head = nodoU

    currentNode = nodoU
    for i in range(length(L)):

        if i != 0:

            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            if G[key].head.color == "WHITE":
                countConnectionsV2(G, G[key].head, time)

        currentNode = currentNode.nextNode

    nodoU.color = "BLACK"
    cont = time[0] + 1
    time[0] = cont
    nodoU.finalized = time[0]


def countConnections(G):

    time = Array(1, 0)
    time[0] = 0

    for i in range(len(G)):
        if G[i] != None:
            if G[i].head.color == "WHITE":
                countConnectionsV2(G, G[i].head, time)

    cont = 0
    for i in range(len(G)):

        # cuando el valor finalized se diferencia en uno con
        # el valor moment contamos una componenete conexa
        if G[i].head.finalized - G[i].head.moment == 1:
            cont += 1

    return cont


'''
Ejercicio 8
Implementar la función que responde a la siguiente especificación.
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
'''


def convertToBFSTree(G, v):

    # eligo el nodo s
    for i in range(len(G)):
        if G[i].head.value == v.value:
            nodoS = G[i].head
            break

    # print( nodoS.value )
    Q = LinkedList()
    nodoS.color = "GREY"
    enqueue(Q, nodoS)

    # analiza el nodo gris
    while length(Q) != 0:

        nodoAnalizado = dequeue(Q)

        L = LinkedList()
        L.head = nodoAnalizado

        currentNode = nodoAnalizado
        for i in range(length(L)):
            if i != 0:

                # guardo la key
                for j in range(len(G)):
                    if G[j] != None:
                        if G[j].head.value == currentNode.value:
                            key = j

                if G[key].head.color == "WHITE":
                    G[key].head.color = "GREY"
                    G[key].head.distance = nodoAnalizado.distance + 1
                    enqueue(Q, G[key].head)

            currentNode = currentNode.nextNode

        nodoAnalizado.color = "BLACK"

    return G


'''Ejercicio 9
Implementar la función que responde a la siguiente especificación.
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.'''


def convertToDFSTreeV2(G, nodoU, time):
    cont = time[0] + 1
    time[0] = cont

    nodoU.moment = time[0]
    nodoU.color = "GREY"

    # imprime resultado
    print("nodo analizado:", nodoU.value)

    L = LinkedList()
    L.head = nodoU

    currentNode = nodoU
    for i in range(length(L)):

        if i != 0:

            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            if G[key].head.color == "WHITE":
                convertToDFSTreeV2(G, G[key].head, time)

        currentNode = currentNode.nextNode

    nodoU.color = "BLACK"
    cont = time[0] + 1
    time[0] = cont
    nodoU.finalized = time[0]


def convertToDFSTree(G, v):

    time = Array(1, 0)
    time[0] = 0

    for i in range(len(G)):
        if G[i] != None:
            if G[i].head.color == "WHITE":

                # print( G[ hashDiv( len(G), i + v.key ) ].head.value )

                nodoU = G[hashDiv(len(G), i + v.key)].head

                convertToDFSTreeV2(G, nodoU, time)

'''
Ejercicio 10
Implementar la función que responde a la siguiente especificación.
def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el mejor camino, en caso de existir, entre dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.
'''

def bestRoadV2(G, nodoU, time, v1, v2,string):
    
    
    if nodoU.value == v2.value:
        return 
    
    else:

        cont = time[0] + 1
        time[0] = cont

        nodoU.moment = time[0]
        nodoU.color = "GREY"

        L = LinkedList()
        L.head = nodoU


        currentNode = nodoU
        for i in range(length(L)):
            if i != 0:


                # guardo la key
                for j in range(len(G)):
                    if G[j] != None:
                        if G[j].head.value == currentNode.value:
                            key = j


                add( string,currentNode.value )



                if G[key].head.color == "WHITE" or G[key].head.value == v2.value:

                    bestRoadV2(G, G[key].head, time,v1, v2,string)


            currentNode = currentNode.nextNode

        nodoU.color = "BLACK"
        cont = time[0] + 1
        time[0] = cont
        nodoU.finalized = time[0]



def bestRoad(G, v1, v2):

    time = Array(1, 0)
    time[0] = 0


    L = LinkedList()
    string = LinkedList()
    aristasValidas = LinkedList()

    nodoU = G[ v1.key ].head
    
    add( string, nodoU.value )
    bestRoadV2(G, nodoU, time, v1 ,v2, string )


    voltearlista( string, L )


    # encuntra las aristas validas
    cadena=""
    contv1 = 0
    currentNode = L.head
    while currentNode != None:

        cadena += currentNode.value

        if currentNode.value == v1.value:
            contv1 += 1

        if contv1 == 2:
            contv1 = 0
            cadena =""
            
            cadena += currentNode.value

        elif currentNode.value == v2.value:
            add(aristasValidas,cadena)
            cadena =""
            # print (cadena)


        currentNode = currentNode.nextNode


    if aristasValidas==None:
        # si no existen ningun camino
        return aristasValidas
    else:

        # encuentra la logitud minima del camino
        min = 999999999999999
        currentNode = aristasValidas.head
        while currentNode != None:
            
            if min > len(currentNode.value) :
                min = len(currentNode.value)

            currentNode = currentNode.nextNode 


        # los caminos que no sean de logitud minima se borran
        currentNode = aristasValidas.head
        while currentNode != None:
            if min != len(currentNode.value) :
                delete( aristasValidas, currentNode.value)

            currentNode = currentNode.nextNode 

        # printLinkedList( aristasValidas )
        # return 
        return aristasValidas


'''Ejercicio 11
Implementar la función que responde a la siguiente especificación.
def isBipartite(Grafo): 
Descripción: Implementa la operación es bipartito
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es bipartito.

NOTA: Un grafo es bipartito si no tiene ciclos de longitud impar.
'''
def isBipartiteV2(G, nodoU, time,string):
    cont = time[0] + 1
    time[0] = cont

    nodoU.moment = time[0]
    nodoU.color = "GREY"

    # imprime resultado
    # print("nodo analizado:", nodoU.value)
    


    L = LinkedList()
    L.head = nodoU

    currentNode = nodoU
    for i in range(length(L)):

        if i != 0:


            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            if G[key].head.color == "WHITE":
                G[key].head.parent = nodoU
                isBipartiteV2(G, G[key].head, time,string)




        currentNode = currentNode.nextNode

    nodoU.color = "BLACK"
    cont = time[0] + 1
    time[0] = cont
    nodoU.finalized = time[0]

    add( string, nodoU.value)


def isBipartite( G ): 
    if isConnected( G ):
        # pone todos los nodos de color blanco
        for i in range( len(G) ):
            G[i].head.color = "WHITE" 
        


        ciclos = LinkedList()
        string = LinkedList()


        time = Array(1, 0)
        time[0] = 0
        

        for i in range(len(G)):
            if G[i] != None:
                if G[i].head.color == "WHITE":
                    if i == 0:
                        root = G[i].head.value

                    isBipartiteV2(G, G[i].head, time,string)
    

        
        # elimina los nodos con el valor root
        currentNode = string.head
        while currentNode != None:
            if currentNode.value == root:
                delete( string , root )

            currentNode = currentNode.nextNode




        # coloco el/los valores de root en lugares correctos 
        cont = 0
        currentNode = string.head
        while currentNode != None:


            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            
            if G[key].head.finalized - G[key].head.moment == 1:
                insert( string, root, cont )
                cont += 1
            

            cont += 1
            currentNode = currentNode.nextNode
        
        
        
        cadena = ""
        currentNode = string.head
        while currentNode != None:
            cadena += currentNode.value

            # guardo la key
            for j in range(len(G)):
                if G[j] != None:
                    if G[j].head.value == currentNode.value:
                        key = j

            if G[key].head.finalized - G[key].head.moment == 1:
                add( ciclos, cadena )
                cadena = ""


            currentNode = currentNode.nextNode
        
        
        

        # elimino los ciclos
        currentNode = ciclos.head
        while currentNode != None:
            if len(currentNode.value) < 3:
                delete( ciclos, currentNode.value ) 
            currentNode = currentNode.nextNode
        
        cont = 0
        currentNode = ciclos.head
        while currentNode != None:
            
            valor = currentNode.value
            for i in range( len(valor) ):
                

                for j in range( len(valor) ):
                    if valor[j] != valor[i]:
                        # soy conciente de la cantidad de ciclo que hay :c
                        
                        # guardo la key
                        for k in range(len(G)):
                            if G[k] != None:
                                if G[k].head.value == valor[i]:
                                    key = k

                        if search( G[key], valor[j] ) != None :
                            cont += 1
            
            # print("cont:",cont)
            if cont != len(valor) * 2:
                delete( ciclos, valor)

            cont = 0
            currentNode = currentNode.nextNode


        # veo si hay ciclo de longuitud impar
        currentNode = ciclos.head
        while currentNode != None:
            if len(currentNode.value) % 2 != 0 :
                return False 
            currentNode = currentNode.nextNode

        return True 




    else:
        return False


# DATOS:
# ------------------------------------------
vertices = LinkedList()
nodeA = DictionaryNode()
nodeB = DictionaryNode()
nodeC = DictionaryNode()
nodeD = DictionaryNode()
nodeE = DictionaryNode()
# nodeF = DictionaryNode()

vertices.head = nodeA
nodeA.nextNode = nodeB
nodeB.nextNode = nodeC
nodeC.nextNode = nodeD
nodeD.nextNode = nodeE
# nodeE.nextNode = nodeF

nodeA.value = "A"
nodeB.value = "B"
nodeC.value = "C"
nodeD.value = "D"
nodeE.value = "E"
# nodeF.value = "F"

nodeA.key = 0
nodeB.key = 1
nodeC.key = 2
nodeD.key = 3
nodeE.key = 4
# nodeF.key = 5

aristas = LinkedList()

add(aristas, "A")
add(aristas, "B")

add(aristas, "B")
add(aristas, "D")


add(aristas, "D")
add(aristas, "C")

add(aristas, "A")
add(aristas, "C")

add(aristas, "E")
add(aristas, "A")

# add( aristas, "A")
# add( aristas, "F")

# add( aristas, "C")
# add( aristas, "D")

# add( aristas, "B")
# add( aristas, "E")

# add( aristas, "B")
# add( aristas, "F")

# add( aristas, "B")
# add( aristas, "D")

# ------------------------------------------

# print("punto 1: crear grafo\n")
# Graph = createGraph(vertices, aristas)
# printDictionary(Graph)
# print(" - - - - - - - - - -")

# print("breadth first search\n")
# Graph = createGraph( vertices, aristas )
# bfs( Graph )
# print("distancia a",Graph[0].head.value,":")
# for i in range( len(Graph) ):
#     print( Graph[i].head.value,":",Graph[i].head.distance )
# print(" - - - - - - - - - -")


# print("depth first search\n")
# Graph = createGraph( vertices, aristas )
# dfs( Graph )
# print()
# print("pasos:")
# for i in range( len(Graph) ):
#     print( Graph[i].head.value,":",Graph[i].head.moment,"/",Graph[i].head.finalized )
# print(" - - - - - - - - - -")

# print("punto 2: camino entre 2 nodos \n")
# Graph = createGraph(vertices, aristas)
# print(existPath(Graph, nodeA, nodeC))
# print(" - - - - - - - - - -")

# print("punto 3: es conexo \n")
# Graph = createGraph( vertices, aristas )
# print( isConnected( Graph ) )
# print(" - - - - - - - - - -")

# print("punto 4: es arbol\n")
# Graph = createGraph( vertices, aristas )
# print( isTree( Graph ) )
# print(" - - - - - - - - - -")

# print("punto 5: grafo completo\n")
# Graph = createGraph( vertices, aristas )
# print( isComplete( Graph ) )
# print(" - - - - - - - - - -")

# print("punto 6: aristas que si se eliminan el grafo se convierte en un árbol\n")
# Graph = createGraph( vertices, aristas )
# L = convertTree( Graph )
# for i in range(0, length( L ) ,+2 ):
#     a = access(L,i)
#     b = access(L,i+1)
#     print( a,"-",b )
# print(" - - - - - - - - - -")

# print("punto 7: componentes conenxas\n")
# Graph = createGraph( vertices, aristas )
# print( countConnections( Graph ) )
# print(" - - - - - - - - - -")

# print("punto 8: convertir a arbol BFS\n")
# Graph = createGraph( vertices, aristas )
# convertToBFSTree( Graph, nodeB )
# printDictionary( Graph )
# print("distancia a",nodeB.value,":")
# for i in range( len(Graph) ):
#     print( Graph[i].head.value,":",Graph[i].head.distance )
# print(" - - - - - - - - - -")

# print("punto 9: convertir a arbol DFS\n")
# Graph = createGraph( vertices, aristas )
# convertToDFSTree( Graph, nodeB )
# printDictionary( Graph )
# print("pasos:")
# for i in range( len(Graph) ):
#     print( Graph[i].head.value,":",Graph[i].head.moment,"/",Graph[i].head.finalized )
# print(" - - - - - - - - - -")



# print("punto 10: mejor camino DFS\n")
# Graph = createGraph( vertices, aristas )
# printLinkedList(  bestRoad( Graph, nodeD, nodeA ) )
# print(" - - - - - - - - - -")


# print("punto 11: es bipartito \n")
# Graph = createGraph( vertices, aristas )
# isBipartite( Graph )

# print()
# print("pasos:")
# for i in range( len(Graph) ):
#     print( Graph[i].head.value,":",Graph[i].head.moment,"/",Graph[i].head.finalized )
# print(" - - - - - - - - - -")



