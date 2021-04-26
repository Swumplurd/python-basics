#Las tuplas son inmutables, se implementan similares a las listas con la diferencia que lo haremos dentro de parentesis en lugar de corchetes

tupla = ('Hola', 1, True, [1,2,3,4,5,6,7,8,9,0], 'Adios')
print(tupla)

#Las tuplas al igual que las listas soportan indexacion y slicing
print(tupla[0])         #Hola
print(tupla[-1])        #Adios
print(tupla[1:])        #(1, True, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'Adios')
print(tupla[2:4])       #(True, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(tupla[3][-2])     #9

#tupla[0] = 30          #Lanza error puesto que es inmutable

#Al igual que las listas podemos obtener su longitud, algun index
print(len(tupla))           #5
print(tupla.index('Hola'))  #0 || Lanza error si no encuentra el elemento en la tupla

#El metodo count nos permitira saber cuantas veces se repite un elemento en la tupla
print(tupla.count(1))       #2