# EJERCICIO CON CLASES

""" 
Crear una clase llamada Punto con sus dos coordenadas X,Y
Añadir un metodo constructor para crear puntos facilmente. Si no se recibe una coordenada su valor sera 0
Sobreescribe el metodo str para que al imprimir por pantalla un punto aparezca en formato (X, Y)
Añadir un metodo llamado cuadrante que indique a que cuadrante pertenece el punto, mostrar Origen si es (0, 0)
Añadir un metodo llamado vector que tome otro punto y calcule el vector resultante entre los dos puntos
Añade un metodo llamado distancia que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla
"""

import math

class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        else:
            return "Origen"

    def vector(self, punto):
        return f"El vector resultante es ({punto.x - self.x}, {punto.y - self.y})"

    def distancia(self, punto):
        return f"La distancia entre los puntos es: {math.sqrt(pow(punto.x - self.x, 2) + pow(punto.y - self.y, 2))}"

class Rectangulo:
    def __init__(self, punto1 = Punto(), punto2 = Punto()):
        self.diagonal = Punto(punto2.x - punto1.x, punto2.y - punto1.y)
    
    def base(self):
        return f"La base del rectangulo es: {abs(self.diagonal.x)}"
    def altura(self):
        return f"La base del rectangulo es: {abs(self.diagonal.y)}"
    def area(self):
        return f"El area del rectangulo es: {abs(self.diagonal.x) * abs(self.diagonal.y)}"

punto_a = Punto(3, 3)
punto_b = Punto(5, -2)
print(str(punto_a))
print(str(punto_b))
print(punto_a.cuadrante())
print(punto_b.cuadrante())
print(punto_a.vector(punto_b))
print(punto_b.vector(punto_a))
print(punto_a.distancia(punto_b))
print(punto_b.distancia(punto_a))


rectangulo = Rectangulo(punto_b, punto_a)
print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())
