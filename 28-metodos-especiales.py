#Los metodos especiales son metodos los cuales cumplen una tarea en especifico, caracterizandose por esta sintaxis __metodo__

class Cancion:
    #Constructor de clase
    def __init__(self, nombre, duracion, grupo):
        self.nombre = nombre
        self.duracion = duracion
        self.grupo = grupo

    #Destructor de clase
    def __del__(self):
        print(f"Se ha borrado la cancion: {self.nombre}")

    #Redefinicion del metodo str
    def __str__(self):
        return f"Cancion {self.nombre} del grupo {self.grupo} con una duracion de {self.duracion}"

    #Redefinicion del metodo len
    def __len__(self):
        return self.duracion

cancion = Cancion("Enter Sandman", 180, "Metallica")

print(str(cancion))     #Como podemos observar los metodos especiales se usan diferente ya que no hacemos cancion.str() o cancion.len()
print(len(cancion))
del(cancion)