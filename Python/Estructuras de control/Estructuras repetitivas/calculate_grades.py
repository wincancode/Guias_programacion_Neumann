
# 0. Por cada uno de los N estudiantes se tienen la nota obtenida en una materia hacer
# un algoritmo que obtenga: la nota máxima, la mínima, cuántos perdieron y cuántos
# ganaron la asignatura.

n = int(input("Ingrese la cantidad de estudiantes: "))
perdieron = 0
ganaron = 0

for i in range(n):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    if i == 0:
        nota_max = nota
        nota_min = nota
    else:
        if nota > nota_max:
            nota_max = nota
        if nota < nota_min:
            nota_min = nota
    if nota < 10:
        perdieron += 1
    else:
        ganaron += 1

print(f"La nota máxima es {nota_max}.")
print(f"La nota mínima es {nota_min}.")
print(f"Perdieron {perdieron} estudiantes.")
print(f"Ganaron {ganaron} estudiantes.")