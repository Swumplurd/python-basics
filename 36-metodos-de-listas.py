#Metodos de cadenas

lista = [1, 2, 3, 4, 5]

#El metodo append() nos permite agregar un nuevo elemento al final de la lista
lista.append(6)
print(lista)

#El metodo clear() vaciara una lista
lista.clear()
print(lista)

#Con el metodo extend() podemos extender una lista con otra
l1 = [1, 2, 3]
l2 = [3, 4, 5]
l1.extend(l2)
print(l1)

#El metodo count() nos permite contar cuantas veces se repite un elemento en una lista
print(l1.count(3))

#El metodo insert() nos permite agregar un nuevo elemento en un indice deseado
l3 = [5, 10, 15, 25]
l3.insert(-1, 20)   #Inserta en la penultima posicion el valor de 20
print(l3)

#El metodo pop() nos permite sacar elementos y sacarlos de la lista en la ultima posicion aun que si le pasamos por parametro un indice podemos obtener dicho valor y sacarlo de la lista
l3.pop(0)
print(l3)   #Sacamos de la lista el primer elemento

#Para directamente eliminar un elemento de una lista tenemos el metodo remove()
l3.remove(25)   #Elimina el numero 25 de nuestra lista
print(l3)

#El metodo reverse() nos permite darle la vuelta a una lista
l4 =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
l4.reverse()
print(l4)

#En listas tambien podemos usar el metodo join() para crear cadenas a partir de los elementos de una lista
l5 = ['H', 'o', 'l', 'a']
print("".join(l5))  #Une los elementos de la lista con un caracter vacio

#Con el metodo sort() podemos organizar los elementos de una lista
l6 = [3, 6, 34, 7, 6, 3, 4, 6, 87, 9]

l6.sort()   #Ordenado de menor a mayor
print(l6)
l6.sort(reverse = True)
print(l6)   #Ordenado de mayor a menor