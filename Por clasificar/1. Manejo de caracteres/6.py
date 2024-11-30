"""
6. Elabore un programa que escriba en pantalla de forma ordenada toda la tabla de caracteres ASCII.
Nota: utilice el ciclo de repetición for para la solución.
"""

# Proceso y salida
for i in range(256):
    caracter_ascii = chr(i)
    print(f"Valor: {i} - Caracter: {caracter_ascii}")
