#Metodos de los diccionarios

dict = {"amarillo": "yellow", "azul": "blue", "verde": "green"}

#Para obtener un valor dentro de un diccionario mediante su clave lo hacemos de la siguiente manera
print(dict["amarillo"])

#Existen otras maneras de obtener el valor y dar una respuesta por defecto en caso de que no se encuentre el valor
print(dict.get("azul", "No se encuentra"))
print(dict.get("negro", "No se encuentra"))

#Podemos usar in para saber si una clave se encuentra en un diccionario o no
print("verde" in dict)
print("rojo" in dict)

#Para obtener una lista con las claves de un diccionario podemos hacer lo siguiente
print(dict.keys())

#Para obtener una lista con los valores de un diccionario podemos hacer lo siguiente
print(dict.values())

#Si queremos tanto claves como valores usamos lo siguiente
print(dict.items())

#En los diccionarios tambien podemos utilizar pop() para sustraer un elemento del diccionario
dict.pop("amarillo", "No se encuentra") #Tambien nos permite agregar un mensaje en caso de que no encuentre el elemento
print(dict)

#Para vaciar un diccionario podemos usar clear()
dict.clear()
print(dict)
