# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp4


from algo1 import*
from print_tree import*
from linkedlist import*
from binarytree import*
from stack import *


class Trie:
	root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


'''
Ejercicio 1
Crear un modulo de nombre trie.py que implemente las siguientes especificaciones de las operaciones elementales para el TAD Trie .

insert(T,element) 
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida

search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
Salida: Devuelve False o True  según se encuentre el elemento.
'''
# imprime una LinkedList con nodos Trie
def printLinkedListTrie(L):
    if L==None:
        print( None )
    else:
        cadena = ""
        """➜"""
        currentNode = L.head
        while( currentNode != None):
            cadena = cadena + str( currentNode.value.key ) + ' ➜ ' 

            currentNode = currentNode.nextNode
        cadena = cadena + "None"
        print(cadena)

######################################################################
def imprimirHastaRoot( r, nodoTrie ):
    if nodoTrie.parent != None:
        add( r , nodoTrie.parent.key )
        imprimirHastaRoot( r, nodoTrie.parent )
    else:
      return


def printTrieV2( nodoTrie, listaHijos, resultado ):
    if nodoTrie.isEndOfWord:
        # print( nodoTrie.key )
        add( resultado, nodoTrie.key )
        imprimirHastaRoot( resultado, nodoTrie )

    if listaHijos == None:
        return 
    else:
        currentNode = listaHijos.head
        while currentNode != None:

            # if currentNode.value.children != None:
            printTrieV2( currentNode.value, currentNode.value.children, resultado ) 


            currentNode = currentNode.nextNode  


def printTrie( T ):
    if T.root == None:
        print( None )
    else:
        resultado = LinkedList()
        printTrieV2( T.root, T.root.children, resultado )

        # printLinkedList( resultado )
            
        stringFinal = ""
        currentNode = resultado.head
        while currentNode!=None:
            if currentNode.value == None:
                stringFinal += " "
            else:
                stringFinal += currentNode.value
            currentNode = currentNode.nextNode

        print( stringFinal )


######################################################################
def insertTrie(T,element):
#   print(element)
  if T.root == None:
    #Si la raíz esta vacia, inicializamos el árbol.
    T.root = TrieNode()
    # T.root.key = "Root"
    T.root.children = LinkedList()

    parentTrieNode = T.root
    currentList = T.root.children
    finished = False
    i = 0
    elementlength = len(element)

    while finished == False:

      newNode = TrieNode()
      newNode.key = element[i]


      insert(currentList,newNode,0)
    #   print(currentList.head.value.key)

      if i+1 < elementlength:

        newNode.children = LinkedList()
        newNode.parent = parentTrieNode
        parentTrieNode = currentList.head.value
        currentList = newNode.children
        i+=1

      else:

        newNode.isEndOfWord = True
        newNode.parent = parentTrieNode
        finished = True

  else:
    #Si la raiz no está vacía.

    elementlength = len(element)
    currentTrieNode = T.root
    currentList = currentTrieNode.children
    currentNode = currentList.head
    i = 0
    found = 0
    searching = True
    insertionfinished = False

    while searching == True:
    
      if currentNode != None and currentNode.value.key == element[i]:
        # print("Encontrada coincidencia.")
        found+=1
        if found == elementlength:

          searching = False
          currentNode.value.isEndOfWord = True
          insertionfinished = True

        else:

          currentTrieNode = currentNode.value
          currentList = currentTrieNode.children
        
          if currentList != None:

            currentNode = currentList.head

          else:

            searching = False

          i+=1

      elif currentNode == None:

        searching = False
        
      else:

        currentNode = currentNode.nextNode
    
    while insertionfinished == False:

      newNode = TrieNode()
      newNode.key = element[i]
      newNode.parent = currentTrieNode

      if currentTrieNode.children == None:

        currentTrieNode.children = LinkedList()
        # print("Nueva lista añadida.")
        currentList = currentTrieNode.children
        insert(currentList,newNode,length(currentList))
        currentTrieNode = newNode
        # print("elemento ",i," ",element[i]," insertado.")

      else:

        currentList = currentTrieNode.children
        # print("Elemento insertado en la lista de hijos de: ", currentTrieNode.key)
        insert(currentList,newNode,length(currentList))
        currentTrieNode = newNode
        # print("elemento ",i," ",element[i]," insertado.")

      i+=1

      if i == elementlength:
        # print("El ultimo elemento es: ",currentTrieNode.key)
        currentTrieNode.isEndOfWord = True
        insertionfinished = True
        # print("Insercion finalizada.")

