# INPUTS

#Para leer valores que introduzcamos por teclado usamos la funcion input()
print('Ingresa un valor: ')
valor = input()
print(valor)                #Todos los valores que introduzacamos por teclado se almacenaran como cadenas de texto

#Tambien podemos imprimir alguna instruccion antes de introducir el valor por teclado
valor = input('Introduce un numero entero: ')
print(valor)

#Un inconveniete que podriamos tener es que al pedir numeros no podremos operarlos como quisieramos
#Para convertir una cadena que contiene un numero entero usamos lo siguiente
valor = input('Introduce un numero entero: ')
valor = int(valor)          #De esta manera ya tendremos un tipo de dato int que podremos operar
resultado = valor + valor
print(resultado)

#Para numeros flotantes tendremos que convertirlos de la siguiente manera
valor = input('Ingresa un numero flotante: ')
valor = float(valor)
print(valor)

#Algo que es conveniente al momento de pedir numeros es hacerlo de la siguiente manera
valor = float(input('Ingresa un numero flotante o entero: '))   #De esta manera parseamos al mismo tiempo que pedimos el dato, ademas, al parsear a float incluimos la posibilidad de que el numero proporcionado sea int

#Tambien podemos convertir numeros a string
num1 = 3.3
num2 = 6.7
res = str(num1 + num2)      #Resultado en una string que posteriormente no podremos operar
print(res)