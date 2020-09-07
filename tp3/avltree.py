# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401

"""
Parte 1
Importante: Los ejercicios de esta primera parte tienen como objetivo codificar las diferentes
funciones básicas necesarias para la implementar un árbol AVL.
A partir de estructuras definidas como :
class AVLTree:
    root = None
class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    balanceFactor = None
Copiar y adaptar todas las operaciones del binarytree.py (i.e insert(), delete(), search(),etc) al nuevo
módulo avltree.py. Notar que estos luego deberán ser implementados para cumplir que la propiedad
de un árbol AVL
"""


from algo1 import*
from linkedlist import*
from print_tree import*
from queue import*


########################################
class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    balanceFactor = None

########################################
def searchAvl(B,element):
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

def accessAvl(B,k):
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

def updateAvl(B,element,k):
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
    

'''
Ejercicio 1
Crear un modulo de nombre avltree .py Implementar las siguientes funciones:
rotateLeft(Tree,avlnode)
Descripción: Implementa la operación rotación a la izquierda
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la
rotación a la izquierda
Salida: retorna la nueva raíz
'''


def rotateLeft(Tree, avlnode):

    newRoot = avlnode.rightnode
    avlnode.rightnode = newRoot.leftnode


    if newRoot.leftnode != None:
        newRoot.leftnode.parent = avlnode
    newRoot.parent = avlnode.parent
    
    if avlnode.parent == None:
        Tree.root = newRoot
    else:
        if avlnode.parent.leftnode == avlnode:
            avlnode.parent.leftnode = newRoot
        else:
            avlnode.parent.rightnode = newRoot 
    
    newRoot.leftnode = avlnode
    avlnode.parent = newRoot

    return newRoot
'''
rotateRight(Tree,avlnode)
Descripción: Implementa la operación rotación a la derecha
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la
rotación a la derecha
Salida: retorna la nueva raíz
'''

def rotateRight(Tree, avlnode):
    newRoot = avlnode.leftnode
    avlnode.leftnode = newRoot.rightnode


    if newRoot.rightnode != None:
        newRoot.rightnode.parent = avlnode
    
    newRoot.parent = avlnode.parent
    
    if avlnode.parent == None:
        Tree.root = newRoot
    else:
        if avlnode.parent.rightnode == avlnode:
            avlnode.parent.rightnode = newRoot
        else:
            avlnode.parent.leftnode = newRoot 
    
    newRoot.rightnode = avlnode
    avlnode.parent = newRoot

    return newRoot


'''
Ejercicio 2
Implementar una función recursiva que calcule el elemento balanceFactor de cada subárbol
siguiendo la siguiente especificación:
calculateBalance(AVLTree)
Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda .
Entrada: El árbol AVL sobre el cual se quiere operar.
Salida: El árbol AVL con el valor de balanceFactor para cada subarbol
'''
def alturaRama(nodo):
    
    if nodo==None:
        return -1
    else:
        L=LinkedList()
        Altura(L,nodo,0)

        max = Max(L) 
        # printLinkedList(L)
        # print("Max ",max )


        return max


def Altura(L, r, nivel):
    '''
    Me dice la altura de cada nodo en una lista 
    '''
    add(L,nivel)
    if r.leftnode!=None:
        nivel = nivel + 1
        Altura(L, r.leftnode, nivel)
        nivel = nivel - 1
    if r.rightnode!=None:
        nivel = nivel + 1
        Altura(L, r.rightnode, nivel)
        nivel = nivel -1



def Max(L):
    '''
    Obtiene el maximo de una lista y lo devuelve
    '''
    max = L.head.value
    currenNode = L.head
    while currenNode!=None:
        if currenNode.value > max:
            max = currenNode.value
        currenNode = currenNode.nextNode
    return max



def calculateBalanceV2(r):
    

    izq = alturaRama(r.leftnode)+ 1
    der = alturaRama(r.rightnode)+ 1
    
    r.balanceFactor = izq - der  


    # print("Nodo ", r.value )
    # print("izq ",izq)
    # print("der ",der)
    # print("balanceFactor ", izq - der)
    # print("\n")

    if r.leftnode!=None:
        calculateBalanceV2(r.leftnode)
        
    if r.rightnode!=None:
        calculateBalanceV2(r.rightnode)
    

def calculateBalance(AVLTree):
    if AVLTree == None:
        return None
    else:
        calculateBalanceV2(AVLTree.root) 


'''
Ejercicio 3
Implementar una funcion en el modulo avltree.py de acuerdo a las siguientes especifcaciones:
reBalance(AVLTree)
Descripción: balancea un árbol binario de búsqueda . Para esto se deberá
primero calcular el balanceFactor del árbol y luego en función de esto
aplicar la estrategia de rotación que corresponda.
Entrada: El árbol binario de tipo AVL sobre el cual se quiere operar.
Salida: Un árbol binario de búsqueda balanceado. Es decir luego de
esta operación se cumple que la altura (h) de su subárbol derecho e
izquierdo difieren a lo sumo en una unidad.
'''
def reBalance(AVLTree):
    # print(AVLTree.root.balanceFactor)
    if AVLTree.root.balanceFactor < 0:
        # print(AVLTree.root.rightnode.balanceFactor)
        if AVLTree.root.rightnode.balanceFactor > 0:
            rotateRight(AVLTree, AVLTree.root.rightnode)
            rotateLeft(AVLTree, AVLTree.root)        
        else:
            # printTree(AVLTree)
            rotateLeft(AVLTree, AVLTree.root)
            
    
    elif AVLTree.root.balanceFactor > 0:
        if AVLTree.root.leftnode.balanceFactor < 0:
            rotateLeft(AVLTree, AVLTree.root.leftnode)
            rotateRight(AVLTree,AVLTree.root)
        
        else:
            rotateRight(AVLTree.root)

