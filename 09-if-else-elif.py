# IF ELSE ELIF

""" En python tenemos condicionales como otros lenguajes de programacion, tenemos 'if', 'else', 
    pero en este caso no tenemos una sentencia como 'else if' en su defecto tenemos su equivalente 
    'elif'. A diferencia de otros lenguajes de programacion no usamos llaves para indicar el bloque 
    de codigo que ejecutara el condicional, en python usamos la identacion """

#if
if True:
    print('La condicion es veradera')

#if else
if False:
    print('Esto nunca se ejecutara si la condicion es falsa')
else:
    print('La condicion fue falsa')

#elif
if False:
    print('Esto nunca se ejecutara si la condicion es falsa')
elif False:
    print('Esto nunca se ejecutara si la condicion es falsa')
elif False:
    print('Esto nunca se ejecutara si la condicion es falsa')
elif True:
    print('Tercer elif')
else:
    print('En el else')

''' elif sirve para evaluar diferentes condiciones, la peculiaridad radica en que la cadena de elif terminara cuando
    una condicion sea verdadera, una ves encontrada una condicion verdadera los elif consiguientes no se evaluaran '''