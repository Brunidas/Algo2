# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp8

from algo1 import *
from linkedlist import *
from advanced_sort import *
from queue import *
from math import *

# PARTE 1: Backtracking
'''
Ejercicio 1
Implementar la función Dar Cambio que devuelve la cantidad mínima de monedas que hay que dar para cambiar n pesos con monedas de la denominación dada como parámetro.

def darCambio(Cambio, Monedas) 
Descripción: Implementa la operación devolver cambio
Entrada: Cambio número que representa el monto del cambio, Monedas, un Array con las monedas que se dispone para dar ese cambio.
Salida: retorna el número mínimo de monedas que son utilizadas para devolver el cambio.

Nota: Asuma que en la lista de monedas siempre está la moneda con valor 1. Y que las monedas no se agotan.
Ejemplos: 
monedas = [1, 2, 6, 8, 10],  cambio = 14,  solución: 2 (una moneda con denominación 6 y otra con 8) 
monedas = [1, 3, 11, 7, 12],  cambio = 20,  solución: 3 (utilizando la combinación de monedas 12,7,1)
'''


def darCambioV2(cambio, monedas, cont, suma, minimo):
    for i in range(len(monedas)):
        cont += 1
        suma += monedas[i]

        if suma == cambio:
            if minimo > cont:
                minimo = cont
        elif suma > cambio:
            suma -= monedas[i]
            cont -= 1
        elif suma < cambio:
            minimo = darCambioV2(cambio, monedas, cont, suma, minimo)
            cont -= 1
            suma -= monedas[i]

    return minimo


def darCambio(cambio, monedas):
    minimo = darCambioV2(cambio, monedas, 0, 0, 9999999)
    return minimo


"""
Ejercicio 2
Se dispone de una mochila que acepta un peso máximo PesoMax, y de k latas de peso P1, P2, P3, …, Pk, todos diferentes. Se desea llevar la mayor cantidad de peso posible en la mochila. Implemente un método que decida que latas deben echarse con este fin.

def mochila(PesoMax, latas): 
Descripción: Implementa la función mochila 
Entrada: PesoMax número que representa el peso máximo que acepta la mochila, latas Array con el peso de las latas p1, p2, p3, …, p length_array.
Salida: retorna un array con las latas que maximizan el peso de la mochila.
"""


def sacarUltimo(cadena, d):
    newCadena = ""
    for i in range(len(cadena) - d):
        newCadena += cadena[i]
    return newCadena


def mochilaV2(PesoMax, latas, cont, suma, minimo, stringLatas, L, S):
    for i in range(len(latas)):
        cont += 1
        suma += latas[i]
        cantDigitos = len(str(latas[i]))

        stringLatas += str(latas[i])
        # print(stringLatas)

        if suma == PesoMax:
            if minimo > cont:
                minimo = cont
                add(L, stringLatas)

            stringLatas = sacarUltimo(stringLatas, cantDigitos)

        elif suma > PesoMax:
            suma -= latas[i]
            cont -= 1
            stringLatas = sacarUltimo(stringLatas, cantDigitos)

        elif suma < PesoMax:
            add(S, stringLatas)
            minimo, stringLatas = mochilaV2(PesoMax, latas, cont, suma, minimo,
                                            stringLatas, L, S)
            cont -= 1
            suma -= latas[i]
            stringLatas = sacarUltimo(stringLatas, cantDigitos)

    return minimo, stringLatas


def mochila(PesoMax, latas):
    L = LinkedList()
    S = LinkedList()
    minimo, stringLatas = mochilaV2(PesoMax, latas, 0, 0, 99999, "", L, S)

    # printLinkedList(L)
    # printLinkedList(S)

    # obtiene el valor que creara el nuevo array
    if L.head != None:
        datosArray = L.head.value
        tamMenor = len(L.head.value)
        currentNode = L.head
        while currentNode != None:
            if tamMenor > len(currentNode.value):
                datosArray = currentNode.value
            currentNode = currentNode.nextNode

        arr = Array(len(datosArray), 0)
        for i in range(len(datosArray)):
            arr[i] = int(datosArray[i])

        # print(arr)
        return arr

    else:
        # obtengo los datos para comparar
        datosArray = S.head.value
        sumaDatosArray = 0
        for i in range(len(S.head.value)):
            sumaDatosArray += int(datosArray[i])

        tamMenor = len(S.head.value)
        currentNode = S.head
        while currentNode != None:
            suma = 0
            for i in range(len(currentNode.value)):
                suma += int(currentNode.value[i])
            if suma > sumaDatosArray:
                sumaDatosArray = suma
                datosArray = currentNode.value
            currentNode = currentNode.nextNode

        # sumaDatosArray -> valor de la suma de los pesos
        # datosArray -> tengo los pesos

        arr = Array(len(datosArray), 0)
        for i in range(len(datosArray)):
            arr[i] = int(datosArray[i])

        return arr


