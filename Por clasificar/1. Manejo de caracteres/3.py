"""
3. Elabore un programa que lea un valor entero desde el teclado y compruebe que esta entre 0 y 255,
y luego escriba en pantalla el carácter correspondiente en la tabla ASCII. Si el valor no esta entre
0 y 255 debe dar un mensaje de error.
"""

# Entrada de datos
valor_entero = int(input("Ingrese un valor entero: "))
# Proceso y salida
if valor_entero >= 0 and valor_entero <= 255:
    caracter_ascii = chr(valor_entero)
    print(f"El caracter correspondiente al valor {valor_entero} en la tabla ASCII es: {caracter_ascii}")
else:
    print("Error: El valor debe estar entre 0 y 255.")
