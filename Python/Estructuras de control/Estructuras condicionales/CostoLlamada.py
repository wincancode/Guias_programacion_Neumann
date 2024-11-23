
# 2. Escriba un Algoritmo, que determine el monto a pagar de una llamada
# telefónica teniendo en cuenta lo siguiente: toda llamada que dure hasta 3
# minutos tiene un costo de 35 Bs. Por cada minuto adicional se cobra una
# tari fa de 15 Bs. Se debe leer el tiempo de llamadas en el formato hh:mm.
# Salida: tiempo de llamada y costo

# Entradas
print("Calculadora de llamadas")
horas = int(input("Ingrese las horas de la llamada: "))
minutos = int(input("Ingrese los minutos de la llamada: "))

# Procesos
if horas == 0:
    costo = 35
else:
    costo = 35 + (horas - 1) * 60 * 15
if minutos > 3:
    costo += (minutos - 3) * 15

tiempo_llamada = horas*60 + minutos

# Salidas
print(f'tiempo de llamada: {tiempo_llamada} minutos')
print(f'costo: {costo}')