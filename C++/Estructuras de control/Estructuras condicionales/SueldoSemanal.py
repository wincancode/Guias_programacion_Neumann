
# Los trabajadores de una fabrica de autos tiene tres turnos: mañana, noche y
# festivos. Se desea calcular el sueldo semanal a razón de 5 días de trabajo a la semana
# según la siguiente tarifa:
#  600 Ptas./hora turno de la mañana
#  800 Ptas./hora turno de la tarde
# 1000 Ptas./hora día festivo.
# Se debe leer el turno y el número de horas trabajadas.

#Entradas 
print("Ingrese el turno de trabajo: ")
print("1. Mañana")
print("2. Noche")
print("3. Festivo")
turno = int(input())
horas = int(input("Ingrese el número de horas trabajadas: "))

#Proceso
if turno == 1:
    sueldo = horas * 600
elif turno == 2:
    sueldo = horas * 800
else:
    sueldo = horas * 1000

sueldo = sueldo * 5

#Salidas
print(f"El sueldo semanal es de: {sueldo} Ptas.")