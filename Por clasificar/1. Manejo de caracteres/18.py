

"""
18. Utilizando el mismo formato para número de cedula del ejercicio anterior, escriba un programa
que determine la nacionalidad del portador de ese número.
"""

# Entrada de datos
cedula = input("Ingrese un número de cédula: ")
# Proceso y salida
if cedula.startswith("V"):
    print("El portador de la cédula es de nacionalidad venezolana.")
elif cedula.startswith("E"):
    print("El portador de la cédula es de nacionalidad extranjera.")
else:
    print("El número de cédula no cumple con el formato correcto.")

