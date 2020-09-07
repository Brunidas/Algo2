# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp7

from algo1 import *
from linkedlist import *
from dictionary import *
from binarytree import *
from random import *
from queue import *
import math

#-------------------------------------------------
#imprimir matriz
def imprimir_matriz(A):
  n = len(A)
  m = len(A[0])
  cadena = "     "
  for i in range(0,m):
    cadena += str(i)
    cadena += "  "
  print(cadena)
  print("")
  for x in range(0,n):
    cadena = str(x)
    cadena += ":   "
    for y in range(0,m):
      cadena += str(A[x][y])
      cadena += "  "
    print (cadena)
#-------------------------------------------------


'''
PARTE 1
String = String(“esto es un string”)

Ejercicio 1
Implementar la función que responde a la siguiente especificación.
def existChar(String, c):
	Descripción: Confirma la existencia de un carácter específico en una cadena.
Entrada: String con la cadena en la cual buscar el carácter, c caracter a buscar en la cadena.
Salida: Retorna True si el carácter se encuentra en la cadena, o False en caso contrario'''

def existChar(String, c):
    for i in range( len(String) ):
        if String[i] == c:
            return True
    return False


'''
Ejercicio 2
Implementar una función que detecte si una cadena es un Palíndromo. La implementación debe responder a la siguiente especificación:
def isPalindrome(String):
	Descripción: Determina si la cadena es un palíndromo
Entrada: String con la cadena a evaluar.
Salida: Retorna True si la cadena es palíndromo, o False en caso contrario

 la función es Palíndromo que devuelve True si una cadena es Palindromo y Falso en caso contrario. Nota: Una cadena es palíndromo si se lee igual en ambos sentidos ej. anitalavalatina, radar.
'''

def isPalindrome(String):
    nuevoString = ""
    for i in range( len(String)-1,-1,-1 ):
        print( i )
        nuevoString += String[i]
    if String == nuevoString:
        return True
    else:
        return False


'''
Ejercicio 3
Implementar la función que responde a la siguiente especificación.
def mostRepeatedChar(String):
	Descripción: Encuentra el caracter que más se repite en una cadena.
Entrada: String con la cadena a ser evaluada.
Salida: Retorna el caracter que más se repite. En caso que haya más de un caracter con mayor ocurrencia devuelve el primero de ellos.
'''


def mostRepeatedChar(String):
    lista = LinkedList()
    for i in range( len(String) ):
        cont = 0
        for j in range( len(String) ):
            if String[i] == String[j]:
                cont += 1
        
        push(lista,String[i])
        push(lista,cont)
    
    mayor = 0
    indexMayor = 0
    for i in range( 0,length(lista),2 ):    
        if access(lista,i+1) > mayor:
            mayor = access(lista,i+1)
            indexMayor = i

    return access(lista, indexMayor )
        
'''
Ejercicio 4
Implementar la función que dado un String S devuelve la dimensión de la isla de mayor tamaño. Una isla es una secuencia consecutiva de un mismo carácter dentro de S. Por ejemplo S = “cdaaaaaasssbbb” su mayor isla es de tamaño 6 (aaaaaa) y además tiene dos islas de tamaño 3 (sss, bbb) el resto de las islas en s  son de tamaño 1.
def getBiggestIslandLen(String):
	Descripción: Determina el tamaño de la isla de mayor tamaño en una cadena.
Entrada: String con la cadena a ser evaluada.
Salida: Retorna un entero con la dimensión de la isla más grande dentro de la cadena.
'''

def getBiggestIslandLen(s):
    max = 0
    cont = 0
    for i in range(1,len(s),+1):
        if s[i] != s[i-1]:
            cont = 0
        else:
            cont += 1

        if max < cont:
            max = cont

    return max+1
    


'''
Ejercicio 5
Implementar la función que responde a la siguiente especificación.

def isAnagram(String, String):
	Descripción: Determina si una cadena es un anagrama de otra.
Entrada: Un String con la cadena original, y otro String con el posible anagrama a evaluar.
Salida: Retorna un True si la segunda cadena es anagrama de la primera, en caso contrario devuelve False.

Nota: Una cadena s es anagrama de otra cadena p si existe alguna ordenación de los elementos de s con lo cual se obtenga la cadena p
'''

