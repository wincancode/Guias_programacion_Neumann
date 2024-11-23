# 1. Se desea calcular el salario neto semanal de un trabajador en función del número
# de horas trabajadas y la tasa de impuestos d acuerdo a lo siguiente:
# - Las primeras 35 horas se pagan a tarifa normal
# - Las horas que pasen de 35 se pagan a 1.5 veces la tarifa normal
# - Las tasas de impuesto son:
# - Los rimeros 50$ son libres de impuesto
# - Los siguientes 40$ tienen un 25% de impuesto
# - Los restantes un 45% de impuesto
# Se pide mostrar el nombre del trabajador, salario bruto, tasas y salario neto.


# Entradas
nombre = input("Ingrese el nombre del trabajador: ")
horas = int(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

# Proceso
if horas <= 35:
    salario_bruto = horas * tarifa
else:
    salario_bruto = 35 * tarifa + (horas - 35) * tarifa * 1.5

if salario_bruto <= 50:
    impuesto = 0
elif salario_bruto <= 90:
    impuesto = (salario_bruto - 50) * 0.25
else:
    impuesto = 40 * 0.25 + (salario_bruto - 90) * 0.45

salario_neto = salario_bruto - impuesto

# Salidas
print(f"Nombre: {nombre}")
print(f"Salario bruto: {salario_bruto}")
print(f"Tasas: {impuesto}")
print(f"Salario neto: {salario_neto}")
