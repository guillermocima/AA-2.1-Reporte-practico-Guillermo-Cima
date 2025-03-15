def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def calcular_bonus(num_porciones):  # función para calcular bonus que recibe el número de porciones
    if num_porciones >= 2:  # si el número de porciones es mayor a 2
        return "coca gratis"  # retorna coca gratis
    return ""  # sino retorna vacío

def ordenar_alimento(preparar_alimento, num_porciones):  
    porciones_alimento = [preparar_alimento() for _ in range(num_porciones)]
    bonus = calcular_bonus(num_porciones)  # llamamos a la función calcular_bonus y le pasamos el número de porciones
    return porciones_alimento, bonus  # retornamos las porciones de alimento y el bonus

# Ejemplo de uso
alimento_grupoA = ordenar_alimento(preparar_pizza, 5)
alimento_grupoB = ordenar_alimento(preparar_hamburguesa, 3)
alimento_grupoC = ordenar_alimento(preparar_hotdog, 2)

print(alimento_grupoA, alimento_grupoB, alimento_grupoC)
    