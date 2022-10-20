# OPERACIONES CON NUMEROS (MATH)

#En python tenemos diferentes formas que son nativas en python para operar numeros, sin embargo tambien contamos con paquetes como math

import math

pi = 3.14159

#Con el metodo round() podemos redondear un numero
print(round(pi))    #Si el valor a redondear en sus decimales es menor igual a .5 redondea a la baja
print(round(4.6))   #Si el valor a redondear en sus decimales es mayor a .5 redondea a la alta

#Gracias a la libreria math podemos decidir si queremos redondear a la alta o a la baja con sus metodos floor() y ceil()
print(math.floor(pi))   #floor redondea siempre a la baja
print(math.ceil(pi))    #ceil redondea siempre a la alta

#Con el metodo abs() podemos obtener el valor absoluto de un numero
print(abs(-3))
print(abs(4))

#Para realizar la suma de los elementos de una lista que contiene numeros usamos sum()
lista = [1, 2, 3]
print(sum(lista))

#Sin embargo sum tiene un pequeño inconveniente al manejar flotantes
lista2 = [0.9999999, 1, 2, 3]
print(sum(lista2))      #Muestra 6.999999900000001

#Para resolver este inconveniente mediante math y su metodo fsum
print(math.fsum(lista2))    #Muestra 6.9999999

#Podemos truncar valores flotantes con el metodo trunc()
print(math.trunc(math.fsum(lista2)))    #Muestra 6

#Python de manera nativa nos permite realizar potencias de la siguiente forma
print(2**3)

#El equivalente con math es:
print(math.pow(2, 3))

#Sin embargo python ya implementa de forma nativa el metodo pow()
print(pow(2,3))

#Para realizar raiz cuadrada con math
print(math.sqrt(9))

#Por ultimo podemos consultar el valor de constantes tales como pi de la siguiente forma
print(math.pi)
print(math.e)
