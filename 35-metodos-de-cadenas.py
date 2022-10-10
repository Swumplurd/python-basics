#Metodos de cadenas

frase = "hola mundo!"

#El metodo upper() convierte una cadena a mayusculas
print(frase.upper())

#El metodo lower() convierte una cadena a minusculas
print(frase.lower())

#El metodo capitalize() convierte la primera letra de una cadena a mayuscula
print(frase.capitalize())

#El metodo title() convierte las primeras letras de cada palabra en una cadena a mayuscula
print(frase.title())

#El metodo count() cuenta cuantas veces se encuentra una palabra o letra en una cadena
print(frase.count("o"))
print(frase.count("mundo"))

frase1 = "adios mundo mundo!"

#Con el metodo find podemos obtener el indice de donde se encuentra una palabra o una letra empezando por el principio de la cadena
print(frase1.find("mundo"))
#Con el metodo rfind podemos obtener el indice de donde se encuentra una palabra o una letra pero empezando por el final de la cadena
print(frase1.rfind("mundo"))

#Con el metodo isdigit() podemos saber si una cadena esta compuesta unicamente con digitos
digitos = "123123123"
print(digitos.isdigit())

#El metodo isalnum() nos perite saber si una cadena esta compuesta por caracteres alfa-numericos
alphanumeric = "123ABC"
print(alphanumeric.isalnum())

#El metodo isalpha() nos permite saber si en una cadena unicamente existen letras
alpha = "ABCxyz"
print(alpha.isalpha())

#Con los metodos islower() isupper() istitle() podemos saber si una cadena unicamente tiene minusculas, mayusculas y cada palabra capitalizada respectivamente
minus = "abc"
mayus = "ABC"
title = "Hola Python"

print(minus.islower())
print(mayus.isupper())
print(title.istitle())

#Con el metodo isspace() sabremos si una cadena esta unicamente compuesta por espacios vacios
espacios = "    "
print(espacios.isspace())

#Con los metodos startswith() y endswith() sabremos si una cadena empieza con cierta palabra o caracter o si termina con cierta palabra o caracter
frase2 = "Hola mundo desde python"
print(frase2.startswith("Hola"))
print(frase2.endswith("python"))

#El metodo split() nos permite obtener una lista de palabras de una string dado un caracter de separacion, por defecto es el espacio
frase3 = "Hola-mundo-desde-python"
print(frase2.split())
print(frase3.split("-"))

#Con el metodo join podemos agregar palabras o caracteres entre los caracteres de una cadena
frase4 = "HOLA"
print(" ".join(frase4))
print("-".join(frase4))

#El metodo strip() nos permite quitar caracteres del principio y final de una cadena
frase5 = "    Hola    "
frase6 = "....Adios...."
print(frase5.strip(" "))
print(frase6.strip("."))

#El metodo replace() nos permite reemplazar un caracter o una subcadena de una cadena dada
frase7 = "Hola mundo mundo mundo mundo"
print(frase7.replace("mundo", "marte"))
print(frase7.replace("mundo", "", 3))   #Reemplazara mundo por una cadena vacia 3 veces