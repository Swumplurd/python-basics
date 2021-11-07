#Las cadenas formateadas son similares a las template strings en JS, la forma de implementarlas es la siguiente

nombre = 'Fernando'
apellido = 'Vasquez'
edad = 27

#De esta manera las variables toman el espacio segun su orden de aparicion
cadena = 'Tu nombre es: {} {} y tu edad {}'.format(nombre, apellido, edad)
print(cadena)

#De esta manera podemos cambiar el orden en que se mostrara la informacion
cadena = 'Tu nombre es: {2} {1} y tu edad {0}'.format(edad, apellido, nombre)
print(cadena)

#Tambien podemos hacer referencia a las variables mediante una clave
cadena = 'Tu nombre es: {nom} {ape} y tu edad {num}'.format(num = edad, ape = apellido, nom = nombre)
print(cadena)

#Format tambien nos permite hacer otras cosas como centrar o alinear un texto
print("{:>15}".format('Texto')) #Alinea el texto con 15 espacios por la derecha
print("{:<15}".format('Texto')) #Alinea el texto con 15 espacios por la izquierda
print("{:^15}".format('Texto')) #Centra el texto con 15 espacios

#Format tambien nos permite cortar(truncar) palabras o numeros
print("{:.3}".format('Texto')) #Corta el texto y solo muestra Tex

#Nota: el centrado o alineamiento se puede combinar con el truncamiento
print("{:>15.3}".format('Texto')) #Corta el texto y solo muestra Tex y ademas esta alineado

#Format nos permite rellenar espacios con digitos en numeros
print("{:5d}".format(10))

#Tambien nos permite rellenar con ceros
print("{:05d}".format(10))

#Tambien podemos truncar el valor de un flotante y rellenarlo con espacios
print("{:7.3f}".format(3.14159265359))
print("{:.3f}".format(314.159265359))

#Tambien podemos truncar el valor de un flotante y rellenarlo con ceros
print("{:07.3f}".format(3.14159265359))

#El formateo de cadenas tambien puede implementarse de forma mas sencilla
print(f"Hola {nombre}")