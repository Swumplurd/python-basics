#Pilas LIFO(Last In First Out)
#Python no implementa pilas como tal, pero se pueden simular con listas

pila = [1, 2, 3]
pila.append(4)      #Usamos append() para introducir elementos al final de nuestra pila
pila.append(5)
pila.append(6)
print(pila)         # [1, 2, 3, 4, 5, 6]

#Para sacar elementos por el final usamos el metodo pop()
ult = pila.pop()  #Devuelve el ultimo elemento de nuestra pila y lo borra
print(ult)      # 6
print(pila)     # [1, 2, 3, 4, 5]


#Colas FIFO(First In First Out)7
#Para usar colas en Python debemos importar un modulo que nos permita utilizarlas

from collections import deque
import collections

cola = deque()
print(cola)     #deque([])

#Para definir elementos dentro de la cola le podemos pasar una lista
cola = deque(['Fernando', 'Laura', 'Carlos'])
print(cola)     #deque(['Fernando', 'Laura', 'Carlos'])

#Para seguir añadiendo elementos usamos append para añadir al final de la cola
cola.append('Posi')
cola.append('Marco')
print(cola)     #deque(['Fernando', 'Laura', 'Carlos', 'Posi', 'Marco'])

#Para sacar elementos de la cola por el inicio usamos un popleft()
primero = cola.popleft()
print(primero)  #Fernando
print(cola)     #deque(['Laura', 'Carlos', 'Posi', 'Marco'])