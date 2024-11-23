
#4 Escribir un algoritmo que lea cuatro números y a continuación imprima el mayor de
#ellos.

# Entradas
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

# Procesos
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    mayor = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    mayor = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    mayor = num3
else:
    mayor = num4

# Salidas
print(f"El número mayor es: {mayor}")

#4.1 ¿Qué pasa si dos o más números son iguales y son los mayores?
# En este caso, el programa siempre mostrará el primer número que sea mayor o igual a los demás.
# Por ejemplo, si se ingresan los números 5, 5, 5 y 4, el programa mostrará 5 como el número mayor.