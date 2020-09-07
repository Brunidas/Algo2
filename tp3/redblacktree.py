
# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://https://repl.it/@BrunoFuentes/tp3


from algo1 import*
from binarytree import*
from print_tree import*
from queue import*
from avltree import*





'''
Ejercicio 3
Crear un modulo de nombre redblacktree.py Implementar las siguientes funciones:
insert(RedBlackTree,key)
Descripción: Implementa la operación insert
Entrada: Un RedBlackTree junto a un key que se va a insertar en el
árbol
Salida: retorna el nuevo árbol
'''


class RedBlackTree:
    root = None
class RedBlackNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    color = None



def fixup( T, node ):
    while node.parent.color == "RED":
        if node.parent == node.parent.parent.leftnode:
            y = node.parent.parent.leftnode
            if y.parent.color == "RED":
                # caso 1
                node.parent.color = "BLACK"
                y.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            elif node == node.parent.rightnode:
                # caso 2
                node = node.parent 
                rotateLeft( T, node )
            # caso 3
            node.parent.color = "BLACK"
            node.parent.parent.color = "RED"
            rotateRight( T, node.parent.parent )
        else:
            y = node.parent.parent.rightnode
            if y.parent.color == "RED":
                # caso 1
                node.parent.color = "BLACK"
                y.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            elif node == node.parent.leftnode:
                # caso 2
                node = node.parent 
                rotateRight( T, node )
            # caso 3
            node.parent.color = "BLACK"
            node.parent.parent.color = "RED"
            rotateLeft( T, node.parent.parent )
            
    T.root.color = "BLACK"



def insertRB( RedBlackTree, key, value ):
    newNode = RedBlackNode()
    newNode.key = key
    newNode.value = value

    y = None
    x = RedBlackTree.root

    while x != None:
        y = x  # memorizamos el padre
               # buscando la hoja en donde insertar
        if newNode.key < x.key:
            x = x.leftnode
        else:
            x = x.rightnode
    
    # se asigna el padre
    newNode.parent = y

    # actualizados la raiz, o el padre DevuelveNodo
    if y == None:
        RedBlackTree.root = newNode
    elif newNode.key < y.key:
        y.leftnode = newNode
    else:
        y.rightnode = newNode

    # terminamos de crear newNode
    newNode.color = "RED"

    # arreglamos los colores
    fixup( RedBlackTree, newNode )

def searchRB(B,element):
    r=B.root
    q=LinkedList()
    enqueue(q,r)
    

    while length(q)!=0:
        Node=dequeue(q)
        
        if Node.value==element:
            return Node.key
        
        if Node.leftnode!=None:
            enqueue(q,Node.leftnode)
        if Node.rightnode!=None:
            enqueue(q,Node.rightnode)

def accessRB(B,k):
    r=B.root
    q=LinkedList()
    enqueue(q,r)

    while length(q)!=0:
        Node=dequeue(q)
        
        if Node.key==k:
            return Node.value
            
    
        if Node.leftnode!=None:
            enqueue(q,Node.leftnode)
        if Node.rightnode!=None:
            enqueue(q,Node.rightnode)

def updateRB(B,element,k):
    r=B.root
    q=LinkedList()
    enqueue(q,r)

    while length(q)!=0:
        Node=dequeue(q)
        
        if Node.key==k:
            Node.value=element
        
        if Node.leftnode!=None:
            enqueue(q,Node.leftnode)
        if Node.rightnode!=None:
            enqueue(q,Node.rightnode)
