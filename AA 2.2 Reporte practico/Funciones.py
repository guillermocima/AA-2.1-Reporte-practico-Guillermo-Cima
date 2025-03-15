'''#Ejemplo callback
def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma(a,b):
    return a + b

def resta(a, b): #funcion de primer orden
    return a - b

resultado = operar(5, 3, suma) #la funcion suma actua como callback al ejecutarse en operar
print(resultado)'''

'''#Ejemplo funcion primera clase

def saludo():
    return "¡Hola!"

mi_variable = saludo() #Ejecutamos la funcion y la asignamos a una variable
print(mi_variable) #'''

'''def elegir_operacion(operacion): # funcion de orden superior
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    if operacion == "multiplicar"
        return multiplicar #retomamos la funcion sin ejecutar
    else:
        return dividir
    
doble = elegir_operacion("multiplicar") #devuelve la funcion multiplicar
print(doble(10))
divide2 = elegir_operacion("dividir") #devuelve la funcion dividir
print(divide2(10))'''

'''#Ejemplo funcion anonima - lambda

doble = lambda x: x * 2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

alumnos = ['Alejandro', 'Miguel', 'Vinicio', 'Rodney', 'Marcial']
saludar_alumnos = list(map(lambda nombre: 'Hola ' + nombre, alumnos))
#print(saludar_alumnos)

#sin lambda
def saludar(nombre):
    return 'Hola ' + nombre

#usamos map con la funcion saludar
lista_saludos = list(map(saludar, alumnos))'''


