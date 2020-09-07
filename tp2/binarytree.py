# Bruno Fuentes
# 12401

from linkedlist import*
from queue import*

class BinaryTree:
	root=None

class BinaryTreeNode:
	key=None
	value=None
	leftnode=None
	rightnode=None
	parent=None

#punto1
"""
search(B,element)
Descripción: Busca un elemento  en el TAD árbol binario.
Entrada: el árbol binario B en el cual se quiere realizar la búsqueda (BinaryTree) y el valor del elemento (element) a buscar.
Salida: Devuelve la key asociada a la primera instancia del elemento. Devuelve None si el elemento no se encuentra.
"""

def searchB(B,element):
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


"""
insert(B,element,key)
Descripción: Inserta un elemento con una clave determinada del TAD árbol binario.
Entrada: el árbol B sobre el cual se quiere realizar la inserción (BinaryTree), el valor del elemento (element) a insertar y la clave (key) con la que se lo quiere insertar.
Salida: Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None. 
"""
def insertBv2(newNode,currentnode):
    if newNode.key!=currentnode.key:
        if newNode.key > currentnode.key:
            if currentnode.rightnode==None:
                newNode.parent=currentnode
                currentnode.rightnode=newNode
                
            else:
                insertBv2(newNode,currentnode.rightnode)
        else:
            if currentnode.leftnode ==None:
                newNode.parent=currentnode
                currentnode.leftnode=newNode
            else:
                insertBv2(newNode,currentnode.leftnode)
    else:
        return None

def insertB(B,e,k):
    if B==None:
        return None
    else:
        newNode=BinaryTreeNode()
        newNode.key=k
        newNode.value=e
        currentnode=B.root
        insertBv2(newNode,currentnode)

"""
delete(B,element)
Descripción: Elimina un elemento del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.  
Entrada: el árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor del elemento (element) a eliminar.
Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
"""
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


def deleteBv2(r,e,retorno,B):
    ##
    if r.leftnode!=None:
        deleteBv2(r.leftnode,e,retorno,B)

    if r.value==e:
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
            
            
            print("##:",mayores.head.value)
            print("key eliminada:",retorno)
    ##

    if r.rightnode!=None:
        deleteBv2(r.rightnode,e,retorno,B)
   
  
def deleteB(B,element):
    if B==None or element==None:
        return None
    else:
        r=B.root
        retorno=None
        
        deleteBv2(r,element,retorno,B)

"""
deleteKey(B,key)
Descripción: Elimina una clave del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.  
Entrada: el árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor de la clave (key) a eliminar.
Salida: Devuelve clave (key) a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
"""

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


def deleteKeyv2(r,k,retorno,B):
    ##
    if r.leftnode!=None:
        deleteKeyv2(r.leftnode,k,retorno,B)

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
            
            
            print("##:",mayores.head.value)
            print("key eliminada:",retorno)
    ##

    if r.rightnode!=None:
        deleteKeyv2(r.rightnode,k,retorno,B)
   
  

def deleteKey(B,k):
    if B==None or k==None:
        return None
    else:
        r=B.root
        retorno=None
        deleteKeyv2(r,k,retorno,B)




"""
access(B,key)
Descripción: Permite acceder a un elemento del árbol binario con una clave determinada.
Entrada: El árbol binario (BinaryTree) y la key del elemento al cual se quiere acceder.
Salida: Devuelve el valor de un elemento con una key del árbol binario, devuelve None si no existe elemento con dicha clave.
"""
def accessB(B,k):
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
    

"""
update(L,element,key)
Descripción: Permite cambiar el valor de un elemento del árbol binario con una clave determinada.
Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual se quiere asignar el valor de  element. 
Salida: Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update.

"""
def updateB(B,element,k):
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
    




#########################################################
#punto2





#entra una lista vacia(Q) y una lista con los datos(L)
#sale la lista(Q) con los datos al revez y (L) queda vacia
def voltearlista(L,Q):
    index=0

    currentNode=L.head
    while currentNode!=None:
        if currentNode.nextNode==None:
            insert(Q,currentNode.value,index)
            index=index+1

            delete (L,currentNode.value)

            currentNode=L.head

        currentNode=currentNode.nextNode
        
    insert(Q,L.head.value,index)
    delete(L,L.head.value)
    
"""
traverseInOrder(B)
Descripción: Recorre un árbol binario en orden
Entrada: El árbol binario (BinaryTree) 
Salida: Devuelve una lista (LinkedList) con los elementos del árbol en orden. Devuelve None si el árbol está vacío.
"""



def traverseInOrderv2(L,r):
    if r.leftnode!=None:
        traverseInOrderv2(L,r.leftnode)
    
    add(L,r.value)

    if r.rightnode!=None:
        traverseInOrderv2(L,r.rightnode)
 
def traverseInOrder(B):
    if B== None:
        return None
    else:
        # L lista inicial, Q lista final
        L=LinkedList()
        Q=LinkedList()


        traverseInOrderv2(L,B.root) 
        voltearlista(L,Q)

        printLinkedList(Q)


"""
traverseInPostOrder(B)
Descripción: Recorre un árbol binario en post-orden
Entrada: El árbol binario (BinaryTree) 
Salida: Devuelve una lista (LinkedList) con los elementos del árbol en post-orden. Devuelve None si el árbol está vacío.
"""
def traverseInPostOrderv2(L,r):
    if r.leftnode!=None:
        traverseInPostOrderv2(L,r.leftnode)
   
    if r.rightnode!=None:
        traverseInPostOrderv2(L,r.rightnode)
    
    add(L,r.value)

def traverseInPostOrder(B):
    if B== None:
        return None
    else:
        # L lista inicial, Q lista final
        L=LinkedList()
        Q=LinkedList()


        traverseInPostOrderv2(L,B.root) 
        voltearlista(L,Q)
        
        printLinkedList(Q)

"""
traverseInPreOrder(B)
Descripción: Recorre un árbol binario en pre-orden
Entrada: El árbol binario (BinaryTree) 
Salida: Devuelve una lista (LinkedList) con los elementos del árbol en pre-orden. Devuelve None si el árbol está vacío.
"""
def traverseInPreOrderv2(L,r):
    add(L,r.value)
    
    if r.leftnode!=None:
        traverseInPreOrderv2(L,r.leftnode)
        
    if r.rightnode!=None:
        traverseInPreOrderv2(L,r.rightnode)
    

def traverseInPreOrder(B):
    if B== None:
        return None
    else:
        # L lista inicial, Q lista final
        L=LinkedList()
        Q=LinkedList()


        traverseInPreOrderv2(L,B.root) 
        voltearlista(L,Q)
        printLinkedList(Q)


"""
traverseBreadFirst(B)
Descripción: Recorre un árbol binario en modo primero anchura/amplitud
Entrada: El árbol binario (BinaryTree) 
Salida:
"""
def traverseBreadFirstv2(L,r):
    q=LinkedList()
    enqueue(q,r)
    while length(q)!=0:
        Node=dequeue(q)
        insert(L,Node.value,length(L))
        if Node.leftnode!=None:
            enqueue(q,Node.leftnode)
        if Node.rightnode!=None:
            enqueue(q,Node.rightnode)


def traverseBreadFirst(B):
    L=LinkedList()
    traverseBreadFirstv2(L,B.root)
    printLinkedList(L)


# URL : https://repl.it/@BrunoFuentes/BinaryTree