#Indices
''' Los indices en una palabra son los espacios que ocupa cada caracter, por ejemplo en la palabra "python" la 'p' 
    ocupa la posicion numero 0 y la 'n' la posicion numero 5
    En Python los indices de las palabras se pueden contar tanto de izquerda a derecha como de derecha a izquierda 
    como en el siguiente ejemplo:
     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
     0   1   2   3   4   5
    -6  -5  -4  -3  -2  -1
    Si contamos los indices de derecha a izquierda haremos referencia a los numeros con signo negativo '''

palabra = "python"

print(palabra[0])       #Arroja 'p'
print(palabra[-1])      #Arroja 'n'

print(palabra[5])       #Arroja 'n'
print(palabra[-6])      #Arroja 'p'

#Slice
''' Para obtener subcadenas de una palabra existe una funcion nativa de Python llamada slice
     y la podemos implementar como se muestra:'''
print(palabra[0:2])     #Nos arrojara la subcadena definida desde el indice 0 hasta el indice 2 excluyente

#Podemos generar el intervalo tomando en cuenta tanto indices positivos como indices negativos
print(palabra[2:-1])    #Arroja 'tho'
print(palabra[-4:5])    #Arroja 'tho'

#Si queremos tomar en cuenta la primera parte de la palabra podemos hacerlo asi
print(palabra[:4])      #Arroja 'pyth'

#Podemos hacer lo mismo si queremos tomar en cuenta la parte final de la palabra
print(palabra[4:])      #Arroja 'on'

#Si en una palabra intentamos acceder a un indice que se encuentre fuera de la propia definicion de la palabra nos arrojara error
#print(palabra[77])     Arroja error

#Si en un slice indicamos un indice fuera de la definicion de la palabra pueden pasar dos cosas
print(palabra[2:77])    #Muestra 'thon'
print(palabra[:77])     #Muestra 'python'
print(palabra[77:])     #Muestra ''

#En python las palabras son inmutables sin embargo podemos modificarla de la siguiente forma
palabra = palabra[:3] + 's' + palabra[4:]
print(palabra)          #Muestra 'pytson'

#Para obtener la longitud de una palabra usamos la funcion len()
print(len(palabra))     #Muestra 6

#Mediante slicing podemos volear cadenas usando un tercer parametro como se muestra:
frase = 'Pablito saca un clavito'
print(frase[::-1])      #Frase mostrada alreves