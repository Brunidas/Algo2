# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp5


from algo1 import*
from linkedlist import*
from math import*



# Funciones de HASH

# -- metodo de la divicion --
def hashDiv( m, k ):
    return k % m

# -- metodo de la multiplicacion --
def hashMul( m, k ):
    A = ( sqrt( 5 ) - 1 ) / 2
    return ( m *( k * A % 1 ) )

# -- hash del punto4 --
def hashPunto4 ( k ) :
    return ord( k )

# -- hash del punto6 --
def hashPunto6( string ):
    resultado = 0

    cadena0 = ord( string[0] ) 
    
    cadena1 = ( ord( string[1] ) * (10**3) ) + ( ord( string[2] ) * (10**2) ) +( ord( string[3] ) * (10**1) )

    cadena2 = ( ord( string[5] ) * (10**3) ) + ( ord( string[6] ) * (10**2) ) +( ord( string[7] ) * (10**1) )
    
    
    return( cadena0 + cadena1 + cadena2 )

# -- funcion universal de hash --
def hashUni ( k, a, b, m, p ) :
    ''' k: key , p: numero primo, m: tamaño de hash table, a: elemento del conjuto Za y b: elemento del conjuto Zb.
    Debe cumplirse: 0 < k < p , m < P
    '''
    return ( ( a * k ) % p ) % m
    ''' 
    Datos necesarios para hash universal
    p = 7 
    Za= Array( p-1, 0 )
    for i in range( len(Za) ):
        Za[ i ] = i

    Zb = Array( p-2, 0 )
    cont = 1
    i = 0
    while cont != 6:
        Zb[ i ] = cont

        cont += 1
        i += 1

    a = randint( 0, len(Za) )
    b = randint( 0, len(Zb) )'''

# -- linear probing --
def hashLinP( k, m, i ):
    h = hashDiv( m,k)
    return (h + i) % m

# -- quadratic probing --
def hashQuaP( k, m, i ):
    h = hashDiv( m, k)
    c1 = 1
    c2 = 3
    return (h + ( c1 * i ) + ( c2 * (i ** 2) ) ) % m

# -- doble hash --
def DoubleHash( k, m, i):
    '''
    m debe ser potencia de 2 => h2(k) siempre debe devolver un numero impar
    m debe ser primo => h2(k) siempre debe devolver un numero menor a m
    '''
    # h1 = hashDiv( m, k )
    # h2 = 1 + hashDiv( m-2 ,k )
    
    h1 = k
    h2 = 1 +(k % ( m - 1))

    return ( h1 + ( i * h2 ) ) % m 




# Funciones Utilizadas
# ------------------------------------

class DictionaryNode():
    value=None
    nextNode=None
    key = None

# ------------------------------------

def addLinkedListD(L, key , value ):
    newNode = DictionaryNode()
    newNode.value = value
    newNode.key = key 
    newNode.nextNode = L.head

    L.head = newNode 

# ------------------------------------

def deleteLinkedListD(L, key):
    position  = searchLinkedListD(L, key)
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

# ------------------------------------


def searchLinkedListD( L, key ):
    if L==None:
        return None
    else:
        retorno = None
        cont = 0
        currentNode = L.head
        while( currentNode != None):
            if (currentNode.key == key ):
                retorno = cont 
            cont += 1
            currentNode = currentNode.nextNode
        return retorno

# ------------------------------------

def insertLinkedListD(L, key, element, position):
    #inserta el elemento en la primera posicion 
    if (position == 0):
        addLinkedListD(L, key , element )
        return position
    
    # si la posicion a insertar es en nodo "None"  el nodo se insertara ahi
    # y la lista tendra un nodo mas 
    elif position == length(L):
        newNode = DictionaryNode()
        newNode.value = element
        newNode.key = key 


        currentNode = L.head
        while( currentNode != None):
            if ( currentNode.nextNode == None):
                currentNode.nextNode = newNode
                break
            currentNode = currentNode.nextNode
        return length(L)
        
    #inserta el elemento en la position y desplaza los demas elementos 
    elif position < length(L) :
        newNode = DictionaryNode()
        newNode.value = element
        newNode.key = key

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

# ------------------------------------