#   print("--------------------")    



def searchTrie(T,element):
  if T.root == None:
    # print("El árbol está vacio por lo tanto el elemento no está contenido")
    return False      

  else:

    elementlength = len(element)
    currentList = T.root.children
    currentNode = currentList.head
    searching = True
    i = 0
    found = 0

    while searching == True:

      if currentNode != None and currentNode.value.key == element[i]:

        found+=1
        if found == elementlength and currentNode.value.isEndOfWord == True:
          return True
        elif found == elementlength and currentNode.value.isEndOfWord == False:
          return False
        else:
        
          currentList = currentNode.value.children
          currentNode = currentList.head
          i+=1

      elif currentNode == None:
          
        searching = False
        return False

      else:

        currentNode = currentNode.nextNode

    return False



######################################################################
'''
Ejercicio 3
delete(T,element)
Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Tr
y el valor del elemento (palabra) a eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento
'''

def deleteTrie( T, element ):
    
    if searchTrie( T, element ) == False :
        return False
    else:

        posicionCorrecta = False
        currentTrieNode = T.root  
        currentNode = T.root.children.head
        i = 0
        elementosEncontrados = 0
        tamString = len( element )

        # al terminar este bucle en currentTrieNode se deberia 
        # guardar el nodo de fin de palabra a eliminar
        while posicionCorrecta == False :
  
            if currentNode.value.key == element[i]:
                
                elementosEncontrados += 1
                
                if elementosEncontrados == tamString:
                    
                    currentTrieNode = currentNode.value
                    # currentTrieNode.isEndOfWord = False
                    posicionCorrecta = True
                
                else:
                    currentNode = currentNode.value.children.head
                    i += 1

            else:
                currentNode = currentNode.nextNode


        finalEliminado = False
        currentNode = currentTrieNode
        while currentNode.parent != None:
            # print nodo actual
            print("Nodo actual:", currentNode.key )
            print("Final de palabra:" ,currentNode.isEndOfWord )
            

            if currentNode.isEndOfWord and finalEliminado == False :
                
                if  currentNode.children != None :
                    # pregunta si el nodo tiene hijos
                    currentNode.isEndOfWord = False
                    finalEliminado = True
                    currentNode = currentNode.parent #sube de nivel
                else:
                    # cuando no tiene hijos entra aqui
                    
                    if length( currentNode.parent ) == 1 :
                        # si el padre tiene solo un hijo
                        currentNode.parent.children =  None #desvivula el hijo
                        currentNode = currentNode.parent #sube de nivel
                    
                    else:
                        # cuando el padre tiene mas de un hijo
                        delete( currentNode.parent.children, currentNode )
                                # lista de los hijos , hijo a eliminar
                        finalEliminado = True
                        currentNode = currentNode.parent #sube de nivel

            else:
                if currentNode.children != None:
                    currentNode = currentNode.parent #sube de nivel

                else:
                    currentNode.parent = None
                    currentNode = currentNode.parent #sube de nivel


######################################################################



'''
Parte 2
Ejercicio 4
Escribir una algoritmo que dado un árbol Trie T, una palabra p y un entero n, escriba todas las palabras del árbol que empiezan por p y sean de longitud n.
'''
def palabraTamanoNV2( index, TrieNode, r ):
    # print( "index:",index)
    # print("Nodo",TrieNode.key)

    if index == 0:
        if TrieNode.isEndOfWord:
            add( r, TrieNode.key )
            imprimirHastaRoot( r, TrieNode )
        # else:
        #     print( "NADA" )
            
    else:
        if TrieNode.children != None:
            index -= 1

            currentNode = TrieNode.children.head
            while currentNode!=None:
                palabraTamanoNV2( index, currentNode.value , r )

                currentNode = currentNode.nextNode
            
            index += 1

        # else:
        #     print( "NADA" )


