#Los conjuntos son colecciones desordenadas de elementos unicos

conjunto = set()        #Asi declaramos un conjunto vacio
conjunto = {1, 2, 3}    #Asi creamos un conjunto con tres elementos

#Agregar elementos al conjunto
conjunto.add(4)         #Podemos agregar mas elementos al conjunto con .add()
print(conjunto)         #{1, 2, 3, 4}
conjunto.add(0)         #Se dice que un conjunto es desordenado puesto que los elementos agregados no se agragan a la ultima posicion estrictamente
print(conjunto)         #{0, 1, 2, 3, 4}

#Agregando caracteres al conjunto
conjunto.add('H')
conjunto.add('A')
conjunto.add('Z')
print(conjunto)         #{0, 1, 2, 3, 4, 'A', 'Z', 'H'}

#Podemos usar los conjuntos para saber la existencia
grupo = {'Fernando', 'Laura', 'Alberto'}

print('Fernando' in grupo)      #True
print('Hector' in grupo)        #False
print('Hector' not in grupo)    #True

#En un conjunto no puede haber elementos repetidos
test = {1, 1, 1}    #Los valores repetidos de un conjunto se eliminan
print(test)         #{1}

#Podemos eliminar los elementos repetidos de una lista casteandola a un conjunto
lista = [1, 2, 3, 2, 1]

conj = set(lista)   #Ahora tenemos los elementos sin duplicados
print(conj)         #{1, 2, 3}

#Nuevamente podemos castearlo a una lista
lista = list(conj)  #Tenemos ahora la conversion a una lista
print(lista)        #[1, 2, 3]

#Podemos hacer lo mismo con cadenas de caracteres
cadena = 'anita lava la tina'
conjunto = set(cadena)
print(conjunto)     #{'n', 't', 'l', 'i', 'v', 'a', ' '}