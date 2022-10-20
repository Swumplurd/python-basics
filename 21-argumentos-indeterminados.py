# ARGUMENTOS INDETERMINADOS

#En ocaciones necesitaremos crear funciones de las cuales no tenemos un numero determinado de parametros, para ello python tiene formas de gestionar parametros indeterminados
#Ya que en python podemos mandar parametros por posicion o por nombre python tiene dos formas diferentes para gestionar los parametros indeterminados

def indeterminados_posicion(*args):     #Poniendo *args es la manera de decirle a python de que los argumentos que esperamos son indeterminados
    print(args)     #Python gestiona estros parametros como una tupla
    for arg in args:    #Podemos recorrer esta tupla para obtener todos sus elementos
        print(arg) 

indeterminados_posicion(1, 2, 3, "Hola", ["Adios", 4, 5])

def indeterminados_nombre(**kwargs):    #Poniendo **kwargs es la manera de decirle a python de que esperamos argumentos indeterminados con nombre
    print(kwargs)   #Cuando los parametros son nombrados python los gestiona como un diccionario
    for key in kwargs:  #Podemos recorrer el diccionario para obtener sus claves y valores
        print(key, ":", kwargs[key])

indeterminados_nombre(num = 7, list = ["Hola", "Adios"], string = "cadena")

def ambas_formas(*args, **kwargs):  #De esta forma podemos gestionar ambas formas en una misma funcion
    print(args)
    print(kwargs)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, ":", kwargs[key])

ambas_formas(1,2,3,4,5, data=['a', 'b', 'c'])