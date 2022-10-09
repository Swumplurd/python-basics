#El polimorfismo es una propiedad de la herencia en la que objetos de distintas subclases pueden responder a una misma accion

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
class Libro(Producto):
    isbn = None
    autor = None

class Alimento(Producto):
    distribuidor = None
    productor = None

libro = Libro("El señor de los anillos", 600)
libro.isbn = "01-2345-678-9"
libro.autor = "JRR Tolkien"

alimento = Alimento("Jamon", 100)
alimento.distribuidor = "De casa"
alimento.productor = "Fud"

def rebajar_precio(producto, rebaja):       #Gracias al polimorfismo todos nuestros objetos deberian de ser capaces de funcionar con esta funcion ya que todos cuentan con el atributo precio
    producto.precio = producto.precio - ((producto.precio / 100) * rebaja)

print("El precio original es:", libro.precio)
rebajar_precio(libro, 10)
print("El precio rebajado es:", libro.precio)

print("El precio original es:", alimento.precio)
rebajar_precio(alimento, 50)
print("El precio rebajado es:", alimento.precio)

""" 
Debemos de tener cuidado al modificar un atributo en un objeto ya que al pasarse como referencia en nuestra funcion de
rebajar_precio() en realidad se modifica el precio original y en ocaciones esto no sera lo que buscamos, para crear
copias de objetos es necesario usar un modulo externo llamado copy

import copy

copia_libro = copy.copy(libro)

y de esta forma preservamos la informacion original del objeto
"""

