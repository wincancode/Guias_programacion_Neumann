
"""
15. Realice un programa que permita determinar cuántas veces aparece cada una de las vocales dentro
de un string.
"""

# Entrada de datos
texto = input("Ingrese un texto: ")
# Proceso
contador_vocales = {
    "a": texto.count("a") + texto.count("A"),
    "e": texto.count("e") + texto.count("E"),
    "i": texto.count("i") + texto.count("I"),
    "o": texto.count("o") + texto.count("O"),
    "u": texto.count("u") + texto.count("U")
}
# Salida
for vocal, cantidad in contador_vocales.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces en el texto.")

