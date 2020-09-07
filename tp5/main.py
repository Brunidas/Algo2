# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp5


from algo1 import*
from linkedlist import*
from dictionary import*
from binarytree import*
from random import*

# print("punto 2\n")
# tam = 9
# D = Array( tam, LinkedList() )


# insertD( D, 5, "A" )
# insertD( D, 28, "B" )
# insertD( D, 19, "C" )
# insertD( D, 15, "D" )
# insertD( D, 20, "E" )
# insertD( D, 33, "F" )
# insertD( D, 12, "G" )
# insertD( D, 17, "H" )
# insertD( D, 10, "I" )


# printDictionary( D )
# print("- - - - - -")
# deleteD( D, 19 )
# printDictionary( D )

# print("- - - - - - - - - - - - - ")




'''
PARTE 2

Ejercicio 3
Considerar una tabla hash de tamaño m = 1000 y una función de hash correspondiente al método de la multiplicación donde A = (sqrt(5)-1)/2). Calcular las ubicaciones para las claves 61,62,63,64 y 65.
'''
print("punto 3\n")

m = 1000
D = Array( m, LinkedList() )

print( hashMul( m, 61 ) )
print( hashMul( m, 62 ) )
print( hashMul( m, 63 ) )
print( hashMul( m, 64 ) )
print( hashMul( m, 65 ) )
print("- - - - - - - - - - - - - ")


'''
Ejercicio 4
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: S = ‘hola’ , P = ‘ahlo’
Salida: True, ya que P es una permutación de S

Ejemplo 2:
Entrada: S = ‘hola’ , P = ‘ahdo’
Salida: Falso, ya que P tiene al caracter ‘d’ que no se encuentra en S por lo que no es una permutación de S 

'''

def pasarANumero( string ):
    retorno = 0
    for i in range( len(string) ):
        retorno += hashPunto4( string[i] )

    return retorno 

def punto4( s, p ):
    '''S y P son strings'''
    if len( s ) == len( p ):
        
        sEnNumero = pasarANumero( s )
        pEnNumero = pasarANumero( p )

        if sEnNumero == pEnNumero:
            return True
        else:
            return False


    else:
        return False


print("punto 4 \n")
print( punto4("hola", "hoal") )
print("- - - - - - - - - - - - - ")

'''
Su complejidad de es de O(n) lo cual se lo da funcion 
pasarANumero ya que cuenta con un ciclo for
'''



'''
Ejercicio 5
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: L = [1,5,12,1,2]
Salida: Falso, L no tiene todos sus elementos únicos, el 1 se repite en la 1ra y 4ta posición

'''
def punto5( L ):

    max = 0
    
    currentNode = L.head
    while currentNode != None: 
        if max < currentNode.value:
            max = currentNode.value

        currentNode = currentNode.nextNode
    
    D = Array( max+1, LinkedList() )

    currentNode = L.head
    while currentNode != None: 
        if D[ currentNode.value ] != None:
            print()
            return False
        else:
            insertD( D, currentNode.value, currentNode.value )

        currentNode = currentNode.nextNode

    return True

print("punto 5 \n")
L = LinkedList( )
add( L, 2)
add( L, 1)
add( L, 12)
add( L, 5)
add( L, 1)
print( punto5( L ) )
print("- - - - - - - - - - - - - ")

'''
Tiene una complejidad de O(n) ya que cuenta con ciclo while
no anidados
'''



'''
Ejercicio 6
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e implementar una función de hash apropiada para los códigos postales argentinos.
'''
print("punto 6 \n")

print( hashPunto6("C1024CWN") )
print("- - - - - - - - - - - - - ")




'''
Ejercicio 7
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.

'''


def punto7 ( string ):
    aux = ""
    L = LinkedList()

    cont = 0 
    for i in range( len( string ) ):

        if i == 0:
            cont += 1

            aux += string[ i ]
        else:
            if string[ i ] == string[ i-1 ]:
                cont += 1

                aux += string[ i ]
            else:
                add( L, aux )
                aux = ""


                aux += string[ i ]

                cont = 1  

    add( L, aux )

    S = LinkedList()
    voltearlista( L, S)


    D = Array( length( S ), LinkedList() )

    for i in range( length( S ) ):
        cadena = access( S, i )


        for j in range( len( cadena ) ):
            # a = substr( cadena, 0, j+1, )
            a = cadena[0]

            insertD( D, i, a )

    printDictionary( D )

    retorno = ""
    for i in range( length( S ) ):
        cadena = access( S, i )
        
        retorno += cadena[0]
        if length( D[ i ] ) > 1:
            retorno += str( length( D[ i ] ) )

    # print( retorno )

    if len( retorno ) > len( string ):
        return string
    else:
        return retorno



