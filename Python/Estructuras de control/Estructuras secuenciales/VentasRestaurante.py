
# El menú de un restaurante de comida rápida es:
# Hamburguesa250 Ptas.
# Cerveza 100 Ptas.
# Coca cola 125 Ptas.
# Ensalada 200 Ptas.
# Salchichas 275 Ptas.
# Sopa 260 Ptas.
# Pastel 300 Ptas.
# Se desea un algoritmo que calcule las ventas totales al final del día, así como los
# impuestos a pagar (12%). El algoritmo tendrá como entrada el número de cada uno e
# los productos vendidos ese día. 

# Entradas
hamburguesas = int(input("Ingrese el número de hamburguesas vendidas: "))
cervezas = int(input("Ingrese el número de cervezas vendidas: "))
cocas = int(input("Ingrese el número de cocas vendidas: "))
ensaladas = int(input("Ingrese el número de ensaladas vendidas: "))
salchichas = int(input("Ingrese el número de salchichas vendidas: "))
sopas = int(input("Ingrese el número de sopas vendidas: "))
pasteles = int(input("Ingrese el número de pasteles vendidos: "))
impuesto = 0.12

# Procesos
total = hamburguesas * 250 + cervezas * 100 + cocas * 125 + ensaladas * 200 + salchichas * 275 + sopas * 260 + pasteles * 300
impuestos = total * impuesto
ventas_tot = total - impuestos

# Salidas
print(f"Las ventas totales del día son: {ventas_tot}")
print(f"Los impuestos a pagar son: {impuestos}")