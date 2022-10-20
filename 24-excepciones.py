# EXCEPCIONES

#Las excepciones nos permiten anticiparnos a errores y tener un manejo de estos sin interrumpir la ejecucion del script

def dividir(a, b):
    try:
        return a / b
    except:
        return "No puedes dividir entre cero"

print(dividir(5, 0))

#El uso de try-except puede ir incluso mas alla como se muestra

def dividir1(a, b):
    try:
        return a / b
    except:
        return "No puedes dividir entre cero"
    finally:
        return "finally se ejecuta sin importar si hubo o no un error"

print(dividir1(5, 9))