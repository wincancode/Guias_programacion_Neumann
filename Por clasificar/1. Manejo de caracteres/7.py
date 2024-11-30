"""
7. Elabore un programa que escriba en pantalla de forma ordenada toda la tabla de caracteres ASCII.
Nota: utilice el ciclo de repetición while para la solución.
"""

# Inicialización
i = 0
# Proceso y salida
while i < 256:
    caracter_ascii = chr(i)
    print(f"Valor: {i} - Caracter: {caracter_ascii}")
    i += 1

