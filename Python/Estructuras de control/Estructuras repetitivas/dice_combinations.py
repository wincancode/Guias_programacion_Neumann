
# Con dos dados al azar se pueden obtener los números: 2..12. Por ejemplo, para
# obtener el número 2, la única forma es que ambos salgan con el uno; para obtener un
# cuatro existen dos combinaciones posibles, que ambos tengan un dos o que un dado
# salga con uno y el otro con tres. Diseñe un algoritmo (utilizando estructuras iterativas)
# que leyendo un valor N, validado entre 2 y 12, genere cuáles son las combinaciones
# posibles, sin repetición, para ese valor.

#Entradas: El valor N
#Proceso: Calcular las combinaciones posibles para el valor N
#Salidas: Las combinaciones posibles para el valor N

n = int(input("Ingrese un número entre 2 y 12: "))
while n < 2 or n > 12:
    n = int(input("Ingrese un número entre 2 y 12: "))
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == n:
            print(f"({i}, {j})")