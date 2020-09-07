# FUENTES, Bruno
# 12401


from algo1 import *

'''
search(Array,element)
    Descripción: Busca un elemento en el Array que representa el TAD secuencia, 
Entrada: el  Arreglo sobre el cual se quiere realizar la búsqueda (Array) y el  elemento (element) a buscar.
Salida:  EL índice donde se encuentra el elemento. Devuelve None si no se encuentra dentro del array. 
'''

def search(vector, element):
    for i in range( len(vector) ):
        if ( element==vector[i] ):
            retorno = i
            break
        else: 
            retorno = None
    return retorno


'''
insert(Array,element,position)
Descripción:Inserta un elemento en una posición determinada de un Array que representa el TAD secuencia. 
Poscondición: Se desplazan todos los demás elementos hacia el final. El elemento en la última posición del Array se pierde. 
Entrada: el arreglo (Array) sobre el cual se va a hacer la inserción, el elemento (element) y la posición (position) donde se quiere insertar.
Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve None. Devuelve None si la posición a insertar es mayor que el número de elementos en el array.
'''

def insert(vector,element,position):
    if ( position < len(vector) ):
        newVector = Array(len(vector), 0 )

        #rellena los elemento anteriores a el lugar a insertar
        cont=0
        while(True):
            if ( cont==position ):
                break
            else:
                newVector[cont] = vector[cont]
                cont += 1

        #inserta el "elemento"    
        newVector[position] = element
        
        #agrega los elementos despues del "posicion"
        cont=position
        for i in range(position+1, len(vector) ):
            newVector[i] = vector[cont]
            cont += 1

        vector = newVector
        print('')
        print(str(vector)+'\n vector resultado' )
        print('')

        return position
    else:
        return None


'''
delete(Array,element)
Descripción: Elimina un elemento del arreglo que representa el TAD secuencia.
Poscondición: Se desplazan los elementos restantes y se rellena con  None hacia el final. 
Entrada: el  arreglo sobre el cual se quiere realizar la eliminación (Array) y el elemento (element) a eliminar.
Salida: Devuelve None si el elemento no se encuentra.
'''
def delete(vector,element):
    #guardo la posicion del elemento a eliminar
    position = search(vector,element) 
    
    if (position == None): 
        return None
    else:
        newVector = Array(len(vector), 0 )

        #rellena los elemento anteriores a el lugar a elimininacion
        cont=0
        while(True):
            if ( cont==position ):
                break
            else:
                newVector[cont] = vector[cont]
                cont += 1
 

        #agregar los elementos que le siguen al elemento eliminado
        cont = position
        for i in range(position+1,len(newVector) ):
            newVector[cont] = vector[i]
            cont += 1 
        
        vector = newVector
        print('')
        print(str(vector)+'\n vector resultado' )
        print('')

        return position



'''
length(Array)
    Descripción: Calcula el número de elementos activos que hay en la secuencia
Entrada: El arreglo sobre el cual se quiere calcular el número de elementos
Salida: El número de elementos distintos a None
'''
def length(vector):
    cont=0
    for i in range( len(vector) ):
        if( vector[i]!=None ):
            cont+=1
    return cont


#URL:
# https://repl.it/@BrunoFuentes/array-py      