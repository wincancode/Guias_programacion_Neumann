
# . Leer tres números del teclado y deducir si se han introducido en orden creciente.

#Entradas
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

#Proceso
if num1 < num2 and num2 < num3:
    print("Los números están en orden creciente.")
else:
    if num1 > num2 and num2 > num3:
        print("Los números están en orden decreciente.")
    else:
        print("Los números no están en orden creciente ni decreciente.")