print("punto 7 \n")
a = punto7( "aabcccccaaa" )
print( a )
print("- - - - - - - - - - - - - ")

'''
Su complejidad es de O(n^2) ya que para insertar 
las palabras en el diccionario ultiliza 2 ciclos 
for anidados 
'''





'''Ejercicio 8
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta).  Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: S = ‘abracadabra’ , P = ‘cada’
Salida: 4, índice de la primera ocurrencia de P dentro de S (abracadabra)'''


def punto8( s, p ):
    
    L = LinkedList()
    tam = 23
    D = Array( tam, LinkedList() )


    # recorro la primer cadena( la mas larga)
    for i in range( len (s) ):

        key = DoubleHash( i+1, tam, i )  


        a = Array(2,0) #en este array guardo:
                         #el indice de cada caracter en (0)
                         #y su key en (1)

        a[ 0 ] = i
        a[ 1 ] = key
        insert( L, a, i )

        hashInsert( D, key, s[ i ] )


    cont = 0
    currentNode = L.head
    while currentNode!=None :
        indexChar = currentNode.value[ 0 ] 
        keyChar = currentNode.value[ 1 ] 
        valorDic = D[ keyChar ].head.value
        

        if valorDic == p[ cont ]:
            cont += 1
        else:
            cont = 0

        if cont == len( p ):
            # print("indice:",indexChar)
            # print("key :",keyChar)
            # print("valor en dicc:",valorDic,"\n")

            return len(s)-indexChar



        currentNode = currentNode.nextNode



print("punto 8 \n")
print( punto8( "habracadabra", "cada" ) )
print("- - - - - - - - - - - - - ")

'''
tomando como contante el factor de carga 
cunado se inseta un valor en el diccionairio seria
de complejidad O(1) entonces la complejidad del argoritmo 
es O(n), esto se lo da el recorrer alguna cadena
'''


'''
Ejercicio 9
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal de caso promedio del algoritmo propuesto?
'''
def punto9( s, t ):
    # sabiendo que t es mas grande
    tam = 23
    D = Array( tam, LinkedList() )


    llavero = LinkedList()

    for i in range( len( t ) ):
        
        key = DoubleHash( t[i], tam, t[i] )  

        
        # print("key t:", key)
        hashInsert( D, key, t[ i ] )


    # print("- - - -")
    # printDictionary( D )
    

    cont = 0
    for i in range( len( s ) ):
        
        key = DoubleHash( s[ i ], tam, s[ i ] )  
        # print("key s:", key)
        
        if hashSearch( D, key ) != None:
            cont += 1

    if cont ==  len( s ):
        return True
    else:
        False



s = Array( 3, 0 )
s[ 0 ] = 1
s[ 1 ] = 2
s[ 2 ] = 3

t = Array( 5, 0 )
t[ 0 ] = 3
t[ 1 ] = 7
t[ 2 ] = 1
t[ 3 ] = 2
t[ 4 ] = 6


print("punto 9 \n")
print( punto9( s, t ) )
print("- - - - - - - - - - - - - ")




'''
Parte 3
Ejercicio 10
Considerar la inserción de las siguientes llaves: 10; 22; 31; 4; 15; 28; 17; 88; 59 en una tabla hash de longitud m = 11 utilizando direccionamiento abierto con una función de hash h’(k) = k. Mostrar el resultado de insertar estas llaves utilizando:
1-Linear probing
2-Quadratic probing con c1 =  1 y c2 = 3 
3-Double hashing con  h1(k) = k y  h2(k) = 1 +(k mod ( m - 1))

'''

print("punto 10 \n")
m = 11

Linear probing
D1 = Array( m, LinkedList() )
hashInsertLinP( D1, 10, "A" )
hashInsertLinP( D1, 22, "B" )
hashInsertLinP( D1, 31, "C" )
hashInsertLinP( D1, 4, "D" )
hashInsertLinP( D1, 15, "E" )
hashInsertLinP( D1, 28, "F" )
hashInsertLinP( D1, 17, "G" )
hashInsertLinP( D1, 88, "H" )
hashInsertLinP( D1, 59, "I" )
printDictionary( D1 )
print("- - - - -")


