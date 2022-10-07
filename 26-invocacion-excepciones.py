#En ocasiones necesitaremos crear una excepcion nosotros mismos y para ello debemos hacer lo siguiente

""" 
def func(a = None):
    if a is None:
        raise ValueError("Error! no se permiten valores nulos")

func()
"""

#Una vez creada nuestra excepcion podemos optimizar nuestro codigo y hacer el manejo de esta excepcion
def func1(a = None):
    try:
        if a is None:
            raise ValueError("Error! no se permiten valores nulos")
    except ValueError:
        print("Error! no se permiten valores nulos (desde except)")
        
func1()