"""
Ejercicio 3
Implementar la función SubsecuenciaCreciente que devuelva un array con la mayor cantidad de elementos del array de entrada que formen una secuencia monótona creciente. Los elementos en el resultado deben aparecer en el mismo orden en que aparecían en el array de entrada, y no tienen que ser consecutivos dentro de este. Por ejemplo, la mayor subsecuencia creciente en [ 5, 1, 2, 3, 100, 20, 17, 8, 19, 21 ] es [1, 2,3 , 8, 19, 21 ]. 

def subsecuenciaCreciente(numeros): 
Descripción: Implementa la función SubsecuenciaCreciente 
Entrada: numeros array de números naturales.
Salida: retorna array de números con la mayor subsecuencia creciente en el array de entrada numero.

Nota: puede haber más de una respuesta, el ejercicio solo exige que usted devuelva una de ellas.
"""


def convertirListaArray(lista):
    arr = Array(length(lista), 0)
    cn = lista.head
    for i in range(length(lista)):
        arr[i] = cn.value
        cn = cn.nextNode
    return arr


def subsecuenciaCrecienteV2(numeros, valorActual, i, L, R):
    push(L, valorActual)
    # printLinkedList(L)

    if length(L) > len(R):
        R = convertirListaArray(L)
        # print(R)

    for j in range(i, len(numeros)):
        # print(numeros[j]," : ",valorActual)
        if numeros[j] > valorActual:
            R = subsecuenciaCrecienteV2(numeros, numeros[j], j, L, R)
            pop(L)

    return R


def subsecuenciaCreciente(numeros):
    R = Array(0, 0)
    for i in range(len(numeros)):
        L = LinkedList()
        R = subsecuenciaCrecienteV2(
            numeros,
            numeros[i],
            i,
            L,
            R,
        )
    print(R)


'''
Ejercicio 4
Dado un array X de números enteros positivos y un número entero de T, implementar un algoritmo que  devuelva si existe un subconjunto de elementos en X que suman el valor T. Por ejemplo si X = {8, 6, 7, 5, 3, 10, 9} y T = 15, la respuesta es True, porque los subconjuntos {8, 7} , {7, 5, 3} , {6, 9} , {5, 10} todos suman 15. Con este otro ejemplo X = {11, 6, 5, 1, 7, 13, 12} y T = 15, la respuesta es False.

def subconjuntoSuma(numeros, valor): 
Descripción: Implementa la función Subconjunto Suma 
Entrada: numeros array de enteros positivos, valor entero positivo.
Salida: retorna True si existe un grupo de enteros en números cuya suma del valor de entrada.'''


def subconjuntoSumaV2(numeros, valor, valorActual, i, suma, R):

    for j in range(i, len(numeros)):
        suma += valorActual

        if suma == valor:
            R = True
        elif suma < valor:
            R = subconjuntoSumaV2(numeros, valor, valorActual, i, suma, R)

    return R


def subconjuntoSuma(numeros, valor):
    R = False
    for i in range(len(numeros)):
        R = subconjuntoSumaV2(
            numeros,
            valor,
            numeros[i],
            i,
            0,
            R,
        )

    return R


# Parte 2: Greedy
'''Ejercicio 5
N actividades requieren el uso exclusivo de un recurso común. Cada actividad dispone de un tiempo de inicio y fin. Seleccionar el mayor conjunto posible de actividades que no se superpongan.
def adminActividades(tareas, inicio, fin): 
Descripción: Implementa la función Administrar tareas 
Entrada: tareas array con las tareas donde cada tarea dispone de un tiempo de inicio t0 y un tiempo final tf, inicio entero positivo que representa desde cuando esta disponible el recurso común, fin entero positivo que representa hasta cuando esta disponible el recurso común. Toda tarea esta dentro de ese tiempo.
Salida: retorna el listado de tareas que maximiza el uso del espacio en común sin que se solapen ninguna de estas.'''


