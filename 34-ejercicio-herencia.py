# EJERCICIO CON HERENCIA

class Vehiculo:
    def __init__(self, color = None, ruedas = 0):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color = None, ruedas = 0, velocidad = 0, cilindrada = 0):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Coche):
    def __init__(self, color=None, ruedas=0, velocidad=0, cilindrada=0, carga = 0):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, color=None, ruedas=0, tipo = None):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color=None, ruedas=0, tipo=None, velocidad = 0, cilindrada = 0):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche = Coche("Rojo", 4, 200, 400)
camioneta = Camioneta("Blanco", 4, 240, 800, 700)

bici = Bicicleta("Azul", 2, "Urbana")
moto = Motocicleta("Negra Mate", 2, "Deportiva", 200, 400)

vehiculos = [coche, camioneta, bici, moto]

def catalogar(vehiculos, ruedas = None):
    if ruedas is None:
        for vehiculo in vehiculos:
            if type(vehiculo).__name__ == "Coche":
                print(f"{type(vehiculo).__name__}: {vehiculo.color} {vehiculo.ruedas} {vehiculo.velocidad} {vehiculo.cilindrada}")
            elif type(vehiculo).__name__ == "Camioneta":
                print(f"{type(vehiculo).__name__}: {vehiculo.color} {vehiculo.ruedas} {vehiculo.velocidad} {vehiculo.cilindrada} {vehiculo.carga}")
            elif type(vehiculo).__name__ == "Bicicleta":
                print(f"{type(vehiculo).__name__}: {vehiculo.color} {vehiculo.ruedas} {vehiculo.tipo}")
            elif type(vehiculo).__name__ == "Motocicleta":
                print(f"{type(vehiculo).__name__}: {vehiculo.color} {vehiculo.ruedas} {vehiculo.tipo} {vehiculo.velocidad} {vehiculo.cilindrada}")
            else:
                print("No se reconoce el tipo de vehiculo")
    else:
        i = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                print(f"{type(vehiculo).__name__}: {vehiculo.color} {vehiculo.ruedas}")
                i += 1

        print(f"Se encontraron {i} vehiculos con {ruedas} ruedas")


catalogar(vehiculos)
catalogar(vehiculos, 2)