# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp4


from algo1 import*
from print_tree import*
from linkedlist import*
from binarytree import*
from stack import *
from trie import*




# ------------------------------------------

def encriptarv2(L,r):
    q=LinkedList()
    
    listaDeListas = r.children
    currentNode = r.children.head 
    while currentNode != None:
        # print( currentNode.value.key ) #imprime los valores
        enqueue(q, currentNode.value )
        currentNode = currentNode.nextNode


    while length(q)!=0:
        Node=dequeue(q)
        # print(Node.key,"-",Node.level)
        insert(L,Node,length(L))
        if Node.children != None:
            # print( Node.children.head )
            currentNode = Node.children.head
            while currentNode != None:
                enqueue(q,currentNode.value )
                currentNode = currentNode.nextNode


def acomodarNiveles( node,cont ):
    if node.children != None:
        currentNode = node.children.head
        while currentNode != None:
            currentNode.value.level = cont+1
            acomodarNiveles( currentNode.value,cont+1 )
            currentNode = currentNode.nextNode

def invertirSting( cadena ):
    retorno = ""
    for i in range(len(cadena)-1,-1,-1 ):
        retorno += cadena[i]
    return retorno

def encriptar(T,niveles):
    L=LinkedList()

    acomodarNiveles(T.root,0) #agrega el nivel a cada nodo
    
    encriptarv2(L,T.root) #parte recursiva

    arr = Array(length(L),"")
    for i in range(len(arr)):
        arr[i] = ""

    currentNode = L.head
    while currentNode != None:
        # print( currentNode.value.key,"-",currentNode.value.level )
        arr[ currentNode.value.level ] += str( currentNode.value.key )
        currentNode =  currentNode.nextNode



    # recorro la lista de niveles
    currentNode = niveles.head
    while currentNode != None:
        index =  currentNode.value
        if arr[index] != "":
            arr[index] = invertirSting( arr[index] )
        currentNode = currentNode.nextNode

    # intervir los valores del trie
    currentNode = niveles.head
    while currentNode != None:
        index =  currentNode.value
        
        j = 0
        nodoL = L.head
        # print(nodoL.value.key)
        for i in range(1,length(L) ):
            if nodoL.value.level == index:
                string = arr[index]
                nodoL.value.key = string[j]
                j += 1
            nodoL = nodoL.nextNode
        j=0
        currentNode =  currentNode.nextNode

    
# ------------------------------------------


T = Trie()

insertTrie( T,"OSO")
insertTrie( T,"OSA")
insertTrie( T,"TERNA")
printTrie( T ) 
print("- - - - - - - -")
L = LinkedList()
add(L,1)
add(L,2)

encriptar(T,L )
printTrie( T ) 