def adminActividades(tareas, inicio, fin):
    L = LinkedList()

    while inicio < fin:
        # print("w:",inicio)
        cambio = False
        currentT = tareas.head
        for i in range(length(tareas)):
            # print("f:",inicio)
            if inicio == currentT.value[0]:
                push(L, currentT.value)
                # print(currentT.value)
                inicio = currentT.value[1]
                cambio = True
                break
            currentT = currentT.nextNode
        if cambio == True:
            continue

        inicio += 1

    return L


"""
Ejercicio 6
Se tienen n números naturales distintos, siendo n una cantidad par, que tienen que juntarse formando parejas de dos números cada una. A continuación, de cada pareja se obtiene la suma de sus dos componentes, y de todos estos resultados se toma el máximo. Diseñar un algoritmo greedy que cree las parejas de manera que el valor máximo de las sumas de los números de cada pareja sea lo más pequeño posible. Ejemplo: suponiendo que los datos se encuentran en el siguiente vector[5,8,1,4,7,9]

vamos a ver un par de formas de resolver el problema (no necesariamente la óptima):
Seleccionamos como pareja los elementos consecutivos. De esta forma conseguimos las parejas (5, 8), (1, 4) y (7, 9); entonces, al sumar las componentes tenemos los valores 15, 5 y 16, por lo que el resultado final es 16.  
Seleccionamos como pareja los elementos opuestos en el vector Ahora tenemos las parejas (5, 9), (8, 7) y (1, 4); sumando conseguimos 14, 15 y 5, por lo que el resultado final es 15 (mejor que antes).

¿Habrá una resultado mejor para este ejemplo?
def buscaPares(vector): 
Descripción: Implementa la función busca pares 
Entrada: vector de tamaño par que contiene números enteros positivos.
Salida: retorna el valor mínimo de sumar los posibles pares que se pueden formar del vector (justo como se explica en la especificación anterior).
"""


def buscaPares(vector):
    L = LinkedList()
    for i in range(len(vector)):
        push(L, vector[i])

    mergesort(L)

    currentNode = L.head
    for i in range(len(vector)):
        vector[i] = currentNode.value
        currentNode = currentNode.nextNode

    min = 99999999999
    cont = len(vector) - 1
    for i in range(int(len(vector) / 2)):
        print(vector[cont])
        print(vector[i])
        print()

        if vector[cont] + vector[i] < min:
            min = vector[cont] + vector[i]

        cont -= 1

    return min


'''
Ejercicio 7
Se dispone de una mochila que acepta un peso máximo PesoMax, y de k latas de peso P1, P2, P3, …, Pk, todos diferentes. Cada lata dispone de un beneficio B1, B2, B3, …, Bk. Se desea llevar la mayor cantidad de beneficio posible en la mochila sin sobrepasar el peso. Implemente un método que decida que latas deben echarse con este fin.

def mochila(PesoMax, latas): 
Descripción: Implementa la función mochila 
Entrada: PesoMax número que representa el peso máximo que acepta la mochila, latas Array con el peso de las latas p1, p2, p3, …, plength_array.
Salida: retorna un array con las latas que maximizan el beneficio de la mochila.
NOTA: Parecido al ejercicio 2 solo notar que en este caso se le agrega un beneficio a cada lata y lo que se quiere es maximizar el beneficio en total sin sobrepasar el peso de la mochila
'''


def mochilaEj7V2(PesoMax, latas, suma, beneficio, stringLatas):
    # encontrar la lata con el mayor benefio sin sobrepasarse del peso max

    for i in range(len(latas)):

        suma += latas[i][0]

        if latas[i][1] > beneficio and suma < PesoMax:
            beneficio = latas[i][1]

        suma -= latas[i][0]

    # print("beneficio:" ,beneficio)
    # print("suma:",suma)

    for i in range(len(latas)):
        if latas[i][1] == beneficio:
            suma += latas[i][0]
            stringLatas += str(latas[i][0])
            beneficio = 0
            suma, stringLatas, beneficio = mochilaEj7V2(
                PesoMax, latas, suma, beneficio, stringLatas)

    return suma, stringLatas, beneficio


