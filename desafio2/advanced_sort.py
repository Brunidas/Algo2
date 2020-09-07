# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401

from algo1 import*
from linkedlist import*

# advanced_sort.py
#····················································
def particion(arr,primero,ultimo): 
    i = ( primero-1 )       #  sera la referencia para el mayor
    pivot = arr[ultimo]     # toma como pivote al ultimo elemeto
    for j in range(primero , ultimo): 
  
        #si el elemento es mas chico que el pivote
        if   arr[j] < pivot: 
            
            i = i+1 
            valorI = arr[i]   # intercanbia valores
            valorJ = arr[j]
            arr[i] = valorJ 
            arr[j] = valorI
 
    valorII = arr[i+1]       # intercanbia valores      
    valorU = arr[ultimo]
    arr[i+1] = valorU 
    arr[ultimo] = valorII

    return ( i+1 ) 
  
def quicksortRecursivo(arr,primero,ultimo): 
    if primero < ultimo: 

        indexPivote = particion(arr,primero,ultimo) 

        #lista izquierda
        quicksortRecursivo(arr, primero, indexPivote-1)

        #lista derecha
        quicksortRecursivo(arr, indexPivote+1, ultimo) 

def quicksort(L):
    arr = Array(length(L),0)     #se usa un vector para trabajar
    for i in range ( len(arr) ):
        arr[i] = access(L,i)

    # llama a la fucion que ordena
    quicksortRecursivo(arr,0, len(arr)-1 ) 

    # actualiza los valores de la lista
    for i in range ( len(arr) ):
        update(L, arr[i], i)
#····················································
def mergesortResursivo(arr): 
    if len(arr) >1: 

        mid = len(arr)//2 #Encuenta el medio del array

        tamL = mid           # tamaños del los arrays...
        tamR = len(arr)-mid  # L y R

        L = Array(tamL,0)   #defino los arrays
        R = Array(tamR,0)

        cont = 0
        for i in range(0,mid):   # completo los arrays
            L[cont] = arr[i]
            cont += 1 
        cont = 0
        for j in range(mid, len(arr) ):
            R[cont] = arr[j]
            cont += 1 


        mergesortResursivo(L) # Lado izquierdo 
        mergesortResursivo(R) # Lado derecho
  
        i = j = k = 0
          
        # Copio los datos de L y R en arr
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          

        while i < len(L):   # Chequa los elemetos...
            arr[k] = L[i]   # de L
            i+=1
            k+=1
          
        while j < len(R):   # Chequa los elemetos...
            arr[k] = R[j]   # de R
            j+=1
            k+=1
  
def mergesort(L):
    arr = Array(length(L),0)     #se usa un vector para trabajar
    for i in range ( len(arr) ):
        arr[i] = access(L,i)

    mergesortResursivo(arr)

    # actualiza los valores de la lista
    for i in range ( len(arr) ):
        update(L, arr[i], i)


# URL: https://repl.it/@BrunoFuentes/ordenamientos-avanzados