def palabraTamanoN( T, p, n ):
    posicionCorrecta = False
    currentTrieNode = T.root  
    currentNode = T.root.children.head
    i = 0 #longitud encontrada
    elementosEncontrados = 0
    tamString = len( p )

    # al terminar este bucle en currentTrieNode se deberia 
    # guardar el nodo de donde termina la cadena p
    # en caso de que no se encuetre posicionCorrecta == False 
    while posicionCorrecta == False :
        if currentNode == None:
            return

        elif currentNode.value.key == p[i]:
            
            elementosEncontrados += 1
            
            if elementosEncontrados == tamString:
                
                currentTrieNode = currentNode.value
                # currentTrieNode.isEndOfWord = False
                posicionCorrecta = True
            
            else:
                currentNode = currentNode.value.children.head
                i += 1

        else:
            currentNode = currentNode.nextNode
    

    # si la cadena no esta en el arbol sale del programa
    if posicionCorrecta == False:
        return None
    else:
        r = LinkedList() #resultado
        i += 1
        nivelesABajar = n - i

        palabraTamanoNV2( nivelesABajar, currentTrieNode, r )

        stringFinal = ""
        currentNode = r.head
        while currentNode!=None:
            if currentNode.value == None:
                stringFinal += " "
            else:
                stringFinal += currentNode.value
            currentNode = currentNode.nextNode

        print( stringFinal )




'''
Ejercicio 5
Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo
documento y False en caso contrario. Se considera que un 2 Trie pertenecen al mismo documento
cuando:
1 . Ambos Trie sean iguales
2. El Trie A contiene un subconjunto de las palabras del Trie B.
3. Si la implementación está basada en LinkedList, considerar el caso donde las hayan sido
insertadas en un orden diferente.
Analizar el costo computacional.
'''
def convertirAlista( T ):
    resultado = LinkedList()
    printTrieV2( T.root, T.root.children, resultado )
    # se guradan las palabras de arbol T en una lista
    lista = LinkedList() 
    string = ""
    currentNode = resultado.head
    while currentNode!=None:
        if currentNode.value == None:
            add( lista, string )
            string=""
        else:
            string += currentNode.value
        currentNode = currentNode.nextNode
    add( lista, string )
    delete( lista,"" )
    
    return( lista )



def mismoDocumento( T1, T2 ):
    if T1.root == None or T1.root == None:
        print( None )
    else:
        # a partir del arbol T1 creo una lista L1 con sus palabras dentro
        L1 = LinkedList()
        L1 = convertirAlista( T1 )

        # a partir del arbol T2 creo una lista L2 con sus palabras dentro
        L2 = LinkedList()
        L2 = convertirAlista( T2 )

        printLinkedList( L1 )
        printLinkedList( L2 )

        tam = length(L1)

        # si el tamaño de las listas es distino no pueder ser iguales
        if length( L1 ) == length( L2 ):
            cont = 0
            for i in range( tam ):
                # comparo si son iguales L1 y L2 miebro a miebro
                if access( L1,i ) == access( L2, i ):
                    cont += 1

            if cont == tam:
                # los arboles son iguales
                print("son iguales")
                return True


        # si L1 tiene por lo menos un conjunto de L2
        # L2 es subconjunto de L1
        for i in range( tam ):
            for j in range( tam ):
                if access( L1,i ) == access( L2, j ):
                    print("L2 es subconjunto de L1")
                    return True

        
        return False



'''
Ejercicio 6
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas
invertidas. Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos
caracteres que si se lee de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y
asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren en un
carácter.
'''
def invertirPalabra( palabra ):
    palabraIvertida = ""
    for i in range( len(palabra)-1, -1, -1 ):
        palabraIvertida += palabra[i] 
    return palabraIvertida


