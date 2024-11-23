
# Dado un número entero de N dígitos, se pide que construya un algoritmo que
# substituya todas las ocurrencias de un dígito dado X por otro dígito
# suministrado Y.
# Ejemplo:
# Entrada Salida
# 14123 64623
# X=1
# Y=6

n = int(input("Ingrese un número entero: "))
x = int(input("Ingrese el dígito a reemplazar: "))
y = int(input("Ingrese el dígito por el que reemplazar: "))

nuevo_numero = 0
multiplo = 1

while n > 0:
    digito = n % 10
    if digito == x:
        digito = y
    nuevo_numero = digito * multiplo + nuevo_numero
    n //= 10
    multiplo *= 10
    print(f"Digito: {digito}, Nuevo número: {nuevo_numero}")

print(f"El número resultante es {nuevo_numero}.")