def mochilaEj7(PesoMax, latas):
    a, b, c = mochilaEj7V2(PesoMax, latas, 0, 0, "")

    # conveir el string en un Array, stringLatas -> b
    arr = Array(len(b), 0)
    for i in range(len(b)):
        arr[i] = int(b[i])

    return arr


# Parte 3: Divide y Vencerás
'''Ejercicio 8
Búsqueda de un elemento X en una lista ordenada utilizando la técnica de divide y vencerás.
def busquedaBinaria(lista, x): 
Descripción: Implementa la función búsqueda binaria 
Entrada: lista de números ordenados de con monotonía creciente, x número.
Salida: True si X se encuentra en la lista, False en caso contrario.'''


def busquedaBinariaV2(lista, x, inicio, fin, pivote, r):
    if inicio == pivote or fin == pivote:
        if lista[pivote] == x:
            r = True
        else:
            r = False

    else:
        if x > lista[pivote]:
            newPivote = floor((fin - (pivote + 1)) / 2) + (pivote + 1)
            r = busquedaBinariaV2(lista, x, pivote + 1, fin, newPivote, r)
        else:
            newPivote = floor((pivote - inicio) / 2) + inicio
            r = busquedaBinariaV2(lista, x, inicio, pivote, newPivote, r)

    return r


def busquedaBinaria(lista, x):
    inicio = 0
    fin = len(lista) - 1
    pivote = floor(len(lista) / 2)
    return busquedaBinariaV2(lista, x, inicio, fin, pivote, False)


'''
Ejercicio 9

Búsqueda del k-ésimo menor elemento de una lista.
def busquedaKesimo(lista, k):
Descripción: Implementa la función búsqueda del k-ésimo elemento 
Entrada: lista de números, k número que representa el k-ésimo elemento en la lista si se ordena de menor a mayor.
Salida: Valor numérico que representa el k-ésimo menor elemento en la lista.
'''


def menoresMayores(lista, inicio, fin, pivote):
    L = LinkedList()
    push(L, lista[pivote])
    lista[pivote] = None

    cont = 0
    for i in range(inicio, fin + 1):

        if lista[i] != None:

            if lista[i] < access(L, cont):
                insert(L, lista[i], cont)
                cont += 1
            else:
                insert(L, lista[i], cont + 1)

    j = 0
    for i in range(inicio, fin + 1):
        lista[i] = access(L, j)
        j += 1

    return cont, lista


def busquedaKesimoV2(lista, k, inicio, fin, pivote, r):

    if inicio == pivote or fin == pivote:
        r = lista[pivote]

    else:
        indexPivote, lista = menoresMayores(lista, inicio, fin, pivote)
        if indexPivote < k:

            newPivote = floor(
                (fin - (indexPivote + 1)) / 2) + (indexPivote + 1)
            r = busquedaKesimoV2(lista, k, indexPivote + 1, fin, newPivote, r)
        else:
            newPivote = floor((indexPivote - inicio) / 2) + inicio
            r = busquedaKesimoV2(lista, k, inicio, indexPivote, newPivote, r)

    return r


def busquedaKesimo(lista, k):
    inicio = 0
    fin = len(lista) - 1
    pivote = floor(len(lista) / 2)
    r = busquedaKesimoV2(lista, k, inicio, fin, pivote, 0)
    # print(r)


'''
Ejercicio 10
Implementar la función SubsecuenciaCreciente que devuelva un array con la mayor cantidad de elementos del array de entrada que formen una secuencia monótona creciente. Los elementos en el resultado deben aparecer en el mismo orden en que aparecían en el array de entrada, y no tienen que ser consecutivos dentro de este. Por ejemplo, la mayor subsecuencia creciente en [ 5, 1, 2, 3, 100, 20, 17, 8, 19, 21 ] es [1, 2,3 , 8, 19, 21 ]. 

def subsecuenciaCreciente(numeros): 
Descripción: Implementa la función SubsecuenciaCreciente 
Entrada: numeros array de números naturales.
Salida: retorna array de números con la mayor subsecuencia creciente en el array de entrada números.

Nota: este ejercicio ya lo tuvieron que realizar con una estrategia Backtracking, ahora es necesario usar la estrategia Divide y Vencerás para encontrar la solución.
'''


