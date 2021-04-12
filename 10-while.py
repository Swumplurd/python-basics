#La sintaxis de la sentencia while es la siguiente
c = 0
while c <= 5:   #While evalua una condicion si esta da true se ejecuta.
    c += 1
    print('c tiene el valor de',c)

while False:
    print('El while tiene un False')
else:
    print('Una peculiaridad de while es que una ves la condicion sea False, se puede usar un else')

while c <= 10:
    c += 1
    if c == 9:      #Cuando c sea igual a 9, se ejecutara el continue y el print no se ejecutara, se continuara a la siguiente iteracion
        continue
    print('El valor es:',c)

#Puesto que en python no existe la sentencia switch podemos usar while para hacer menus interactivos

while True:
    op = input('''Elige un opcion
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Divicion
    5) Salir
    ''')

    if op == '1':
        n1 = float(input('Introduce el primer numero '))
        n2 = float(input('Introduce el segundo numero '))
        print('El resultado de la suma es: ',n1 + n2)
    elif op == '2':
        n1 = float(input('Introduce el primer numero '))
        n2 = float(input('Introduce el segundo numero '))
        print('El resultado de la resta es: ',n1 - n2)
    elif op == '3':
        n1 = float(input('Introduce el primer numero '))
        n2 = float(input('Introduce el segundo numero '))
        print('El resultado de la multiplicacion es: ',n1 * n2)
    elif op == '4':
        n1 = float(input('Introduce el primer numero '))
        n2 = float(input('Introduce el segundo numero '))
        print('El resultado de la divicion es: ',n1 / n2)
    elif op == '5':
        print('Hasta luego')
        break   #break rompe el bucle
    else:
        print('Comando invalido, intenta con una opcion valida')
    