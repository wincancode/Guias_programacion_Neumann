
# Se introduce por teclado una hora determinada con el formato H, M, S. Se pide
# calcular la hora que será dentro de un segundo.

#Entradas
hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

#Proceso
if segundos == 59:
    segundos = 0
    if minutos == 59:
        minutos = 0
        if hora == 23:
            hora = 0
        else:
            hora += 1
    else:
        minutos += 1
else:
    segundos += 1

#Salidas
print(f"La hora dentro de un segundo será: {hora}:{minutos}:{segundos}")