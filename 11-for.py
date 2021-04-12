#La sentencia For trabaja algo diferente a otros lenguajes con Java, C++, etc.
#For trabaja en python a partir de una lista. La sintaxis de For es la siguiente:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)

#Sin embargo si quisieramos modificar un numero de la lista dentro de el for, tendriamos que usar un indice externo
i = 0
for numero in numeros:
    numeros[i] *= 10
    i += 1 
print(numeros)

#Existe una manera mas corta de hacerlo sin necesidad de un indice externo
for i,numero in enumerate(numeros):     #De esta manera no tenemos ni que aumentar el indice manualmente, la funcion enumerate() lo hace por nosotros
    numeros[i] *= 10
print(numeros)

#En otros lenguajes de programacion no hace falta una lista para poder utilizar For, en python podemos usar la funcion range() para evitar usar una lista
for i in range(10):     
    print(i)

print(list(range(0,10)))    #range() nos evita que una lista ocupe espacio en memoria