'''
Ejercicio 4:
Implementar la operacion insert() en el modulo avltree.py garantizando que el arbol binario
resultante sea un arbol AVL.
'''
def insertAvlV2(newNode,currentnode, L):
    if newNode.key!=currentnode.key:
        if newNode.key > currentnode.key:
            if currentnode.rightnode==None:
                newNode.parent=currentnode
                currentnode.rightnode=newNode
                add(L, currentnode)
            else:
                insertAvlV2(newNode,currentnode.rightnode, L)
        else:
            if currentnode.leftnode ==None:
                newNode.parent=currentnode
                currentnode.leftnode=newNode

                add(L, currentnode)                
            else:
                insertAvlV2(newNode,currentnode.leftnode, L)
    else:
        return None

def insertAvl(B,e,k):
    '''
    Descripción de ejemplo :D
    '''
    
    if B==None:
        return None
    else:
        L = LinkedList()
        newNode=AVLNode()
        newNode.key=k
        newNode.value=e
        currentnode=B.root
        

        insertAvlV2(newNode,currentnode, L) 

        # printTree(B)
        # print(' - - - - - - - - - - - -')
        
        calculateBalance( B )
        # print(' - - - - - - - - - - - -')
        reBalance( B )

        calculateBalance( B )
        # print(' - - - - - - - - - - - -')
        return k




'''
Ejercicio 5:
Implementar la operacion delete() en el modulo avltree.py garantizando que el arbol binario
resultante sea un árbol AVL.
'''

def NodoIgualnewNode(r,newNode,B):
    if r.key==newNode.key:
        if r.parent.rightnode==r:
            r.parent.rightnode=None
        else:
            r.parent.leftnode=None
        return B

    if r.leftnode!=None:
        NodoIgualnewNode(r.leftnode,newNode,B)
    if r.rightnode!=None:
        NodoIgualnewNode(r.rightnode,newNode,B) 

def DevuelveNodo(r,k,newNode):
    if r.key==k:
        newNode.key=r.key
        newNode.value=r.value
        newNode.leftnode=r.leftnode
        newNode.rightnode=r.rightnode
        newNode.parent=r.parent

        return newNode
    if r.leftnode!=None:
        DevuelveNodo(r.leftnode,k,newNode)
    if r.rightnode!=None:
        DevuelveNodo(r.rightnode,k,newNode)


def MayorDeSusMenores(r,m,mayores):
    if r.key > m:
        m=r.key
        add(mayores,m)
    if r.leftnode!=None:
        MayorDeSusMenores(r.leftnode,m,mayores)
    if r.rightnode!=None:
        MayorDeSusMenores(r.rightnode,m,mayores)


def deleteKeyAvlV2(r,k,retorno,B):
    ##
    if r.leftnode!=None:
        deleteKeyAvlV2(r.leftnode,k,retorno,B)

    if r.key==k:
        retorno=r.key
        #cuando no tiene hijos
        if r.leftnode==None and r.rightnode==None:
            print("Sin hijos")
            if r.parent.leftnode==r:
                r.parent.leftnode=None
                print("key eliminada:",retorno)
            if r.parent.rightnode==r:
                r.parent.rightnode=None
                print("key eliminada:",retorno)
        #cuando tiene solo hijo (derecho)
        if r.leftnode==None and r.rightnode!=None:   
            print("Con hijo derecho")
            if r!=B.root:
                if r.parent.rightnode==r:
                    #si r es el hijo derecho
                    r.parent.rightnode=r.rightnode
                    print("key eliminada:",retorno)
                else:
                    #si no es hijo izquierdo
                    r.parent.leftnode=r.rightnode
                    print("key eliminada:",retorno)   
        #cuando tiene solo hijo (izquierdo)     
        if r.leftnode!=None and r.rightnode==None:   
            print("Con hijo izquierdo")
            if r!=B.root:
                if r.parent.rightnode==r:
                    #si r es el hijo derecho   
                    r.parent.rightnode=r.leftnode
                    print("key eliminada:",retorno)
                else:
                    r.parent.leftnode=r.leftnode
                    print("key eliminada:",retorno)

        #cuando tiene 2 hijos 
        if r.leftnode!=None and r.rightnode!=None:
            mayores=LinkedList()
            #devuelve la key del nodo que reemplazara al nodo a borrar
            MayorDeSusMenores(r.leftnode,0,mayores)

            newNode=BinaryTreeNode()
            DevuelveNodo(r,mayores.head.value,newNode)
            #eliminar nodo igual a newNode
            NodoIgualnewNode(B.root,newNode,B)

            r.key=newNode.key
            r.value=newNode.value
            
            
            # print("##:",mayores.head.value)
            # print("key eliminada:",retorno)
    ##

    if r.rightnode!=None:
        deleteKeyAvlV2(r.rightnode,k,retorno,B)
   
  

def deleteKeyAvl(B,k):
    if B==None or k==None:
        return None
    else:
        r=B.root
        retorno=None
        deleteKeyAvlV2(r,k,retorno,B)
        

        reBalance(B)

        calculateBalance( B )
