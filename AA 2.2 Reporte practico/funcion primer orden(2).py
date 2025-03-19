def aprobado(nota):
    return nota >= 70

nota_estudiante = 80
resultado = aprobado(nota_estudiante)

if resultado:
    print("El estudiante aprobo.")
else:
    print("El estudiante no aprobo.")