def crear_saludo(nombre):
    def saludo():
        return f"Hola, {nombre}, bienvenido al sistema."
    return saludo

saludo = crear_saludo("Guillermo")

print(saludo())