def isAnagram(s1, s2):
    if len(s1) == len(s2):

        valorS1 = LinkedList()
        for i in range( len(s1) ):
            add( valorS1, s1[i] )


        valorS2 = LinkedList()
        for i in range( len(s2) ):
            add( valorS2, s2[i] )


        currentNode = valorS1.head
        cont = 0
        while currentNode != None:
            if search( valorS2,currentNode.value ) != None:
                cont += 1
                delete( valorS2,currentNode.value )

            currentNode = currentNode.nextNode

        if cont == length(valorS1):
            return True
        else:
            return False

    else:
        return False


'''
Ejercicio 6
Implementar la función que responde a la siguiente especificación.

def verifyBalancedParentheses(String):
	Descripción: Verifica si los paréntesis contenidos en una cadena se encuentran balanceados.
Entrada: Un String con la cadena a ser evaluada.
Salida: Retorna un True si la cadena posee sus paréntesis correctamente balanceados, en caso contrario devuelve False.

Ejemplo: “(ccc(ccc)cc((ccc(c))))” es correcto, pero “)ccc(ccc)cc((ccc(c)))(“ no lo es, aunque tenga el mismo número de paréntesis abiertos que cerrados.
'''


def verifyBalancedParentheses(s):
    bloque = 0 # bloque = (algo entre parentesis)
    for i in range( len(s) ):
        if bloque < 0:
            return False

        if s[i] == "(":
            bloque += 1
        elif s[i] == ")":
            bloque -= 1

    print("bloque:",bloque)
    if bloque == 0:
        return True
    else:
        return False




'''
Ejercicio 7
Se tiene una cadena de caracteres y se lo quiere reducir a su longitud más corta haciendo una serie de operaciones. En cada operación se selecciona un par de caracteres adyacentes que coinciden, y se borra. Por ejemplo, la cadena “aab” puede ser acortada a “b” en una sola operación. Implementar una función que borre tantos caracteres como sea posible y devuelva la cadena resultante.

def reduceLen(String):
	Descripción: Reduce la longitud de una cadena removiendo iterativamente pares de caracteres repetidos.
Entrada: Un String con la cadena a ser reducida.
Salida: Retorna un String con la cadena resultante tras haber aplicado las remociones. 

Ejemplo: “aaabccddd” se puede reducir a “abd”  de la siguiente manera: 
“aaabccddd” → “abccddd” → “abddd” → “abd”
'''

def reduceLen(s):
    L = LinkedList()
    for i in range( len(s) ):
        push( L,s[i] )


    for i in range( 1, length(L),+1 ):
        a = ""
        if access(L,i) == access(L,i-1):
            update( L,None,i )
            update( L,None,i-1 )


    for i in range( length(L) ):
        delete( L, None )


    resultado = ""
    for i in range( length(L) ):
        resultado += access(L,i)

    print( resultado )

'''
Ejercicio 8
Implementar una función que dadas dos palabras determine si la segunda está contenida dentro de la primera bajo la siguiente premisa. Una cadena s contiene la palabra “amarillo” si un subconjunto ordenado de sus caracteres deletrea la palabra amarillo. Por ejemplo, la cadena s = "aaafffmmmarillzzzllhooo" contiene amarillo, pero s = "aaafffmmmarrrilzzzhooo" no (debido a que le falta una l). Si ordenamos la primera cadena como s = "aaaaillllfffzzzhrmmmooo", ya no contiene la subsecuencia debido al ordenamiento.

def isContained(String,String):
	Descripción: Determina si los caracteres de una cadena se encuentran contenidos y en el mismo orden dentro de otra cadena.
Entrada: Un String con la cadena a evaluar, y otro String con la cadena posiblemente contenida en la primera.
Salida: Retorna un True si la segunda cadena se encuentra contenida en la primera, o False en caso contrario.
'''

def isContained(s1,s2):
    listaS1 = LinkedList()
    listaS2 = LinkedList()

    for i in range( len(s1) ):
        push( listaS1,s1[i] )

    for i in range( len(s2) ):
        push( listaS2,s2[i] )


    currentNode = listaS2.head
    for i in range( length(listaS2) ):
        a = currentNode.value 
        if search( listaS1, a ) != None :
            delete( listaS1, a )
        else:
            return False

        currentNode = currentNode.nextNode
    return True