def divideSubs(vector, inicio, fin, L):
    if inicio < fin:
        pivote = int((inicio + (fin - 1)) / 2)

        divideSubs(vector, inicio, pivote, L)
        divideSubs(vector, pivote + 1, fin, L)
    elif (inicio == fin):

        unir(vector, inicio, fin, L)
    return vector


def unir(vector, inicio, fin, L):

    if length(L) == 0 or vector[fin] > access(L, length(L) - 1):
        insert(L, vector[fin], length(L))

    elif vector[fin] < access(L, length(L) - 1):
        if fin != len(vector) - 1:
            for x in range(0, length(L)):
                if vector[fin] < access(L, x):
                    break
            delete(L, access(L, x))
            insert(L, vector[fin], x)


def subsecuenciaCrecienteEj10(numeros):
    L = LinkedList()
    divide_subs(numeros, 0, len(numeros) - 1, L)

    r = Array(length(L), 0)
    for i in range(len(r)):
        r[i] = access(L, i)

    return r
    # print(r)
    # printLinkedList(L)


'''
Ejercicio 11
Dos cadenas se dicen que distan en uno si para obtener una de otra hay que insertar, cambiar o quitar un solo carácter. La distancia entre dos cadenas es la menor cantidad de transformaciones que hay que realizar para obtener una a partir de la otra.

def distancia(string1, string2): 
Descripción: Implementa una función dadas dos cadenas, determinar la distancia entre ellas. 
Entrada: string1 y string2 cadenas de texto.
Salida: entero que representa la distancia entre las cadenas string1 y string2.
'''


def distanciaDiv(string1, string2, distancia, inicio, fin):

    if inicio < fin:
        pivote = int((inicio + fin) / 2)

        distancia = distanciaDiv(string1, string2, distancia, inicio, pivote)

        distancia = distanciaDiv(string1, string2, distancia, pivote + 1, fin)

    elif inicio == fin:
        if string1[inicio] != string2[inicio]:
            distancia += 1

    return distancia


def distancia(string1, string2):

    if len(string1) < len(string2):
        distancia = len(string2) - len(string1)
        string2 = substr(string2, 0, len(string1))

    elif len(string1) > len(string2):
        distancia = len(string1) - len(string2)
        string1 = substr(string1, 0, len(string2))

    return distancia_div(string1, string2, distancia, 0, len(string1) - 1)


# Parte 4 Programación Dinámica
'''Ejercicio 12
Implementar la función Dar Cambio que devuelve la cantidad mínima de monedas que hay que dar para cambiar n pesos con monedas de la denominación dada como parámetro.

def darCambio(Cambio, Monedas) 
Descripción: Implementa la operación devolver cambio
Entrada: Cambio número que representa el monto del cambio, Monedas, un Array con las monedas que se dispone para dar ese cambio.
Salida: retorna el número mínimo de monedas que son utilizadas para devolver el cambio.

Nota: Asuma que en la lista de monedas siempre está la moneda con valor 1. Y que las monedas no se agotan. Es el mismo ejercicio de la Parte 1 pero esta vez hay solucionarlo utilizando la estrategia de Programación Dinámica.'''


def darCambioEj12(cambio, Monedas):
    D = Array(len(Monedas), Array(cambio + 1, 0))

    for i in range(0, len(Monedas)):
        for j in range(0, cambio + 1):
            D[i][j] = darCambioEj12V2(D, i, j,
                                      Monedas)  #j seria el cambio, i la moneda

    return D[len(Monedas) - 1][cambio]


def darCambioEj12V2(D, i, j, Monedas):
    if j < Monedas[i]:
        if i == 0:
            return 0
        else:
            return D[i - 1][j]
    elif j == Monedas[i]:
        return 1
    else:
        if i == 0:
            return j * Monedas[i]
        elif j % Monedas[i] == 0:
            return int(j / Monedas[i])
        else:

            if D[i - 1][j] < (D[i][j - Monedas[i]] + 1):
                return D[i - 1][j]

            else:
                return (D[i][j - Monedas[i]] + 1)


'''
Ejercicio 13
Una variante del problema de la mochila es la siguiente. Tenemos un conjunto de enteros (positivos) A = {a1, a2, ..., an} y un entero K. El objetivo es encontrar si existe algún subconjunto de A cuya suma sea exactamente K. Implementar un algoritmo que resuelva este problema utilizando la estrategia de programación dinámica.
'''


