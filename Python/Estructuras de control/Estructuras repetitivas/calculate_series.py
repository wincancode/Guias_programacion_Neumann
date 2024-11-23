
# # Escriba un algoritmo que calcule el resultado de la siguiente serie:
# a) 2, 5, 7, 10, 12, 15, 17, 20, …. 1800
# b) 1+ 1/2 + 1/3 + 1/4 + ... + 1/n
# c) 1 - 1/2 + 1/3 - 1/4 + ... + 1/n

#Entradas: La cantidad de numeros de la serie
#Proceso: Calcular la serie
#Salidas: La serie

n = int(input("Ingrese la cantidad de números de la serie: "))

#a)

suma = 0
#los tres parametros son el inicio, el final y el incremento. 
#El inicio es 2, el final es 1800 y el incremento es 3
#Se coloca 1801 porque el rango no incluye el último número
for i in range(2, 1801, 3):
    suma += i

print(f"La suma de la serie es {suma}")

#b)

suma = 0
for i in range(1, n + 1):
    suma += 1 / i

print(f"La suma de la serie es {suma}")

#c)

suma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        suma -= 1 / i
    else:
        suma += 1 / i

print(f"La suma de la serie es {suma}")