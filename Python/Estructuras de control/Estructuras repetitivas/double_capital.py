
# 7. Un capital C se coloca a un interés anual R. Al cabo de cuantos años se doblará?

#Entradas
capital = float(input("Ingrese el capital: "))
interes = float(input("Ingrese el interés anual: "))
años = 0

#Proceso
while capital < capital * 2:
    capital += capital * interes
    años += 1

#Salidas
print(f"El capital se doblará en {años} años.")