#La encapsulacion es una funcionalidad que no permite la lectura y ejecucion de atributos y metodos externamente a la clase
#En comparacion a otros lenguajes de programacion python no cuenta con palabras reservadas para este fin, sin embargo se puede lograr de la siguiente manera

class Ejemplo:
    __atrubuto_privado = "Soy un atributo inalcanzable desde fuera"     #La manera de crear atributos privados es nombrarlos empezando con __ (doble guion bajo)

    def __metodo_privado(self):     #De igual manera para crear metodos privados debemos nombrarlos empezando con __
        print("Soy un metodo inalcanzable desde fuera")

ejemplo = Ejemplo()

""" 
print(ejemplo.__atrubuto_privado)   #Esto mostrara un AttributeError
print(ejemplo.__metodo_privado())   #AttributeError tambien
"""

#Si queremos acceder a un atributo o metodo privado lo podemos hacer a travez de un metodo publico
class Ejemplo1:
    __atrubuto_privado = "Soy un atributo inalcanzable desde fuera"

    def __metodo_privado(self):
        return "Soy un metodo inalcanzable desde fuera"

    def acceso_atr_publico(self):
        return self.__atrubuto_privado
    
    def acceso_mtd_publico(self):
        return self.__metodo_privado()

ejemplo1 = Ejemplo1()

print(ejemplo1.acceso_atr_publico())
print(ejemplo1.acceso_mtd_publico())
