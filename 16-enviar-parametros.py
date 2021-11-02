import  sys     #Usamos la libreria sys para poder parasar parametros a nuestro script

print(sys.argv) #De esta manera recibimos parametros, todos los parametros se reciben como una cadena

'''
para enviar parametros a nuestro script usamos desde nuestra terminal la siguiente instruccion:

py 16-enviar-parametros.py "primer parametro" 1 2 3

el programa nos responde con ['.\\16-enviar-parametros.py', 'primer parametro', '1', '2', '3']
donde efectivamente vemos que todos los parametros fueron recibidos como cadenas
'''

'''
Despues ya que podemos recibir parametros podemos procesarlos de la manera que mejor queramos
por ejemplo: recibiremos una cadena y el numero de veces que queremos que se repita
puesto que los argumentos se reciben en una lista, podemos hacer referencia a los indices
de dicha lista para acceder a los argumentos
'''

cadena = sys.argv[1]
repeticiones = int(sys.argv[2])

print(cadena * repeticiones)

'''
Nota: si utilizamos un script que ocupa argumentos y dichos argumentos no se proporcionan
el script lanzara un error
'''