Quadratic probing con c1 =  1 y c2 = 3 
D2 = Array( m, LinkedList() )
hashInsertQuaP( D2, 10, "A" )
hashInsertQuaP( D2, 22, "B" )
hashInsertQuaP( D2, 31, "C" )   
hashInsertQuaP( D2, 4, "D" )
hashInsertQuaP( D2, 15, "E" )
hashInsertQuaP( D2, 28, "F" )
hashInsertQuaP( D2, 17, "G" )
hashInsertQuaP( D2, 88, "H" )
hashInsertQuaP( D2, 59, "I" )
printDictionary( D2 )
print("- - - - -")



hashInsert usa la funcion de doble hashsing
D3 = Array( m, LinkedList() )
hashInsert( D3, 10, "A" )
hashInsert( D3, 22, "B" )
hashInsert( D3, 31, "C" )
hashInsert( D3, 4, "D" )
hashInsert( D3, 15, "E" )
hashInsert( D3, 28, "F" )
hashInsert( D3, 17, "G" )
hashInsert( D3, 88, "H" )
hashInsert( D3, 59, "I" )
printDictionary( D3 )

print("- - - - - - - - - - - - - ")

'''
Ejercicio 11

Implementar las operaciones de insert() y delete() dentro de una  tabla hash vinculando todos los nodos libres en una lista. Se asume que un slot de la tabla puede almacenar un indicador (flag), un valor, junto a una o dos referencias (punteros). Todas las operaciones de diccionario y manejo de la lista enlazada deben ejecutarse en O(1). La lista debe estar doblemente enlazada o con una simplemente enlazada alcanza?
'''


print("punto 11 \n")


def insertPunto11( T, key, value ):
    
    tam = len( T )

    newNode = DictionaryNode()
    newNode.value = value
    newNode.key = key


    i = 0
    while i < tam:
        j = DoubleHash( key, tam, i)
    

        if T[ j ].head.key == None:
            L = LinkedList()
            addLinkedListD( L, key , value )
            T[ j ] = L
            break
        else:
            if T[ j ].head.key == "deleted":
                L = LinkedList()
                addLinkedListD( L, key , value )
                T[ j ] = L
                break 
            i += 1



    # print( "tam",tam)
    # print("key",j)
    if j != 0:
        if j == tam-1:
            D[ j ].head.nextNode =None
        else:
            D[ j-1 ].head.nextNode = D[ j+1 ].head

    # D[ j-1 ].head.nextNode = D[ j+1 ].head

    return D

# la funcion de delete() no se tuvo
#  que modificar para que funcione



m = 11
D = Array( m, LinkedList() )


# con una LinkedList(Q) en cada slot
# con un DictionaryNode en cada lista Q
for i in range( m ):
    newNode = DictionaryNode()
    Q = LinkedList()

    addLinkedListD( Q, None, i)

    # insert( L, Q.head, i )
    D[ i ] = Q


# se acomodan los apuntadores y se muestra:
for i in range( m-1 ):
    # print( D[i].head )
    D[ i ].head.nextNode = D[ i+1 ].head

    # print(D[ i ].head.value,"apunta a:", D[ i+1 ].head.value )
    print( D[ i ].head.value,"apunta a",D[ i ].head.nextNode.value )

insertPunto11( D, 10, "A" )
hashDelete( D, 10 )



# muesta las modificaciones :
for i in range( m ):
    # print( D[i].head )
    # D[ i ].head.nextNode = D[ i+1 ].head

    cadena = ""
    cadena = str( D[ i ].head.value )
    cadena += " apunta a "
    if ( D[ i ].head.nextNode != None ):
        cadena += str( D[ i ].head.nextNode.value )
    else:
        cadena += " None"

    print( cadena )
    
print(" - - - - - ")
printDictionary( D )

'''
Ya con todos los comentarios hechos la funcion de insert()
, en este caso llamada insertPunto11() no sufio cambios
sigficatiovos es su complejidad, Ya que no se agrego
ningun ciclo. Entoces su complejidad es de O(1)
'''