'''
Ejercicio 9	
Suponga que se quiere encontrar si existe la ocurrencia exacta de una cadena p dentro de una cadena s. Suponga que se permite que el patrón  tenga caracteres comodín que pueden matchear con cualquier cadena de caracteres (incluso de longitud 0). Por ejemplo, el patrón “ab♢ba♢c” ocurre en el texto “cabccbacbacab” como sigue:


Note que el carácter comodín (♢) puede aparecer un número arbitrario de veces en el patrón p, pero se asume que no aparecerá en la cadena s. Proponga un algoritmo en tiempo polinomial para determinar si un patrón p aparece en un texto s dado.

def isPatternContained(String,String,c):
	Descripción: Determina en tiempo polinomial si un patrón de caracteres conformado por caracteres fijos y comodines se encuentra en otra cadena.
Entrada: Un String con la cadena a evaluar, un String con el patrón a buscar, y un carácter c que especifica el carácter comodín dentro del patrón.
Salida: Retorna un True si el patrón proporcionado se encuentra en la cadena, o False en caso contrario.
'''
def isPatternContained(s1,s2,c):
    # busco s1 en s2
    
    listaS1 = LinkedList()
    listaS2 = LinkedList()

    for i in range( len(s1) ):
        push( listaS1,s1[i] )

    for i in range( len(s2) ):
        push( listaS2,s2[i] )


    # caracteres comunes --> cc
    cc = 0
    currentNode = listaS1.head
    while currentNode != None:
        if currentNode.value != c:
            cc += 1
        currentNode = currentNode.nextNode

    print("cc:",cc )


    i = 0
    valoresEncontrados = 0
    currentNode = listaS2.head
    while currentNode != None:
        if valoresEncontrados == cc:
            return True

        if access(listaS1,i) == c:
            i += 1

        if currentNode.value == access(listaS1,i):
            i += 1
            valoresEncontrados += 1
        else:
            i = 0

        currentNode = currentNode.nextNode

    return False




'''
PARTE 2

Ejercicio 11
Sean el texto T y el patrón P de longitudes m y n respectivamente. Plantee un algoritmo para encontrar el mayor prefijo de P que se encuentra en T en O(n+m).

'''
def ejercicio11( T, P ):
    """
    busca el mayor prefijo de P en T
    """
    i = 0 
    maxPrefijo = ""
    prefijo = ""
    for j in range( len(T) ): 
        if T[ j ] == P[ i ]:
            prefijo += T[ j ]
            i += 1
        else:
            i = 0
            prefijo = ""

        if len( maxPrefijo ) < len( prefijo ):
            maxPrefijo = prefijo
            
        if i >= len( P ):
            break
    
    # print( "maxPrefijo:",maxPrefijo)
    return len(maxPrefijo)


'''
Ejercicio 12
Implementar en pseudo-python un autómata de estados finitos para buscar cualquier patrón P (consecutivo) en una cadena de texto T.
'''
def compute_transition_function(P,vocabulary):
  m = len(P) 
  delta = Array(m+1,Array(len(vocabulary),0)) 
  Pq = ""
  for q in range(0,m+1):
    

    for i in range(0,q):
      if i == 0:
        Pq = P[i]
      else:
        Pq = str(Pq)
        Pq += P[i]

    for j in range(0,len(vocabulary)):
      Pqa = str(Pq)            
      Pqa += vocabulary[j]

      r = False
      n = m
      k = 0
      if len(Pqa) > len(P):
        w = len(Pqa)-len(P)
      else:
        w = 0

      for x in range(0,len(Pqa)):
        v = w
        for y in range(0,n):

          if Pqa[w] != P[y]:
            k = 0
            w += 1
            break
          else:
            k += 1
            w += 1

          if w == len(Pqa) or k == len(P):
            r = True
            break
        w = v + 1
        if r == True:
          break
        n -= 1

      delta[q][j] = k

  return delta

