# CLASES Y OBJETOS

#Para definir una clase en python lo hacemos de la siguiente manera
class Cliente:
    pass    #Por ahora dejaremos la clase vacia, pero dentro de la clase comunmente van atributos y metodos

#Para generar instancias de una clase creada lo hacemos de la siguiente forma
fernando = Cliente()    #Y de esta manera tenemos una instancia de la clase Cliente
print(type(fernando))   #Esto muestra <class '__main__.Cliente'> lo cual indica que es instancia de la clase Cliente


#Ahora crearemos una clase con sus atributos y metodos
class Banda:
    discografica = None     #Estos son atributos de la clase inicializados

    def __init__(self, nombre = "Sin nombre", estilo = "Sin estilo", integrantes = 1): #Init es un metodo especial que se ejecuta al instanciar un nuevo objeto de la clase. En todos los metodos el obligatorio el parametro self
        #self hace referencia a los atributos del objeto con lo cual podemos inicializarlos con los parametros recibidos en la funcion
        self.nombre = nombre
        self.estilo = estilo
        self.integrantes = integrantes

    def tocar(self, cancion):
        if cancion is None:
            return "debes especificar que cancion tocara la banda"
        
        return f"La banda esta tocando: {cancion}"

    def firmar_dicografica(self, discografica):
        self.discografica = discografica
    
    def info(self):
        return f"\nNombre: {self.nombre} \nIntegrantes: {self.integrantes} \nEstilo: {self.estilo} \nDiscografica: {self.discografica}"

banda1 = Banda("Metallica", "Metal", 4)
print(banda1.tocar("Enter Sandman"))
banda1.firmar_dicografica("EMI")
print(banda1.info())