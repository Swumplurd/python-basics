# LISTAS

''' Las listas en python son similares a lo que conocemos como arreglos en otros lenguajes de programacion
    Para declarar una lista en python lo hacemos de la siguiente manera:'''

#Listas pueden ser de un mismo tipo de dato
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Tambien pueden ser de diferentes tipos de dato
datos = ['Hola', 55, 'mundo', 3.14, 'desde', 777, 'python']

#Podemos acceder a los elementos de una lista por medio de su indice tal cual lo haciamos con las cadenas
print(datos[0])         #Muestra 'Hola'
print(numeros[-1])      #Muestra 9

#Podemos hacer slicing al igual que lo haciamos con las cadenas
print(datos[:3])        #Muestra ['Hola', 55, 'mundo']
print(numeros[-3:])     #Muestra [7, 8, 9]

#Podemos concatenar una lista a una lista ya existente
numeros = numeros + [0]
print(numeros)          #Muestra [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#A diferencia de las cadenas, las listas no son inmutables, por lo que podemos reemplazar el valor de un indice haciendo referencia al mismo
datos[1] = 29           #Esto reemplaza en valor 55 por un valor 29 de la lista de datos
print(datos)            #Muestra ['Hola', 29, 'mundo', 3.14, 'desde', 777, 'python']

#Con el metod append() podemos añadir elementos al final de una lista
pares = [2, 4, 6, 8]
pares.append(10)        #Agrega 10 al final de la lista pares
pares.append(6 * 2)     #Soporta operaciones
print(pares)            #Muestra [2, 4, 6, 8, 10, 12]

#Podemos reemplazar elementos de una lista mediante slicing
letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3] = ['A', 'B', 'C']
print(letras)           #Muestra ['A', 'B', 'C', 'd', 'e', 'f']
letras[-3:] = []        #Si asignamos una lista vacia, eliminamos los elementos seleccionados con slice 
print(letras)           #Muestra ['A', 'B', 'C']
letras = []             #Podemos vaciar toda la lista asignando una lista vacia
print(letras)           #Muestra []

#Podemos saber la longitud de una lista al igual que en las cadenas con el metodo len()
print(len(numeros))     #Muestra 10
print(len(datos))       #Muestra 7
print(len(letras))      #Muestra 0

#Podemos tener una lista que almacene listas
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
r = [a, b, c]           #Esta lista almacena las listas a, b y c

print(r)                #Muestra [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(r[1])             #Podemos acceder a las listas internas mediante el indice, esto muestra [4, 5, 6]
print(r[1][1])          #Muestra 5
print(r[2][1])          #Muestra 8

#Podemos sumar los elementos de una lista usando la funcion sum(lista)
print(sum(a))           #El resultado es la suma de sus elementos en este caso es 6