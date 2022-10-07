#Una funcion recursiva es aquella que se llama a si misma, tenemos funciones recursivas sin retorno y con retorno

#Funcion recursiva sin retorno
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("La cuenta atras ha finalizado!")

cuenta_atras(5)

#Para entender mejor como se comporta una funcion recursiva sin retorno podemos agregar los siguientes print
def cuenta_atras_explicada(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras_explicada(num)
    else:
        print("La cuenta atras ha finalizado!")
    
    print("Fin de la funcion", num)

cuenta_atras_explicada(5)

#Funcion recursiva con retorno
def factorial(num):
    print("Valor inicial:", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("Valor final:", num)
    return num

print(factorial(5))

#Para comprender mejor el comportamiento de una funcion recursiva con retorno podemos hacer lo siguiente

def sumatorio(numero):
    if numero > 0:
        numero = numero + (sumatorio(numero - 1))
    return numero

print(sumatorio(3))