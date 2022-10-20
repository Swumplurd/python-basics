# HERENCIA MULTIPLE

#La herencia multiple es una caracteristica con la cual una clase puede heredar atributos y metodos de dos o mas superclases

class A:
    def __init__(self):
        print("Soy de clase A")
    
    def a(self):
        print("Metodo de clase A")

class B:
    def __init__(self):
        print("Soy de clase B")
    
    def b(self):
        print("Metodo de clase B")

#La herencia multiple se hace de la siguiente manera

class C(A, B):  #Las clases a la izquierda tienen prioridad en cuanto a atributos y metodos por lo cual si dos clases tienen un mismo metodo se priorizara el de la clase a la izquierda
    def c(self):
        print("Metodo de clase C")

c = C()     #Al instanciar la clase se mostrara "Soy de clase A" ya que tiene prioridad sobre B al encontrarse a la izquierda

c.a()
c.b()
c.c()