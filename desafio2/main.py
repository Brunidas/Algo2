# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/desafio2

'''
El enfoque tomado para este desafio es el de recorer la matriz ingresada de desde el ultimo elemento hasta el primer revisando si ese elememto es uno o no. En caso de ser uno verfica si toda la matriz es de solo unos , en cambio si tiene un cero envia esa matriz a la funcion cambiar valores 
'''

from algo1 import*
from binarytree import*
from print_tree import*
from avltree import*
from priorityqueue import*
from advanced_sort import*
from math import *
from random import  *
'''
Desafío 2:
Considere una matriz de tamaño N*M conformada únicamente por 1 s o 0s. Las filas se
numeran de 1 a N, mientras que las columnas se numeran de 1 a M. Al arrancar la matriz se
llena aleatoriamente, por ejemplo:
0 1 0 1 1 0
0 0 1 1 0 1
1 0 1 0 0 0
1 1 1 0 1 1
0 0 0 1 0 1
El objetivo es lograr que la matriz llegue a un estado en donde todos sus números sean
1 s, pero realizando T operaciones que se conforman de los siguientes pasos:
- Se seleccionarán dos enteros x e y para indicar una posición en la matriz, por lo que
estos números estarán comprendidos en los rangos 1 ≤ x ≤ N y 1 ≤ y ≤ M.
- Dichos números denotarán una submatriz que irá desde el elemento (1 , 1 ) al (x, y).
Siguiendo el ejemplo anterior, si x = 2 e y = 4, entonces la submatriz será:
0 1 0 1
0 0 1 1
- Una vez seleccionada la submatriz, todos los elementos comprendidos por la misma
cambiarán, por lo que los 1 s se volverán 0s, y los 0s se volverán 1 s. Por ejemplo la
submatriz seleccionada anteriormente quedará como:
1 0 1 0
1 1 0 0
y como resultado de la operación la matriz completa se verá modificada:
1 0 1 0 1 0
1 1 0 0 0 1
1 0 1 0 0 0
1 1 1 0 1 1
0 0 0 1 0 1
Usted deberá implementar una función que dada una matriz N*M, devuelva el número mínimo
de operaciones necesarias para lograr que la matriz se encuentre completamente llena de 1 s.
Ejemplo:
Con Z=0 0 0 1 1
0 0 0 1 1
0 0 0 1 1
1 1 1 1 1
1 1 1 1 1
Al ejecutar transformaMatriz(Z) la función devolverá 1 , ya que con una sola operación donde
x = 3 e y = 3 la matriz queda completa de 1 s.
'''

def printMatrix(matrix):
    for i in range( len(matrix) ):
        print(matrix[i])

def valoresMatriz( matrix, M, N ):
    for i in range( M ):
        for j in range ( N ):
            matrix[i][j] = randint(0,1)
    return

def cambiarValores( matrix, M, N ):
    for i in range( M ):
        for j in range ( N ):
            if matrix[i][j] == 1 :
                matrix[i][j] = 0
            else: 
                matrix[i][j] = 1
    return

def matrizSoloUnos( matrix ):
    M = len( matrix )
    N = len( matrix[0] )
    cantElem = N * M
    cont = 0

    for i in range( M ):
        for j in range ( N ):
            if matrix[i][j] == 1:
                cont += 1

    if cont == cantElem:
        return True
    else:
        return False


def transformaMatriz( matrix ):
    M = len( matrix )
    N = len( matrix[0] )
    pasos = 0

    # print("M: ",M)
    # print("N: ",N)

    # for i in range( 0, M, +1 ):
    #     for j in range ( 0, N, +1 ):
    #         print( "("+str(i)+","+str(j)+")" )

    # print("- - - - - - -")


    for i in range( M-1, -1, -1 ):
        for j in range ( N-1, -1, -1 ):

            if matrix[i][j] == 0:
                pasos += 1
                cambiarValores( matrix, i+1, j+1 )

            if ( matrizSoloUnos( matrix ) ):
                return pasos


dimMatrizM = 3
dimMatrizN = 2
matriz = Array(dimMatrizM, Array(dimMatrizN, 0) )
valoresMatriz(matriz, dimMatrizM, dimMatrizN )
printMatrix( matriz ) 
print('- - - - - - - ')
pasos = transformaMatriz( matriz )
printMatrix( matriz ) 
print("pasos ",pasos)