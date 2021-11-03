#Para implementar funciones usamos la palabra reservada def seguido del nombre de la funcion y los parentesis de parametros, terminando con :
def holiwo():
    print('Holiwo')

holiwo()

#Las variables declaradas dentro de una funcion tienen un scope local, a continuacion varios ejemplos de scope de variables
nombre = 'Morma'    #Scope global
def chaito():
    nombre = 'Fernando' #Scope local dentro de la funcion unicamente prro!
    print(f'Adios {nombre}')

chaito()
print(nombre)

#Ejemplo basico de uso de funciones
def tabla(num):
    for i in range(11):
        if(i == 0):
            continue
        print(f'{num} * {i} = ', num * i)

tabla(9)

#Retorno de valores en funciones
def ret_cad():
    return 'soy un retorno string'  #retorno string
print(ret_cad())

def ret_num():
    return 3.1415   #retorno numerico
print(ret_num() * 3)

def ret_list():
    return [1, 2, 3, 4, 5]
print(ret_list())
print(ret_list()[-1])   #Podemos usar operadores directamente en la llamada a la funcion

def ret_tupla():
    return 'Hola Mundo', 3.1415, [1, 2, 3]  #Podemos retornar mas de un tipo de dato
print(ret_tupla())  #Se imprimen como una tupla
cadena, pi, lista = ret_tupla()
print(cadena, pi, lista) #Podemos almacenar cada valor devuelto en variables distintas