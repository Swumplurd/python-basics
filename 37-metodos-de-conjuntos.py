# METODOS DE CONJUNTOS

c1 = set();   #Creamos un conjunto vacio

#Con el metodo add() podemos agregar elementos a este conjunto
c1.add(1)
c1.add(2)
c1.add(3)
c1.add(4)
print(c1)

#Con el metodo discard() podemos quitar un elemento por su valor de un conjunto
c1.discard(4)
print(c1)

#Para copiar un conjunto en otro conjunto se hace de la siguiente manera
c2 = c1.copy()  #Este metodo nos crea una copia del conjunto y no una copia de la referencia en memoria
print(c2)

#Para limpiar un conjunto y dejarlo vacio usamos clear()
c2.clear()
print(c2)

#PPartiremos de estos cuatro conjuntos para hacer las siguientes operaciones
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {-1, 99}
c4 = {1, 2, 3, 4, 5, 6}

#Para saber si un conjunto es disjunto de otro (que nungun elemento exista en comun en los dos conjuntos) isdisjoint()
print(c1.isdisjoint(c3))
print(c1.isdisjoint(c2))

#Para saber si un conjunto es un subcojunto de otro (que los valores de un conjunto se encuentren dentro de otro) issubset()
print(c1.issubset(c4))
print(c2.issubset(c4))
print(c3.issubset(c4))

#Para saber si un conjunto es un superconjunto de otro (es decir que un conjunto contenga a otro) issuperset()
print(c1.issuperset(c4))
print(c2.issuperset(c4))
print(c3.issuperset(c4))
print(c4.issuperset(c1))

#Para realizar operaciones con conjuntos tales como union, diferencia, interseccion, diferencia simetrica
#Union
print(c1.union(c2))
c1.update(c2)   #Si quisieramos almacenar la union en c1 usamos update()
print(c1)

#Diferencia
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {-1, 99}
c4 = {1, 2, 3, 4, 5, 6}

print(c1.difference(c2))
c1.difference_update(c2)    #Esto hara que se almacene la diferencia en el c1
print(c1)

#Interseccion
c1 = {1, 2, 3}
c2 = {3, 4, 5}

print(c1.intersection(c2))  #Devuelve un nuevo conjunto con los elementos en comun de ambos conjuntos
c1.intersection_update(c2)  #Almacena en c1 la interseccion de los dos conjuntos
print(c1)

#Diferencia Simetrica
c1 = {1, 2, 3}
c2 = {3, 4, 5}

print(c1.symmetric_difference(c2))  #Devuelve los elementos que no se comparten entre ambos conjuntos
c1.symmetric_difference_update(c2)  #Almacena el resultado de la diferencia simetrica en c1
print(c1)