def finite_automaton_matcher(T,P):
    m = len(P)
    L = LinkedList()
    vocabulary = ""
    for i in range( len(P) ):
        elemento = P[i]
        if search(L, elemento ) == None:
            push(L,elemento)
            vocabulary += elemento

    delta = compute_transition_function(P,vocabulary)
  
    n = len(T)
    q = 0
    for x in range(0,n):
        for y in range(0,len(vocabulary)):
            if T[x] == vocabulary[y]:
                letra = y
                break
        q = delta[q][letra]
        if q == m:
            print("El patrón ocurre en ", (x-m+1))
            return
    print("El patrón no ocurre en T")

  

finite_automaton_matcher("aaababaabaababaab","aabab")




'''
Ejercicio 13
Implemente el algoritmo de Rabin-Karp estudiado. Para el mismo deberá implementarse una función de hash que dado un patrón p de tamaño m se resuelva en O(1). Considerar lo detallando en las presentación del tema correspondiente a las funciones de hash en Rabin-karp. 
'''
def hash_rk(p):
  hp = 0
  for x in range(0,len(p)):
    hp += (128**x)*ord(p[len(p)-1-x])
  return hp

def Rabin_Karp(t,p):
    m=len(p)
    n=len(t)
    hp = hash_rk(p)
    for s in range(0,n-m):
        ts=substr(t,s,s+m)
        if hash_rk(ts)==hp:
            if strcmp(ts,p):
                print(p,"found at",s)
                return True
    return False


'''
Ejercicio 14
Implemente el algoritmo KMP estudiado. 	
def KMP(String,String):
	Descripción: Implementa el algoritmo KMP.
Entrada: Un String con la cadena a evaluar, y un String con el patrón a buscar.
Salida: Retorna un arreglo de índices con las posiciones en donde se encuentra el patrón, o None en caso de no encontrar el patrón.
'''
def compute_prefix_function(P):
  m = len(P)
  pi = Array(m,0)
  
  k = 0
  for q in range(0,m):
    value = False
    if q == 0:
      pi[q] = 0
    else:
      mayor = 0
      r = q
      for k in range(1,q):
        for i in range(0,k):
          if P[i] == P[r]:
            value = True
          else:
            value = False
            break
          r += 1
        r = q-k

        if value == True:
          if mayor == 0:
            mayor = k
          elif k > mayor:
            mayor = k
      pi[q] = mayor
  return pi

def KMP(T,P):
  n = len(T)
  m = len(P)
  pi = compute_prefix_function(P)
  print(pi)
  q = 0
  A = Array(n,0)
  r = False
  for i in range(0,n):
    while q > 0 and P[q] != T[i]:
      q = pi[q]
    
    if P[q] == T[i]:
      q = q + 1
    if q == m:
      r = True
      print("El patrón ocurre en ",i-m+1)
      A[i-m+1] = 1
      if P[0] == T[i]:
        q = 1
      else:
        q = 0
  print("")
  if r == True:
    return A
  else:
    return None
'''
Ejercicio 15
Realice una modificación al algoritmo KMP para encontrar las ocurrencias no solapadas del patrón P en el texto T. Por ejemplo: si P = aba y T = aabababaaa las ocurrencias de P aabababaaa y aabababaaa se solapan por lo que la mayor cantidad de ocurrencias no solapadas son 2, o sea aabababaaa.
def KMPmod(String,String):
	Descripción: Implementa el algoritmo KMP sin solapado.
Entrada: Un String con la cadena a evaluar, y un String con el patrón a buscar.
Salida: Retorna un arreglo de índices con las posiciones en donde se encuentra el patrón sin solapado, o None en caso de no encontrar el patrón.
'''
def KMPmod(T,P):
  n = len(T)
  m = len(P)
  pi = compute_prefix_function(P)
  print(pi)
  q = 0
  A = Array(n,0)
  r = False
  for i in range(0,n):
    while q > 0 and P[q] != T[i]:
      q = pi[q]
    
    if P[q] == T[i]:
      q = q + 1
    if q == m:
      r = True
      print("El patrón ocurre en ",i-m+1)
      A[i-m+1] = 1
      q = 0
  print("")
  if r == True:
    return A
  else:
    return None