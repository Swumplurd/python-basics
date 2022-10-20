# DICCIONARIOS

#Los diccionarios son una estructura mapeada de claves-valor, no puede haber dos claves iguales dentro de un mismo diccionario

vacio = {}      #Creacion de un diccionario vacio
print(vacio)    #muestra {}
type(vacio)     #muestra el tipo 'dict'

traducciones = {
    "verde": "green",   #clave: verde, valor: green
    "rosa": "pink",
    "azul": "blue",
    "amarillo": "yellow"
}

print(traducciones)         #Los diccionarios son estructuras desordenadas
print(traducciones["azul"]) #Nos muestra "blue", asi que para acceder a los valores debemos hacer referencia a la clave

#Para redefinir el valor de una clave se hace de la siguiente manera
traducciones["rosa"] = "pinky"  #Cambia su valor de "pink" a "pinky"
print(traducciones["rosa"])     #Muestra "pinky"

#Para borrar un elemento
del(traducciones["amarillo"])   #Borra amarillo
print(traducciones)             #Ya no esta amarillo, ni su clave ni su valor

#Podemos recorrer los elementos de un diccionario con un for
edades = {
    "Marco": 22,
    "Posi": 34,
    "Fernando": 27,
    "Carlos": 25
}
for edad in edades:
    print(edad) #Sin embargo esto nos muestra la clave y no el valor

#Para mostrar el valor en lugar de la clave en diccionarios
for clave in edades:
    print(edades[clave])    #Asi hacemos referencia al valor de la clave que estamos pasando

#Para mostrar tanto la clave como el valor
for clave in edades:
    print(clave,edades[clave])

#De manera correcta lo anterior se hace con items()
for clave,valor in edades.items():
    print(clave,valor)

#Podemos usar diccionares en conjunto con otras estructuras como las listas
personas = []
persona1 = {"nombre": "Fernando", "apellido": "Vasquez", "edad": 27}
persona2 = {"nombre": "Posi", "apellido": "Ibanez", "edad": 57}
persona3 = {"nombre": "Carlos", "apellido": "Ayala", "edad": 25}
personas.append(persona1)
personas.append(persona2)
personas.append(persona3)
print(personas) #Tenemos una lista de diccionarios

#Para hacer referencia a los valores de una lista de diccionarios
for persona in personas:
    print(persona["nombre"], persona["apellido"], persona["edad"])  #Obtenemos todos los valores