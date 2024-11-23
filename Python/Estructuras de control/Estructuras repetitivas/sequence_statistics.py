
# Dada una secuencia de enteros terminada en cero, elabore un algoritmo para
# resolver cada uno de los siguientes problemas:
# a) Calcular el promedio de dicha secuencia.
# b) Calcular el porcentaje de números impares y el porcentaje de números pares.
# c) Calcular la cantidad de valores iguales a un valor N dado por el usuario.
# d) Contar la cantidad de números primos.

N = input("Ingrese un numero entero")
suma_numeros = 0
cantidad_numeros = 0
cantidad_impares = 0
cantidad_pares = 0
cantidad_iguales_N = 0
cantidad_primos = 0


print("Si ingresa un cero, se terminara el programa.")
num = input("ingrese un numero.")
while num != 0: 
    suma_numeros += num
    cantidad_numeros += 1

    #Verificar pares e impares
    if num % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    #Verificar numeros iguales a N
    if num == N:
        cantidad_iguales_N += 1

    #Verificar numeros primos
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            cantidad_primos += 1
    num = input("ingrese un numero.")

promedio = suma_numeros / cantidad_numeros
porcentaje_impares = (cantidad_impares / cantidad_numeros) * 100
porcentaje_pares = (cantidad_pares / cantidad_numeros) * 100

print("El promedio de la secuencia es: ", promedio)
print("El porcentaje de numeros impares es: ", porcentaje_impares)
print("El porcentaje de numeros pares es: ", porcentaje_pares)
print("La cantidad de numeros iguales a N es: ", cantidad_iguales_N)
print("La cantidad de numeros primos es: ", cantidad_primos)