def saludo(nombre):
    def saludo():
        return f"Hola, {nombre}!"
    return saludo

saludo_personalizado = saludo("Guillermo")
print(saludo_personalizado())