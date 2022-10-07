from __future__ import print_function


def resta(a, b):    #Definimos una funcion para recibir los parametros a y b
    return a - b

print(resta(5, 4))          #Usamos la funcion y le mandamos los parametros por posicion
print(resta(b = 4, a = 5))  #Tambien podemos enviar los parametros referenciando el nombre en lugar de la posicion

def suma(a = None, b = None):   #Podemos asignar parametros por defecto
    if a == None or b == None:  #Con los parametros por defecto podemos hacer validaciones
        return "Error, debes introducir dos parametros"

    return a + b

print(suma(5, 5))