def cadenasInvetidas( T ):
    if T.root == None:
        print( None )
    else:
        resultado = LinkedList()
        printTrieV2( T.root, T.root.children, resultado )


        # se guradan las palabras de arbol en una lista
        lista = LinkedList() 
        string = ""
        currentNode = resultado.head
        while currentNode!=None:
            if currentNode.value == None:
                add( lista, string )
                string=""
            else:
                string += currentNode.value
            currentNode = currentNode.nextNode
        add( lista, string )
        delete( lista,"" )
        

        # copio los valores de lista en listaInvertida
        listaInvertida = LinkedList()
        currentNode = lista.head
        while currentNode!=None:
            add( listaInvertida, currentNode.value )
            currentNode = currentNode.nextNode 


        # inviero los valores de la listaInvertida
        currentNode = listaInvertida.head
        while currentNode!=None:
            currentNode.value = invertirPalabra( currentNode.value )
            currentNode = currentNode.nextNode 



        tam = length( listaInvertida )
        # creo una nueva lista 
        listaInvertidaFinal = LinkedList()
        voltearlista( listaInvertida, listaInvertidaFinal )



        printLinkedList( lista )
        printLinkedList( listaInvertidaFinal )



        # recorre las dos lista y si encuetra que alguna palabra
        # de la LinkedList "lista" que es igual algun elemento de la 
        # LinkedList "listaInvertidaFinal" devuele True
        for i in range( tam ):
            for j in range( tam ):
                
                if i!=j:
                    string1 = access( lista,i ) 
                    string2 = access( listaInvertidaFinal, j) 
                    if string1 == string2 :
                        return True
        return False

'''
Ejercicio 7
Un corrector ortográfico interactivo utiliza un Trie para representar las palabras de su diccionario.
Queremos añadir una función de auto-completar (al estilo de la tecla TAB en Linux): cuando estamos
a medio de escribir una palabra, si sólo existe una forma correcta de continuarla entonces debemos
ndicarlo.
mplementar la función autoCompletar(Trie, cadena) dentro del módulo trie. py, que dado el árbol
Trie T y la cadena “pal” devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada
autoCompletar(T, ‘groen’) devolvería “land”, ya que podemos tener “groenlandia” o
“groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que
representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. Por ejemplo,
autoCompletar(T, ma’) devolvería “” si T presenta las cadenas “madera” y “mama”.
'''

def autoCompletar( T, cadena) :
    posicionCorrecta = False
    currentTrieNode = T.root  
    currentNode = T.root.children.head
    i = 0 #longitud encontrada
    elementosEncontrados = 0
    tamString = len( cadena )

    # al terminar este bucle en currentTrieNode se deberia 
    # guardar el nodo de donde termina la cadena 
    # en caso de que no se encuetre posicionCorrecta == False 
    while posicionCorrecta == False :
        if currentNode == None:
            return

        elif currentNode.value.key == cadena[i]:
            
            elementosEncontrados += 1
            
            if elementosEncontrados == tamString:
                
                currentTrieNode = currentNode.value
                # currentTrieNode.isEndOfWord = False
                posicionCorrecta = True
            
            else:
                currentNode = currentNode.value.children.head
                i += 1

        else:
            currentNode = currentNode.nextNode
    

    # print( currentTrieNode.key )

    # si la cadena no esta en el arbol sale del programa
    if posicionCorrecta == False:
        return ""
    else:
        string =""
        final = False

        while final == False:
            if currentTrieNode.children == None: 
                # si no tiene hijos termina 
                final = True
            else:
                if length( currentTrieNode.children ) == 1:
                    #agrego el hijo a string
                    string += currentTrieNode.children.head.value.key

                    currentTrieNode = currentTrieNode.children.head.value
                elif length( currentTrieNode.children ) > 1:
                    final = True 
        
        return( string )

            

        