def K(D, i, j, A):
    if j < A[i]:
        if i == 0:
            return 0
        else:
            return D[i - 1][j]
    elif j == A[i]:
        return 1
    else:
        if i == 0:
            return j * A[i]
        elif j % A[i] == 0:
            return int(j / A[i])
        else:

            if D[i - 1][j] < (D[i][j - A[i]] + 1):
                return D[i - 1][j]

            else:
                return (D[i][j - A[i]] + 1)


def sumaSubconj(A, k):
    D = Array(len(A), Array(k + 1, 0))

    for i in range(0, len(A)):
        for j in range(0, k + 1):
            D[i][j] = K(D, i, j, A)

    if D[len(A) - 1][k] != 0:
        return True
    else:
        return False


'''
Ejercicio 14
Dada una tabla de tamaño nxn de números naturales, se pretende resolver el problema de obtener el camino de la casilla (1, 1) a la casilla (n, n) que minimice la suma de los valores de las casillas por las que pasa. En cada casilla (i, j) habrá sólo dos posibles movimientos: ir hacia abajo (i+1, j), o hacia la derecha (i, j+1). Implementar un algoritmo que resuelva este problema utilizando la estrategia de programación dinámica.
'''


def calcular(A, B, x, y):
    if x == 0 and y == 0:
        return A[0][0]
    else:
        if y == 0:
            return (B[x - 1][y] + A[x][y])
        elif x == 0:
            return (B[x][y - 1] + A[x][y])
        else:
            if B[x][y - 1] < B[x - 1][y]:
                return (B[x][y - 1] + A[x][y])
            else:
                return (B[x - 1][y] + A[x][y])


def minSum(A):
    B = Array(len(A), Array(len(A), 0))
    for x in range(0, len(A)):
        for y in range(0, len(A)):
            B[x][y] = calcular(A, B, x, y)

    return B[len(A) - 1][len(A) - 1]


'''
Ejercicio 15
Problema de la Secuencia Común más Larga (LCS). Dadas dos secuencias v = v1 v2…vm y w = w1 w2…wn la LCS de v y w es una secuencia de posiciones en v: 1 < i1 < i2 < … < it < m y otra secuencia de posiciones en w: 1 < j1 < j2 < … < jt < n tal que la it-sima letra de v es igual a la jt-sima letra de w y t es máximo. Implemente un algoritmo que encuentre la LCS más larga dada dos secuencias de entradas.
'''


def chequearAnt(A, v, w, x, y, secuencia):
    if x >= 0 and y >= 0:
        if v[y - 1] == w[x - 1]:
            secuencia[x - 1] = w[x - 1]
            secuencia[x] = w[x]
            chequearAnt(A, v, w, x - 1, y - 1, secuencia)


def encontrar(A, v, w, x, y, secuencia):
    if (x == 0 or y == 0):
        if v[y] == w[x]:
            secuencia[x] = w[x]
            return 0
        else:
            return -1
    else:
        if v[y] == w[x]:
            if v[y - 1] == w[x - 1]:
                secuencia[x - 1] = w[x - 1]
                secuencia[x] = w[x]
                chequearAnt(A, v, w, x - 1, y - 1, secuencia)
                return A[x - 1][y - 1] + 1
            else:
                if x == len(w) - 1:
                    if A[x][y - 1] > A[x - 1][y]:
                        if secuencia[x - 1] == v[y - 1]:
                            secuencia[x] = w[x]
                        return A[x][y - 1]
                    else:
                        if secuencia[x - 1] == v[y - 1]:
                            secuencia[x] = w[x]
                        return A[x - 1][y]
                else:
                    if secuencia[x - 1] != v[y - 1]:
                        for i in range(0, x):
                            secuencia[i] = ''
                    secuencia[x] = w[x]

                    return 0
        else:
            if A[x][y - 1] > A[x - 1][y]:
                return A[x][y - 1]
            else:
                return A[x - 1][y]


def LCS(v, w):
    A = Array(len(w), Array(len(v), 0))

    secuencia = Array(len(w), '')
    for x in range(0, len(w)):
        for y in range(0, len(v)):
            A[x][y] = encontrar(A, v, w, x, y, secuencia)

    sec = ''
    for x in range(0, len(w)):
        if secuencia[x] != None and secuencia[x] != '':
            sec += secuencia[x]

    return sec
