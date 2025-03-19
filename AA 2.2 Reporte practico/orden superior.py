def operacion(a, b, funcion):
    return funcion(a, b)

def sumar(a, b):
    return a + b

resultado = operacion(45, 15, sumar)
print("Resultado de la suma:", resultado)