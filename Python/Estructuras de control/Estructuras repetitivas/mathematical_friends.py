
# La amistad cuadrática entre números se podría explicar en la siguiente
# conversación entre el numero 13 y el numero 16
# 16 al 13: Quiero ofrecerte mi homenaje amigo, mi cuadrado es 256 cuya suma
# de guarismos es 13
# 13 al 16: Agradezco tu bondad y quiero retribuirla en la misma forma. Mi
# cuadrado es 169 cuya suma de guarismos es 16.
# Dado este pequeño fragmento de “El hombre que calculaba” realice un programa que
# diga si dos números son amigos matemáticos


#Entradas
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
#Proceso

cuadrado1 = num1 ** 2

cuadrado2 = num2 ** 2

suma1 = 0

suma2 = 0

while cuadrado1 != 0:
    suma1 += cuadrado1 % 10
    cuadrado1 //= 10

while cuadrado2 != 0:
    suma2 += cuadrado2 % 10
    cuadrado2 //= 10

#Salidas

if suma1 == num2 and suma2 == num1:
    print("Los números son amigos matemáticos.")
else:
    print("Los números no son amigos matemáticos.")