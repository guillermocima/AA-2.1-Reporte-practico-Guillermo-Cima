# Inicialización de los contadores de puntos para cada rama
redes = 0
bases_de_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

# Imprimir el título del programa
print('=========')
print('Sombrero Seleccionador de Ramas de Sistemas Computacionales')
print('=========')

# Pregunta 1
print('\nP1) ¿Qué te interesa más?')
print('  1) Solucionar problemas de conectividad entre dispositivos')
print('  2) Organizar y analizar grandes volúmenes de información')
print('  3) Crear aplicaciones que resuelvan problemas cotidianos')
print('  4) Experimentar con componentes electrónicos y circuitos')
print('  5) Diseñar personajes y escenarios virtuales')
print('  6) Coordinar equipos para alcanzar objetivos comunes')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 2
print('\nP2) ¿Qué tipo de herramientas te gustaría utilizar en tu trabajo?')
print('  1) Herramientas de diagnóstico y configuración de redes')
print('  2) Sistemas de gestión de bases de datos como MySQL o MongoDB')
print('  3) Entornos de desarrollo integrado (IDEs) como Visual Studio Code')
print('  4) Herramientas de diseño de circuitos como Arduino o Raspberry Pi')
print('  5) Software de modelado 3D como Blender o Maya')
print('  6) Herramientas de gestión de proyectos como Jira o Trello')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 3
print('\nP3) ¿Qué tipo de desafíos te motivan más?')
print('  1) Asegurar la estabilidad y seguridad de una red')
print('  2) Optimizar consultas y mejorar el rendimiento de bases de datos')
print('  3) Resolver problemas complejos mediante código')
print('  4) Integrar hardware y software para crear sistemas inteligentes')
print('  5) Crear animaciones realistas y efectos visuales impactantes')
print('  6) Liderar equipos para cumplir plazos y objetivos')
respuesta = int(input('Ingresa tu respuesta (1-6): '))


if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 4
print('\nP4) ¿Qué tipo de proyectos te gustaría realizar?')
print('  1) Implementar una red segura para una empresa')
print('  2) Diseñar una base de datos para una aplicación móvil')
print('  3) Desarrollar un videojuego o una aplicación web')
print('  4) Crear un robot autónomo o un sistema IoT')
print('  5) Producir una película animada o un cortometraje en 3D')
print('  6) Gestionar el desarrollo de un software desde cero')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 5
print('\nP5) ¿Qué tipo de habilidades te gustaría destacar?')
print('  1) Conocimientos avanzados en protocolos de red')
print('  2) Habilidad para diseñar esquemas de bases de datos eficientes')
print('  3) Dominio de múltiples lenguajes de programación')
print('  4) Experiencia en el diseño y programación de hardware')
print('  5) Creatividad en el diseño y modelado 3D')
print('  6) Capacidad para liderar y motivar equipos')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Imprimir los puntos acumulados para cada rama
print("\nResultados:")
print("Redes: ", redes)
print("Bases de Datos: ", bases_de_datos)
print("Desarrollo de Software: ", desarrollo_software)
print("Programación Hardware: ", programacion_hardware)
print("Modelado 3D: ", modelado_3d)
print("Gestión de Proyectos de Software: ", gestion_proyectos)

# Determinar y anunciar la rama con más puntos
puntos = {
    "Redes": redes,
    "Bases de Datos": bases_de_datos,
    "Desarrollo de Software": desarrollo_software,
    "Programación Hardware": programacion_hardware,
    "Modelado 3D": modelado_3d,
    "Gestión de Proyectos de Software": gestion_proyectos
}

rama_seleccionada = max(puntos, key=puntos.get)
print(f'\n¡La rama más recomendada para ti es: {rama_seleccionada}!')