def printDictionary( D ):
    tam =  len(D)
    cadena = ""
 
    """➜"""
 
    for i in range( len( D ) ):
        
        cadena += str( i ) + ":"
        
        # print( i ) 
        
        if D[ i ] !=None: 
            currentNode = D[ i ].head
        
            cadena +=  "➜ "
        
            while( currentNode != None):
                if currentNode.key != None:
                    
                    # print( currentNode.key, currentNode.value ) 
                    
                    if currentNode.key=="deleted" and currentNode.value=="deleted":
                        cadena += "["
                        cadena += "deleted"
                        cadena += "] ➜ "

                    # elif currentNode.key==None and currentNode.value==None:
                    #     cadena += "["
                    #     cadena += "None"
                    #     cadena += "] ➜ "


                    else:
                        cadena += "["
                        cadena = cadena + str( currentNode.key ) + ',' + str( currentNode.value )
                        cadena += "] ➜ "

                currentNode = currentNode.nextNode

            cadena = cadena + " None"
            
            print( cadena )
            cadena = ""
        else:
            cadena +=  "➜ "
            cadena = cadena + " None"
            print( cadena )
            cadena = ""


'''
Ejercicio 2
A partir de una definición de diccionario como la siguiente:

dictionary = Array(m,0)

Crear un modulo de nombre dictionary.py que implemente las siguientes especificaciones de las operaciones elementales para el TAD diccionario .

Nota: puede dictionary puede ser redefinido para lidiar con las colisiones por encadenamiento



insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar 
Salida: Devuelve D
'''

def insertD( D, key, value ):
    # busqueda = searchD( D, key )
    # if busqueda == None:
        
        tam = len( D )

        newNode = DictionaryNode()
        newNode.value = value
        newNode.key = key


        pos = hashDiv( tam, key )

        if D[ pos ] == None:
            L = LinkedList()
            addLinkedListD( L, key , value )
            D[ pos ] = L        
        else:
            indexLista = length( D[pos])
            L = D[pos]
            insertLinkedListD( L, key, value, indexLista )


        return D

    # else:
    #     return D

# ------------------------------------

def hashInsert( T, key, value ):
    
    tam = len( T )

    newNode = DictionaryNode()
    newNode.value = value
    newNode.key = key


    i = 0
    while i < tam:
        j = DoubleHash( key, tam, i)
    

        if T[ j ] == None:
            L = LinkedList()
            addLinkedListD( L, key , value )
            T[ j ] = L
            return
        else:
            if T[ j ].head.key == "deleted":
                L = LinkedList()
                addLinkedListD( L, key , value )
                T[ j ] = L
                return 
            
            
            i += 1

# ------------------------------------

def hashInsertLinP( T, key, value ):
    
    tam = len( T )

    newNode = DictionaryNode()
    newNode.value = value
    newNode.key = key


    i = 0
    while i < tam:
        j = hashLinP( key, tam, i)

        # print("j:",j)
        if T[ j ] == None:


            # print("value:",value)
            
            L = LinkedList()
            addLinkedListD( L, key , value )
            T[ j ] = L
            return
        else:
            if T[ j ].head.key == "deleted":
                L = LinkedList()
                addLinkedListD( L, key , value )
                T[ j ] = L
                return 
            
            
            i += 1

# ------------------------------------

def hashInsertQuaP( T, key, value ):
    
    tam = len( T )

    newNode = DictionaryNode()
    newNode.value = value
    newNode.key = key


    i = 0
    while i < tam:
        j = hashQuaP( key, tam, i)
    

        if T[ j ] == None:
            L = LinkedList()
            addLinkedListD( L, key , value )
            T[ j ] = L
            return
        else:
            if T[ j ].head.key == "deleted":
                L = LinkedList()
                addLinkedListD( L, key , value )
                T[ j ] = L
                return 
            
            
            i += 1



'''
search(D,key)
	Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
'''

def searchD( D, key ):
    tam = len( D )
    pos = hashDiv( tam, key )

    # busca en la lista si existe el elemnto de la key 
    retorno = searchLinkedListD( D[pos], key ) 
    
    if retorno == None:
        return None
    else:
        return key

# ------------------------------------

def hashSearch( T, key ):
    
    tam = len( T )

    i = 0
    while i < tam:
        j = DoubleHash( key, tam, i)
        
        # print( "j:", j)
        # print(T[ j ].head.key )

        if T[ j ] == None:
            a = None
        else:
            a = T[ j ].head.key 

        if a == key:
            return j
        else:
            i += 1
    
    return None


'''
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo  el key  a eliminar.  
Entrada: El diccionario sobre se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D
'''
def deleteD( D, key ):
    busqueda = searchD( D, key )
    
    if busqueda == None:    
        return D
    else:
        tam = len( D )
        pos = hashDiv( tam, key )

        L = D[ pos ]

        deleteLinkedListD( L, key )

        return D

# ------------------------------------


def hashDelete( T, key ):
    
    busqueda = hashSearch( T, key )

    if  busqueda == None:
        return None
    else:
        L =  LinkedList()       
        insertLinkedListD( L,"deleted","deleted", 0 )
        T[ busqueda ] = L
        return busqueda


