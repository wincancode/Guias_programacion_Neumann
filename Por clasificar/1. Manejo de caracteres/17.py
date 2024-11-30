
"""
17. Dado un número de cedula contenido en un string, determine si ese número de cédula este escrito
correctamente de acuerdo con el siguiente formato:
V11e22333 E22333444
"""

# Entrada de datos
cedula = input("Ingrese un número de cédula: ")

# Proceso y salida

# Verifica si El string de 1 al tamaño contiene solo digitos
estaFormateado = True
for i in range(1, len(cedula)):
    if not cedula[i].isdigit():
        estaFormateado = False
# Si solo contiene digitos, se verifica lo demas
if estaFormateado:
    # verifica si empiza con V o E, y tienen tamaños de 10 y 11 respectivamente.
    if (cedula.startswith("V") and len(cedula) == 10) or (cedula.startswith("E") and len(cedula) == 11):
        print("El número de cédula está escrito correctamente.")
    else:
        print("El número de cédula no cumple con el formato correcto.")
