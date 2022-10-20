# ARGUMENTOS POR VALOR O POR REFERENCIA

#En python hay dos formas en la que los argumentos son pasados a las funciones; por valor y por referencia

def doblar_numero(numero):  #En esta funcion el parametro pasa por valor e internamente python crea una copia de ese valor para realizar procesos sin afectar al valor original
    numero *= 2

num = 10
doblar_numero(num)
print(num)  #Muestra 10 ya que el valor no fue modificado por la funcion


def doblar_numeros(numeros):    #Cuando usamos listas el parametro se recibe como referencia con lo cual el valor original si se vera modificado
    for i,numero in enumerate(numeros):
        numeros[i] *= 2

nums = [10, 20, 30, 40]
doblar_numeros(nums)
print(nums)     #Muestra [20, 40, 60, 80] ya que el valor si fue modificado por la funcion


#Sin embargo cuando un parametro pasa por valor si podemos modificar el valor original y cuando el parametro pasa por referencia podemos respaldar la lista original para no modificar el valor
def doblar_numeros2(numero):
    return numero * 2   #Necesitamos hacer el retorno con el valor deseado

numero = 10
numero = doblar_numeros2(numero)    #Ya que retornamos el valor deseado hacemos la asignacion a la variable origial
print(numero)   #El valor mostrado es 20 ya que se modifico en la linea anterior


def doblar_numeros2(numeros):   #La funcion es exactamente la misma
    for i,numero in enumerate(numeros):
        numeros[i] *= 2

numeros = [10, 20, 30, 40]
doblar_numeros2(numeros[:])     #Lo que hacemos es mandar una copia de la lista origial para no modificar su valor
print(numeros)  #Muestra [10, 20, 30, 40] ya que la lista original no se modifico


#Es importatnte tener en cuenta lo siguiente; ya que diferentes tipos de dato se manejan de maneras diferente como lo vimos con anterioridad
a = 10
b = a   #En este punto se crea una copia del valor que tiene a al momento
a = 1000
print(b)    #Por lo tanto aqui se muesta 10

lista1 = [1, 2, 3, 4]
lista2 = lista1     #Aqui se crea una copia de la referencia de la lista1
lista1[0] = 1000
print(lista2)   #Por lo tanto aqui se muestra [1000, 2, 3, 4]