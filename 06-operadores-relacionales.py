#Operadores relacionales

a = [1, 2, 3]
b = [3, 4, 5]

#Operador 'igual que'
print(1 == 1)       #True
print(0 == 1)       #False
print(a[2] == b[0]) #True

#Operador 'distinto de'
print(0 != 1)       #True
print(1 != 1)       #False
print(a[1] != b[2]) #True

#Mayor que
print(1 > 0)        #True
print(0 > 1)        #False
print(b[2] > a[0])  #True 

#Menor que
print(0 < 1)        #True
print(1 < 0)        #False
print(a[1] < b[0])  #True

#Mayor igual que
print(1 >= 1)       #True
print(1 >= 0)       #True
print(a[2] >= b[0]) #True

#Menor igual que
print(0 <= 0)       #True
print(0 <= 1)       #True
print(b[0] <= a[2]) #True

#Boleanos
print(True == False)    #False
print(False != True)    #True
print(False > True)     #False
print(False < True)     #True