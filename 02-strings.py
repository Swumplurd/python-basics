# STRINGS

''' En el interprete nosotros podemos escribir texto directamente, simplemente tenemos que escribir el texto entre comillas dobles o simples
    Podemos escribir comillas simples dentro de unas comillas dobles y viceversa
    Si queremos escribir comillas dobles dentro de comillas dobles debemos escapar las comillas mas internas: "Hola \"Morminiwini\"" '''

#Se recomienda usar la funcion print() para imprimir cadenas
print('Hola Mundo desde print()')

cadena = 'Hola Mundo'   #Podemos asignar una cadena a una variable
print(cadena)

#Podemos usar sentencias de escape para dar saltos de linea, tabulaciones, etc.
print('\tVengo de ser tabulado\nVengo de un salto de linea')

#Podemos usar la siguiente sintaxis para no tener que escapar los saltos de linea con \n
print("""Este tipo
de sintaxis nos
permite escribir
en lineas separadas
""")

#Podemos usar concatenacion de la siguiente manera
cadena1 = 'Hola'
cadena2 = 'Mundo'
print(cadena1 + cadena2)

#Tambien podemos multiplicar cadenas de la siguiente forma
cadena3 = 'hola o la\n'
print(cadena3 * 5)