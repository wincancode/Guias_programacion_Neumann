
# Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de
# ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que
# obtenga una calificación mayor que a un mínimo dado en cualquiera de los
# exámenes es aceptado; en caso contrario es rechazado. Realice un
# Algoritmo, que lea el nombre y calificaciones del aspirante. Realice un
# Algoritmo, que indique si es aceptado o rechazado. (Ejemplo mínimo = 90)

# Entradas
nombre = input("Ingrese el nombre del aspirante: ")
c1 = float(input("Ingrese la calificación del primer examen: "))
c2 = float(input("Ingrese la calificación del segundo examen: "))
minimo = float(input("Ingrese la calificación mínima: "))

# Procesos
if c1 >= minimo or c2 >= minimo:
    resultado = "Aceptado"
else:
    resultado = "Rechazado"

# Salidas
print(f"El aspirante {nombre} ha sido {resultado}")

# ¿Qué sucede si las dos calificaciones son menores al mínimo?
# En este caso, el aspirante es rechazado.