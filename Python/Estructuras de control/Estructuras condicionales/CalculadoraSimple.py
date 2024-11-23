# 2. Escriba el algoritmo para simular una calculadora. Se debe leer los operandos y el
# operador. 

# Entradas
print("Calculadora")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador: ")

#procesos
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    resultado = "Operador no válido"

# Salidas
print(f"El resultado de {num1} {operador} {num2} es: {resultado}")