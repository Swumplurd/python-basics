# HERENCIA

#La herencia es la forma que tiene una clase de pasar sus atributos y metodos a otra clase, sus aplicaciones pueden ser variadas aun que son tema de debate

class Producto:
    def __init__(self, referencia, nombre, precio, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    
    def __str__(self):
        return f"""
        REFERENCIA:     {self.referencia}
        NOMBRE:         {self.nombre}
        PRECIO:         {self.precio}
        DESCRIPCION:    {self.descripcion}
        """

prod = Producto(2403, "Cachibache dorado", 513, "Lindo cachibache color dorado")
print(str(prod))

#Para heredar de producto se hace de la siguiente manera
class Alimento(Producto):
    productor = None        #Creamos los atributos de clase unicos de esta clase heredada
    distribuidor = None

    def __str__(self):      #Reescribimos el metodo str que se adecue al contenido de nuestra clase
        return f"""
        REFERENCIA:     {self.referencia}
        NOMBRE:         {self.nombre}
        PRECIO:         {self.precio}
        DESCRIPCION:    {self.descripcion}
        PRODUCTOR:      {self.productor}
        DISTRIBUIDOR:   {self.distribuidor}
        """

alimento = Alimento(2404, "Jamon de pierna de pavo", 58, "Jamon de pierna de pavo listo para rebanar")
alimento.productor = "Fud"          #Gracias a la asignacion externa de python podemos asignar el valor a los atributos de nuestra clase heredada
alimento.distribuidor = "De casa"

print(str(alimento))